from src.bronze.extraction import Extraction
import pandas as pd


class ResultsTransacional(Extraction):
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
            "home_score": "gols_time_casa",
            "away_score": "gols_time_visitante",
            "tournament": "torneio",
            "city": "cidade",
            "country": "pais",
            "neutral": "estadio_neutro"
        })
        return processed_data
    
    def alter_types(self, processed_data):
        processed_data["data"] = pd.to_datetime(processed_data["data"], format="%Y-%m-%d")
        processed_data["time_casa"] = processed_data["time_casa"].astype(str)
        processed_data["time_visitante"] = processed_data["time_visitante"].astype(str)
        processed_data["gols_time_casa"] = processed_data["gols_time_casa"].astype(pd.Int64Dtype())
        processed_data["gols_time_visitante"] = processed_data["gols_time_visitante"].astype(pd.Int64Dtype())
        processed_data["torneio"] = processed_data["torneio"].astype(str)
        processed_data["cidade"] = processed_data["cidade"].astype(str)
        processed_data["pais"] = processed_data["pais"].astype(str)
        processed_data["estadio_neutro"] = processed_data["estadio_neutro"].astype(bool)
        return processed_data
    

if __name__ == "__main__":
    results_transacional = ResultsTransacional()
    processed_data = results_transacional.process_data("src/data/raw/results.csv")
    processed_data = results_transacional.alter_columns_names(processed_data)
    processed_data = results_transacional.alter_types(processed_data)
    print("================ Dados Processados =================")
    print(processed_data.head())
    print("")
    print("================ Tipos de Dados =================")
    print(processed_data.dtypes)