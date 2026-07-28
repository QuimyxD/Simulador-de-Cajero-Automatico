# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 17:01:15 2025

@author: quime
"""

import tkinter as tk
from tkinter import ttk, messagebox

usuario_correcto = "quim"
contraseña_correcta = "1234"
saldo_actual = 10000
saldo_ahorro = 100000
saldo_corriente = 15000
saldo_credito = 8000
historial_transacciones = []

def mostrar_mensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)

def mostrar_error(mensaje):
    messagebox.showerror("Error", mensaje)

def Bienvenida():
    ventana = tk.Tk()
    ventana.title("Bienvenido al banco de robux")
    ventana.geometry("600x400")

    tk.Label(ventana, text="Hola, bienvenido al banco de Robux, ingresa tu tarjeta para continuar").grid(row=0, column=0, padx=10, pady=10)
    ttk.Button(ventana, text="Iniciar", command=lambda: [ventana.destroy(), Autentificacion()]).grid(row=1, column=0, padx=10, pady=10)

    ventana.mainloop()

def Autentificacion():
    ventana = tk.Tk()
    ventana.title("Autenticación")
    ventana.geometry("600x400")

    tk.Label(ventana, text="Ingrese su usuario y contraseña").grid(row=0, column=0, padx=10, pady=10)

    tk.Label(ventana, text="Usuario:").grid(row=1, column=0, padx=10, pady=5)
    entrada_usuario = ttk.Entry(ventana)
    entrada_usuario.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Contraseña:").grid(row=2, column=0, padx=10, pady=5)
    entrada_contraseña = ttk.Entry(ventana, show="*")
    entrada_contraseña.grid(row=2, column=1, padx=10, pady=5)

    def validar():
        usuario = entrada_usuario.get()
        contraseña = entrada_contraseña.get()

        if usuario == usuario_correcto and contraseña == contraseña_correcta:
            ventana.destroy()
            Menu()
        else:
            mostrar_error("Usuario o contraseña incorrectos")

    ttk.Button(ventana, text="Continuar", command=validar).grid(row=3, column=1, padx=10, pady=10)

def Menu():
    ventana = tk.Tk()
    ventana.title("Menú Principal")
    ventana.geometry("600x400")

    tk.Label(ventana, text="Menú principal").grid(row=0, column=0, padx=10, pady=10)

    ttk.Button(ventana, text="Ver Saldo", command=ver_saldo).grid(row=1, column=0, padx=10, pady=10)
    ttk.Button(ventana, text="Depositar Robux", command=depositar_robux).grid(row=2, column=0, padx=10, pady=10)
    ttk.Button(ventana, text="Retirar Robux", command=retirar_robux).grid(row=3, column=0, padx=10, pady=10)
    ttk.Button(ventana, text="Transferir Robux", command=transferir_robux).grid(row=1, column=5, padx=10, pady=10)
    ttk.Button(ventana, text="Ver Historial", command=ver_historial).grid(row=2, column=5, padx=10, pady=10)
    ttk.Button(ventana, text="Salir", command=ventana.quit).grid(row=3, column=5, padx=10, pady=10)
    
def ver_saldo():
    mostrar_mensaje("Saldo", f"Tu saldo actual es de {saldo_actual} Robux.\n"
                              f"Saldo Ahorro: {saldo_ahorro} Robux\n"
                              f"Saldo Corriente: {saldo_corriente} Robux\n"
                              f"Saldo Crédito: {saldo_credito} Robux.")

def depositar_robux():
    def realizar_deposito():
        global saldo_actual
        try:
            cantidad = int(entrada_cantidad.get())
            if cantidad > 0:
                saldo_actual += cantidad
                historial_transacciones.append(f"Depósito: +{cantidad} Robux")
                mostrar_mensaje("Depósito", f"Has depositado {cantidad} Robux. Saldo actual: {saldo_actual} Robux.")
                ventana_deposito.destroy()
            else:
                mostrar_error("La cantidad debe ser mayor que 0.")
        except ValueError:
            mostrar_error("Por favor, ingresa un número válido.")

    ventana_deposito = tk.Tk()
    ventana_deposito.title("Depositar Robux")
    ventana_deposito.geometry("600x400")

    tk.Label(ventana_deposito, text="Cantidad a depositar:").pack(pady=10)
    entrada_cantidad = ttk.Entry(ventana_deposito)
    entrada_cantidad.pack(pady=10)

    ttk.Button(ventana_deposito, text="Depositar", command=realizar_deposito).pack(pady=10)
    ttk.Button(ventana_deposito, text="Cancelar", command=ventana_deposito.destroy).pack(pady=10)

def retirar_robux():
    def seleccionar_monto(cuenta):
        ventana_cuenta.destroy()

        ventana_monto = tk.Tk()
        ventana_monto.title("Seleccionar Monto")
        ventana_monto.geometry("600x400")

        tk.Label(ventana_monto, text="Selecciona el monto a retirar:").pack(pady=10)

        montos = [5, 10, 20, 50, 100, 200, 500]
        for monto in montos:
            ttk.Button(ventana_monto, text=f"${monto}", command=lambda m=monto: realizar_retiro(m, cuenta)).pack(pady=2)

        ttk.Button(ventana_monto, text="Otro", command=lambda: ingresar_otro_monto(cuenta)).pack(pady=2)

    def ingresar_otro_monto(cuenta):
        ventana_otro = tk.Tk()
        ventana_otro.title("Ingresar Monto")
        ventana_otro.geometry("600x400")

        tk.Label(ventana_otro, text="Cantidad a retirar:").pack(pady=10)
        entrada_cantidad = ttk.Entry(ventana_otro)
        entrada_cantidad.pack(pady=10)

        def confirmar_otro_monto():
            try:
                cantidad = int(entrada_cantidad.get())
                if cantidad > 0:
                    realizar_retiro(cantidad, cuenta)
                    ventana_otro.destroy()
                else:
                    mostrar_error("La cantidad debe ser mayor que 0.")
            except ValueError:
                mostrar_error("Por favor, ingresa un número válido.")

        ttk.Button(ventana_otro, text="Confirmar", command=confirmar_otro_monto).pack(pady=10)

    def realizar_retiro(cantidad, cuenta):
        global saldo_corriente, saldo_ahorro, saldo_credito

        if cuenta == "Ahorro" and cantidad <= saldo_ahorro:
            saldo_ahorro -= cantidad
            historial_transacciones.append(f"Retiro: -{cantidad} Robux de Ahorro")
        elif cuenta == "Corriente" and cantidad <= saldo_corriente:
            saldo_corriente -= cantidad
            historial_transacciones.append(f"Retiro: -{cantidad} Robux de Corriente")
        elif cuenta == "Crédito" and cantidad <= saldo_credito:
            saldo_credito -= cantidad
            historial_transacciones.append(f"Retiro: -{cantidad} Robux de Crédito")
        else:
            mostrar_error("No tienes suficientes Robux en esa cuenta.")
            return

        mostrar_mensaje("Retiro", f"Has retirado {cantidad} Robux de la cuenta {cuenta}.")

    ventana_cuenta = tk.Tk()
    ventana_cuenta.title("Seleccionar Cuenta")
    ventana_cuenta.geometry("600x400")

    tk.Label(ventana_cuenta, text="Selecciona la cuenta:").pack(pady=10)
    ttk.Button(ventana_cuenta, text="Ahorro", command=lambda: seleccionar_monto("Ahorro")).pack(pady=5)
    ttk.Button(ventana_cuenta, text="Corriente", command=lambda: seleccionar_monto("Corriente")).pack(pady=5)
    ttk.Button(ventana_cuenta, text="Crédito", command=lambda: seleccionar_monto("Crédito")).pack(pady=5)

def transferir_robux():
    def realizar_transferencia():
        global saldo_actual
        try:
            cantidad = int(entrada_cantidad.get())
            usuario_destino = entrada_usuario.get()

            if cantidad > 0 and cantidad <= saldo_actual and usuario_destino:
                saldo_actual -= cantidad
                historial_transacciones.append(f"Transferencia: -{cantidad} Robux a {usuario_destino}")
                mostrar_mensaje("Transferencia", f"Has transferido {cantidad} Robux a {usuario_destino}.")
                ventana_transferencia.destroy()
            else:
                mostrar_error("Cantidad inválida o saldo insuficiente.")
        except ValueError:
            mostrar_error("Por favor, ingresa un número válido.")

    ventana_transferencia = tk.Toplevel()
    ventana_transferencia.title("Transferir Robux")
    ventana_transferencia.geometry("600x400")

    tk.Label(ventana_transferencia, text="Cantidad a transferir:").pack(pady=10)
    entrada_cantidad = ttk.Entry(ventana_transferencia)
    entrada_cantidad.pack(pady=10)

    tk.Label(ventana_transferencia, text="Usuario destino:").pack(pady=10)
    entrada_usuario = ttk.Entry(ventana_transferencia)
    entrada_usuario.pack(pady=10)

    ttk.Button(ventana_transferencia, text="Transferir", command=realizar_transferencia).pack(pady=10)
    ttk.Button(ventana_transferencia, text="Cancelar", command=ventana_transferencia.destroy).pack(pady=10)

def ver_historial():
    ventana_historial = tk.Toplevel()
    ventana_historial.title("Historial de Transacciones")
    ventana_historial.geometry("600x400")

    if historial_transacciones:
        historial_texto = "\n".join(historial_transacciones)
        tk.Label(ventana_historial, text="Historial de Transacciones:").pack(pady=10)
        tk.Label(ventana_historial, text=historial_texto, justify=tk.LEFT).pack(pady=10)
    else:
        tk.Label(ventana_historial, text="No hay transacciones registradas.").pack(pady=10)

    ttk.Button(ventana_historial, text="Cerrar", command=ventana_historial.destroy).pack(pady=10)

Bienvenida()