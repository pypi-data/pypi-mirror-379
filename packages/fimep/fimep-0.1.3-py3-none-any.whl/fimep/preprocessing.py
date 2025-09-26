
## Format results from different programs


def format_effectorp_result(input_file, kingdom, output_file=None):
    """
    Format the raw output from EffectorP into a standardized format for downstream use.

    The function:
    - Reads the EffectorP output file.
    - Converts effector class labels to binary (1 for effector, 0 for non-effector).
    - Retains only necessary columns: 'Identifier', 'Prediction', 'Kingdom', 'Program'.
    - Returns a cleaned pandas DataFrame.
    - Optionally saves the result as a CSV file.

    Parameters:
    -----------
    input_file : str
        Path to the raw EffectorP result file (typically tab-delimited).
    
    kingdom : str
        The target organism kingdom (e.g., 'fungi', 'oomycete'). Included for reference.
        It is automatically converted to lowercase for consistency.

    output_file : str, optional
        Path to save the formatted DataFrame as a CSV file.

    Returns:
    --------
    pd.DataFrame
        A cleaned DataFrame with columns: ['Identifier', 'Prediction', 'Kingdom', 'Program']

    Raises:
    -------
    FileNotFoundError
        If the input file does not exist or can't be read.
    
    ValueError
        If the file format is incorrect or expected columns are missing.

    Example:
    --------
    >>> df = format_effectorp_result("EffectorP_results.txt", kingdom="Fungi", output_file="effp_formatted.csv")
    """

    import pandas as pd
    import os

    # Ensure lowercase for consistency
    kingdom = kingdom.lower()

    # Check that the input file exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"[ERROR] File not found: {input_file}")

    try:
        # Read the EffectorP results
        df = pd.read_csv(
            input_file,
            sep="\t",
            header=7,
            names=["Identifier", "Cytoplasmic effector", "Apoplastic effector", "Non-effector", "Prediction"]
        )
    except Exception as e:
        raise ValueError(f"[ERROR] Failed to read file: {e}")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Replace effector class labels with binary values
    pattern_conversion = {
        "Cytoplasmic effector": 1,
        "Apoplastic effector": 1,
        "Non-effector": 0,
        "Apoplastic/cytoplasmic effector": 1,
        "Cytoplasmic/apoplastic effector": 1
    }

    if "Prediction" not in df.columns:
        raise ValueError("[ERROR] Expected 'Prediction' column is missing.")

    df["Prediction"] = df["Prediction"].map(pattern_conversion)


    # Clean identifier column
    df["Identifier"] = df["Identifier"].astype(str).str.strip().str.split().str[0]

    # Drop empty rows
    df = df.dropna(thresh=2)

    # Add metadata
    df["Program"] = "EffectorP"
    df["Kingdom"] = kingdom

    # Keep only relevant columns
    df = df[["Identifier", "Prediction", "Kingdom", "Program"]]


    # Optionally save output
    if output_file:
        try:
            df.to_csv(output_file, index=False)
            print(f"[INFO] Formatted result saved to: {output_file}")
        except Exception as e:
            raise IOError(f"[ERROR] Failed to write output file: {e}")

    return df








# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– #



