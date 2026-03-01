# Proyecto Final - Juego de Preguntas: Tecnologia y Sociedad
# Autor: Kevin Jimenez
# Fecha: 2025
# Descripcion: Juego de preguntas sobre el impacto de las nuevas
# tecnologias en la sociedad. Integra los temas de las 4 unidades.

import random
from functools import reduce

# ----------------------------------------------------------
# UNIDAD 2 - Estructuras de datos
# Guardo las preguntas en una lista de diccionarios
# Cada pregunta tiene su texto, opciones, respuesta y categoria
# ----------------------------------------------------------

preguntas = [
    {
        "pregunta": "¿Cual es uno de los principales riesgos de la Inteligencia Artificial en el trabajo?",
        "opciones": ["A) Mejora todos los empleos", "B) Puede reemplazar empleos repetitivos", "C) No tiene ningun efecto", "D) Solo afecta a los medicos"],
        "respuesta": "B",
        "categoria": "Inteligencia Artificial",
        "dificultad": "facil"
    },
    {
        "pregunta": "¿Que son los vehiculos autonomos?",
        "opciones": ["A) Carros que vuelan", "B) Carros que se manejan solos sin conductor", "C) Carros electricos normales", "D) Carros controlados por control remoto"],
        "respuesta": "B",
        "categoria": "Transporte",
        "dificultad": "facil"
    },
    {
        "pregunta": "¿Cual es un efecto negativo de las redes sociales en la salud?",
        "opciones": ["A) Mejora la vision", "B) Genera mas empleo", "C) Puede causar ansiedad y adiccion", "D) Ayuda a dormir mejor"],
        "respuesta": "C",
        "categoria": "Redes Sociales",
        "dificultad": "facil"
    },
    {
        "pregunta": "¿Para que sirve la telemedicina?",
        "opciones": ["A) Para hacer ejercicio en linea", "B) Para recibir atencion medica a distancia", "C) Para comprar medicamentos", "D) Para estudiar medicina"],
        "respuesta": "B",
        "categoria": "Salud",
        "dificultad": "facil"
    },
    {
        "pregunta": "¿Que protege la ciberseguridad?",
        "opciones": ["A) Solo las computadoras fisicas", "B) Los datos y sistemas digitales de ataques", "C) Solo las redes sociales", "D) Los cajeros automaticos unicamente"],
        "respuesta": "B",
        "categoria": "Seguridad",
        "dificultad": "medio"
    },
    {
        "pregunta": "¿Cual es una ventaja del Internet de las Cosas?",
        "opciones": ["A) Usa menos internet", "B) Permite controlar dispositivos del hogar de forma remota", "C) Elimina la necesidad de celulares", "D) Hace mas lenta la conexion"],
        "respuesta": "B",
        "categoria": "IoT",
        "dificultad": "medio"
    },
    {
        "pregunta": "¿Que tecnologia permite hacer transacciones sin bancos tradicionales?",
        "opciones": ["A) Redes Sociales", "B) Telemedicina", "C) Blockchain", "D) GPS"],
        "respuesta": "C",
        "categoria": "Blockchain",
        "dificultad": "medio"
    },
    {
        "pregunta": "¿Cual es el mayor impacto de la IA en la educacion?",
        "opciones": ["A) Reemplaza a todos los maestros", "B) Personaliza el aprendizaje para cada estudiante", "C) Elimina las escuelas", "D) Solo sirve para hacer tareas"],
        "respuesta": "B",
        "categoria": "Inteligencia Artificial",
        "dificultad": "medio"
    },
    {
        "pregunta": "¿Que problema social generan los vehiculos autonomos?",
        "opciones": ["A) Mas trafico", "B) Contaminacion del aire", "C) Desempleo en conductores profesionales", "D) Menos carreteras"],
        "respuesta": "C",
        "categoria": "Transporte",
        "dificultad": "dificil"
    },
    {
        "pregunta": "¿Cual de estas tecnologias tuvo mayor crecimiento durante la pandemia?",
        "opciones": ["A) Vehiculos autonomos", "B) Blockchain", "C) Telemedicina", "D) Realidad Virtual"],
        "respuesta": "C",
        "categoria": "Salud",
        "dificultad": "dificil"
    },
    {
        "pregunta": "¿Que significa IoT?",
        "opciones": ["A) Internet of Technology", "B) Internet of Things", "C) Index of Tools", "D) Interface of Technology"],
        "respuesta": "B",
        "categoria": "IoT",
        "dificultad": "facil"
    },
    {
        "pregunta": "¿Cual es un riesgo de depender demasiado de la tecnologia?",
        "opciones": ["A) Mas creatividad", "B) Mejor memoria", "C) Vulnerabilidad ante fallas tecnicas", "D) Mayor independencia"],
        "respuesta": "C",
        "categoria": "Sociedad",
        "dificultad": "dificil"
    }
]

