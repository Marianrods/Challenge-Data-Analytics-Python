from sqlalchemy import create_engine
from Procesamiento_de_datos import Tabla_Unificada, df_regristros, df_provincias

engine = create_engine('postgresql://postgres:12345@localhost:5432/PostgreSQL')

Tabla_Unificada.to_sql('tabla_unificada', con=engine, if_exists='replace')
df_regristros.to_sql('cantidades_cines', con=engine, if_exists='replace')
df_provincias.to_sql('categorias_fuentes', con=engine, if_exists='replace')