def format_effectiveT3_result(input_file, kingdom="bacteria", output_file=None):
    """
    Format the raw output from EffectiveT3 into a standardized DataFrame for downstream processing.

    This function:
    - Reads EffectiveT3 prediction results from a semicolon-delimited file.
    - Converts 'True'/'False' string predictions to binary strings '1'/'0'.
    - Cleans the data by dropping rows with insufficient data.
    - Adds metadata columns indicating the kingdom and program source.
    - Optionally saves the cleaned DataFrame to a CSV file.

    Parameters:
    -----------
    input_file : str
        Path to the raw EffectiveT3 result file.

    kingdom : str, optional, default='bacteria'
        Target organism kingdom, used for metadata tagging.
        The value is normalized to lowercase internally.

    output_file : str, optional
        File path to save the formatted DataFrame as CSV. 
        If None, the result will not be saved to disk.

    Returns:
    --------
    pd.DataFrame
        A DataFrame with columns: ['Identifier', 'Description', 'Score', 'Prediction', 'Kingdom', 'Program'].

    Raises:
    -------
    FileNotFoundError
        If the input file cannot be found.

    ValueError
        If the file cannot be parsed or expected columns are missing.

    Example:
    --------
    >>> df = format_effectiveT3_result("EffectiveT3_output.csv", kingdom="Bacteria", output_file="effT3_formatted.csv")
    """
    # Import needed packages
    import pandas as pd

    df = pd.read_csv(input_file, sep=";", header=0, names= ["Identifier", "Description", "Score", "Prediction"])
    renaming_prediction = {"True" : 1, "False" : 0} ### This creates a dictionary of what is to be replaced
    df["Prediction"] = df["Prediction"].astype(str).map(renaming_prediction) ## Replacing the names in the prediction column
    df = df.dropna(thresh=3)
    df["Kingdom"] = kingdom.lower()
    df["Program"] = "EffectiveT3"
    df.drop(["Description", "Score"], axis=1, inplace=True)

   # Optional write to disk 
    if output_file:
        df.to_csv(output_file, index= False)
        print(f"Formatted result saved to {output_file}")
    return df









# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– #



def format_effectoro_result(input_file, kingdom="oomycete", output_file=None):
    """
    Format the raw output from EffectorO into a standardized DataFrame for downstream processing.

    This function:
    - Reads EffectorO prediction results from a CSV file.
    - Drops unnecessary columns, retaining only Identifier, Prediction, and Program metadata.
    - Adds metadata columns indicating the kingdom and program source.
    - Normalizes the kingdom string to lowercase.
    - Optionally saves the formatted DataFrame to a CSV file.

    Parameters:
    -----------
    input_file : str
        Path to the raw EffectorO result file.

    kingdom : str, optional, default='oomycete'
        Target organism kingdom, used for metadata tagging.
        The value is normalized to lowercase internally.

    output_file : str, optional
        File path to save the formatted DataFrame as CSV.
        If None, the result will not be saved to disk.

    Returns:
    --------
    pd.DataFrame
        A DataFrame with columns: ['Identifier', 'Prediction', 'Program', 'Kingdom'].

    Raises:
    -------
    FileNotFoundError
        If the input file cannot be found.

    ValueError
        If the input file cannot be parsed correctly or required columns are missing.

    Example:
    --------
    >>> df = format_effectoro_result("EffectorO_output.csv", kingdom="oomycete", output_file="effectoro_formatted.csv")
    """
    import pandas as pd

    try:
        df = pd.read_csv(input_file, header=0, names=["Index", "Identifier", "Sequence", "Prediction", "Score", "Meaning"])
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {input_file}")
    except Exception as e:
        raise ValueError(f"Failed to read the input file: {e}")

    try:
        # Drop unnecessary columns
        df = df.drop(df.columns[[0, 2, 4, 5]], axis=1)
    except Exception as e:
        raise ValueError(f"Failed to process columns in the input file: {e}")

    df["Program"] = "EffectorO"
    df["Kingdom"] = kingdom.lower()
    df["Identifier"] = df["Identifier"].str.split().str[0]    

    if output_file:
        try:
            df.to_csv(output_file, index=False)
            print(f"Formatted result saved to {output_file}. NB: '1 means Effector' and '0 means Non-effector'")
        except Exception as e:
            raise IOError(f"Failed to save formatted result: {e}")

    return df








# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– #




