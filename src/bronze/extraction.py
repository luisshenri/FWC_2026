import pandas as pd

class Extraction:
    
    def extract(self, input_data: str):
        df = pd.read_csv(input_data)
        return df
    

if __name__ == "__main__":
    extraction = Extraction()
    df_extracted = extraction.extract("src/data/raw/former_names.csv")
    print(df_extracted.head())