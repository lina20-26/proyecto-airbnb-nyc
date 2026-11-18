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

# %% [markdown]
# ## 5. Creación de variables  (Integrante A)

# %% [markdown]
# ## 6. Filtrado y condiciones en pandas  (Integrante B)

# %% [markdown]
# ## 7. Agrupación con groupby  (Integrante A)

# %% [markdown]
# ## 8. Visualizaciones  (Integrante B)

# %% [markdown]
# ## 9. Conclusiones finales  (Integrante A)