# Registro de puntajes de la sesion
historial_puntajes = []


# ----------------------------------------------------------
# UNIDAD 1 - Funciones base del programa
# Aqui defini las funciones principales que usa el juego
# ----------------------------------------------------------

def mostrar_bienvenida():
    print("\n" + "=" * 45)
    print("   JUEGO: Tecnologia y Sociedad")
    print("   Proyecto Final - Kevin Jimenez 2025")
    print("=" * 45)
    print("  Pon a prueba lo que sabes sobre")
    print("  el impacto de las nuevas tecnologias.")
    print("=" * 45)


def mostrar_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("  1. Jugar (preguntas aleatorias)")
    print("  2. Jugar por categoria")
    print("  3. Jugar por dificultad")
    print("  4. Ver mi historial de puntajes")
    print("  5. Ver estadisticas del juego")
    print("  0. Salir")
    print("----------------------")


def mostrar_categorias():
    # Uso map + lambda para sacar las categorias unicas - Unidad 4
    todas = list(map(lambda p: p["categoria"], preguntas))
    unicas = list(set(todas))
    unicas.sort()
    print("\n  Categorias disponibles:")
    for i, cat in enumerate(unicas, 1):
        print(f"    {i}. {cat}")
    return unicas


# ----------------------------------------------------------
# UNIDAD 3 - Estructuras logicas y ciclos
# Use if/elif/else para validar respuestas y while para el juego
# ----------------------------------------------------------

def hacer_pregunta(pregunta, numero, total):
    print(f"\n  Pregunta {numero} de {total}")
    print(f"  Categoria: {pregunta['categoria']} | Dificultad: {pregunta['dificultad']}")
    print(f"\n  {pregunta['pregunta']}\n")

    # Ciclo for para mostrar las opciones
    for opcion in pregunta["opciones"]:
        print(f"    {opcion}")

    # Ciclo while para validar que la respuesta sea valida
    while True:
        respuesta = input("\n  Tu respuesta (A/B/C/D): ").strip().upper()
        if respuesta in ["A", "B", "C", "D"]:
            break
        else:
            print("  Solo puedes escribir A, B, C o D.")

    # Condicional para saber si acerto o no
    if respuesta == pregunta["respuesta"]:
        print("  Correcto!")
        return True
    else:
        print(f"  Incorrecto. La respuesta era: {pregunta['respuesta']}")
        return False


def jugar(lista_preguntas, modo=""):
    if not lista_preguntas:
        print("\n  No hay preguntas para este filtro.")
        return

    # Mezclo las preguntas aleatoriamente
    seleccion = lista_preguntas.copy()
    random.shuffle(seleccion)

    # Limito a 5 preguntas por ronda
    if len(seleccion) > 5:
        seleccion = seleccion[:5]

    correctas = 0
    total = len(seleccion)

    print(f"\n  {'Modo: ' + modo if modo else 'Modo: Aleatorio'}")
    print(f"  Responde {total} preguntas. Suerte!\n")

    # Ciclo for para recorrer cada pregunta de la ronda
    for i, pregunta in enumerate(seleccion, 1):
        if hacer_pregunta(pregunta, i, total):
            correctas += 1
        input("  Presiona Enter para continuar...")

    # Calculo el puntaje final
    puntaje = round((correctas / total) * 100)

    print("\n" + "=" * 40)
    print("  FIN DE LA RONDA")
    print(f"  Correctas: {correctas} de {total}")
    print(f"  Puntaje:   {puntaje}/100")

    # Condicional para mostrar un mensaje segun el resultado
    if puntaje == 100:
        print("  Perfecto! Lo sabias todo.")
    elif puntaje >= 60:
        print("  Bien hecho, aprobaste!")
    else:
        print("  Necesitas repasar un poco mas.")

    print("=" * 40)

    # Guardo el resultado en el historial
    historial_puntajes.append({
        "modo": modo if modo else "Aleatorio",
        "correctas": correctas,
        "total": total,
        "puntaje": puntaje
    })


