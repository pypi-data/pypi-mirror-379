import argparse
import sys
import os
from pathlib import Path
import pandas as pd
from fimep import preprocessing, encode, prediction

def main():
    parser = argparse.ArgumentParser(
        prog="fimep", 
        description="fimep - For integration of multiple effector prediction"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # runall command
    runall_parser = subparsers.add_parser("runall", help="Run full workflow for a given kingdom")
    runall_parser.add_argument("--kingdom", required=True, 
                              choices=["fungi", "bacteria", "oomycete", "all"],
                              help="Kingdom name (fungi, bacteria, oomycete, or all)")
    runall_parser.add_argument("--effectorp", help="Path to EffectorP result file")
    runall_parser.add_argument("--deepredeff", help="Path to Deepredeff result file")
    runall_parser.add_argument("--effectivet3", help="Path to EffectiveT3 result file")  # Fixed typo
    runall_parser.add_argument("--effectoro", help="Path to EffectorO result file")
    runall_parser.add_argument("--t3sepp", help="Path to T3SEpp result file")
    runall_parser.add_argument("--wideeffhunter", nargs=2, metavar=("COMPLETE_FASTA", "PRED_FASTA"),
                              help="WideEffHunter: complete sequences FASTA and predicted sequences FASTA")
    runall_parser.add_argument("--output", required=True, help="Path to save final prediction file")

    # Individual preprocess commands
    for prog in ["effectorp", "effectivet3", "effectoro", "t3sepp", "deepredeff", "wideeffhunter"]:
        p = subparsers.add_parser(f"preprocess_{prog}", help=f"Preprocess {prog} output")
        p.add_argument("--input", required=True, help=f"{prog} result file")
        if prog == "wideeffhunter":
            p.add_argument("--pred", required=True, help="WideEffHunter predicted FASTA file")
        p.add_argument("--output", required=True, help="Formatted output CSV file")
        p.add_argument("--kingdom", required=True, 
                      choices=["fungi", "bacteria", "oomycete", "all"],
                      help="Kingdom name")

    # merge command
    merge_parser = subparsers.add_parser("merge_prediction", help="Merge formatted prediction files")
    merge_parser.add_argument("--input", nargs="+", required=True, help="List of formatted input files")
    merge_parser.add_argument("--output", required=True, help="Path to save merged output")

    # encode command
    encode_parser = subparsers.add_parser("encode", help="Encode merged data")
    encode_parser.add_argument("--input", required=True, help="Path to merged CSV")
    encode_parser.add_argument("--output", required=True, help="Path to save encoded file")
    encode_parser.add_argument("--kingdom", required=True, 
                              choices=["fungi", "bacteria", "oomycete", "all"],
                              help="Kingdom: fungi, bacteria, oomycete, or all")

    # prediction command
    predict_parser = subparsers.add_parser("predict", help="Generate final prediction from encoded data")
    predict_parser.add_argument("--input", required=True, help="Path to encoded CSV")
    predict_parser.add_argument("--output", required=True, help="Path to save prediction CSV")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        if args.command == "runall":
            run_full_workflow(args)
        elif args.command.startswith("preprocess_"):
            preprocess_single(args)
        elif args.command == "merge_prediction":
            merge_predictions(args)
        elif args.command == "encode":
            encode_data(args)
        elif args.command == "predict":
            make_prediction(args)
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)

def run_full_workflow(args):
    """Run the complete workflow from preprocessing to final prediction."""
    print(f"[INFO] Running full workflow for kingdom: {args.kingdom}")
    
    dfs = []
    k = args.kingdom.lower()
    
    # Validate kingdom-specific tool combinations
    validate_kingdom_tools(args, k)
    
    # Process each tool if provided
    try:
        if args.effectorp and k in {"fungi", "oomycete"}:
            print("[INFO] Processing EffectorP results...")
            validate_file_exists(args.effectorp)
            df = preprocessing.format_effectorp_result(args.effectorp, k)
            dfs.append(df)
            
        if args.deepredeff and k in {"fungi", "oomycete", "bacteria"}:
            print("[INFO] Processing Deepredeff results...")
            validate_file_exists(args.deepredeff)
            df = preprocessing.format_deepredeff_result(args.deepredeff, k)
            dfs.append(df)
            
        if args.effectivet3 and k == "bacteria":
            print("[INFO] Processing EffectiveT3 results...")
            validate_file_exists(args.effectivet3)
            df = preprocessing.format_effectiveT3_result(args.effectivet3, k)
            dfs.append(df)
            
        if args.effectoro and k == "oomycete":
            print("[INFO] Processing EffectorO results...")
            validate_file_exists(args.effectoro)
            df = preprocessing.format_effectoro_result(args.effectoro, k)
            dfs.append(df)
            
        if args.t3sepp and k == "bacteria":
            print("[INFO] Processing T3SEpp results...")
            validate_file_exists(args.t3sepp)
            df = preprocessing.format_T3SEpp_result(args.t3sepp, k)
            dfs.append(df)
            
        if args.wideeffhunter and k in {"fungi", "oomycete"}:
            print("[INFO] Processing WideEffHunter results...")
            complete, pred = args.wideeffhunter
            validate_file_exists(complete)
            validate_file_exists(pred)
            df = preprocessing.format_WideEffHunter_result(complete, pred, k)
            dfs.append(df)
            
    except Exception as e:
        raise RuntimeError(f"Error processing tool results: {e}")
    
    if not dfs:
        raise ValueError(f"No valid tool results provided for kingdom '{k}'. Please check your input files and kingdom compatibility.")
    
    # Merge predictions
    print("[INFO] Merging predictions...")
    try:
        merged = preprocessing.merge_predictions_by_identifier(dfs)
    except Exception as e:
        raise RuntimeError(f"Error merging predictions: {e}")
    
    # Encode data
    print("[INFO] Encoding data...")
    try:
        encoded = encode.encode_scale_predictions(merged, args.output.replace('.csv', '_encoded.csv'), k)
    except Exception as e:
        raise RuntimeError(f"Error encoding data: {e}")
    
    # Make final prediction
    print("[INFO] Making final predictions...")
    try:
        prediction.model_prediction(args.output.replace('.csv', '_encoded.csv'), args.output)
        # Clean up intermediate file
        os.remove(args.output.replace('.csv', '_encoded.csv'))
    except Exception as e:
        raise RuntimeError(f"Error making final prediction: {e}")
    
    print(f"[SUCCESS] Full workflow completed. Final predictions saved to: {args.output}")

