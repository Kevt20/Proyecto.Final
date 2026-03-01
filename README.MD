# Juego de Tecnologia y Sociedad

Nombre: Kevin Jimenez
Curso: Lógica de Programación
Fecha: 01/03/2026

---

## ¿Qué es este proyecto?

Es un juego de preguntas sobre el impacto de las nuevas tecnologías en la sociedad. Lo hice para practicar lo que estoy aprendiendo en el curso de programación y al mismo tiempo aprender sobre cómo la tecnología nos afecta en el trabajo, la salud y la educación.

---

## ¿Cómo funciona?

1. El juego te muestra un menú con varias opciones
2. Escoges cómo quieres jugar: aleatorio, por categoría o por dificultad
3. El juego te hace preguntas de 4 opciones (A, B, C o D)
4. Al final de cada ronda te dice cuántas acertaste y tu puntaje
5. Puedes ver tu historial y estadísticas del banco de preguntas

---

## ¿Cómo usar el programa?

1. Abre la terminal o consola
2. Ve a la carpeta donde está el archivo
3. Escribe: `python3 proyecto_juego.py`
4. ¡A jugar!

---

## Lo que incluye el proyecto

**Ya funciona:**
- Tres modos de juego: aleatorio, por categoría y por dificultad
- Banco de 12 preguntas sobre tecnologías emergentes
- Sistema de puntaje por ronda
- Historial de partidas con promedio general
- Estadísticas del banco de preguntas

**Todavía en desarrollo:**
- Guardar el historial en un archivo .txt
- Agregar más preguntas al banco
- Hacer que se vea con colores en la terminal

---

## Estructuras de programación que usé

**Estructuras repetitivas (bucles):**
- `for` para recorrer cada pregunta de la ronda
- `while` para el menú principal
- `while` para validar que la respuesta sea A, B, C o D

**Estructuras condicionales:**
- `if/elif/else` para el menú según la opción elegida
- `if/elif/else` para saber si la respuesta es correcta
- `if/elif/else` para mostrar el mensaje según el puntaje final

**Programación funcional:**
- `filter` + `lambda` para filtrar preguntas por categoría o dificultad
- `map` + `lambda` para extraer categorías de las preguntas
- `reduce` para calcular el promedio del historial de puntajes
- `sorted` + `lambda` para ordenar el ranking de categorías

---

## Ejemplo de uso

```
=============================================
   JUEGO: Tecnologia y Sociedad
   Proyecto Final - Kevin Jimenez 2025
=============================================

--- MENU PRINCIPAL ---
  1. Jugar (preguntas aleatorias)
  2. Jugar por categoria
  3. Jugar por dificultad
  4. Ver mi historial de puntajes
  5. Ver estadisticas del juego
  0. Salir

  Elige una opcion: 1

  Modo: Aleatorio
  Responde 5 preguntas. Suerte!

  Pregunta 1 de 5
  Categoria: Inteligencia Artificial | Dificultad: facil

  ¿Cual es uno de los principales riesgos de la IA en el trabajo?

    A) Mejora todos los empleos
    B) Puede reemplazar empleos repetitivos
    C) No tiene ningun efecto
    D) Solo afecta a los medicos

  Tu respuesta (A/B/C/D): B
  Correcto!

  FIN DE LA RONDA
  Correctas: 4 de 5
  Puntaje:   80/100
  Bien hecho, aprobaste!
```

---

## Lo que aprendí

- Cómo usar ciclos `for` y `while` para recorrer datos y validar entradas
- Cómo usar `if/elif/else` para tomar decisiones en el código
- Cómo guardar datos en listas de diccionarios
- Cómo usar `filter`, `map`, `lambda` y `reduce` para procesar datos
- Cómo organizar el código en funciones para que sea más fácil de entender
- Cómo hacer un programa interactivo que el usuario pueda usar sin errores

---

## Repositorio

https://github.com/Kevt20/Proyecto.Final
