import requests
import pandas as pd
import time

def download_meliponini_data():
    base_url = "https://api.gbif.org/v1/occurrence/search"
    
    # Parâmetros para Meliponini (Family: Apidae, Subfamily: Apinae, Tribe: Meliponini)
    # Meliponini taxonKey: 4334
    params = {
        'taxonKey': 4334,
        'country': 'BR',
        'hasCoordinate': 'true',
        'limit': 300, # Limitando para o exemplo, mas podemos aumentar
        'offset': 0
    }
    
    all_results = []
    
    print("Iniciando download de dados do GBIF...")
    
    for i in range(5): # Baixar as primeiras 1500 ocorrências para o protótipo
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            if not results:
                break
            all_results.extend(results)
            params['offset'] += params['limit']
            print(f"Baixados {len(all_results)} registros...")
            time.sleep(1)
        else:
            print(f"Erro na API: {response.status_code}")
            break
            
    df = pd.DataFrame(all_results)
    
    # Selecionar colunas relevantes
    columns_to_keep = [
        'species', 'scientificName', 'decimalLatitude', 'decimalLongitude', 
        'eventDate', 'municipality', 'stateProvince', 'basisOfRecord'
    ]
    
    # Verificar quais colunas existem no DF
    existing_columns = [col for col in columns_to_keep if col in df.columns]
    df_clean = df[existing_columns]
    
    df_clean.to_csv('/home/ubuntu/meliponini_br_occurrences.csv', index=False)
    print(f"Dados salvos em meliponini_br_occurrences.csv. Total: {len(df_clean)} registros.")

if __name__ == "__main__":
    download_meliponini_data()
