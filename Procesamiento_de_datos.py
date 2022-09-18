import pandas as pd

df_museos = pd.read_csv('museos/2022-septiembre/museos-15-09-2022.csv')
df_cines = pd.read_csv('cines/2022-septiembre/cines-15-09-2022.csv')
df_bibliotecas = pd.read_csv('bibliotecas/2022-septiembre/bibliotecas-15-09-2022.csv')


#Normalizamos los nombres que nos interesan
df_museos2 = df_museos.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'categoria':'categoría', 'direccion':'domicilio', 'CP':'código postal', 'telefono':'número de teléfono',  'Mail':'mail', 'Web':'web'})
df_cines2 = df_cines.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia','Dirección':'domicilio', 'CP':'código postal', 'Teléfono':'número de teléfono',  'Mail':'mail', 'Web':'web'})
df_bibliotecas2 = df_bibliotecas.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia', 'Localidad':'localidad', 'Nombre':'nombre', 'Domicilio':'domicilio', 'CP':'código postal', 'Teléfono':'número de teléfono',  'Mail':'mail', 'Web':'web'})



#nos quedamos con las tablas que vamos a usar. 

df_museos2 = df_museos2.drop(['Observaciones', 'subcategoria', 'piso', 'cod_area', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'fuente', 'jurisdiccion', 'año_inauguracion', 'actualizacion'], axis=1)
df_cines2 = df_cines2.drop(['Observaciones', 'Departamento','Piso', 'cod_area', 'Información adicional','Latitud', 'Longitud', 'TipoLatitudLongitud', 'Fuente', 'tipo_gestion',	'Pantallas',	'Butacas',	'espacio_INCAA', 'año_actualizacion'], axis=1)
df_bibliotecas2 = df_bibliotecas2.drop(['Observacion', 'Subcategoria', 'Departamento','Piso', 'Cod_tel', 'Información adicional','Latitud', 'Longitud', 'TipoLatitudLongitud','Fuente', 'Tipo_gestion',	'año_inicio',	'Año_actualizacion'], axis=1)


#Generamos la tabla para inuficar la informacion

Tabla_Unificada = pd.DataFrame(columns=['cod_localidad', 'id_provincia', 'id_departamento', 'categoría', 'provincia', 'localidad', 'nombre', 'domicilio', 'código postal', 'número de teléfono', 'mail', 'web'])

#La rellenamos
Tabla_Unificada = Tabla_Unificada.append(df_museos2)
Tabla_Unificada = Tabla_Unificada.append(df_cines2)
Tabla_Unificada = Tabla_Unificada.append(df_bibliotecas2)


#Generamos las dos tablas pedidas

#Procesamos los datos conjuntos para poder generar una tabla con la siguiente informacion
# Cantidad de registros totales por categoría
# Cantidad de registros totales por fuente
# Cantidad de registros por provincia 
df_museos3 = df_museos.rename(columns={'fuente':'Fuente', 'categoria':'Categoría', 'provincia':'Provincia', 'nombre':'Nombre'})
df_completo = df_museos3.append(df_cines).append(df_bibliotecas)
df_completo = df_completo.drop(['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Observaciones', 'subcategoria', 'localidad', 'direccion', 'piso', 'CP', 'cod_area', 'telefono', 'Mail', 'Web', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'jurisdiccion', 'año_inauguracion', 'actualizacion', 'Departamento', 'Localidad', 'Dirección', 'Piso', 'Teléfono', 'Información adicional', 'tipo_gestion', 'Pantallas', 'Butacas', 'espacio_INCAA', 'año_actualizacion', 'Observacion', 'Subcategoria', 'Domicilio', 'Cod_tel', 'Tipo_gestion', 'año_inicio', 'Año_actualizacion'], axis=1)
df_regristros = df_completo.pivot_table(values='Nombre', index=['Fuente', 'Categoría'], columns=['Provincia'], aggfunc='count', margins=True)
df_regristros=df_regristros.fillna(0)


#Procesar la información de cines para poder crear una tabla que contenga:
#Provincia
#Cantidad de pantallas
#Cantidad de butacas
#Cantidad de espacios INCAA

df_provincias = df_cines[['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]
#normalizamos los datos de la columna espacio_INCAA
df_provincias['espacio_INCAA'] = df_provincias['espacio_INCAA'].replace('si', 'SI').replace('SI', 1)
df_provincias['espacio_INCAA'] = df_provincias['espacio_INCAA'].fillna(0)
df_provincias['espacio_INCAA'] = df_provincias['espacio_INCAA'].astype("int")
df_provincias = df_provincias.groupby('Provincia').sum()