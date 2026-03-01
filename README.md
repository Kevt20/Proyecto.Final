# 🌐 TechImpact Explorer

> **El impacto de las nuevas tecnologías en la sociedad: visualización del futuro**

---

## 📌 Datos del Proyecto

| Campo | Detalle |
|-------|---------|
| **Autor** | Kevin Jiménez |
| **GitHub** | @KevinJimenez |
| **Lenguaje** | Python 3.x |
| **Fecha** | 2025 |
| **Proyecto** | Proyecto Integrador Final — 4 Unidades |

---

## 🎯 Objetivo del Programa

Explorar, analizar y visualizar el impacto de las **nuevas tecnologías emergentes** en distintos ámbitos de la sociedad (social, laboral, educativo y de salud). El programa permite comparar tecnologías, generar gráficas estadísticas y exportar reportes completos, todo mediante una interfaz de consola interactiva en Python.

---

## 🚀 Funcionalidades Principales

| # | Opción | Descripción |
|---|--------|-------------|
| 1 | Ver todas las tecnologías | Lista completa del dataset con impacto social |
| 2 | Analizar una tecnología | Análisis detallado con ventajas, desventajas y tendencia |
| 3 | Comparar dos tecnologías | Comparativa lado a lado en 4 indicadores |
| 4 | Estadísticas generales | Promedios, máximos, mínimos y distribución por categoría |
| 5 | Buscar por categoría | Filtrado por automatización, comunicación, salud, etc. |
| 6 | Tecnologías de alto impacto | Filtrado funcional con `filter()` + `lambda` |
| 7 | Ranking de impacto social | Ordenamiento con `sorted()` + `lambda` |
| 8 | Gráfica comparativa | Barras agrupadas por indicador con `matplotlib` |
| 9 | Gráfica de tendencia | Línea de adopción tecnológica por año |
| 10 | Exportar reporte | Genera archivo `.txt` con análisis completo |

---

## 🗂️ Unidades Integradas

### Unidad 1 — Arquitectura y Diagramas
- Definición del problema y alcance del software
- Diagramas de flujo y arquitectura de la aplicación
- Diseño de la estructura modular del proyecto

### Unidad 2 — Desarrollo del Entorno y Estructuras de Datos
- Configuración del entorno Python y GitHub
- Estructuras de datos: listas de diccionarios para el dataset
- Funciones de análisis y búsqueda

### Unidad 3 — Estructuras Lógicas y Repetitivas
- Condicionales `if/elif/else` para clasificación de impacto
- Ciclos `for` para recorrer datasets y mostrar información
- Ciclos con `zip()` para comparaciones paralelas
- Visualización con `matplotlib`

### Unidad 4 — Programación Funcional
- `filter()` + `lambda`: filtrar por impacto o categoría
- `map()` + `lambda`: transformar y extraer datos
- `reduce()`: calcular promedios y acumulados
- `sorted()` + `lambda`: ranking de tecnologías

---

## 📂 Estructura del Proyecto

```
TechImpact-Explorer/
│
├── main.py                     ← Menú principal e interfaz de usuario
├── requirements.txt            ← Dependencias (matplotlib)
├── README.md                   ← Documentación del proyecto
│
├── datos/
│   ├── __init__.py
│   └── tecnologias.py          ← Dataset con 10 tecnologías emergentes
│
├── funciones/
│   ├── __init__.py
│   ├── analisis.py             ← Lógica de análisis (Unidades 2 y 3)
│   └── funcional.py            ← Programación funcional (Unidad 4)
│
├── visualizacion/
│   ├── __init__.py
│   └── graficas.py             ← Gráficas con matplotlib (Unidad 3)
│
└── reportes/
    ├── __init__.py
    └── exportar.py             ← Exportación de reportes .txt (Unidad 2)
```

---

## ▶️ Cómo Ejecutar

### 1. Clonar el repositorio
```bash
git clone https://github.com/KevinJimenez/TechImpact-Explorer.git
cd TechImpact-Explorer
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar el programa
```bash
python main.py
```

---

## 💻 Ejemplo de uso

```
=========================================
       🌐  TechImpact Explorer  🌐
=========================================
  1. Ver todas las tecnologías
  2. Analizar una tecnología
  3. Comparar dos tecnologías
  ...

  Selecciona una opción: 2
  Nombre de la tecnología: Inteligencia Artificial

  🔍 Análisis Completo: Inteligencia Artificial
  =============================================
  📌 Categoría: automatizacion
  📊 Impacto Social:     +9/10  ✅ Muy Alto
  💼 Impacto Laboral:    -6/10  ❌ Negativo
  🎓 Impacto Educación:  +9/10  ✅ Muy Alto
  🏥 Impacto Salud:      +8/10  ✅ Muy Alto
```

---

## 🧪 Tecnologías Incluidas en el Dataset

1. Inteligencia Artificial
2. Redes Sociales
3. Internet de las Cosas (IoT)
4. Blockchain
5. Realidad Virtual y Aumentada
6. Automatización Robótica
7. Computación en la Nube
8. Ciberseguridad
9. Telemedicina
10. Vehículos Autónomos

---

## 📊 Ejemplo de Programación Funcional (Unidad 4)

```python
from functools import reduce

# filter + lambda: tecnologías con alto impacto
alto_impacto = list(filter(lambda t: t["impacto_social"] >= 7, tecnologias))

# map + lambda: extraer solo nombres
nombres = list(map(lambda t: t["nombre"], tecnologias))

# reduce: calcular promedio de impacto social
suma = reduce(lambda acum, t: acum + t["impacto_social"], tecnologias, 0)
promedio = suma / len(tecnologias)

# sorted + lambda: ranking
ranking = sorted(tecnologias, key=lambda t: t["impacto_social"], reverse=True)
```

---

## 📝 Licencia

Proyecto académico — Kevin Jiménez © 2025
