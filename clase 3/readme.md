# Análisis Exploratorio de Datos (EDA) con Pandas y PandaSQL

Este repositorio contiene ejercicios enfocados en realizar un análisis exploratorio de datos (EDA) sobre un dataset de Spotify utilizando Pandas y PandaSQL.

## Características del Dataset

Fuente:
[https://www.kaggle.com/datasets/abdulszz/spotify-most-streamed-songs](Fuente)

El dataset incluye las siguientes características:

- **Información Básica de la Canción:**

  - `track_name`: Nombre de la canción.
  - `artist(s)_name`: Nombre del(los) artista(s) que interpretan la canción.
  - `artist_count`: Número de artistas que contribuyen a la canción.
  - `released_year`, `released_month`, `released_day`: Detalles de la fecha de lanzamiento.

- **Métricas de Streaming:**

  - `in_spotify_playlists`: Número de playlists en Spotify en las que aparece la canción.
  - `in_spotify_charts`: Ranking de la canción en las listas de Spotify.
  - `streams`: Número total de streams en Spotify.
  - `in_apple_playlists`, `in_apple_charts`: Presencia en playlists y listas de Apple Music.
  - `in_deezer_playlists`, `in_deezer_charts`: Presencia en playlists y listas de Deezer.
  - `in_shazam_charts`: Ranking en las listas de Shazam.

- **Atributos Musicales:**
  - `bpm`: Puntuación de beats por minuto, que representa el tempo de la canción.
  - `key`: Tono de la canción.
  - `mode`: Indica si la canción está en modo mayor o menor.
  - `danceability_%`: Indica la idoneidad de la canción para bailar.
  - `valence_%`: Positividad del contenido musical de la canción.
  - `energy_%`: Nivel percibido de energía de la canción.
  - `acousticness_%`: Presencia de sonido acústico en la canción.
  - `instrumentalness_%`: Proporción de contenido instrumental en la pista.
  - `liveness_%`: Presencia de elementos de interpretación en vivo.
  - `speechiness_%`: Cantidad de palabras habladas en la canción.

## Ejercicios con Pandas

1. **Cargar el dataset y obtener una vista general:**

   - Cargar el dataset y mostrar las primeras 5 filas.
   - Obtener información general del dataset (tipos de datos, valores nulos, etc.).

2. **Verificar valores nulos:**

   - Identificar cuántos valores nulos hay por columna.
   - Calcular el porcentaje de valores nulos por columna.

3. **Distribución de canciones por año de lanzamiento:**

   - Crear un histograma que muestre la distribución de canciones por año de lanzamiento.

4. **Top 10 de artistas con más canciones:**

   - Agrupar por el nombre del artista y contar cuántas canciones tienen en el dataset. Mostrar los 10 artistas con más canciones.

5. **Comparar el promedio de streams por modo musical:**

   - Calcular el promedio de streams para canciones en modo mayor y menor.

6. **Analizar la relación entre "danceability" y "streams":**

   - Crear un gráfico de dispersión para ver la relación entre "danceability" y el número de streams.

7. **Canciones más populares (streams) en función de su key musical:**

   - Agrupar por la columna `key` y calcular el promedio de streams para cada key.

8. **Explorar la distribución de la energía de las canciones:**

   - Crear un histograma que muestre cómo se distribuye la energía de las canciones.

9. **Correlación entre atributos musicales:**
   - Obtener la correlación entre atributos como `bpm`, `energy_%`, `valence_%`, etc., y generar un heatmap de correlación.

## Ejercicios con PandaSQL

1. **Consulta de las 10 canciones más populares (streams):**

   - Seleccionar las 10 canciones con más streams utilizando PandaSQL.

2. **Canciones lanzadas en el 2023 con más de 100 millones de streams:**

   - Filtrar las canciones lanzadas después del año 2015 que tengan más de 100 millones de streams.

3. **Promedio de bpm de las canciones lanzadas entre 2010 y 2020:**
   - Calcular el bpm promedio de las canciones lanzadas entre 2010 y 2020.

## Requisitos

- Python 3.x
- Pandas
- Matplotlib
- Seaborn (opcional para el heatmap)
- Pandasql
