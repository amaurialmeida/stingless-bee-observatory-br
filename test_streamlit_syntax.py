#!/usr/bin/env python3
import sys
import ast

try:
    with open('/home/ubuntu/app_streamlit.py', 'r') as f:
        code = f.read()
    
    ast.parse(code)
    print("✓ Sintaxe do Streamlit OK - Nenhum erro de sintaxe encontrado!")
    
except SyntaxError as e:
    print(f"✗ Erro de sintaxe: {e}")
    sys.exit(1)
except Exception as e:
    print(f"✗ Erro: {e}")
    sys.exit(1)
