import tkinter as tk 
from tkinter import Radiobutton, messagebox
import re
import mysql.connector 

def insertarRegistros (nombre, apellidos, telefono, estatura, edad, genero):
    try:
        conexion = mysql.connector.connect (
            host = "localhost",
            port = "3306",
            user = "root",
            password = "cajed",
            database = "formulario" )
        cursor = conexion.cursor()
        
        query = "insert into tabla (nombre, apellidos, telefono, estatura, edad, genero) values (%s, %s, %s, %s, %s, %s)"
        values = (nombre, apellidos, telefono, estatura, edad, genero )
        cursor.execute (query, values)
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("informacion", "Datos guardados a la base de datos con exito.")
    except mysql.connector.Error as err:
        messagebox.showerror ("Error", f"Error al insertar los datos: {err}")
        

def save():
    nombre = tbNombre.get()
    apellidos = tbApellidos.get()
    telefono = tbTelefono.get()
    estatura = tbEstatura.get()
    edad = tbEdad.get()
    genero = ""
    if varGenero.get() ==1:
        genero = "Masculino"
    elif varGenero.get() ==2:
        genero = "Femenino"
    if (Enterovalido(edad) and Decimalvalido(estatura) and Telefonovalido(telefono) and Textovalido (apellidos) ):
      insertarRegistros (nombre, apellidos, telefono, estatura, edad, genero)
      data = "Nombres: " + nombre + "\nApellidos: " + apellidos + "\nEstatura: " + estatura + "\nTelefono: " + telefono + "\nEdad: " + edad + "\nGenero: " + genero
      with open ("302024Data.txt", "a") as file: 
         file.write(data + "\n\n")
      messagebox.showinfo ("Informacion" + "Datos guardados correctamente\n\n", data)
    else:
        messagebox.showerror ("Error", "No se pudieron guardar los datos\n\nDatos Erroneos")
   


 
def clear ():
    tbNombre.delete (0,tk.END)
    tbApellidos.delete (0,tk.END)
    tbEstatura.delete (0,tk.END)
    tbTelefono.delete (0,tk.END)
    tbEdad.delete (0,tk.END)
    varGenero.set (0)

#Validaciones
def Enterovalido (valor):
    try:
        int (valor)
        return True 
    except ValueError:
        return False
def Decimalvalido (valor):
    try:
        float (valor)
        return True 
    except ValueError:
        return False
def Telefonovalido (valor):
    return valor.isdigit() and len(valor)==10
def Textovalido (valor):
    return bool (re.match ("^[a-zA-Z\s]+$",valor))


ventana = tk.Tk()
ventana.geometry ("520x500")
ventana.title ("FormularioP")

varGenero = tk.IntVar()

lbNombre = tk.Label (ventana, text = "Nombre: ")
lbNombre.pack()
tbNombre = tk.Entry()
tbNombre.pack()
lbApellidos = tk.Label (ventana, text = "Apellidos: ")
lbApellidos.pack()
tbApellidos = tk.Entry()
tbApellidos.pack()
lbEstatura = tk.Label (ventana, text = "Estatura: ")
lbEstatura.pack()
tbEstatura = tk.Entry()
tbEstatura.pack()
lbTelefono = tk.Label (ventana, text = "Telefono: ")
lbTelefono.pack()
tbTelefono = tk.Entry()
tbTelefono.pack()
lbEdad = tk.Label (ventana, text = "Edad: ")
lbEdad.pack()
tbEdad = tk.Entry()
tbEdad.pack()
lbGenero = tk.Label (ventana, text = "Genero: ")
lbGenero.pack()
rbMasculino =  Radiobutton (ventana, text = "Masculino", variable = varGenero, value=1)
rbMasculino.pack ()
rbFemenino = Radiobutton (ventana, text = "Femenino", variable = varGenero, value =2)
rbFemenino.pack()

btnClear = tk.Button (ventana, text = "Borrar valores", command=clear)
btnClear.pack()
btnSave= tk.Button (ventana, text = "Guardar valores" , command=save)
btnSave.pack()

ventana.mainloop()
