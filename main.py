# ============================================================
# TechImpact Explorer - Programa Principal
# Autor: Kevin Jiménez
# Descripción: Exploración del impacto de tecnologías emergentes
#              en la sociedad mediante análisis y visualización.
# ============================================================

from datos.tecnologias import tecnologias
from funciones.analisis import (
    mostrar_todas,
    analizar_tecnologia,
    comparar_tecnologias,
    estadisticas_generales,
    buscar_por_categoria
)
from funciones.funcional import (
    filtrar_alto_impacto,
    promedio_funcional,
    ranking_funcional,
    resumen_funcional
)
from visualizacion.graficas import (
    grafica_impacto_comparativo,
    grafica_tendencia
)
from reportes.exportar import exportar_reporte


def mostrar_menu():
    print("\n" + "=" * 45)
    print("       🌐  TechImpact Explorer  🌐")
    print("=" * 45)
    print("  1. Ver todas las tecnologías")
    print("  2. Analizar una tecnología")
    print("  3. Comparar dos tecnologías")
    print("  4. Estadísticas generales")
    print("  5. Buscar por categoría")
    print("  6. Tecnologías de alto impacto")
    print("  7. Ranking de impacto social")
    print("  8. Generar gráfica comparativa")
    print("  9. Generar gráfica de tendencia")
    print(" 10. Exportar reporte completo")
    print("  0. Salir")
    print("=" * 45)


def main():
    print("\n  Bienvenido a TechImpact Explorer")
    print("  Visualizando el futuro tecnológico...")

    while True:
        mostrar_menu()
        opcion = input("\n  Selecciona una opción: ").strip()

        if opcion == "1":
            mostrar_todas(tecnologias)

        elif opcion == "2":
            nombre = input("  Nombre de la tecnología: ").strip()
            analizar_tecnologia(nombre, tecnologias)

        elif opcion == "3":
            t1 = input("  Primera tecnología: ").strip()
            t2 = input("  Segunda tecnología: ").strip()
            comparar_tecnologias(t1, t2, tecnologias)

        elif opcion == "4":
            estadisticas_generales(tecnologias)

        elif opcion == "5":
            print("\n  Categorías disponibles: automatizacion, comunicacion,")
            print("  seguridad, educacion, salud, transporte")
            cat = input("  Ingresa la categoría: ").strip()
            buscar_por_categoria(cat, tecnologias)

        elif opcion == "6":
            umbral = input("  Umbral de impacto (default 7): ").strip()
            umbral = int(umbral) if umbral.isdigit() else 7
            resultados = filtrar_alto_impacto(tecnologias, umbral)
            if resultados:
                print(f"\n  🔥 Tecnologías con impacto social >= {umbral}:")
                for t in resultados:
                    print(f"     • {t['nombre']} — Impacto: {t['impacto_social']}/10")
            else:
                print("  No se encontraron tecnologías con ese umbral.")

        elif opcion == "7":
            print("\n  📊 Ranking por Impacto Social:")
            ranking = ranking_funcional(tecnologias)
            for i, t in enumerate(ranking, 1):
                print(f"  {i:2}. {t['nombre']:<30} {t['impacto_social']}/10")

        elif opcion == "8":
            grafica_impacto_comparativo(tecnologias)

        elif opcion == "9":
            nombre = input("  Tecnología para ver tendencia: ").strip()
            grafica_tendencia(nombre, tecnologias)

        elif opcion == "10":
            promedio = promedio_funcional(tecnologias)
            ranking = ranking_funcional(tecnologias)
            altos = filtrar_alto_impacto(tecnologias, 7)
            resumen = resumen_funcional(tecnologias)
            exportar_reporte(tecnologias, promedio, ranking, altos, resumen)

        elif opcion == "0":
            print("\n  ¡Hasta pronto! 👋")
            print("  Reflexiona sobre el impacto tecnológico en tu vida.\n")
            break

        else:
            print("  ⚠️  Opción no válida. Intenta de nuevo.")

        input("\n  Presiona Enter para continuar...")


if __name__ == "__main__":
    main()
