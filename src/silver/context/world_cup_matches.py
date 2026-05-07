import pandas as pd
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WorldCupMatches():
    
    def world_cup_matches(self, process_data: pd.DataFrame) -> pd.DataFrame:
        df = process_data.copy()
        # Substitui o nome do torneio para as eliminatórias da FIFA, pois o nome original estava em conflito com o nome da Copa do Mundo
        qualifications = df["torneio"].str.contains("FIFA World Cup qualification", na=False)
        df.loc[qualifications, "torneio"] = "Eliminatorias FIFA"

        # Filtra apenas partidas da Copa do Mundo
        world_cup = df["torneio"].str.contains("FIFA World Cup", na=False)
        world_cup_matches = df[world_cup]

        return world_cup_matches

    def teams_in_world_cup_2026(self, world_cup_matches: pd.DataFrame) -> pd.DataFrame:
        # Filtra as partidas da Copa do Mundo de 2026.
        teams_2026 = world_cup_matches[world_cup_matches["data"].dt.month == 6][world_cup_matches["data"].dt.year == 2026][world_cup_matches["torneio"].str.contains("FIFA World Cup")]
         
        return teams_2026
    
    def save_data(self, df: pd.DataFrame) -> pd.DataFrame:
        output_dir = "src/data/silver/context"
        output_path = os.path.join(output_dir, "world_cup_matches.parquet")
        os.makedirs(output_dir, exist_ok=True)
        df.to_parquet(output_path, index=False)
        logger.info(f"Dados salvos em {output_path}")
        return df
    
    def run_pipeline(self, input_data: str):
        # Executa o pipeline de processamento e retorna os times que participarão da Copa do Mundo de 2026.
        world_cup_matches = self.world_cup_matches(input_data)
        teams_2026 = self.teams_in_world_cup_2026(world_cup_matches)
        self.save_data(world_cup_matches)
        return world_cup_matches


if __name__ == "__main__":
    df_results = pd.read_parquet("src/data/silver/transacional/results.parquet")
    df = WorldCupMatches()
    world_cup_matches = df.run_pipeline(df_results)

    #teams_2026 = df.teams_in_world_cup_2026(world_cup_matches)
    #total = df.world_cup_matches(df_results)
    #yugoslavia_matches = df.world_cup_matches(df_results[df_results["time_casa"] == "Yugoslavia"])
    #yugoslavia = df.world_cup_matches(df_results[df_results["time_visitante"] == "Yugoslavia"])


    print("================ World Cup Matches =================")
    print(world_cup_matches.head(60))
    print("")
    print("================ Tipos de Dados =================")
    print(world_cup_matches.dtypes)
