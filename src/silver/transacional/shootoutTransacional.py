from src.bronze.extraction import Extraction
import pandas as pd
import os
class ShootoutTransacional(Extraction):
    

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

    def save_data(self, df: pd.DataFrame) -> pd.DataFrame:
        output_dir = "src/data/silver/transacional"
        output_path = os.path.join(output_dir, "shootouts.parquet")
        os.makedirs(output_dir, exist_ok=True)
        df.to_parquet(output_path, index=False)
        print(f"Dados salvos em {output_path}")
        return df

    def run_pipeline(self, input_data: str):
        processed_data = self.process_data(input_data)
        processed_data = self.alter_columns_names(processed_data)
        processed_data = self.alter_types(processed_data)
        processed_data = self.exchange_nans(processed_data)
        self.save_data(processed_data)
        return processed_data

if __name__ == "__main__":
    shootout_transacional = ShootoutTransacional()
    processed_data = shootout_transacional.run_pipeline("src/data/raw/shootouts.csv")
    print(processed_data.head())
    print(processed_data.dtypes)