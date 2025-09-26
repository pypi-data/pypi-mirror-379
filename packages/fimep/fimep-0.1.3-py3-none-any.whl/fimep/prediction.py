



def model_prediction(input_file, output_file):
    """
    Predict effector vs non-effector proteins using a pre-trained Deep Neural Network (DNN).

    Parameters:
    ----------
    input_file : str
        Path to a CSV file containing prediction scores from kingdom-specific effector predictors.
        The file **must be one-hot encoded** using the function `encode_scale_predictions()` from the `encode` module
        (available in this package).
        
    output_file : str
        Path to write the final CSV with two columns: `Identifier`, and `Pred_Label` (Effector/Non-Effector).

    Model:
    ------
    This function uses a Keras model (`fimep_model.keras`) built into the package. No user action is required.

    Input Requirements:
    -------------------
    The input file must contain the following:
    - A column named `Identifier`
    - One-hot encoded feature columns like: `EffectorP_Effector`, `EffectorP_Non-Effector`, ..., `T3SEpp_Non-Effector`.

    If your data is **not encoded yet**, please ensure:
    - The appropriate effector prediction programs have been run **based on the pathogen kingdom**:
    
      ```
      kingdom_expected_col = {
          "bacteria" : {"Deepredeff", "EffectiveT3", "T3SEpp"},
          "fungi"    : {"EffectorP", "Deepredeff", "WideEffHunter"}, 
          "oomycete" : {"EffectorP", "Deepredeff", "WideEffHunter", "EffectorO"},
          "all"      : {"EffectorP", "EffectiveT3", "EffectorO", "Deepredeff", "WideEffHunter", "T3SEpp"}
      }
      ```

    - You must run the `encode_scale_predictions()` function from the `encode` module to convert the predictions
      into the correct format for the model.

    Output:
    -------
    A CSV file with the predicted labels for each input sequence.

    Example:
    --------
    >>> from fimep.prediction import model_prediction
    >>> model_prediction("encoded_input.csv", "final_prediction.csv")
    """

    import pandas as pd
    import numpy as np
    from pathlib import Path
    from keras.models import load_model

    # Load the model packaged with the module
    model_path = Path(__file__).parent / "fimep_model.keras"
    if not model_path.exists():
        raise FileNotFoundError(f"Model not found at {model_path}")
    dnn_model = load_model(model_path)

    # Load the input
    try:
        df = pd.read_csv(input_file)
        print(f"Loaded input file: {input_file}")
    except Exception as e:
        raise ValueError(f"Could not load input file: {e}")

    if "Identifier" not in df.columns:
        raise ValueError("Missing required column 'Identifier' in input data.")

    df_identifier = df["Identifier"]
    df = df.drop("Identifier", axis=1)

    try:
        features_test = df.to_numpy().astype(np.float32)
    except Exception as e:
        raise ValueError(f"Failed to convert input to float32: {e}")

    prediction = dnn_model.predict(features_test)
    prediction = (prediction > 0.5).astype(int)
    prediction_label = np.where(prediction == 1, "Effector", "Non-Effector")

    prediction_df = pd.DataFrame(prediction_label, columns=["Pred_Label"])
    prediction_output = pd.concat([df_identifier, prediction_df], axis=1)

    prediction_output.to_csv(output_file, index=False)
    print(f"Predictions saved to {output_file}")