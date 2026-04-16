import kagglehub

# Download latest version
path = kagglehub.dataset_download("martj42/international-football-results-from-1872-to-2017")

print("Path to dataset files:", path)

"""
Para copiar os arquivos CSV para a pasta de dados brutos, você pode usar o seguinte comando no terminal:

cp /home/luisshenri/.cache/kagglehub/datasets/martj42/international-football-results-from-1872-to-2017/versions/110/*.csv
 /home/luisshenri/projects/projetoEngDados/src/data/raw/
"""

