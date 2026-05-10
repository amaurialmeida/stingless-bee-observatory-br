#!/usr/bin/env python3
import pandas as pd
import sys

try:
    df = pd.read_csv('/home/ubuntu/processed_bee_data.csv')
    print(f"✓ Dados carregados com sucesso!")
    print(f"  - Total de registros: {len(df)}")
    print(f"  - Colunas: {', '.join(df.columns.tolist())}")
    print(f"  - Espécies únicas: {df['nome_popular'].nunique()}")
    print(f"  - Estados: {df['stateProvince'].nunique()}")
    print(f"  - Municípios: {df['municipality'].nunique()}")
    print(f"\n  Primeiras 5 linhas:")
    print(df.head())
except Exception as e:
    print(f"✗ Erro ao carregar dados: {e}")
    sys.exit(1)
