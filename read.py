import util
import pandas as pd


def read(file_path:str):
    if not util.is_file(file_path):
        raise Exception(f"{file_path} not exist.\nGenerate report or making sure root path is correct")

    df = pd.read_csv(file_path, keep_default_na=False, engine = "python")
    print(df.to_string())
    return df
