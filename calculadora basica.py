# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:41:32 2024

@author: Lenovo
"""

import tkinter as tk
from tkinter import messagebox

# Funciones de operaciones
def click(boton):
    entrada.insert(tk.END, boton)  # Agregar el valor del botón a la pantalla

def limpiar():
    entrada.delete(0, tk.END)  # Limpiar la pantalla

def calcular():
    try:
        resultado = eval(entrada.get())  # Evaluar la expresión en la pantalla
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))  # Mostrar el resultado
    except Exception as e:
        messagebox.showerror("Error", "Expresión inválida")
        limpiar()

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")
ventana.resizable(False, False)

# Pantalla de entrada
entrada = tk.Entry(ventana, font=("Arial", 20), justify="right", bd=10, insertwidth=2)
entrada.grid(row=0, column=0, columnspan=4)

# Botones de números y operaciones
botones = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

fila = 1
columna = 0
for boton in botones:
    if boton == "=":
        tk.Button(ventana, text=boton, font=("Arial", 18), command=calcular).grid(row=fila, column=columna, sticky="nsew")
    elif boton == "C":
        tk.Button(ventana, text=boton, font=("Arial", 18), command=limpiar).grid(row=fila, column=columna, sticky="nsew")
    else:
        tk.Button(ventana, text=boton, font=("Arial", 18), command=lambda x=boton: click(x)).grid(row=fila, column=columna, sticky="nsew")
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Ajustar tamaño de botones
for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)
    ventana.grid_columnconfigure(i, weight=1)

ventana.mainloop()
