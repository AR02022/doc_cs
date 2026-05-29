#parte 0
from fastapi import FastAPI #libreria crwadora de web para guaradar info de api

app = FastAPI() # objeto

@app.get("/") # es para generar url para para web donde se guarda api, SE PONE ARRIBA DELA FUNCION QUE QUIERES QUE CORRA

def inicio(archivo): #caracteristica

    #parte 1 extracción: extrae los datos de el pdf
    import pdfplumber

    with pdfplumber.open("archivo") as pdf:
        primera_pagina = pdf.pages[0] # escoge las paginas
        texto = primera_pagina.extract_text() #IDENTIFICA, SEPARA Y GUARDA EN UNA LISTA LA INFO, pero guarda todo 
        #print(texto)# en una lista de una columna letra por letra
        print("paso 1 extracción concluida")

    # paso 2 organizacion de datos en formato de lectura normal    
        lineas = texto.split("\n") # "\n" significa salto de linea pero todo junto "texto.split("\n")" organiza todas las palbras dentro dde una lista-
        #print(lineas)
        print("paso 2 organización completado")

    #paso 3 
    lista = ["USD","Medio de Transporte:","Nombre / Razón Social:", "Producto:", "Descripción:", "Fecha de salida:","Factura", "Folio:"] 

    list_new =  [] # save nuevos datos
    num = 0
    print("iniciando paso 3")
    for palabra in lista: # sirve para reiniciar el codigo y volver a leer todo, pero necesita que el "break" este dentro del if, para que reinicie cada vez que encuentra la respuesta
        
        for i in range(len(lineas)): # #"Range" sirve para contar desde "0", "len" sirve para contar el numero de elementos que hay dentro de la base de datos. juntos cuenta los umeros de la lista desde el "0"
            
            linea = lineas[i].strip() # la funcion "strip()" sirve para borrar espacios en blanco, tabulaciones y saltos de línea.        
            print("valor de linea",linea)

            if lista[num] in linea:

                if lista[num] == "Medio de Transporte:":
                    print("ingreso al if") 
                    dato = linea.split("Medio de Transporte:")[1].split("No. de Embarque:")[0].strip()
                    print("proceso 3 completado", dato)
                    list_new.append(dato)
                    num = num + 1 
                    break

                elif lista[num] == "No. de Embarque:":
                    print("ingreso al elif No. de Embarque:")
                    dato = linea.split("No. de Embarque:")[1].split("Medio de Transporte:")[0].strip()
                    print("proceso 3 completado", dato)
                    list_new.append(dato)
                    num = num + 1 
                    break

                elif lista[num] == "Fecha de salida:":
                    import re
                    print("ingreso al elif Fecha de salida:")
                    fecha = re.findall(r"\d{2}/\d{2}/\d{4}", linea)#si la fecha 02/05/2027 esto significa: \d{2} =02 ,/\d{2}/=05 , \d{4}= 2027               
                    print("proceso 3 completado", fecha)
                    list_new.extend(fecha) #con extend se borra la lista "fecha" y los datos se guardan dentro de la lista "list_new"
                    num = num + 1 
                    break
                

                elif lista[num] == "Factura":
                    import re
                    match = re.search(r"Factura\s+.+", linea) #lo que hace import re,es con la "r" rastrear la palabra y/o datos que le pidas dentro
                                                               # s+ significa que lo que copeas tiene espacio y ".+" sirve para agregar que tome en cuenta mas datos. 
                    if match:

                        dato = match.group()

                        if "Folio:" in dato: # en caso de existir mas datos dentro de la misma caja, 
                             dato = dato.split("Folio:")[0] #corta los datos antes de entrar en folio

                        dato = dato.strip()

                        print(dato)
                    list_new.append(dato)
                    num = num + 1 
                    print(list_new)
                    break

                    
                    """
                    print("ingreso al factura")
                    #dato = linea.split("Factura","")
                    dato=re.search(r"Factura\s+([A-Za-z0-9-]+)")
                    print("proceso 3 completado", dato)
                    
                    """

                elif lista[num] == "Folio:":
                    print("ingreso a folio")
                    dato = linea.split("Folio:")[1].split("No. de Conocimiento:")[0].strip()
                    print("proceso 3 completado", dato)
                    list_new.append(dato)
                    num = num + 1 
                    break                       

                else:
                    print("ingreso al else")
                    dato = linea.replace(palabra, "").strip()
                
                # busca la palabra de lista en el texto
                    print("proceso 3 completado", dato)
                    list_new.append(dato)
                    num = num + 1 
                    break
                  
            else:
                print("no se encontro la informacion",i)
        print("proceso 3 completado")

    #return lineas
    return list_new        
   

    #para iniciar code          
    #uvicorn pdf-xlsx_2:app --reload  
        

        #ES HORA DE EMPEZAR A HACER PRUEBAS CON LA HOJA DE CALCULO, 
    # EN CUANTO TENGAS LUZ VERDE, TIENES QUE AGREGAR TODAS LAS PALBARAS CLAVES.
