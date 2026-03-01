# Análisis Proyecto - Juego de Tecnología y Sociedad

Estudiante: Kevin Jimenez
Curso: Lógica de Programación
Fecha: 28 de Febrero 2026

---

## Introducción

Este documento explica lo que hice en mi proyecto y por qué lo hice así. Es un juego de preguntas sobre tecnología y su impacto en la sociedad, programado para practicar lo que estamos aprendiendo en clase.

---

## ¿Qué quería lograr?

Mi objetivo principal era hacer un programa que funcionara y que usara las cosas que estamos viendo en clase:

- Bucles (while y for)
- Condicionales (if, elif, else)
- Funciones
- Programación funcional (filter, map, lambda, reduce)
- Estructuras de datos (listas y diccionarios)

También quería que fuera algo que realmente se pudiera jugar y que tuviera un tema relacionado con la materia, que es el impacto de las nuevas tecnologías en la sociedad.

---

## ¿Cómo lo desarrollé?

**Paso 1: La idea**

Primero pensé qué tipo de programa hacer. Me decidí por un juego de preguntas porque es interactivo y me permite usar todas las estructuras que necesito demostrar, además de que el tema encaja perfecto con lo que pide el proyecto.

**Paso 2: El banco de preguntas**

Empecé creando el banco de preguntas usando listas de diccionarios. Cada pregunta tiene su texto, las cuatro opciones, la respuesta correcta, la categoría y el nivel de dificultad.

**Paso 3: Las funciones del juego**

Después fui armando las funciones principales:

- Mostrar el menú
- Hacer una pregunta y validar la respuesta
- Calcular el puntaje al final de cada ronda
- Guardar el historial de partidas

**Paso 4: Los modos de juego**

Al final agregué tres modos: preguntas aleatorias, por categoría y por dificultad, para que el usuario pueda elegir cómo quiere jugar.

---

## Estructuras de programación que usé

### 1. Estructuras repetitivas (for y while)

**¿Dónde las usé?**

- En el menú principal para que siga funcionando hasta que el usuario quiera salir
- En el juego para recorrer cada pregunta de la ronda
- Para validar que la respuesta sea A, B, C o D

Ejemplo del código:

```python
for i, pregunta in enumerate(seleccion, 1):
    if hacer_pregunta(pregunta, i, total):
        correctas += 1

while True:
    respuesta = input("Tu respuesta (A/B/C/D): ").strip().upper()
    if respuesta in ["A", "B", "C", "D"]:
        break
    else:
        print("Solo puedes escribir A, B, C o D.")
```

¿Por qué es importante? El for me permite recorrer todas las preguntas de la ronda y el while me sirve para seguir pidiendo la respuesta hasta que sea válida.

---

### 2. Estructuras condicionales (if/elif/else)

**¿Dónde las usé?**

- Para saber si la respuesta del usuario es correcta o no
- Para el menú según la opción que elija
- Para mostrar un mensaje diferente según el puntaje obtenido

Ejemplo del código:

```python
if respuesta == pregunta["respuesta"]:
    print("Correcto!")
    return True
else:
    print(f"Incorrecto. La respuesta era: {pregunta['respuesta']}")
    return False

if puntaje == 100:
    print("Perfecto! Lo sabias todo.")
elif puntaje >= 60:
    print("Bien hecho, aprobaste!")
else:
    print("Necesitas repasar un poco mas.")
```

¿Por qué es importante? Los condicionales me permiten tomar decisiones en el programa. Según lo que responda el usuario el programa reacciona de forma diferente.

---

### 3. Programación Funcional (filter, map, lambda, reduce)

**¿Dónde la usé?**

- filter + lambda para filtrar preguntas por categoría o dificultad
- map para extraer las categorías de todas las preguntas
- reduce para calcular el promedio de puntajes del historial
- sorted + lambda para ordenar el ranking de categorías

Ejemplo del código:

```python
# filter: solo preguntas de una categoria
filtradas = list(filter(lambda p: p["categoria"] == categoria_elegida, preguntas))

# map: extraer los nombres de categoria
todas_categorias = list(map(lambda p: p["categoria"], preguntas))

# reduce: calcular promedio de puntajes
suma = reduce(lambda acum, p: acum + p["puntaje"], historial_puntajes, 0)
promedio = round(suma / len(historial_puntajes))
```

¿Por qué es importante? La programación funcional me permite procesar los datos de forma más corta y limpia.

---

## Desafíos que tuve

**Problema 1: Organizar bien las preguntas**

Qué pasaba: Al principio no sabía cómo guardar las preguntas con sus opciones y respuesta juntas de forma ordenada.

Cómo lo resolví: Usé una lista de diccionarios donde cada diccionario es una pregunta completa con todos sus datos adentro.

---

**Problema 2: Filtrar por categoría o dificultad**

Qué pasaba: No sabía cómo mostrar solo las preguntas de una categoría sin tener que hacer listas separadas para cada una.

Cómo lo resolví: Usé filter con lambda para filtrar la lista principal en el momento que el usuario elige, sin necesidad de tener listas aparte.

---

**Problema 3: El código se veía desordenado**

Qué pasaba: Al principio todo estaba junto y era difícil de seguir.

Cómo lo resolví: Separé el código en funciones:

- Una función para mostrar el menú
- Una función para hacer cada pregunta
- Una función para correr una ronda completa
- Una función para el historial y las estadísticas

---

## Lo que funciona bien

- El juego corre sin errores
- Valida que la respuesta sea solo A, B, C o D
- Tiene tres modos de juego diferentes
- Guarda el historial de la sesión y calcula el promedio
- Muestra estadísticas del banco de preguntas

---

## Lo que me falta hacer

- Guardar el historial en un archivo para que no se pierda al cerrar
- Agregar más preguntas al banco
- Hacer que se vea más bonito con colores en la terminal

---

## ¿Qué aprendí?

Lo más importante que aprendí es que cuando divides el problema en partes pequeñas se vuelve mucho más manejable. Al principio no sabía por dónde empezar pero cuando separé todo en funciones fue más fácil ir avanzando de a poco.

También aprendí que la programación funcional como filter y map hace el código más corto y fácil de leer una vez que le agarras el modo.

---

## ¿Qué fue lo más difícil?

Lo más difícil fue entender cómo usar reduce para calcular el promedio del historial. No lo entendía al principio pero cuando lo probé varias veces y vi el resultado ya me quedó claro cómo funciona.

---

## ¿Qué mejoraría?

Si tuviera más tiempo me gustaría:

- Agregar un modo multijugador
- Hacer que guarde los puntajes en un archivo .txt
- Agregar más categorías de tecnología

---

## Conclusión

Este proyecto me ayudó a entender mejor cómo se usan los ciclos, los condicionales y la programación funcional en un programa real. El tema del impacto de las tecnologías en la sociedad también me hizo reflexionar sobre cómo las usamos en el día a día sin darnos cuenta de todo lo que implica.

Lo más importante es que el juego funciona y que pude aplicar los cuatro temas de la materia en un solo programa.

---

## Recursos que usé

- Apuntes de clase sobre estructuras de control y programación funcional
- Documentación de Python para random y functools
- Prueba y error para que todo funcionara bien

---

## Repositorio

https://github.com/Kevt20/Proyecto.Final
