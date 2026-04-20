import pandas as pd
from src.bronze.extraction import Extraction

class FormatNames(Extraction):
    def __init__(self):
        pass
    
    def process_data(self, input_data: str):
        df = self.extract(input_data)
        return df
    
    def join_names(self, processed_data):
        former_name = pd.read_csv("src/data/raw/former_names.csv")
        altered_data = former_name.loc[:, ["current", "former"]]
        if processed_data["home_team"].equals(altered_data["former"]):
            processed_data["home_team"] = altered_data["current"]
        if processed_data["away_team"].equals(altered_data["former"]):
            processed_data["away_team"] = altered_data["current"]

        return processed_data





if __name__ == "__main__":
    format_names = FormatNames()
    processed_data = format_names.process_data("src/data/raw/results.csv")
    altered_data = format_names.join_names(processed_data)
    print(altered_data)