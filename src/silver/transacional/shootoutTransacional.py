from src.bronze.extraction import Extraction

class ShootoutTransacional(Extraction):
    def __init__(self, goalscorers_input: Extraction):
        self.goalscorers_input = goalscorers_input

    def process_data(self):
        df = self.goalscorers_input.extract("src/data/raw/goalscorers.csv")
        return df

    def alter_columns_names(self, processed_data):
        processed_data = processed_data.rename(columns={
            "date": "data",
            "home_team": "time_casa",
            "Loser": "time_visitante",
            "winner": "vencedor",
            "first_shooter": "primeiro_batedor"
        })
        return processed_data


if __name__ == "__main__":
    shootout_transacional = ShootoutTransacional(Extraction())
    processed_data = shootout_transacional.process_data()
    processed_data = shootout_transacional.alter_columns_names(processed_data)
    print(processed_data.head())