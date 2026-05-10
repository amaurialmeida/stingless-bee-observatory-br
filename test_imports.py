#!/usr/bin/env python3
import sys

try:
    import streamlit
    print("✓ Streamlit OK")
except ImportError as e:
    print(f"✗ Streamlit: {e}")
    sys.exit(1)

try:
    import pandas
    print("✓ Pandas OK")
except ImportError as e:
    print(f"✗ Pandas: {e}")
    sys.exit(1)

try:
    import folium
    print("✓ Folium OK")
except ImportError as e:
    print(f"✗ Folium: {e}")
    sys.exit(1)

try:
    import plotly
    print("✓ Plotly OK")
except ImportError as e:
    print(f"✗ Plotly: {e}")
    sys.exit(1)

try:
    import streamlit_folium
    print("✓ Streamlit-Folium OK")
except ImportError as e:
    print(f"✗ Streamlit-Folium: {e}")
    sys.exit(1)

print("\n✓ Todas as dependências instaladas com sucesso!")
