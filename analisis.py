# %% [markdown]
# # Análisis de los anuncios de Airbnb en Nueva York (2019)
# Integrantes: Lina María Velásquez Contreras, María Paula Rangel Triana

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("datos/AB_NYC_2019.csv")

# %% [markdown]
# ## 1. Carga e inspección inicial de los datos  (Integrante A)

# %%
df.head()

# %%
df.shape

# %%
df.info()

# %%
df.describe()

# %% [markdown]
# Conclusión: la base tiene 48895 filas y 16 columnas. Las variables categoricas son name, host_name,
# neighbourhood_group, neighbourhood y room_type, las numericas continuas son latitude, longitude y
# reviews_per_month, y las discretas son price, minimum_nights, number_of_reviews,
# calculated_host_listings_count y availability_365. Hay precios de 0 y de 10000 que revisamos despues.

# %% [markdown]
# ## 2. Manejo de datos faltantes  (Integrante B)

# %%
df.isnull().sum()

# %%
sns.heatmap(df.isnull(), cbar=False)
plt.title("Datos faltantes")
plt.show()

# %%
len(df[df["number_of_reviews"] == 0])

# %%
df["reviews_per_month"] = df["reviews_per_month"].fillna(0)
df["name"] = df["name"].fillna("sin nombre")
df["host_name"] = df["host_name"].fillna("sin nombre")

# %%
sns.heatmap(df.isnull(), cbar=False)
plt.title("Datos faltantes despues de limpiar")
plt.show()

# %% [markdown]
# Conclusión: los vacios de reviews_per_month y last_review son los 10052 anuncios que no tienen
# reseñas, por eso en reviews_per_month pusimos 0 en vez de borrar esas filas. last_review la dejamos
# asi porque es una fecha. En name y host_name faltaban muy pocos y les pusimos "sin nombre".

# %% [markdown]
# ## 3. Identificación de outliers  (Integrante A)

# %%
sns.boxplot(x=df["price"])
plt.title("Precio por noche")
plt.show()

# %%
sns.boxplot(x=df["minimum_nights"])
plt.title("Noches minimas")
plt.show()

# %%
q1 = df["price"].quantile(0.25)
q3 = df["price"].quantile(0.75)
iqr = q3 - q1
limite = q3 + 1.5 * iqr
print(limite)
print(len(df[df["price"] > limite]))
print(len(df[df["price"] > 1000]))

# %%
df = df[df["price"] <= 1000].copy()
df.shape

# %% [markdown]
# Conclusión: el precio y las noches minimas tienen muchos outliers. Con el IQR salen 2972 anuncios de
# mas de 334 dolares, pero muchos son apartamentos caros que si existen, entonces solo quitamos los de
# mas de 1000 dolares, que eran 239.

# %% [markdown]
# ## 4. Valores inconsistentes y duplicados  (Integrante B)

# %%
df.duplicated().sum()

# %%
print(df["neighbourhood_group"].unique())
print(df["room_type"].unique())

# %%
df[df["name"].str.isupper()]["name"].head()

# %%
df["name"] = df["name"].str.strip().str.lower()

# %%
print(len(df[df["price"] == 0]))
print(len(df[df["minimum_nights"] > 365]))

# %%
df = df[(df["price"] > 0) & (df["minimum_nights"] <= 365)].copy()
df.shape

# %% [markdown]
# Conclusión: no hay filas duplicadas y las categorias estan bien escritas. Habia nombres de anuncios
# en mayusculas y con espacios de mas, asi que los dejamos todos en minuscula. Tambien quitamos 11
# anuncios con precio 0 y 14 que pedian mas de 365 noches porque eso no tiene sentido.

# %% [markdown]
# ## 5. Creación de variables  (Integrante A)

# %%
df["tipo_precio"] = "medio"
df.loc[df["price"] <= 70, "tipo_precio"] = "barato"
df.loc[df["price"] > 150, "tipo_precio"] = "caro"
df["tipo_precio"].value_counts()

# %%
df["estancia_larga"] = df["minimum_nights"] >= 30
df["estancia_larga"].value_counts()

# %%
df["costo_minimo"] = df["price"] * df["minimum_nights"]
df[["price", "minimum_nights", "costo_minimo"]].head()

# %% [markdown]
# Conclusión: creamos tres variables. tipo_precio dice si el anuncio es barato (hasta 70 dolares),
# medio o caro (mas de 150), estancia_larga dice si pide 30 noches o mas, y costo_minimo es lo minimo
# que paga alguien por quedarse. La mayoria de los anuncios son de precio medio.

# %% [markdown]
# ## 6. Filtrado y condiciones en pandas  (Integrante B)

# %% [markdown]
# ### 6.1 Apartamentos completos en Manhattan por menos de 100 dolares

