from datetime import date, datetime
from os import walk, path
import numpy as np
fecha = date.today()
#d = datetime.strptime("02/07/2020", "%d/%m/%Y").strftime("%Y")
#print(d)
lista_de_pedidos = [
    '15565 2020-12-14', 
    '4505600419G 1999-01-01', 
    '4505600419O 2021-06-10', 
    '4505600419P 2021-02-25', 
    '4506928440 1999-01-01', 
    '4507235865 2020-07-02', 
    '4507257453H 2021-06-10', 
    '4507374555 1999-01-01', 
    '4507536497 2019-04-17', 
    '4507696389 1999-01-01', 
    '4507914072 2019-11-12', 
    '4507918125 2020-05-11', 
    '4507922046 2019-10-26', 
    '4507985616 1999-01-01', 
    '4508051397 2019-09-11', 
    '4508051446 2019-06-12', 
    '4508056791 2019-07-19', 
    '4508056844 2019-10-03', 
    '4508060388 2019-06-13', 
    '4508060577 2019-08-09'
]


for (dirpath, dirnames, filenames) in walk("listas_simi"):
    print(len(filenames))
    print(dirnames)
    if len(filenames) > 0:
        print("Hola estoy aqui")
        for f in filenames:
            fichero = open(path.join(dirpath, f)).read().split("\n")
            data_to_file = []
            not_in_file = list(np.setdiff1d(lista_de_pedidos,fichero))
            for patata in not_in_file:
                if len(patata.split(" ")) > 1:
                    data_to_file.append(patata.split(" ")[0]+" "+patata.split(" ")[1]+"\n")

                else:
                    data_to_file.append(patata.split(" ")[0]+" "+"\n")
            fichero= open(path.join(dirpath, "lista_simi_{}.txt".format(fecha)), "a")
            fichero.writelines(data_to_file)
    else: 
        fichero= open(path.join(dirpath, "lista_simi_{}.txt".format(fecha)), "a")
        fichero.writelines(f'{s}\n' for s in lista_de_pedidos)