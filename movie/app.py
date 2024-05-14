import requests
import json


query = input('Search a movie...')

url = f"https://api.themoviedb.org/3/search/movie?query={query}&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZDY0NWQ2NGZjMmI0ZmVmMmEyMDM3ZjY3N2M3ZWJjMCIsInN1YiI6IjY2NDJhZTlmM2E4ZjdmYmNjODc3YjFkMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Y-8ALgwgnbWwt2DCmgyJcCrvEuaDdyu3jnV1hH574xQ"
}

response = requests.get(url, headers=headers)

query_data = json.loads(response.text)

for i, movie in enumerate(query_data['results'][:5]):  # Usando enumerate para obter o índice e o filme
    print("Título do filme:", movie['title'])  # Acessando o título do filme