# %%
filtro1 = df[(df["neighbourhood_group"] == "Manhattan") & (df["room_type"] == "Entire home/apt") & (df["price"] < 100)]
len(filtro1)

# %% [markdown]
# Son solo 859, en Manhattan es dificil encontrar un apartamento completo barato.

# %% [markdown]
# ### 6.2 Anuncios que piden 30 noches o mas

# %%
filtro2 = df[df["estancia_larga"] == True]
len(filtro2)

# %% [markdown]
# Son 4437 anuncios, parecen mas para arrendar por meses que para turistas.

# %% [markdown]
# ### 6.3 Anuncios baratos con 100 reseñas o mas

# %%
filtro3 = df[(df["tipo_precio"] == "barato") & (df["number_of_reviews"] >= 100)]
len(filtro3)

# %% [markdown]
# Solo 743 de los 13527 anuncios baratos tienen 100 reseñas o mas, o sea que ser barato no hace que
# tenga muchas reseñas.

# %% [markdown]
# ### 6.4 Anuncios sin dias disponibles

# %%
filtro4 = df[df["availability_365"] == 0]
len(filtro4)

# %% [markdown]
# 17463 anuncios no tienen ningun dia disponible en el año, puede ser que ya no se usen.

# %% [markdown]
# ### 6.5 Anuncios de anfitriones con 10 o mas anuncios

# %%
filtro5 = df[df["calculated_host_listings_count"] >= 10]
len(filtro5)

# %% [markdown]
# 3153 anuncios son de anfitriones que tienen 10 o mas, esos parecen empresas y no personas.

# %% [markdown]
# ## 7. Agrupación con groupby  (Integrante A)

# %% [markdown]
# ### 7.1 Precio promedio por distrito

# %%
df.groupby("neighbourhood_group")["price"].mean()

# %% [markdown]
# Manhattan es el mas caro con 179 dolares en promedio y el Bronx el mas barato con 85.

# %% [markdown]
# ### 7.2 Precio promedio por tipo de habitacion

# %%
df.groupby("room_type")["price"].mean()

# %% [markdown]
# Un apartamento completo cuesta mas del doble que una habitacion privada (195 contra 85 dolares).

# %% [markdown]
# ### 7.3 Dias disponibles en promedio por distrito

# %%
df.groupby("neighbourhood_group")["availability_365"].mean()

# %% [markdown]
# En Staten Island y el Bronx los anuncios pasan mas dias disponibles, en Brooklyn y Manhattan menos,
# entonces alla se reservan mas.

# %% [markdown]
# ### 7.4 Barrios con mas anuncios

# %%
df.groupby("neighbourhood")["id"].count().sort_values(ascending=False).head()

# %% [markdown]
# Williamsburg y Bedford-Stuyvesant, los dos en Brooklyn, son los barrios con mas anuncios.

# %% [markdown]
# ### 7.5 Reseñas promedio por tipo de precio

# %%
df.groupby("tipo_precio")["number_of_reviews"].mean()

# %% [markdown]
# Los de precio medio son los que tienen mas reseñas y los caros los que menos.

# %% [markdown]
# ## 8. Visualizaciones  (Integrante B)

# %% [markdown]
# ### 8.1 Histograma del precio

# %%
plt.hist(df["price"], bins=50)
plt.title("Precio por noche")
plt.xlabel("dolares")
plt.show()

# %% [markdown]
# La mayoria de los anuncios cuestan menos de 200 dolares y hay pocos muy caros.

# %% [markdown]
# ### 8.2 Anuncios por distrito

# %%
df["neighbourhood_group"].value_counts().plot(kind="bar")
plt.title("Anuncios por distrito")
plt.show()

# %% [markdown]
# Manhattan y Brooklyn tienen casi todos los anuncios, Staten Island casi no tiene.

# %% [markdown]
# ### 8.3 Tipos de habitacion

# %%
df["room_type"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Tipos de habitacion")
plt.ylabel("")
plt.show()

# %% [markdown]
# Mas o menos la mitad son apartamentos completos y casi la otra mitad habitaciones privadas, las
# compartidas son muy pocas.

# %% [markdown]
# ### 8.4 Mapa de los anuncios

# %%
sns.scatterplot(data=df, x="longitude", y="latitude", hue="tipo_precio", s=5)
plt.title("Ubicacion de los anuncios")
plt.show()

# %% [markdown]
# Los anuncios caros estan casi todos en Manhattan, los baratos estan mas repartidos.

# %% [markdown]
# ### 8.5 Precio por tipo de habitacion

# %%
sns.boxplot(data=df, x="room_type", y="price")
plt.title("Precio por tipo de habitacion")
plt.show()

# %% [markdown]
# Los apartamentos completos son los mas caros y los que mas cambian de precio.

# %% [markdown]
# ## 9. Conclusiones finales  (Integrante A)
