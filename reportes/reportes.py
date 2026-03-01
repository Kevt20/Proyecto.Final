# ============================================================
# Nombre: Kevin Jiménez
# Unidad 2 y 4 - Manejo de archivos y programación funcional
# ============================================================

from datetime import datetime


def exportar_reporte(lista, promedio, ranking, alto_impacto, resumen):
    """
    Genera un reporte completo del análisis tecnológico y lo guarda como .txt.
    Integra datos de análisis y resultados de programación funcional.
    """
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nombre_archivo = f"reporte_techimpact_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    lineas = []

   
    lineas.append("=" * 60)
    lineas.append("        TECHIMPACT EXPLORER — REPORTE DE ANÁLISIS")
    lineas.append("=" * 60)
    lineas.append(f"  Generado el: {fecha_hora}")
    lineas.append(f"  Autor: Kevin Jiménez")
    lineas.append(f"  Proyecto: El Impacto de las Nuevas Tecnologías")
    lineas.append("=" * 60)

    # Resumen general
    lineas.append("")
    lineas.append("  RESUMEN GENERAL (Programación Funcional - reduce)")
    lineas.append("  " + "-" * 45)
    lineas.append(f"  Total de tecnologías analizadas: {resumen['total']}")
    lineas.append(f"  Promedio de impacto social:      {promedio}/10")
    lineas.append(f"  Tecnología de mayor impacto:     {resumen['mayor_impacto']}")
    lineas.append(f"  Tecnología de menor impacto:     {resumen['menor_impacto']}")

    # Ranking (sorted + lambda)
    lineas.append("")
    lineas.append("  RANKING POR IMPACTO SOCIAL (sorted + lambda)")
    lineas.append("  " + "-" * 45)
    for i, tech in enumerate(ranking, 1):
        barra = "█" * tech["impacto_social"] + "░" * (10 - tech["impacto_social"])
        lineas.append(f"  {i:2}. {tech['nombre']:<32} [{barra}] {tech['impacto_social']}/10")

    # Alto impacto (filter + lambda)
    lineas.append("")
    lineas.append("  TECNOLOGÍAS DE ALTO IMPACTO (filter + lambda, umbral >= 7)")
    lineas.append("  " + "-" * 45)
    if alto_impacto:
        for tech in alto_impacto:
            lineas.append(f"  ✓ {tech['nombre']} — {tech['descripcion'][:50]}...")
    else:
        lineas.append("  No se encontraron tecnologías con ese criterio.")

    # Amenaza laboral (filter)
    lineas.append("")
    lineas.append("  TECNOLOGÍAS CON IMPACTO LABORAL NEGATIVO")
    lineas.append("  " + "-" * 45)
    amenazas = [t for t in lista if t["impacto_laboral"] < 0]
    if amenazas:
        for tech in amenazas:
            lineas.append(f"  ⚠ {tech['nombre']:<30} Laboral: {tech['impacto_laboral']}/10")
    else:
        lineas.append("  Ninguna tecnología tiene impacto laboral negativo.")

    # Detalle completo (map)
    lineas.append("")
    lineas.append("  DETALLE COMPLETO POR TECNOLOGÍA (map)")
    lineas.append("  " + "-" * 45)
    for tech in lista:
        promedio_tech = round(
            (tech["impacto_social"] + tech["impacto_laboral"] +
             tech["impacto_educacion"] + tech["impacto_salud"]) / 4, 1
        )
        lineas.append(f"  • {tech['nombre']} ({tech['categoria']})")
        lineas.append(f"    Social: {tech['impacto_social']:+d}  Laboral: {tech['impacto_laboral']:+d}  "
                      f"Educación: {tech['impacto_educacion']:+d}  Salud: {tech['impacto_salud']:+d}  "
                      f"Promedio: {promedio_tech}")

    # Conclusiones
    lineas.append("")
    lineas.append("=" * 60)
    lineas.append("  CONCLUSIONES")
    lineas.append("=" * 60)
    lineas.append("")
    lineas.append("  El análisis muestra que las nuevas tecnologías tienen un")
    lineas.append("  impacto mixto en la sociedad. Mientras que áreas como la")
    lineas.append("  educación y la salud se benefician enormemente, el mercado")
    lineas.append("  laboral enfrenta desafíos significativos por la automatización.")
    lineas.append("")
    lineas.append("  Es fundamental que la sociedad adopte estas tecnologías de")
    lineas.append("  forma consciente, promoviendo la educación digital y políticas")
    lineas.append("  que protejan a los trabajadores durante la transición.")
    lineas.append("")
    lineas.append("=" * 60)
    lineas.append("  Fin del reporte — TechImpact Explorer by Kevin Jiménez")
    lineas.append("=" * 60)

    # Escribir el archivo
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for linea in lineas:
            archivo.write(linea + "\n")

    print(f"\n  ✅ Reporte exportado exitosamente: '{nombre_archivo}'")
    print(f"  📄 El archivo se guardó en el directorio actual.")
    return nombre_archivo
