# ============================================================
#  visualización con matplotlib
# Nombre: Kevin Jiménez
# Unidad 3 - Visualización de datos tecnológicos
# ============================================================

try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    MATPLOTLIB_DISPONIBLE = True
except ImportError:
    MATPLOTLIB_DISPONIBLE = False
    print("  ⚠️  matplotlib no está instalado. Ejecuta: pip install matplotlib")


def _verificar_matplotlib():
    """Verifica que matplotlib esté disponible antes de graficar."""
    if not MATPLOTLIB_DISPONIBLE:
        print("  ❌ No se puede generar la gráfica: matplotlib no instalado.")
        print("     Ejecuta: pip install matplotlib")
        return False
    return True


def grafica_impacto_comparativo(lista):
    """
    Genera una gráfica de barras comparando el impacto social
    de todas las tecnologías del dataset.
    """
    if not _verificar_matplotlib():
        return

    # Extraer datos para la gráfica
    nombres = [t["nombre"].replace(" ", "\n") for t in lista]
    impactos_sociales = [t["impacto_social"] for t in lista]
    impactos_educacion = [t["impacto_educacion"] for t in lista]
    impactos_laborales = [t["impacto_laboral"] for t in lista]

    # Asignar colores según nivel de impacto social
    colores = []
    for imp in impactos_sociales:
        if imp >= 8:
            colores.append("#2ecc71")   # verde
        elif imp >= 6:
            colores.append("#f39c12")   # naranja
        else:
            colores.append("#e74c3c")   # rojo

    x = range(len(lista))
    ancho = 0.28

    fig, ax = plt.subplots(figsize=(16, 7))
    fig.patch.set_facecolor("#1a1a2e")
    ax.set_facecolor("#16213e")

    # Barras agrupadas
    barras1 = ax.bar([i - ancho for i in x], impactos_sociales,
                     width=ancho, label="Impacto Social", color="#2ecc71", alpha=0.85)
    barras2 = ax.bar([i for i in x], impactos_educacion,
                     width=ancho, label="Impacto Educación", color="#3498db", alpha=0.85)
    barras3 = ax.bar([i + ancho for i in x], impactos_laborales,
                     width=ancho, label="Impacto Laboral", color="#e74c3c", alpha=0.85)

    # Etiquetas de valor sobre cada barra
    for barra in [*barras1, *barras2, *barras3]:
        altura = barra.get_height()
        ax.text(barra.get_x() + barra.get_width() / 2, altura + 0.1,
                f"{int(altura):+d}", ha="center", va="bottom",
                fontsize=7, color="white", fontweight="bold")

    # Estilo del gráfico
    ax.set_title("🌐 TechImpact Explorer — Comparativa de Impacto Tecnológico",
                 color="white", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Tecnología", color="#aaaaaa", fontsize=10)
    ax.set_ylabel("Puntaje de Impacto (-10 a +10)", color="#aaaaaa", fontsize=10)
    ax.set_xticks(list(x))
    ax.set_xticklabels(nombres, color="white", fontsize=8)
    ax.set_ylim(-11, 12)
    ax.axhline(y=0, color="white", linewidth=0.8, linestyle="--", alpha=0.5)
    ax.tick_params(colors="white")
    ax.legend(facecolor="#0f3460", labelcolor="white", fontsize=9)
    ax.spines["bottom"].set_color("#444")
    ax.spines["left"].set_color("#444")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    nombre_archivo = "grafica_impacto_comparativo.png"
    plt.savefig(nombre_archivo, dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.show()
    print(f"\n  ✅ Gráfica guardada como '{nombre_archivo}'")


def grafica_tendencia(nombre_tech, lista):
    """
    Genera una gráfica de línea mostrando la tendencia de adopción
    de una tecnología específica en los últimos 5 años.
    """
    if not _verificar_matplotlib():
        return

    # Buscar la tecnología
    encontrada = None
    for tech in lista:
        if tech["nombre"].lower() == nombre_tech.lower():
            encontrada = tech
            break

    if encontrada is None:
        print(f"\n  ⚠️  Tecnología '{nombre_tech}' no encontrada.")
        return

    años = [2020, 2021, 2022, 2023, 2024]
    tendencia = encontrada["tendencia"]

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("#1a1a2e")
    ax.set_facecolor("#16213e")

    # Línea de tendencia
    ax.plot(años, tendencia, marker="o", linewidth=2.5,
            color="#00d2ff", markersize=8, markerfacecolor="#ffffff")

    # Rellenar área bajo la curva
    ax.fill_between(años, tendencia, alpha=0.2, color="#00d2ff")

    # Etiquetas en cada punto
    for año, valor in zip(años, tendencia):
        ax.text(año, valor + 0.2, f"{valor}/10", ha="center",
                fontsize=10, color="white", fontweight="bold")

    ax.set_title(f"📈 Tendencia de Adopción — {encontrada['nombre']}",
                 color="white", fontsize=13, fontweight="bold")
    ax.set_xlabel("Año", color="#aaaaaa", fontsize=10)
    ax.set_ylabel("Nivel de Adopción (1-10)", color="#aaaaaa", fontsize=10)
    ax.set_ylim(0, 11)
    ax.set_xticks(años)
    ax.tick_params(colors="white")
    ax.spines["bottom"].set_color("#444")
    ax.spines["left"].set_color("#444")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    nombre_archivo = f"tendencia_{encontrada['nombre'].replace(' ', '_').lower()}.png"
    plt.savefig(nombre_archivo, dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.show()
    print(f"\n  ✅ Gráfica guardada como '{nombre_archivo}'")


def grafica_radar_impacto(nombre_tech, lista):
    """
    (Bonus) Genera un gráfico de radar con los 4 indicadores de una tecnología.
    """
    if not _verificar_matplotlib():
        return

    import numpy as np

    encontrada = None
    for tech in lista:
        if tech["nombre"].lower() == nombre_tech.lower():
            encontrada = tech
            break

    if not encontrada:
        print(f"  ⚠️  No se encontró '{nombre_tech}'")
        return

    categorias = ["Social", "Laboral", "Educación", "Salud"]
    valores = [
        encontrada["impacto_social"],
        max(encontrada["impacto_laboral"], 0),  # mínimo 0 para radar
        encontrada["impacto_educacion"],
        encontrada["impacto_salud"]
    ]
    valores += valores[:1]  # cerrar el polígono

    angulos = [n / float(len(categorias)) * 2 * 3.14159 for n in range(len(categorias))]
    angulos += angulos[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor("#1a1a2e")
    ax.set_facecolor("#16213e")

    ax.plot(angulos, valores, linewidth=2, color="#2ecc71")
    ax.fill(angulos, valores, alpha=0.3, color="#2ecc71")
    ax.set_xticks(angulos[:-1])
    ax.set_xticklabels(categorias, color="white", fontsize=11)
    ax.set_ylim(0, 10)
    ax.set_title(f"Radar — {encontrada['nombre']}", color="white",
                 fontsize=12, fontweight="bold", pad=20)
    ax.tick_params(colors="#888888")

    plt.tight_layout()
    nombre_archivo = f"radar_{encontrada['nombre'].replace(' ', '_').lower()}.png"
    plt.savefig(nombre_archivo, dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.show()
    print(f"\n  ✅ Gráfica radar guardada como '{nombre_archivo}'")
