import requests
import os

#Extraccion 
"""Con la librearia requests obtenemos los datos requeridos. Estos se obtienen directamente de la pagina oficial del dato"""


datos_bibliotecas = requests.get ("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv", allow_redirects = True)
os.makedirs ("bibliotecas/2022-septiembre")
open ("bibliotecas/2022-septiembre/bibliotecas-15-09-2022.csv", "wb").write(datos_bibliotecas.content)

datos_museos = requests.get ("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv", allow_redirects = True)
os.makedirs ("museos/2022-septiembre")
open ("museos/2022-septiembre/museos-15-09-2022.csv", "wb").write(datos_museos.content)

datos_cines = requests.get ("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv", allow_redirects = True)
os.makedirs ("cines/2022-septiembre")
open ("cines/2022-septiembre/cines-15-09-2022.csv", "wb").write(datos_cines.content)