def format_deepredeff_result(input_file, kingdom, output_file=None):
    """
    Format the raw output from Deepredeff into a standardized DataFrame for downstream processing.

    This function:
    - Reads Deepredeff prediction results from a CSV file.
    - Drops unnecessary columns, retaining only Identifier and Prediction.
    - Converts textual predictions ('effector'/'non-effector') to binary strings ('1'/'0').
    - Normalizes the kingdom string to lowercase for consistency.
    - Adds metadata columns for kingdom and program source.
    - Optionally saves the formatted DataFrame to a CSV file.

    Parameters:
    -----------
    input_file : str
        Path to the raw Deepredeff result file.

    kingdom : str
        Target organism kingdom, used for metadata tagging.
        The value is normalized to lowercase internally.

    output_file : str, optional
        File path to save the formatted DataFrame as CSV.
        If None, the result will not be saved to disk.

    Returns:
    --------
    pd.DataFrame
        A DataFrame with columns: ['Identifier', 'Prediction', 'Kingdom', 'Program'].

    Raises:
    -------
    FileNotFoundError
        If the input file cannot be found.

    ValueError
        If the input file cannot be parsed or required columns are missing.

    IOError
        If saving the formatted file fails.

    Example:
    --------
    >>> df = format_deepredeff_result("Deepredeff_output.csv", kingdom="fungi", output_file="deepredeff_formatted.csv")
    """
    import pandas as pd

    try:
        df = pd.read_csv(input_file, header=0, names=["Identifier", "Sequence", "Score", "Prediction"])
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {input_file}")
    except Exception as e:
        raise ValueError(f"Failed to read the input file: {e}")

    try:
        df = df.drop(df.columns[[1, 2]], axis=1)
    except Exception as e:
        raise ValueError(f"Failed to process columns in the input file, it expects the columns to be 'names', 'sequence', 's_score', 'prediction': {e}")

    column_replacement = {"non-effector": 0, "effector": 1}
    try:
        df["Prediction"] = df["Prediction"].map(column_replacement)
    except Exception as e:
        raise ValueError(f"Failed to replace prediction values: {e}")

    df["Kingdom"] = kingdom.lower()
    df["Program"] = "Deepredeff"
    df["Identifier"] = df["Identifier"].str.split().str[0]

    if output_file:
        try:
            df.to_csv(output_file, index=False)
            print(f"Formatted result saved to {output_file}. NB: '1 means Effector' and '0 means Non-effector'")
        except Exception as e:
            raise IOError(f"Failed to save formatted result: {e}")

    return df








# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– #



def format_WideEffHunter_result(complete_seq_file, pred_seq_file, kingdom, program="WideEffHunter", output_file=None):
    """
    Format WideEffHunter prediction results by comparing complete sequences to predicted effectors.

    This function:
    - Parses FASTA files for the complete sequences and predicted effector sequences.
    - Creates a DataFrame with identifiers, binary predictions (1 if predicted effector, else 0),
      kingdom and program metadata.
    - Normalizes the kingdom string to lowercase for consistency.
    - Optionally saves the formatted DataFrame to a CSV file.

    Parameters:
    -----------
    complete_seq_file : str
        Path to the FASTA file containing the complete set of sequences.

    pred_seq_file : str
        Path to the FASTA file containing predicted effector sequences.

    kingdom : str
        Target organism kingdom, used for metadata tagging.
        The value is normalized to lowercase internally.

    program : str, optional, default='WideEffHunter'
        Name of the prediction program to include as metadata.

    output_file : str, optional
        File path to save the formatted DataFrame as CSV.
        If None, the result will not be saved to disk.

    Returns:
    --------
    pd.DataFrame
        A DataFrame with columns: ['Identifier', 'Prediction', 'Kingdom', 'Program'].

    Raises:
    -------
    FileNotFoundError
        If either of the input FASTA files cannot be found.

    ValueError
        If parsing of FASTA files fails.

    IOError
        If saving the formatted file fails.

    Example:
    --------
    >>> df = format_WideEffHunter_result("all_sequences.fasta", "predicted_effectors.fasta", "fungi", output_file="wideeffhunter_formatted.csv")
    """
    
    import pandas as pd
    from Bio import SeqIO

    kingdom = kingdom.lower()

    try:
        effs = [record.id for record in SeqIO.parse(pred_seq_file, "fasta")]
    except FileNotFoundError:
        raise FileNotFoundError(f"Predicted sequences file not found: {pred_seq_file}")
    except Exception as e:
        raise ValueError(f"Failed to parse predicted sequences file: {e}")

    try:
        data = []
        for record in SeqIO.parse(complete_seq_file, "fasta"):
            prediction = 1 if record.id in effs else 0
            data.append([record.description, prediction, kingdom, program])
    except FileNotFoundError:
        raise FileNotFoundError(f"Complete sequences file not found: {complete_seq_file}")
    except Exception as e:
        raise ValueError(f"Failed to parse complete sequences file: {e}")

    df = pd.DataFrame(data, columns=["Identifier", "Prediction", "Kingdom", "Program"])
    df["Identifier"] = df["Identifier"].str.split().str[0]

    if output_file:
        try:
            df.to_csv(output_file, index=False)
            print(f"Formatted result saved to {output_file}. NB: '1 means Effector' and '0 means Non-effector'")
        except Exception as e:
            raise IOError(f"Failed to save formatted result: {e}")

    return df











# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– #





def format_T3SEpp_result(input_file, kingdom="bacteria", output_file=None):
    """
    Format T3SEpp prediction results to a standardized DataFrame suitable for downstream analysis.

    This function:
    - Loads the T3SEpp output file (tab-separated).
    - Renames relevant columns to standardized names ("Identifier" and "Prediction").
    - Drops all irrelevant columns, keeping only the identifier and prediction.
    - Converts prediction labels from "T3S"/"non-T3S" to "1"/"0".
    - Adds kingdom and program metadata columns.
    - Normalizes the kingdom string to lowercase.
    - Optionally saves the formatted DataFrame to a CSV file.

    Parameters:
    -----------
    input_file : str
        Path to the T3SEpp output file (tab-separated).

    kingdom : str, optional (default='bacteria')
        Target organism kingdom for metadata tagging.
        The value is normalized to lowercase internally.

    output_file : str, optional
        Path to save the formatted DataFrame as a CSV.
        If None, the DataFrame will not be saved.

    Returns:
    --------
    pd.DataFrame
        A DataFrame with columns: ['Identifier', 'Prediction', 'Kingdom', 'Program'].

    Raises:
    -------
    FileNotFoundError
        If the input file cannot be found.

    ValueError
        If the file cannot be read or the required columns are missing.

    IOError
        If saving the formatted DataFrame fails.

    Example:
    --------
    >>> df = format_T3SEpp_result("t3sepp_output.txt", kingdom="bacteria", output_file="t3sepp_formatted.csv")
    """
    import pandas as pd

    try:
        df = pd.read_csv(input_file, sep="\t")
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {input_file}")
    except Exception as e:
        raise ValueError(f"Error reading input file {input_file}: {e}")

    # Rename columns, check if needed columns exist
    expected_cols = {"prot", "Pred"}
    if not expected_cols.issubset(df.columns):
        missing = expected_cols - set(df.columns)
        raise ValueError(f"Missing expected columns in input file: {missing}")

    df.rename(columns={"prot": "Identifier", "Pred": "Prediction"}, inplace=True)

    # Select only the relevant columns
    try:
        df = df[["Identifier", "Prediction"]]
    except Exception as e:
        raise ValueError(f"Columns do not exist: {e}")

    replacing_prediction = {"T3S": 1, "non-T3S": 0}
    df.loc[:, "Prediction"] = df["Prediction"].astype(str).map(replacing_prediction)

    df["Kingdom"] = kingdom.lower()
    df["Program"] = "T3SEpp"
    df["Identifier"] = df["Identifier"].str.split().str[0]
    
    if output_file:
        try:
            df.to_csv(output_file, index=False)
            print(f"Formatted result saved to {output_file}. NB: '1 means Effector' and '0 means Non-effector'")
        except Exception as e:
            raise IOError(f"Failed to save formatted result: {e}")

    return df











# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– #




def merge_predictions_by_identifier(dfs, output_file=None):
    """
    Merge prediction DataFrames by 'Identifier' and return a single DataFrame.

    Each input DataFrame must have the following columns:
      - 'Identifier': the unique sequence ID.
      - 'Prediction': 0 or 1 representing non-effector or effector.
      - 'Program': name of the prediction tool (e.g., 'EffectorP', 'Deepredeff').

    The function renames the 'Prediction' column of each DataFrame to the name of the program,
    and merges them on the 'Identifier' column. Missing values are filled with 0s.

    Parameters:
    -----------
    dfs : list of pandas.DataFrame
        A list of formatted DataFrames to merge. Each should come from a format_* function.

    output_file : str, optional
        Path to save the merged DataFrame as CSV. If None, the file is not saved.

    Returns:
    --------
    pd.DataFrame
        The merged DataFrame with 'Identifier' and prediction columns for each tool.

    Example:
    --------
    >>> from fimep.preprocessing import (
    ...     format_effectorp_result,
    ...     format_deepredeff_result,
    ...     format_WideEffHunter_result,
    ...     merge_predictions_by_identifier
    ... )
    >>> df1 = format_effectorp_result("EffectorP_result.csv", kingdom="fungi", output_file=None)
    >>> df2 = format_deepredeff_result("Deepredeff_result.csv", output_file=None, kingdom="fungi")
    >>> df3 = format_WideEffHunter_result("all_seqs.fasta", "predicted_seqs.fasta", kingdom="fungi", output_file=None)
    >>> combined_df = merge_predictions_by_identifier([df1, df2, df3], output_file="merged_results.csv")
    >>> print(combined_df.head())

    Notes:
    ------
    - If identifiers do not match exactly across tools, rows will be merged using outer join and
      missing predictions will be filled with 0 (non-effector).
    - This function is not strict — mismatched identifiers will still be included.
    """
    import pandas as pd

    merged_df = None
    reference_ids = None
    reference_program = None

    for i, df in enumerate(dfs):
        # --- Check if required columns exist
        required_cols = {"Identifier", "Prediction", "Program"}
        if not required_cols.issubset(df.columns):
            raise ValueError(
                f"[ERROR] DataFrame {i} is missing required columns: {required_cols - set(df.columns)}"
            )

        # --- Get program name
        program_names = df["Program"].unique()
        if len(program_names) != 1:
            raise ValueError(f"[ERROR] DataFrame {i} must have exactly one unique 'Program' value.")
        program = program_names[0]

        
        # --- Validate that Identifier list matches reference
        current_ids = set(df["Identifier"])
        if i == 0:
            reference_ids = current_ids
            reference_program = program
        else:
            if reference_ids != current_ids:
                missing_in_current = reference_ids - current_ids
                extra_in_current = current_ids - reference_ids
                raise ValueError(
                    f"[ERROR] Mismatched 'Identifier' values between '{reference_program}' and '{program}'.\n"
                    f"Missing in '{program}': {sorted(missing_in_current)}\n"
                    f"Extra in '{program}': {sorted(extra_in_current)}"
                )

        # --- Keep only Identifier + Prediction, and rename Prediction to program name
        df_renamed = df[["Identifier", "Prediction"]].copy()
        df_renamed = df_renamed.rename(columns={"Prediction": program})

        # --- Merge into final output
        if merged_df is None:
            merged_df = df_renamed
        else:
            merged_df = pd.merge(merged_df, df_renamed, on="Identifier", how="outer")

    # --- Optionally save to file
    if output_file:
        merged_df.to_csv(output_file, index=False)
        print(f"[INFO] Merged predictions saved to {output_file}. NB: '1 means Effector' and '0 means Non-effector'")

    return merged_df






