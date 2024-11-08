import sqlite3
import tkinter as tk
from tkinter import messagebox

# Conexión a la base de datos SQLite
conn = sqlite3.connect('MiBD.db')
cursor = conn.cursor()

# Función para verificar usuario y contraseña
def verificar_usuario():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND contrasena=?", (usuario, contrasena))
    usuario_valido = cursor.fetchone()

    if usuario_valido:
        ventana_login.destroy()  # Cierra la ventana de login
        ventana_principal()  # Abre la ventana principal si el login es correcto
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Función para mostrar la ventana principal
def ventana_principal():
    ventana = tk.Tk()
    ventana.title("Menú Principal")
    ventana.geometry("400x300")
    ventana.configure(bg="#0077b6")  # Fondo celeste oscuro

    # Botones de opciones
    tk.Button(ventana, text="Productos", command=mostrar_productos).pack(pady=10)
    tk.Button(ventana, text="Clientes", command=mostrar_clientes).pack(pady=10)
    tk.Button(ventana, text="Historial de Ventas", command=mostrar_historial_ventas).pack(pady=10)
    tk.Button(ventana, text="Nueva Venta", command=nueva_venta).pack(pady=10)

    ventana.mainloop()

# Función para mostrar productos
def mostrar_productos():
    ventana = tk.Tk()
    ventana.title("Productos")
    ventana.geometry("400x400")
    ventana.configure(bg="#0077b6")  # Fondo celeste oscuro

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    for producto in productos:
        tk.Label(ventana, text=f"ID: {producto[0]}, Nombre: {producto[1]}, Stock: {producto[3]}, Precio: {producto[4] if len(producto) > 4 else 'No Asignado'}", bg="#0077b6", fg="white").pack()

    tk.Button(ventana, text="Añadir Producto", command=añadir_producto).pack(pady=5)
    tk.Button(ventana, text="Eliminar Producto", command=eliminar_producto).pack(pady=5)
    tk.Button(ventana, text="Establecer Precio de Producto", command=establecer_precio_producto).pack(pady=5)

    ventana.mainloop()

# Función para añadir un producto
def añadir_producto():
    ventana = tk.Tk()
    ventana.title("Añadir Producto")
    ventana.geometry("300x200")
    ventana.configure(bg="#0077b6")  # Fondo celeste oscuro

    tk.Label(ventana, text="Nombre:", bg="#0077b6", fg="white").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Descripción:", bg="#0077b6", fg="white").pack()
    entry_descripcion = tk.Entry(ventana)
    entry_descripcion.pack()

    tk.Label(ventana, text="Stock Inicial:", bg="#0077b6", fg="white").pack()
    entry_stock = tk.Entry(ventana)
    entry_stock.pack()

    def guardar_producto():
        nombre = entry_nombre.get()
        descripcion = entry_descripcion.get()
        stock = int(entry_stock.get())

        cursor.execute("INSERT INTO productos (nombre, descripcion, stock) VALUES (?, ?, ?)", (nombre, descripcion, stock))
        conn.commit()
        messagebox.showinfo("Producto", "Producto añadido exitosamente.")
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar_producto).pack(pady=10)

    ventana.mainloop()

# Función para eliminar un producto
def eliminar_producto():
    ventana = tk.Tk()
    ventana.title("Eliminar Producto")
    ventana.geometry("300x150")
    ventana.configure(bg="#0077b6")  # Fondo celeste oscuro

    tk.Label(ventana, text="ID del Producto a eliminar:", bg="#0077b6", fg="white").pack()
    entry_productoID = tk.Entry(ventana)
    entry_productoID.pack()

    def eliminar():
        productoID = int(entry_productoID.get())
        cursor.execute("DELETE FROM productos WHERE productoID=?", (productoID,))
        conn.commit()
        messagebox.showinfo("Producto", "Producto eliminado exitosamente.")
        ventana.destroy()

    tk.Button(ventana, text="Eliminar", command=eliminar).pack(pady=10)

    ventana.mainloop()

# Función para establecer o actualizar el precio de un producto
def establecer_precio_producto():
    ventana = tk.Tk()
    ventana.title("Establecer Precio")
    ventana.geometry("300x200")
    ventana.configure(bg="#0077b6")  # Fondo celeste oscuro

    tk.Label(ventana, text="ID del Producto:", bg="#0077b6", fg="white").pack()
    entry_productoID = tk.Entry(ventana)
    entry_productoID.pack()

    tk.Label(ventana, text="Nuevo Precio:", bg="#0077b6", fg="white").pack()
    entry_precio = tk.Entry(ventana)
    entry_precio.pack()

    def actualizar_precio():
        productoID = int(entry_productoID.get())
        precio = float(entry_precio.get())

        cursor.execute("UPDATE productos SET precio = ? WHERE productoID = ?", (precio, productoID))
        conn.commit()
        messagebox.showinfo("Producto", "Precio actualizado exitosamente.")
        ventana.destroy()

    tk.Button(ventana, text="Actualizar Precio", command=actualizar_precio).pack(pady=10)

    ventana.mainloop()