def preprocess_single(args):
    """Process a single tool's output."""
    print(f"[INFO] Preprocessing {args.command} results...")
    
    validate_file_exists(args.input)
    
    func_map = {
        "preprocess_effectorp": preprocessing.format_effectorp_result,
        "preprocess_effectivet3": preprocessing.format_effectiveT3_result,
        "preprocess_effectoro": preprocessing.format_effectoro_result,
        "preprocess_t3sepp": preprocessing.format_T3SEpp_result,
        "preprocess_deepredeff": preprocessing.format_deepredeff_result,
        "preprocess_wideeffhunter": preprocessing.format_WideEffHunter_result,
    }
    
    func = func_map[args.command]
    
    try:
        if args.command == "preprocess_wideeffhunter":
            validate_file_exists(args.pred)
            df = func(args.input, args.pred, args.kingdom)
        else:
            df = func(args.input, args.kingdom)
        
        # Create output directory if it doesn't exist
        output_dir = Path(args.output).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        df.to_csv(args.output, index=False)
        print(f"[SUCCESS] Preprocessed results saved to: {args.output}. NB: '1 means Effector' and '0 means Non-effector'")
    except Exception as e:
        raise RuntimeError(f"Error preprocessing {args.command}: {e}")

def merge_predictions(args):
    """Merge multiple formatted prediction files."""
    print("[INFO] Merging prediction files...")
    
    # Validate all input files exist
    for file_path in args.input:
        validate_file_exists(file_path)
    
    try:
        dfs = []
        for file_path in args.input:
            df = pd.read_csv(file_path)
            dfs.append(df)
        
        merged = preprocessing.merge_predictions_by_identifier(dfs)
        
        # Create output directory if it doesn't exist
        output_dir = Path(args.output).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        merged.to_csv(args.output, index=False)
        print(f"[SUCCESS] Merged predictions saved to: {args.output}. NB: '1 means Effector' and '0 means Non-effector'")
    except Exception as e:
        raise RuntimeError(f"Error merging predictions: {e}")

def encode_data(args):
    """Encode merged prediction data."""
    print("[INFO] Encoding prediction data...")
    
    validate_file_exists(args.input)
    
    try:
        # Create output directory if it doesn't exist
        output_dir = Path(args.output).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        encoded = encode.encode_scale_predictions(args.input, args.output, args.kingdom)
        print(f"[SUCCESS] Encoded data saved to: {args.output}")
    except Exception as e:
        raise RuntimeError(f"Error encoding data: {e}")

def make_prediction(args):
    """Generate final predictions from encoded data."""
    print("[INFO] Generating final predictions...")
    
    validate_file_exists(args.input)
    
    try:
        # Create output directory if it doesn't exist
        output_dir = Path(args.output).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        prediction.model_prediction(args.input, args.output)
        print(f"[SUCCESS] Final predictions saved to: {args.output}")
    except Exception as e:
        raise RuntimeError(f"Error making predictions: {e}")

def validate_file_exists(file_path):
    """Validate that a file exists."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

def validate_kingdom_tools(args, kingdom):
    """Validate that the provided tools are compatible with the kingdom."""
    kingdom_tools = {
        "fungi": ["effectorp", "deepredeff", "wideeffhunter"],
        "bacteria": ["deepredeff", "effectivet3", "t3sepp"],
        "oomycete": ["effectorp", "deepredeff", "wideeffhunter", "effectoro"],
        "all": ["effectorp", "deepredeff", "wideeffhunter", "effectivet3", "t3sepp", "effectoro"]
    }
    
    valid_tools = kingdom_tools.get(kingdom, [])
    provided_tools = []
    
    for tool in valid_tools:
        if hasattr(args, tool) and getattr(args, tool) is not None:
            provided_tools.append(tool)
    
    if not provided_tools:
        raise ValueError(f"No valid tools provided for kingdom '{kingdom}'. "
                        f"Valid tools for {kingdom}: {', '.join(valid_tools)}")
    
    # Check for invalid tool combinations
    for tool in ["effectorp", "deepredeff", "wideeffhunter", "effectivet3", "t3sepp", "effectoro"]:
        if hasattr(args, tool) and getattr(args, tool) is not None:
            if tool not in valid_tools:
                print(f"[WARNING] Tool '{tool}' is not compatible with kingdom '{kingdom}' and will be ignored.")

if __name__ == "__main__":
    main()
