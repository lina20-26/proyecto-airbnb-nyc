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

# %% [markdown]
# ## 3. Identificación de outliers  (Integrante A)

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
