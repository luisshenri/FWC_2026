from src.bronze.extraction import Extraction
import pandas as pd
class ShootoutTransacional(Extraction):
    def __init__(self):
        pass

    def process_data(self, input_data: str):
        df = self.extract(input_data)
        return df

    def alter_columns_names(self, processed_data):
        processed_data = processed_data.rename(columns={
            "date": "data",
            "home_team": "time_casa",
            "away_team": "time_visitante",
            "winner": "vencedor",
            "first_shooter": "primeiro_batedor"
        })
        return processed_data
    
    def alter_types(self, processed_data):
        processed_data["data"] = pd.to_datetime(processed_data["data"], format="%Y-%m-%d")
        processed_data["time_casa"] = processed_data["time_casa"].astype(str)
        processed_data["time_visitante"] = processed_data["time_visitante"].astype(str)
        processed_data["vencedor"] = processed_data["vencedor"].astype(str)
        processed_data["primeiro_batedor"] = processed_data["primeiro_batedor"].astype(str)
        return processed_data
    
    def exchange_nans(self, processed_data):
        processed_data["primeiro_batedor"] = processed_data["primeiro_batedor"].fillna("NULL")
        return processed_data



if __name__ == "__main__":
    shootout_transacional = ShootoutTransacional()
    processed_data = shootout_transacional.process_data("src/data/raw/shootouts.csv")
    processed_data = shootout_transacional.alter_columns_names(processed_data)
    processed_data = shootout_transacional.alter_types(processed_data)
    processed_data = shootout_transacional.exchange_nans(processed_data)
    print(processed_data.head())
    print(processed_data.dtypes)