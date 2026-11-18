# Análisis de los anuncios de Airbnb en Nueva York (2019)

Proyecto final de programación II

## Integrantes
- Lina María Velásquez Contreras (Integrante A)
- María Paula Rangel Triana (Integrante B)

## Fuente de los datos
Kaggle: [New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data).
Son los anuncios de Airbnb en Nueva York del 2019.

## Estructura de los datos
La base tiene 48895 filas y 16 columnas, cada fila es un anuncio. Tiene 5 variables categoricas,
3 numericas continuas y 5 numericas discretas, ademas de dos codigos (id y host_id) y una fecha
(last_review). Despues de limpiar quedan 48631 filas y le agregamos 3 variables nuevas.

## Diccionario de datos
| Variable | Tipo | Descripción | Valores / unidades |
|---|---|---|---|
| id | código | id del anuncio | número |
| name | categórica | nombre del anuncio | texto |
| host_id | código | id del anfitrión | número |
| host_name | categórica | nombre del anfitrión | texto |
| neighbourhood_group | categórica | distrito | Manhattan, Brooklyn, Queens, Bronx, Staten Island |
| neighbourhood | categórica | barrio | 221 barrios |
| latitude | numérica continua | latitud | grados |
| longitude | numérica continua | longitud | grados |
| room_type | categórica | tipo de habitación | Entire home/apt, Private room, Shared room |
| price | numérica discreta | precio por noche | dólares |
| minimum_nights | numérica discreta | noches mínimas | noches |
| number_of_reviews | numérica discreta | número de reseñas | cantidad |
| last_review | fecha | fecha de la última reseña | fecha |
| reviews_per_month | numérica continua | reseñas por mes | promedio |
| calculated_host_listings_count | numérica discreta | anuncios que tiene el anfitrión | cantidad |
| availability_365 | numérica discreta | días disponibles en el año | 0 a 365 |
| tipo_precio | categórica (nueva) | barato, medio o caro | barato hasta 70, caro más de 150 |
| estancia_larga | categórica (nueva) | si pide 30 noches o más | True / False |
| costo_minimo | numérica discreta (nueva) | precio por noches mínimas | dólares |

## Organización del repositorio
- analisis.py: solución final
- cuadernos/: cuadernos de exploración de cada una
- datos/: base de datos de Kaggle

## Conclusiones
1. Manhattan es el distrito con mas anuncios y tambien el mas caro.
2. (Integrante B)
3. Hay pocos anfitriones con muchos anuncios y parecen empresas.
4. (Integrante B)
5. Los anuncios de precio medio son los que mas reseñas tienen.
