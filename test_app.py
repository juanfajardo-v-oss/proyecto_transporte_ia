# Importa el framework de pruebas
import pytest

# Importa herramientas para generación de datos aleatorios
from hypothesis import given, strategies as st

# Importa funciones para las pruebas
from main import analyze_data, propose_optimizations


def test_analyze_data():
    
    # Prueba básica para verificacion de analyze_data devolviendo un diccionario.
    
    
    data = ["Problemas en Bogotá", "Retrasos en Suba"]
    result = analyze_data(data)

    # Hace Verificacion del tipo de resultado
    assert isinstance(result, dict)


@given(st.lists(st.text()))
def test_analyze_data_property(data):
    
    # Prueba basada en propiedades: 
    # Verifica que la función siempre retorne a un diccionario,
    # sin importar el contenido de entrada.
    
    
    result = analyze_data(data)
    assert isinstance(result, dict)


@given(st.dictionaries(st.text(), st.integers()))
def test_propose_optimizations(issues):
    
    # Prueba para verificar que la función de propuestas
    #siempre retorne a una lista.
    
    
    result = propose_optimizations(issues)
    assert isinstance(result, list)