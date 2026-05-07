import pandas as pd
from src.bronze.extraction import Extraction
import os

class goalscorersTransacional(Extraction):

    def process_data(self, input_data: str):
        df = self.extract(input_data)
        return df
    
    def alter_columns_names(self, processed_data):
        processed_data = processed_data.rename(columns={
            "date": "data",
            "home_team": "time_casa",
            "away_team": "time_visitante",
            "team": "time_marcador",
            "scorer": "jogador_marcador",
            "minute": "minuto_marcado",
            "own_goal": "gol_contra",
            "penalty": "gol_penalti"
        })
        return processed_data
    
    def alter_types(self, processed_data):
        processed_data["data"] = pd.to_datetime(processed_data["data"], format="%Y-%m-%d")
        processed_data["time_casa"] = processed_data["time_casa"].astype(str)
        processed_data["time_visitante"] = processed_data["time_visitante"].astype(str)
        processed_data["time_marcador"] = processed_data["time_marcador"].astype(str)
        processed_data["jogador_marcador"] = processed_data["jogador_marcador"].astype(str)
        processed_data["minuto_marcado"] = processed_data["minuto_marcado"].astype(pd.Int64Dtype())
        processed_data["gol_contra"] = processed_data["gol_contra"].astype(bool)
        processed_data["gol_penalti"] = processed_data["gol_penalti"].astype(bool)
        return processed_data
    
    def save_data(self, df: pd.DataFrame) -> pd.DataFrame:
        output_dir = "src/data/silver/transacional"
        output_path = os.path.join(output_dir, "goalscorers.parquet")
        os.makedirs(output_dir, exist_ok=True)
        df.to_parquet(output_path, index=False)
        print(f"Dados salvos em {output_path}")
        return df

    def run_pipeline(self, input_data: str):
        processed_data = self.process_data(input_data)
        processed_data = self.alter_columns_names(processed_data)
        processed_data = self.alter_types(processed_data)
        self.save_data(processed_data)
        return processed_data

if __name__ == "__main__":
    goalscorers_transacional = goalscorersTransacional()
    processed_data = goalscorers_transacional.run_pipeline("src/data/raw/goalscorers.csv")
    print("================ Dados Processados =================")
    print(processed_data.tail())
    print("")
    print("================ Tipos de Dados =================")
    print(processed_data.dtypes)