def jugar_por_categoria():
    categorias = mostrar_categorias()
    opcion = input("\n  Escribe el numero de la categoria: ").strip()

    # Condicional para validar que eligio bien
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(categorias):
        print("  Opcion no valida.")
        return

    categoria_elegida = categorias[int(opcion) - 1]

    # filter para quedarme solo con las preguntas de esa categoria - Unidad 4
    filtradas = list(filter(lambda p: p["categoria"] == categoria_elegida, preguntas))
    jugar(filtradas, modo=f"Categoria: {categoria_elegida}")


def jugar_por_dificultad():
    print("\n  Elige la dificultad:")
    print("    1. Facil")
    print("    2. Medio")
    print("    3. Dificil")
    opcion = input("\n  Tu eleccion: ").strip()

    # Condicional para asignar la dificultad elegida
    if opcion == "1":
        nivel = "facil"
    elif opcion == "2":
        nivel = "medio"
    elif opcion == "3":
        nivel = "dificil"
    else:
        print("  Opcion no valida.")
        return

    # filter + lambda para filtrar por dificultad - Unidad 4
    filtradas = list(filter(lambda p: p["dificultad"] == nivel, preguntas))
    jugar(filtradas, modo=f"Dificultad: {nivel}")


# ----------------------------------------------------------
# UNIDAD 4 - Programacion Funcional
# Use filter, map, lambda y reduce para procesar los datos
# ----------------------------------------------------------

def ver_historial():
    if not historial_puntajes:
        print("\n  Todavia no has jugado ninguna ronda.")
        return

    print("\n--- Tu historial de puntajes ---")

    # Ciclo for para mostrar cada partida
    for i, partida in enumerate(historial_puntajes, 1):
        print(f"  Ronda {i} | {partida['modo']}")
        print(f"    Correctas: {partida['correctas']}/{partida['total']} | Puntaje: {partida['puntaje']}/100")

    # reduce para calcular el promedio de todos los puntajes - Unidad 4
    suma = reduce(lambda acum, p: acum + p["puntaje"], historial_puntajes, 0)
    promedio = round(suma / len(historial_puntajes))
    print(f"\n  Promedio general: {promedio}/100")


def ver_estadisticas():
    print("\n--- Estadisticas del juego ---")

    # map para sacar las categorias de todas las preguntas - Unidad 4
    todas_categorias = list(map(lambda p: p["categoria"], preguntas))

    # filter para contar faciles, medias y dificiles - Unidad 4
    faciles  = list(filter(lambda p: p["dificultad"] == "facil",  preguntas))
    medias   = list(filter(lambda p: p["dificultad"] == "medio",  preguntas))
    dificiles = list(filter(lambda p: p["dificultad"] == "dificil", preguntas))

    print(f"  Total de preguntas: {len(preguntas)}")
    print(f"  Faciles:   {len(faciles)}")
    print(f"  Medias:    {len(medias)}")
    print(f"  Dificiles: {len(dificiles)}")

    # Cuento preguntas por categoria con un ciclo - Unidad 3
    conteo = {}
    for cat in todas_categorias:
        if cat in conteo:
            conteo[cat] += 1
        else:
            conteo[cat] = 1

    print("\n  Preguntas por categoria:")
    for cat, cantidad in conteo.items():
        print(f"    {cat}: {cantidad}")

    # sorted + lambda para ver el ranking de categorias - Unidad 4
    ranking = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
    print(f"\n  Categoria con mas preguntas: {ranking[0][0]}")


# ----------------------------------------------------------
# Menu principal del juego
# ----------------------------------------------------------

def main():
    mostrar_bienvenida()

    while True:
        mostrar_menu()
        opcion = input("\n  Elige una opcion: ").strip()

        if opcion == "1":
            jugar(preguntas)
        elif opcion == "2":
            jugar_por_categoria()
        elif opcion == "3":
            jugar_por_dificultad()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            ver_estadisticas()
        elif opcion == "0":
            print("\n  Hasta luego! Gracias por jugar.\n")
            break
        else:
            print("\n  Esa opcion no existe, intenta de nuevo.")

        input("\n  Presiona Enter para volver al menu...")


main()
