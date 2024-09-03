import pandas as pd

def load_data(file_path):
    """
    Load the dataset into a Pandas DataFrame.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - df (pd.DataFrame): Loaded DataFrame.
    """
    df = pd.read_csv(file_path)
    return df