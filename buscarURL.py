import pandas as pd
from googlesearch import search

#Accedemos al excel y leemos a toda su información
df = pd.read_excel('jcr_computer_science_journals_pfg_resultados.xlsx')


def buscarGoogle(busqueda):
    for url in search(busqueda, num_results=10): 
    #Se obtienen los primeros 10 resultados para conseguir alguna que sea posible devolver
        if 'wikipedia.org' not in url:
            return url
    return False

# Iterar sobre cada fila del DataFrame utilizando el índice
for index in df.index:
    # Se accede al nombre de cada revista y se añade "editorial board" para comenzar la busqueda en google
    busqueda = df.loc[index, 'Journal name'] + " editorial Board"
    # se busca en Google y se obtiene la primera URL que no provenga de Wikipedia
    url = buscarGoogle(busqueda)
    if not url:
        encontrada = ""
    else:
        encontrada = url
    # se almacena la primera url que se ha encontrado en google
    df.loc[index, 'URL'] = url
# Volvemos a guardar el mismo Excel pero con los cambios de URL
df.to_excel('jcr_computer_science_journals_pfg_resultados.xlsx', index=False)
