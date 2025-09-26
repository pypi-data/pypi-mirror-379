def encode_scale_predictions(input_file, output_file, kingdom):
    """
    One-hot encodes effector prediction results for downstream use in the deep learning model.

    This function:
    - Validates the prediction columns based on the specified pathogen kingdom.
    - One-hot encodes each predictor column.
    - Adds any missing model-required columns and fills them with 0.
    - Reorders columns to match the format expected by the trained deep learning model.
    - Saves the encoded DataFrame as a CSV file and returns it.

    Parameters
    ----------
    input_file : str
        Path to the CSV file containing raw binary predictions (0 or 1) from kingdom-specific tools.

    output_file : str
        Path where the one-hot encoded and formatted CSV file will be saved.

    kingdom : str
        The biological kingdom of the pathogen. Must be one of:
        - "bacteria"
        - "fungi"
        - "oomycete"
        - "all" - means bacteria, fungi, and oomycete 

        Each kingdom expects specific predictor columns:
            - bacteria:     Deepredeff, EffectiveT3, T3SEpp  
            - fungi:        EffectorP, Deepredeff, WideEffHunter  
            - oomycete:     EffectorP, Deepredeff, WideEffHunter, EffectorO  
            - all:          EffectorP, EffectiveT3, EffectorO, Deepredeff, WideEffHunter, T3SEpp

    Returns
    -------
    pandas.DataFrame
        The processed, encoded DataFrame ready for model prediction.

    Raises
    ------
    ValueError
        If the specified kingdom is invalid or required columns are missing in the input file.
    FileNotFoundError
        If the input file does not exist.

    Notes
    -----
    - This function is meant to be used **after prediction results have been generated** using external tools
      (e.g., EffectorP, Deepredeff, etc.).
    - If your prediction file lacks expected columns, refer to the `preprocessing` module in this package.
      It contains helper functions to format outputs from each tool into the required structure.

    Example
    -------
    >>> encode_scale_predictions("predictions.csv", "encoded.csv", kingdom="fungi")
    """

    # Import needed packages    
    import pandas as pd
    import os

    if isinstance(input_file, pd.DataFrame):
        df = input_file.copy()
    elif isinstance(input_file, str):
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"[ERROR] Input file not found: {input_file}")

    # Load input data
        try:
            df = pd.read_csv(input_file)
        except Exception as e:
            raise ValueError(f"[ERROR] Failed to read CSV file: {e}")
    else:
        raise TypeError("[ERROR] 'input_file' must be a pandas DataFrame of a path to a CSV file (string).") 
    
    # Check if dataframe is empty
    if df.empty:
        raise ValueError("[ERROR] Input file is empty")

    # Columns required by kingdoms
    kingdom_expected_col = {
        "bacteria": {"Deepredeff", "EffectiveT3", "T3SEpp"},
        "fungi": {"EffectorP", "Deepredeff", "WideEffHunter"}, 
        "oomycete": {"EffectorP", "Deepredeff", "WideEffHunter", "EffectorO"},
        "all": {"EffectorP", "EffectiveT3", "EffectorO", "Deepredeff", "WideEffHunter", "T3SEpp"}
    }

    model_expected_col_order = [
        "EffectorP_Effector", "EffectorP_Non-Effector",
        "EffectiveT3_Effector", "EffectiveT3_Non-Effector",
        "EffectorO_Effector", "EffectorO_Non-Effector",
        "Deepredeff_Effector", "Deepredeff_Non-Effector",
        "WideEffHunter_Effector", "WideEffHunter_Non-Effector",
        "T3SEpp_Effector", "T3SEpp_Non-Effector"
    ]

    # Validate kingdom
    kingdom = kingdom.lower()
    if kingdom not in kingdom_expected_col:
        raise ValueError(f"[ERROR] Invalid kingdom: {kingdom}. Must be one of: {list(kingdom_expected_col.keys())}")
    
    present_col = set(df.columns)
    required_col = kingdom_expected_col[kingdom]
    missing_col = required_col - present_col
    
    if missing_col:
        raise ValueError(f"[ERROR] Missing required columns for kingdom '{kingdom}': {sorted(missing_col)}")
    
    # Check for required Identifier column
    if "Identifier" not in df.columns:
        raise ValueError("[ERROR] Required 'Identifier' column not found in input file. This column is needed to track protein sequences.")
    
    # Validate prediction column values (allowing NA for kingdom="all")
    for col in required_col:
        non_na_values = df[col].dropna().unique()
        valid_values = {0, 1}
        if len(non_na_values) > 0 and not set(non_na_values).issubset(valid_values):
            invalid = set(non_na_values) - valid_values
            raise ValueError(f"[ERROR] Column '{col}' contains invalid values: {invalid}. Only 0, 1, and NA are allowed.")
        
        # For kingdom="all", warn if all values are NA (no predictions available)
        if kingdom == "all" and df[col].isna().all():
            print(f"[WARNING] Column '{col}' contains only NA values - predictor likely not run for this organism type")
    
    # Create a copy for processing to avoid modifying original data
    df_processed = df[list(required_col)].copy()
    
    # Replace 0 and 1 with "Non-Effector" and "Effector", keep NA as is
    replacement_dict = {1: "Effector", 0: "Non-Effector"}
    for col in required_col:
        df_processed[col] = df_processed[col].replace(replacement_dict)

    # One-hot encoding - more efficient approach
    encoded_dfs = []
    for col in required_col:
        encoded = pd.get_dummies(df_processed[col], prefix=col, dtype=int)
        encoded_dfs.append(encoded)

    # Concatenate all at once (more efficient)
    encoded_df = pd.concat(encoded_dfs, axis=1)

    # Drop _NA columns if they exist (these will be created by pd.get_dummies for NA values)
    na_columns = [col for col in encoded_df.columns if col.endswith("_NA")]
    if na_columns:
        encoded_df = encoded_df.drop(columns=na_columns)
        print(f"[INFO] Dropped NA indicator columns: {na_columns} (will be handled downstream)")

    # Add missing columns for model compatibility
    missing_model_cols = []
    for col in model_expected_col_order:
        if col not in encoded_df.columns:
            encoded_df[col] = 0
            missing_model_cols.append(col)
    
    if missing_model_cols:
        print(f"[INFO] Added missing columns for model compatibility: {missing_model_cols}")

    # Reorder columns to match model expectations
    encoded_df = encoded_df[model_expected_col_order]

    # Combine Identifier column with encoded predictions to maintain protein order
    identifier_df = df[["Identifier"]].copy()
    final_df = pd.concat([identifier_df, encoded_df], axis=1)
    print("[INFO] Preserved Identifier column to maintain protein sequence tracking")

    # Save the encoded file
    try:
        final_df.to_csv(output_file, index=False)
        print(f"[INFO] Encoded file saved to: {output_file}")
    except Exception as e:
        raise ValueError(f"[ERROR] Failed to save output file: {e}")

    return final_df