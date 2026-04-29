# Importa la función que genera datos simulados de usuarios
from data_simulada import get_simulated_data

# Importa la librería spaCy para procesamiento de lenguaje natural
import spacy

# Importa matplotlib y configura el backend gráfico para evitar errores en Windows
import matplotlib
matplotlib.use('TkAgg')

# Importa el módulo pyplot para crear gráficas
import matplotlib.pyplot as plt

# Carga el modelo de lenguaje en español de spaCy
# Se desactivan componentes innecesarios para mejorar el rendimiento
nlp = spacy.load('es_core_news_sm', disable=["parser", "tagger", "lemmatizer"])



# RECOLECCIÓN DE DATOS

def collect_data():
    
    # Función encargada de obtener los datos simulados
    # que representan opiniones de usuarios sobre el transporte.
    
    # Retorna: ist: Lista de textos simulados
    
    return get_simulated_data()



# ANÁLISIS NLP 

def analyze_data(data):
  
    # Analiza los textos usando spaCy para identificar ubicaciones (LOC)
    # y contar la frecuencia de problemas por cada lugar.

    # Parámetros:  data (list): Lista de textos

    # Retorna: dict: Diccionario con ubicaciones y número de ocurrencias

    
    # Diccionario para almacenar resultados
    issues = {}

    # Procesa todos los textos en lote para mayor eficiencia
    docs = nlp.pipe(data)

    # Itera sobre cada documento procesado
    for doc in docs:
        # Recorre las entidades detectadas en el texto
        for ent in doc.ents:
            # Filtra solo entidades de tipo ubicación
            if ent.label_ == 'LOC':
                
                # Si la ubicación no existe en el diccionario, la inicializa
                if ent.text not in issues:
                    issues[ent.text] = 0
                
                # Incrementa el contador de problemas en esa ubicación
                issues[ent.text] += 1

    # Retorna el diccionario final
    return issues


# ==============================
# 3. PROPUESTAS
# ==============================
def propose_optimizations(issues):
    
    # Genera recomendaciones basadas en la frecuencia de problemas detectados.

    # Parámetros: issues (dict): Diccionario con ubicaciones y número de problemas

    # Retorna: list: Lista de propuestas de mejora
    
    
    # Lista para almacenar propuestas
    optimizations = []

    # Recorre cada ubicación y su número de incidencias
    for location, count in issues.items():
        
        # Si hay más de un problema, se considera relevante
        if count > 1:
            
            # Genera una recomendación
            optimizations.append(f"Aumentar frecuencia de transporte en {location}")

    # Retorna las propuestas
    return optimizations



# 4. GRÁFICA

def plot_issues(issues):
    
    # Genera una gráfica de barras con los problemas detectados
    # por ubicación y guarda la imagen en un archivo.

    # Parámetros: issues (dict): Diccionario con datos a graficar
    
    
    # Verifica si hay datos
    if not issues:
        print("No hay datos para graficar")
        return

    # Extrae nombres (ubicaciones) y valores (frecuencias)
    names = list(issues.keys())
    values = list(issues.values())

    # Crea una nueva figura
    plt.figure()

    # Genera la gráfica de barras
    plt.bar(names, values)

    # Rota las etiquetas para mejor visualización
    plt.xticks(rotation=45)

    # Agrega título a la gráfica
    plt.title("Problemas detectados por ubicación")

    # Ajusta el diseño automáticamente
    plt.tight_layout()

    # Guarda la gráfica como imagen
    plt.savefig("grafica_problemas.png")
    print("Gráfica guardada como grafica_problemas.png")

    # Muestra la gráfica en pantalla
    plt.show(block=True)



# MAIN

if __name__ == "__main__":
    
    # Punto de entrada del programa.
    # Ejecuta todo el flujo del sistema:
    # recolección, análisis, propuestas y visualización.


    # 1. Recolección de datos
    data = collect_data()
    print("Datos recolectados:")

    # Imprime cada dato recolectado
    for d in data:
        print("-", d)

    # 2. Análisis de datos
    issues = analyze_data(data)
    print("\nProblemas detectados:")
    print(issues)

    # 3. Generación de propuestas
    optimizations = propose_optimizations(issues)
    print("\nPropuestas:")

    # Imprime cada propuesta
    for o in optimizations:
        print("-", o)

    # 4. Generación de gráfica
    plot_issues(issues)