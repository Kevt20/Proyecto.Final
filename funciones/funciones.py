# ============================================================
# Funciones de análisis e impacto tecnológico
# Nombre: Kevin Jiménez
# Unidad 1, 2 y 3 - Estructuras de datos, lógica y ciclos
# ============================================================


def clasificar_impacto(puntaje):
    """
    Clasifica un puntaje numérico de impacto en una categoría descriptiva.
    Utiliza estructuras condicionales (if/elif/else) - Unidad 3.
    """
    if puntaje >= 8:
        return "✅ Muy Alto"
    elif puntaje >= 6:
        return "🟢 Alto"
    elif puntaje >= 4:
        return "🟡 Moderado"
    elif puntaje >= 1:
        return "🟠 Bajo"
    else:
        return "❌ Negativo"


def mostrar_todas(lista):
    """
    Muestra todas las tecnologías disponibles con su categoría e impacto social.
    Usa ciclo for para recorrer la lista - Unidad 3.
    """
    print("\n  📋 Tecnologías disponibles:")
    print("  " + "-" * 55)
    print(f"  {'#':<4} {'Nombre':<32} {'Categoría':<15} {'Impacto'}")
    print("  " + "-" * 55)

    # Ciclo for para recorrer todas las tecnologías - Unidad 3
    for i, tech in enumerate(lista, 1):
        print(f"  {i:<4} {tech['nombre']:<32} {tech['categoria']:<15} {tech['impacto_social']}/10")

    print("  " + "-" * 55)
    print(f"  Total: {len(lista)} tecnologías registradas.")


def analizar_tecnologia(nombre, lista):
    """
    Busca y muestra el análisis completo de una tecnología específica.
    Combina ciclos y condicionales - Unidad 3.
    """
    # Búsqueda con ciclo y condicional
    encontrada = None
    for tech in lista:
        if tech["nombre"].lower() == nombre.lower():
            encontrada = tech
            break

    if encontrada is None:
        print(f"\n  ⚠️  Tecnología '{nombre}' no encontrada.")
        print("  Usa la opción 1 para ver los nombres exactos.")
        return

    t = encontrada
    print(f"\n  🔍 Análisis Completo: {t['nombre']}")
    print("  " + "=" * 45)
    print(f"  📌 Categoría: {t['categoria']}")
    print(f"  📝 Descripción: {t['descripcion']}")
    print(f"  📅 Año de auge: {t['año_auge']}")
    print()
    print(f"  📊 Impacto Social:    {t['impacto_social']:+3d}/10  {clasificar_impacto(t['impacto_social'])}")
    print(f"  💼 Impacto Laboral:   {t['impacto_laboral']:+3d}/10  {clasificar_impacto(t['impacto_laboral'])}")
    print(f"  🎓 Impacto Educación: {t['impacto_educacion']:+3d}/10  {clasificar_impacto(t['impacto_educacion'])}")
    print(f"  🏥 Impacto Salud:     {t['impacto_salud']:+3d}/10  {clasificar_impacto(t['impacto_salud'])}")

    # Calcular promedio general con ciclo - Unidad 3
    valores = [t['impacto_social'], t['impacto_laboral'],
               t['impacto_educacion'], t['impacto_salud']]
    suma = 0
    for v in valores:
        suma += v
    promedio = suma / len(valores)
    print(f"\n  📈 Promedio General: {promedio:.1f}/10")

    print("\n  ✅ Ventajas:")
    for ventaja in t["ventajas"]:
        print(f"     + {ventaja}")

    print("\n  ❌ Desventajas:")
    for desventaja in t["desventajas"]:
        print(f"     - {desventaja}")

    print("\n  📉 Tendencia de adopción (últimos 5 años):")
    años = ["2020", "2021", "2022", "2023", "2024"]
    for año, valor in zip(años, t["tendencia"]):
        barra = "█" * valor + "░" * (10 - valor)
        print(f"     {año}: [{barra}] {valor}/10")


