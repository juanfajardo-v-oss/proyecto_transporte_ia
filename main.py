from data_simulada import get_simulated_data
import spacy
import matplotlib.pyplot as plt

# 🔥 spaCy optimizado (más rápido y estable)
nlp = spacy.load('es_core_news_sm', disable=["parser", "tagger", "lemmatizer"])


# ==============================
# 1. RECOLECCIÓN DE DATOS
# ==============================
def collect_data():
    return get_simulated_data()


# ==============================
# 2. ANÁLISIS NLP (OPTIMIZADO)
# ==============================
def analyze_data(data):
    issues = {}

    # Procesamiento en lote (más rápido)
    docs = nlp.pipe(data)

    for doc in docs:
        for ent in doc.ents:
            if ent.label_ == 'LOC':
                if ent.text not in issues:
                    issues[ent.text] = 0
                issues[ent.text] += 1

    return issues


# ==============================
# 3. PROPUESTAS
# ==============================
def propose_optimizations(issues):
    optimizations = []

    for location, count in issues.items():
        if count > 1:
            optimizations.append(f"Aumentar frecuencia de transporte en {location}")

    return optimizations


# ==============================
# 4. GRÁFICA (SIN ERRORES)
# ==============================
def plot_issues(issues):
    if not issues:
        print("No hay datos para graficar")
        return

    names = list(issues.keys())
    values = list(issues.values())

    plt.figure()
    plt.bar(names, values)
    plt.xticks(rotation=45)
    plt.title("Problemas detectados por ubicación")

    plt.tight_layout()

    # ✔ Guardar imagen para el informe
    plt.savefig("grafica_problemas.png")
    print("Gráfica guardada como grafica_problemas.png")

    # ✔ Cerrar para evitar errores de ventana
    plt.close()


# ==============================
# MAIN
# ==============================
if __name__ == "__main__":

    # 1. Recolección
    data = collect_data()
    print("Datos recolectados:")
    for d in data:
        print("-", d)

    # 2. Análisis
    issues = analyze_data(data)
    print("\nProblemas detectados:")
    print(issues)

    # 3. Propuestas
    optimizations = propose_optimizations(issues)
    print("\nPropuestas:")
    for o in optimizations:
        print("-", o)

    # 4. Gráfica
    plot_issues(issues)