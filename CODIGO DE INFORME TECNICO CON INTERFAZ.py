import pandas as pd
import math
import time
from tkinter import Tk, Label, Button, Entry, StringVar, ttk, Text, END

# Funciones de búsqueda
def buscar_por_dni(df, dni):
    resultado = df[df['DNI'] == dni]
    if not resultado.empty:
        return resultado
    else:
        return None

def busqueda_ternaria(lista, objetivo):
    izq = 0
    der = len(lista) - 1
    saltos = 0

    while izq <= der:
        tercio1 = izq + (der - izq) // 3
        tercio2 = der - (der - izq) // 3
        saltos += 1

        if lista[tercio1] == objetivo:
            return tercio1, saltos
        if lista[tercio2] == objetivo:
            return tercio2, saltos
        if objetivo < lista[tercio1]:
            der = tercio1 - 1
        elif objetivo > lista[tercio2]:
            izq = tercio2 + 1
        else:
            izq = tercio1 + 1
            der = tercio2 - 1

    return -1, saltos

def buscar_por_salto(df, dni):
    datos = df.sort_values(by="DNI").reset_index(drop=True)
    n = len(datos)
    step = int(math.sqrt(n))
    saltos = 0

    prev = 0
    while prev < n and datos.iloc[min(step, n) - 1]["DNI"] < dni:
        saltos += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return None, saltos

    for i in range(prev, min(step, n)):
        saltos += 1
        if datos.iloc[i]["DNI"] == dni:
            return datos.iloc[[i]], saltos

    return None, saltos

def crear_hash(df):
    return {row['DNI']: row.to_dict() for _, row in df.iterrows()}

def buscar_por_dni_hash(hash_table, dni):
    return hash_table.get(dni, None), 1

def busqueda_binaria(lista, objetivo):
    izq = 0
    der = len(lista) - 1
    saltos = 0

    while izq <= der:
        medio = (izq + der) // 2
        saltos += 1
        if lista[medio] == objetivo:
            return medio, saltos
        elif lista[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1

    return -1, saltos

# Función para realizar la búsqueda
def realizar_busqueda():
    metodo = combo_metodo.get()
    dni_input = entrada_dni.get()

    if not dni_input.isdigit():
        resultado_texto.insert(END, "Por favor, ingrese un DNI válido (sólo números).\n")
        return

    dni_a_buscar = int(dni_input)
    inicio = time.perf_counter()
    resultado = None
    saltos = 0

    if metodo == "Búsqueda lineal":
        resultado = buscar_por_dni(df, dni_a_buscar)
    elif metodo == "Búsqueda ternaria":
        indice, saltos = busqueda_ternaria(lista_dnis, dni_a_buscar)
        if indice != -1:
            resultado = df.iloc[[indice]]
    elif metodo == "Búsqueda por salto":
        resultado, saltos = buscar_por_salto(df, dni_a_buscar)
    elif metodo == "Búsqueda hash":
        resultado, saltos = buscar_por_dni_hash(hash_table, dni_a_buscar)
    elif metodo == "Búsqueda binaria":
        indice, saltos = busqueda_binaria(lista_dnis, dni_a_buscar)
        if indice != -1:
            resultado = df.iloc[[indice]]
    
    tiempo = time.perf_counter() - inicio

    if resultado is not None and not isinstance(resultado, dict):
        resultado_texto.insert(END, f"\nResultado encontrado:\n{resultado.to_string(index=False)}\n")
    elif isinstance(resultado, dict):
        resultado_texto.insert(END, f"\nResultado encontrado:\n")
        for clave, valor in resultado.items():
            resultado_texto.insert(END, f"{clave}: {valor}\n")
    else:
        resultado_texto.insert(END, "\nNo se encontró ningún registro con el DNI ingresado.\n")

    resultado_texto.insert(END, f"Tiempo de búsqueda: {tiempo:.6f} segundos\n")
    resultado_texto.insert(END, f"Saltos realizados: {saltos if metodo != 'Búsqueda lineal' else 'N/A'}\n")
    resultado_texto.insert(END, "-" * 50 + "\n")

# Leer el archivo y preparar datos
df = pd.read_excel('C:\\Users\\ASUS TUF GAMING\\Documents\\TRABAJOS\\VStudioCode\\Venta.xlsx')
df["DNI"] = pd.to_numeric(df["DNI"], errors="coerce")
lista_dnis = df['DNI'].sort_values().tolist()
hash_table = crear_hash(df)

# Crear ventana principal
ventana = Tk()
ventana.title("Buscador de DNIs")
ventana.geometry("700x500")

# Etiquetas y entradas
Label(ventana, text="Ingrese el DNI a buscar:").pack(pady=5)
entrada_dni = Entry(ventana)
entrada_dni.pack(pady=5)

Label(ventana, text="Seleccione el método de búsqueda:").pack(pady=5)
combo_metodo = ttk.Combobox(ventana, values=["Búsqueda lineal", "Búsqueda ternaria", "Búsqueda por salto", "Búsqueda hash", "Búsqueda binaria"])
combo_metodo.current(0)
combo_metodo.pack(pady=5)

Button(ventana, text="Buscar", command=realizar_busqueda).pack(pady=10)

resultado_texto = Text(ventana, height=15, width=80)
resultado_texto.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
