import pandas as pd
import os

class ResultsMatches:

    def determine_results(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        def determine_result(row):
            if pd.isna(row["gols_time_casa"]) or pd.isna(row["gols_time_visitante"]):
                return 0
            
            if row["gols_time_casa"] > row["gols_time_visitante"]:
                return row["time_casa"]
            elif row["gols_time_casa"] < row["gols_time_visitante"]:
                return row["time_visitante"]
            else:
                return "Empate"
        df["vencedor"] = df.apply(determine_result, axis=1)
        df["vencedor"] = df["vencedor"].astype(str)

        df = df[df["vencedor"] != "0"]

        return df

    def save_data(self, df: pd.DataFrame) -> pd.DataFrame:
        output_dir = "src/data/silver/context"
        output_path = os.path.join(output_dir, "results_matches.parquet")
        os.makedirs(output_dir, exist_ok=True)
        df.to_parquet(output_path, index=False)
        print(f"Dados salvos em {output_path}")
        return df
    
    def run_pipeline(self, input: str):
        df = self.determine_results(input)
        df = self.save_data(df)
        return df

if __name__ == "__main__":
    winner_matches = ResultsMatches()
    run = winner_matches.run_pipeline("src/data/silver/context/world_cup_matches.parquet")
    print("================ Results with Winner =================")
    print(run.tail(60))
    print("")
    print("================ Tipos de Dados =================")
    print(run.dtypes)
    