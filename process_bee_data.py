import pandas as pd

def process_data():
    df = pd.read_csv('/home/ubuntu/meliponini_br_occurrences.csv')
    
    # Mapeamento de nomes científicos para nomes populares e raios de forrageamento
    bee_info = {
        'Tetragonisca angustula': {'popular': 'Jataí', 'radius': 600, 'color': 'yellow'},
        'Melipona quadrifasciata': {'popular': 'Mandaçaia', 'radius': 2000, 'color': 'blue'},
        'Melipona scutellaris': {'popular': 'Uruçu Nordestina', 'radius': 2000, 'color': 'orange'},
        'Melipona bicolor': {'popular': 'Guaraipo', 'radius': 1500, 'color': 'brown'},
        'Nannotrigona testaceicornis': {'popular': 'Iraí', 'radius': 500, 'color': 'gray'},
        'Trigona spinipes': {'popular': 'Irapuá', 'radius': 1000, 'color': 'black'},
        'Scaptotrigona bipunctata': {'popular': 'Tubuna', 'radius': 1000, 'color': 'purple'},
        'Plebeia remota': {'popular': 'Mirim Guaçu', 'radius': 500, 'color': 'green'},
        'Melipona fasciculata': {'popular': 'Tiúba', 'radius': 2000, 'color': 'red'},
        'Apis mellifera': {'popular': 'Apis (Abelha de Mel)', 'radius': 3000, 'color': 'gold'}
    }
    
    def get_popular_name(species):
        if pd.isna(species): return 'Outra Meliponini'
        for sci, info in bee_info.items():
            if sci in species:
                return info['popular']
        return 'Outra Meliponini'

    def get_radius(species):
        if pd.isna(species): return 500
        for sci, info in bee_info.items():
            if sci in species:
                return info['radius']
        return 500

    def get_color(species):
        if pd.isna(species): return 'gray'
        for sci, info in bee_info.items():
            if sci in species:
                return info['color']
        return 'gray'

    df['nome_popular'] = df['species'].apply(get_popular_name)
    df['raio_forrageamento'] = df['species'].apply(get_radius)
    df['cor_mapa'] = df['species'].apply(get_color)
    
    # Remover registros sem coordenadas
    df = df.dropna(subset=['decimalLatitude', 'decimalLongitude'])
    
    df.to_csv('/home/ubuntu/processed_bee_data.csv', index=False)
    print(f"Dados processados e salvos. Total: {len(df)} registros.")

if __name__ == "__main__":
    process_data()
