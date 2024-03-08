import requests
import pandas as pd
from customtkinter  import CTk, CTkFrame, CTkEntry, CTkLabel,CTkButton,CTkCheckBox
import tkinter as tk
import re
import os
from PIL import Image

def Prueba():
    Input_NombreCarta = entrada_1.get()

    lineas = Input_NombreCarta.split("\n")

    # Eliminar espacios en blanco alrededor de cada línea
    lineas = [linea.strip() for linea in lineas]

    # Crear una lista de listas donde cada lista representa una fila de la tabla
    tabla = [linea.split() for linea in lineas if linea]

    # Imprimir la tabla
    for i, fila in enumerate(tabla):

        valor = str(" ".join(fila))

        resultado = re.search(r'(.+?)x\d+', valor)

        if resultado:
            texto_antes_de_x_numero = resultado.group(1)
            tabla[i] = resultado.group(1)
        else:
            tabla[i] = ""
        
   

    tabla = [elemento.strip() for elemento in tabla if elemento.strip() != ""]

    #print(tabla)

    url = 'https://lairentcg.com.ar:8443/api/carta/cartas/ordenadas'

    response = requests.get(url)

    Unidades = []
    Accion = []
    Tesoro = []
    TesoroSagrado = []
    Monumento = []

    if response.status_code == 200:

        data = response.json()
        df = pd.DataFrame(data)
        df = df.sort_index(axis=1)

        for i, fila in enumerate(tabla):
       
            Columnas = ['urlImagen', 'nombreCarta','tipo',"subtipo"]

            Filtro = df['nombreCarta'] == fila
            Resultado = df.loc[Filtro, Columnas]

            NombreCarta = Resultado['nombreCarta'].iloc[0] 
            UrlCarta = Resultado['urlImagen'].iloc[0]
            TipoCarta = Resultado['tipo'].iloc[0]
            Sagrado = Resultado['subtipo'].iloc[0]
            TipoCarta = str(TipoCarta)
            Sagrado = str(Sagrado)

            #print(NombreCarta)
            #print(UrlCarta)
            #print(TipoCarta)
            #print(Sagrado)


            nombre_archivo = "Pruebas_Lairen/"+ NombreCarta  + ".jpg"

            if os.path.exists(nombre_archivo):
                print(NombreCarta + " --- Ya esta descargada")
            else:
                url = (UrlCarta)

                response = requests.get(url)

                if response.status_code == 200:   
                    with open("Pruebas_Lairen/"+ NombreCarta  + ".jpg", 'wb') as file:
                        file.write(response.content)
                        print(NombreCarta + " --- Se descargo")
                else:
                    print(f"Error {response.status_code}: {response.text}")

            if "unidad" in TipoCarta.lower():
                NombreCarta2 = "Pruebas_Lairen/"+ NombreCarta  + ".jpg"                
                Unidades.append(NombreCarta2)
                
            elif "accion" in TipoCarta.lower(): 
                NombreCarta2 = "Pruebas_Lairen/"+ NombreCarta  + ".jpg"        
                Accion.append(NombreCarta2)

            elif "tesoro" in TipoCarta.lower():
                NombreCarta2 = "Pruebas_Lairen/"+ NombreCarta  + ".jpg"
                if "sagrado" in Sagrado.lower():
                    TesoroSagrado.append(NombreCarta2)
                else:
                    Tesoro.append(NombreCarta2)

            elif "monumento" in TipoCarta.lower(): 
                NombreCarta2 = "Pruebas_Lairen/"+ NombreCarta  + ".jpg"        
                Monumento.append(NombreCarta2)

        print("")
        print(Unidades)
        print("")
        print(Accion)
        print("")
        print(Tesoro)
        print("")
        print(TesoroSagrado)
        print("")
        print(Monumento)

        Unidades = Unidades + Accion + Tesoro + TesoroSagrado + Monumento

        print(Unidades)

        columnas = 3

        nombre_salida = "imagen_Side.png"

        filas = -(-len(Unidades) // columnas)

        primera_imagen = Image.open(Unidades[0])
        ancho, alto = primera_imagen.size

        # Crear una nueva imagen con un tamaño que acomode todas las imágenes
        nueva_imagen = Image.new('RGBA', (columnas * ancho, filas * alto))

        
        # Combinar las imágenes en la nueva imagen
        for i, archivo in enumerate(Unidades):
            imagen = Image.open(archivo).convert('RGBA')
            fila = i // columnas
            columna = i % columnas
            nueva_imagen.paste(imagen, (columna * ancho, fila * alto))

        nueva_imagen.save(nombre_salida) 
            
            
    else:
        print(f'Error en la solicitud. Código de respuesta: {response.status_code}')


def Descarga_Imagenes():

    Input_NombreCarta = entrada_1.get()

    lineas = Input_NombreCarta.split("\n")

    # Eliminar espacios en blanco alrededor de cada línea
    lineas = [linea.strip() for linea in lineas]

    # Crear una lista de listas donde cada lista representa una fila de la tabla
    tabla = [linea.split() for linea in lineas if linea]

    # Imprimir la tabla
    for i, fila in enumerate(tabla):

        valor = str(" ".join(fila))

        resultado = re.search(r'(.+?)x\d+', valor)

        if resultado:
            texto_antes_de_x_numero = resultado.group(1)
            tabla[i] = resultado.group(1)
        else:
            tabla[i] = ""
        
   

    tabla = [elemento.strip() for elemento in tabla if elemento.strip() != ""]

    #print(tabla)

    url = 'https://lairentcg.com.ar:8443/api/carta/cartas/ordenadas'

    response = requests.get(url)

    Unidades = []
    Accion = []
    Tesoro = []
    TesoroSagrado = []
    Monumento = []

    if response.status_code == 200:

        data = response.json()
        df = pd.DataFrame(data)
        df = df.sort_index(axis=1)

        for i, fila in enumerate(tabla):
       
            Columnas = ['urlImagen', 'nombreCarta','tipo',"subtipo"]

            Filtro = df['nombreCarta'] == fila
            Resultado = df.loc[Filtro, Columnas]

            NombreCarta = Resultado['nombreCarta'].iloc[0] 
            UrlCarta = Resultado['urlImagen'].iloc[0]
            TipoCarta = Resultado['tipo'].iloc[0]
            Sagrado = Resultado['subtipo'].iloc[0]
            TipoCarta = str(TipoCarta)
            Sagrado = str(Sagrado)

            #print(NombreCarta)
            #print(UrlCarta)
            #print(TipoCarta)
            #print(Sagrado)


            nombre_archivo = "Pruebas_Lairen/"+ NombreCarta  + ".jpg"

            if os.path.exists(nombre_archivo):
                print(NombreCarta + " --- Ya esta descargada")
            else:
                url = (UrlCarta)

                response = requests.get(url)

                if response.status_code == 200:   
                    with open("Pruebas_Lairen/"+ NombreCarta  + ".jpg", 'wb') as file:
                        file.write(response.content)
                        print(NombreCarta + " --- Se descargo")
                else:
                    print(f"Error {response.status_code}: {response.text}")

            if "unidad" in TipoCarta.lower():
                NombreCarta2 = "Pruebas_Lairen/"+ NombreCarta  + ".jpg"                
                Unidades.append(NombreCarta2)
                
            elif "accion" in TipoCarta.lower(): 
                NombreCarta2 = "Pruebas_Lairen/"+ NombreCarta  + ".jpg"        
                Accion.append(NombreCarta2)

            elif "tesoro" in TipoCarta.lower():
                NombreCarta2 = "Pruebas_Lairen/"+ NombreCarta  + ".jpg"
                if "sagrado" in Sagrado.lower():
                    TesoroSagrado.append(NombreCarta2)
                else:
                    Tesoro.append(NombreCarta2)

            elif "monumento" in TipoCarta.lower(): 
                NombreCarta2 = "Pruebas_Lairen/"+ NombreCarta  + ".jpg"        
                Monumento.append(NombreCarta2)


        print("")
        print(Unidades)
        print("")
        print(Accion)
        print("")
        print(Tesoro)
        print("")
        print(TesoroSagrado)

        Unidades = Unidades + Accion + Monumento

        print(Unidades)

        columnas = 6

        nombre_salida = "imagen_unidades.png"

        filas = -(-len(Unidades) // columnas)

        primera_imagen = Image.open(Unidades[0])
        ancho, alto = primera_imagen.size

        # Crear una nueva imagen con un tamaño que acomode todas las imágenes
        nueva_imagen = Image.new('RGBA', (columnas * ancho, filas * alto))

        

       

        # Combinar las imágenes en la nueva imagen
        for i, archivo in enumerate(Unidades):
            imagen = Image.open(archivo).convert('RGBA')
            fila = i // columnas
            columna = i % columnas
            nueva_imagen.paste(imagen, (columna * ancho, fila * alto))

        nueva_imagen.save(nombre_salida) 

        # Guardar la nueva imagen

        columnas = 6

        nombre_salida = "imagen_Tesoro.png"
        filas = -(-len(Tesoro) // columnas)

        primera_imagen = Image.open(Tesoro[0])
        ancho, alto = primera_imagen.size

        # Crear una nueva imagen con un tamaño que acomode todas las imágenes
        nueva_imagen = Image.new('RGBA', (columnas * ancho, filas * alto))

        # Combinar las imágenes en la nueva imagen
        for i, archivo in enumerate(Tesoro):
            imagen = Image.open(archivo).convert('RGBA')
            fila = i // columnas
            columna = i % columnas
            nueva_imagen.paste(imagen, (columna * ancho, fila * alto))

        # Guardar la nueva imagen
        nueva_imagen.save(nombre_salida) 


        columnas = 3

        nombre_salida = "imagen_Sagrado.png"
        filas = -(-len(TesoroSagrado) // columnas)

        primera_imagen = Image.open(TesoroSagrado[0])
        ancho, alto = primera_imagen.size

        # Crear una nueva imagen con un tamaño que acomode todas las imágenes
        nueva_imagen = Image.new('RGBA', (columnas * ancho, filas * alto))

        # Combinar las imágenes en la nueva imagen
        for i, archivo in enumerate(TesoroSagrado):
            imagen = Image.open(archivo).convert('RGBA')
            fila = i // columnas
            columna = i % columnas
            nueva_imagen.paste(imagen, (columna * ancho, fila * alto))

        # Guardar la nueva imagen
        nueva_imagen.save(nombre_salida) 
            
            
    else:
        print(f'Error en la solicitud. Código de respuesta: {response.status_code}')

def limpiar_campos():
    # Limpiar los campos de entrada al hacer clic en el botón "Limpiar"
    entrada_1.delete(0, tk.END)



ventana =CTk()

ventana.title("Cupones Socios")

ventana.config(bg="#010101")  

ventana.geometry("800x700")

entrada_1 = CTkEntry(ventana,font = ('sans serif',12), placeholder_text= '                                PONE ACA EL DECK PUTOOOOOOOOOOOOOOO',
 border_color='#2cb67d', fg_color= '#010101', width =520,height=80)
entrada_1.pack()

boton_obtener = CTkButton(ventana,font = ('sans serif',12), border_color='#2cb67d', fg_color='#010101',
    hover_color='#2cb67d',corner_radius=12,border_width=2,
    text="Descarga", command = Descarga_Imagenes)
boton_obtener.pack()

boton_obtener2 = CTkButton(ventana,font = ('sans serif',12), border_color='#2cb67d', fg_color='#010101',
    hover_color='#2cb67d',corner_radius=12,border_width=2,
    text="SIDE", command = Prueba)
boton_obtener2.pack()

boton_obtener3 = CTkButton(ventana,font = ('sans serif',12), border_color='#2cb67d', fg_color='#010101',
    hover_color='#2cb67d',corner_radius=12,border_width=2,
    text="limpiar", command = limpiar_campos)
boton_obtener3.pack()

ventana.mainloop()