# Función para mostrar clientes
def mostrar_clientes():
    ventana = tk.Tk()
    ventana.title("Clientes")
    ventana.geometry("400x400")
    ventana.configure(bg="#0077b6")  # Fondo celeste oscuro

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    for cliente in clientes:
        tk.Label(ventana, text=f"ID: {cliente[0]}, Nombre: {cliente[1]}, Teléfono: {cliente[3]}", bg="#0077b6", fg="white").pack()

    tk.Button(ventana, text="Añadir Cliente", command=añadir_cliente).pack(pady=10)
    tk.Button(ventana, text="Eliminar Cliente", command=eliminar_cliente).pack(pady=10)

    ventana.mainloop()

# Función para añadir un cliente
def añadir_cliente():
    ventana = tk.Tk()
    ventana.title("Añadir Cliente")
    ventana.geometry("300x200")
    ventana.configure(bg="#0077b6")  # Fondo celeste oscuro

    tk.Label(ventana, text="Nombre:", bg="#0077b6", fg="white").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Dirección:", bg="#0077b6", fg="white").pack()
    entry_direccion = tk.Entry(ventana)
    entry_direccion.pack()

    tk.Label(ventana, text="Teléfono:", bg="#0077b6", fg="white").pack()
    entry_telefono = tk.Entry(ventana)
    entry_telefono.pack()

    def guardar_cliente():
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()

        cursor.execute("INSERT INTO clientes (nombre, direccion, telefono) VALUES (?, ?, ?)", (nombre, direccion, telefono))
        conn.commit()
        messagebox.showinfo("Cliente", "Cliente añadido exitosamente.")
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar_cliente).pack(pady=10)

    ventana.mainloop()

# Función para eliminar un cliente
def eliminar_cliente():
    ventana = tk.Tk()
    ventana.title("Eliminar Cliente")
    ventana.geometry("300x150")
    ventana.configure(bg="#0077b6")  # Fondo celeste oscuro

    tk.Label(ventana, text="ID del Cliente a eliminar:", bg="#0077b6", fg="white").pack()
    entry_clienteID = tk.Entry(ventana)
    entry_clienteID.pack()

    def eliminar():
        clienteID = int(entry_clienteID.get())
        cursor.execute("DELETE FROM clientes WHERE clienteID=?", (clienteID,))
        conn.commit()
        messagebox.showinfo("Cliente", "Cliente eliminado exitosamente.")
        ventana.destroy()

    tk.Button(ventana, text="Eliminar", command=eliminar).pack(pady=10)

    ventana.mainloop()

# Función para mostrar historial de ventas
def mostrar_historial_ventas():
    ventana = tk.Tk()
    ventana.title("Historial de Ventas")
    ventana.geometry("400x400")
    ventana.configure(bg="#0077b6")  # Fondo celeste oscuro

    cursor.execute("SELECT * FROM Entr_Sal_Inv WHERE tipo='Salida'")
    ventas = cursor.fetchall()
    for venta in ventas:
        tk.Label(ventana, text=f"Producto ID: {venta[1]}, Cantidad: {venta[2]}, Fecha: {venta[3]}", bg="#0077b6", fg="white").pack()

    ventana.mainloop()

# Función para realizar una nueva venta
def nueva_venta():
    ventana = tk.Tk()
    ventana.title("Nueva Venta")
    ventana.geometry("300x250")
    ventana.configure(bg="#0077b6")  # Fondo celeste oscuro

    tk.Label(ventana, text="ID del Producto:", bg="#0077b6", fg="white").pack()
    entry_productoID = tk.Entry(ventana)
    entry_productoID.pack()

    tk.Label(ventana, text="Cantidad:", bg="#0077b6", fg="white").pack()
    entry_cantidad = tk.Entry(ventana)
    entry_cantidad.pack()

    def procesar_venta():
        productoID = int(entry_productoID.get())
        cantidad = int(entry_cantidad.get())

        # Verifica si hay suficiente stock
        cursor.execute("SELECT stock FROM productos WHERE productoID=?", (productoID,))
        resultado = cursor.fetchone()
        if resultado and resultado[0] >= cantidad:
            # Actualiza el stock
            nuevo_stock = resultado[0] - cantidad
            cursor.execute("UPDATE productos SET stock = ? WHERE productoID = ?", (nuevo_stock, productoID))

            # Registra la transacción como una salida en el historial de inventario
            cursor.execute("INSERT INTO Entr_Sal_Inv (productoID, cantidad, tipo) VALUES (?, ?, 'Salida')", (productoID, cantidad))
            conn.commit()
            messagebox.showinfo("Venta", "Venta realizada exitosamente.")
        else:
            messagebox.showerror("Error", "Stock insuficiente para realizar la venta.")
        ventana.destroy()

    tk.Button(ventana, text="Realizar Venta", command=procesar_venta).pack(pady=10)

    ventana.mainloop()

# Crear la ventana de inicio de sesión
ventana_login = tk.Tk()
ventana_login.title("Login")
ventana_login.geometry("300x200")
ventana_login.configure(bg="white")  # Fondo blanco para la ventana de login

tk.Label(ventana_login, text="Usuario:", bg="white").pack()
entry_usuario = tk.Entry(ventana_login)
entry_usuario.pack()

tk.Label(ventana_login, text="Contraseña:", bg="white").pack()
entry_contrasena = tk.Entry(ventana_login, show="*")
entry_contrasena.pack()

tk.Button(ventana_login, text="Iniciar Sesión", command=verificar_usuario).pack(pady=10)

ventana_login.mainloop()

# Cierra la conexión a la base de datos cuando termine la aplicación
conn.close()
