import logging
from sqlalchemy import create_engine
from datos import Tabla_unificada, tabla_regristros, Tabla_cine


logging.info('Creacion de base de datos')
engine = create_engine('postgresql://postgres:1234@localhost:5432/Alkemy')


logging.info('Carga de tabla unificada a PostgreSQL')

Tabla_unificada.to_sql('tabla_unica', con = engine, if_exists = 'replace')

logging.info('Carga de tabla a PostgreSQL')

tabla_regristros.to_sql('Tabla', con = engine, if_exists = 'replace')

logging.info('Carga de tabla_cine a PostgreSQL')

Tabla_cine.to_sql('tabla_cine', con = engine, if_exists = 'replace')
logging.info('Proceso finalizado')