def comparar_tecnologias(nombre1, nombre2, lista):
    """
    Compara dos tecnologías lado a lado en todos sus indicadores.
    Usa ciclos y condicionales anidados - Unidad 3.
    """
    t1, t2 = None, None

    # Ciclo para buscar ambas tecnologías
    for tech in lista:
        if tech["nombre"].lower() == nombre1.lower():
            t1 = tech
        if tech["nombre"].lower() == nombre2.lower():
            t2 = tech

    # Validación con condicionales
    if t1 is None:
        print(f"\n  ⚠️  No se encontró: '{nombre1}'")
        return
    if t2 is None:
        print(f"\n  ⚠️  No se encontró: '{nombre2}'")
        return

    print(f"\n  ⚔️  Comparación: {t1['nombre']} vs {t2['nombre']}")
    print("  " + "=" * 55)

    indicadores = [
        ("Impacto Social", "impacto_social"),
        ("Impacto Laboral", "impacto_laboral"),
        ("Impacto Educación", "impacto_educacion"),
        ("Impacto Salud", "impacto_salud"),
    ]

    victorias_t1 = 0
    victorias_t2 = 0

    for nombre_ind, clave in indicadores:
        v1 = t1[clave]
        v2 = t2[clave]

        if v1 > v2:
            ganador = f"← {t1['nombre'][:15]}"
            victorias_t1 += 1
        elif v2 > v1:
            ganador = f"{t2['nombre'][:15]} →"
            victorias_t2 += 1
        else:
            ganador = "Empate"

        print(f"  {nombre_ind:<20} {v1:+3d}  vs  {v2:+3d}   {ganador}")

    print("  " + "-" * 55)
    print(f"  Victorias: {t1['nombre'][:20]}: {victorias_t1} | {t2['nombre'][:20]}: {victorias_t2}")

    if victorias_t1 > victorias_t2:
        print(f"\n  🏆 Ganador general: {t1['nombre']}")
    elif victorias_t2 > victorias_t1:
        print(f"\n  🏆 Ganador general: {t2['nombre']}")
    else:
        print("\n  🤝 Resultado: Empate general")


def estadisticas_generales(lista):
    """
    Calcula y muestra estadísticas generales del dataset.
    Usa ciclos for y estructuras condicionales - Unidades 2 y 3.
    """
    print("\n  📊 Estadísticas Generales del Dataset")
    print("  " + "=" * 45)

    total = len(lista)
    suma_social = 0
    suma_laboral = 0
    suma_educacion = 0
    suma_salud = 0
    max_tech = lista[0]
    min_tech = lista[0]

    # Ciclo para calcular totales
    for tech in lista:
        suma_social += tech["impacto_social"]
        suma_laboral += tech["impacto_laboral"]
        suma_educacion += tech["impacto_educacion"]
        suma_salud += tech["impacto_salud"]

        # Comparar para máximo y mínimo
        if tech["impacto_social"] > max_tech["impacto_social"]:
            max_tech = tech
        if tech["impacto_social"] < min_tech["impacto_social"]:
            min_tech = tech

    print(f"  Total de tecnologías: {total}")
    print(f"\n  Promedios de impacto:")
    print(f"    Social:    {suma_social / total:.2f}/10")
    print(f"    Laboral:   {suma_laboral / total:.2f}/10")
    print(f"    Educación: {suma_educacion / total:.2f}/10")
    print(f"    Salud:     {suma_salud / total:.2f}/10")
    print(f"\n  🥇 Mayor impacto social: {max_tech['nombre']} ({max_tech['impacto_social']}/10)")
    print(f"  📉 Menor impacto social: {min_tech['nombre']} ({min_tech['impacto_social']}/10)")

    # Contar por categoría
    categorias = {}
    for tech in lista:
        cat = tech["categoria"]
        if cat in categorias:
            categorias[cat] += 1
        else:
            categorias[cat] = 1

    print("\n  Distribución por categoría:")
    for cat, count in categorias.items():
        print(f"    {cat:<20}: {count} tecnología(s)")


def buscar_por_categoria(categoria, lista):
    """
    Filtra tecnologías por categoría usando ciclo for y condicional.
    """
    resultados = []

    # Ciclo de búsqueda - Unidad 3
    for tech in lista:
        if tech["categoria"].lower() == categoria.lower():
            resultados.append(tech)

    if not resultados:
        print(f"\n  ⚠️  No se encontraron tecnologías en la categoría '{categoria}'.")
        return

    print(f"\n  🗂️  Tecnologías en categoría: {categoria}")
    print("  " + "-" * 45)
    for tech in resultados:
        print(f"  • {tech['nombre']}")
        print(f"    Impacto social: {tech['impacto_social']}/10 — {clasificar_impacto(tech['impacto_social'])}")
        print(f"    {tech['descripcion']}")
        print()
