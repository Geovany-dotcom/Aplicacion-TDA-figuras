import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
from Geometria import Rectangulo, Circulo, Cuadrado, Triangulo
from PIL import Image, ImageTk  

def crear_interfaz():
    def calcular_rectangulo():
        altura = entrada_altura_rect.get()
        base = entrada_base_rect.get()

        if validar_entrada(altura, base):
            rect = Rectangulo(float(altura), float(base))
            resultado = rect.mostrar_resultados(rect.calcular_area(), rect.calcular_perimetro())
            messagebox.showinfo("Resultados", resultado)
        else:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

    def calcular_circulo():
        radio = entrada_radio.get()

        if validar_entrada(radio):
            circ = Circulo(float(radio))
            resultado = circ.mostrar_resultados(circ.calcular_area(), circ.calcular_perimetro())
            messagebox.showinfo("Resultados", resultado)
        else:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

    def calcular_cuadrado():
        lado = entrada_lado.get()

        if validar_entrada(lado):
            cuad = Cuadrado(float(lado))
            resultado = cuad.mostrar_resultados(cuad.calcular_area(), cuad.calcular_perimetro())
            messagebox.showinfo("Resultados", resultado)
        else:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

    def calcular_triangulo():
        lado_a = entrada_lado_a.get()
        lado_b = entrada_lado_b.get()
        lado_c = entrada_lado_c.get()

        if validar_entrada(lado_a, lado_b, lado_c):
            tri = Triangulo(float(lado_a), float(lado_b), float(lado_c))
            tipo = tri.tipo_triangulo()  
            area = tri.calcular_area()  
            perimetro = tri.calcular_perimetro()  
            resultado = f"Tipo: {tipo}\nÁrea: {area:.2f}\nPerímetro: {perimetro:.2f}"
            messagebox.showinfo("Resultados", resultado)
        else:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

    def validar_entrada(*valores):
        try:
            return all(float(valor) > 0 for valor in valores)
        except ValueError:
            return False


    ventana = tk.Tk()
    ventana.title("Cálculo de Figuras Geométricas")
    ventana.geometry("500x600")
    ventana.configure(bg="#f0f0f0")

    tk.Label(ventana, text="Calculadora de Figuras Geométricas", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack(pady=10)

    notebook = ttk.Notebook(ventana)
    notebook.pack(pady=10, expand=True)

    tab_rect = ttk.Frame(notebook)
    notebook.add(tab_rect, text="Rectángulo")

    tk.Label(tab_rect, text="Rectángulo", font=("Helvetica", 14)).pack(pady=5)
    imagen_rect = PhotoImage(file="rectangulo.png")
    label_imagen_rect = tk.Label(tab_rect, image=imagen_rect)
    label_imagen_rect.pack(pady=5)
    tk.Label(tab_rect, text="Altura:").pack()
    entrada_altura_rect = tk.Entry(tab_rect)
    entrada_altura_rect.pack(pady=5)
    tk.Label(tab_rect, text="Base:").pack()
    entrada_base_rect = tk.Entry(tab_rect)
    entrada_base_rect.pack(pady=5)
    tk.Button(tab_rect, text="Calcular Rectángulo", command=calcular_rectangulo, bg="#4CAF50", fg="white").pack(pady=10)

    tab_circ = ttk.Frame(notebook)
    notebook.add(tab_circ, text="Círculo")

    tk.Label(tab_circ, text="Círculo", font=("Helvetica", 14)).pack(pady=5)
    imagen_circ = PhotoImage(file="circulo.png")
    label_imagen_circ = tk.Label(tab_circ, image=imagen_circ)
    label_imagen_circ.pack(pady=5)
    tk.Label(tab_circ, text="Radio:").pack()
    entrada_radio = tk.Entry(tab_circ)
    entrada_radio.pack(pady=5)
    tk.Button(tab_circ, text="Calcular Círculo", command=calcular_circulo, bg="#4CAF50", fg="white").pack(pady=10)

    tab_cuad = ttk.Frame(notebook)
    notebook.add(tab_cuad, text="Cuadrado")

    tk.Label(tab_cuad, text="Cuadrado", font=("Helvetica", 14)).pack(pady=5)
    imagen_cuad = PhotoImage(file="cuadrado.png")
    label_imagen_cuad = tk.Label(tab_cuad, image=imagen_cuad)
    label_imagen_cuad.pack(pady=5)
    tk.Label(tab_cuad, text="Lado:").pack()
    entrada_lado = tk.Entry(tab_cuad)
    entrada_lado.pack(pady=5)
    tk.Button(tab_cuad, text="Calcular Cuadrado", command=calcular_cuadrado, bg="#4CAF50", fg="white").pack(pady=10)

    tab_tri = ttk.Frame(notebook)
    notebook.add(tab_tri, text="Triángulo")

    tk.Label(tab_tri, text="Triángulo", font=("Helvetica", 14)).pack(pady=5)

    imagen_tri_original = Image.open("triangulo.png")
    imagen_tri_redimensionada = imagen_tri_original.resize((150, 150), Image.LANCZOS)
    imagen_tri = ImageTk.PhotoImage(imagen_tri_redimensionada)

    label_imagen_tri = tk.Label(tab_tri, image=imagen_tri)
    label_imagen_tri.pack(pady=5)

    tk.Label(tab_tri, text="Lado A:").pack()
    entrada_lado_a = tk.Entry(tab_tri)
    entrada_lado_a.pack(pady=5)

    tk.Label(tab_tri, text="Lado B:").pack()
    entrada_lado_b = tk.Entry(tab_tri)
    entrada_lado_b.pack(pady=5)

    tk.Label(tab_tri, text="Lado C:").pack()
    entrada_lado_c = tk.Entry(tab_tri)
    entrada_lado_c.pack(pady=5)

    tk.Button(tab_tri, text="Calcular Triángulo", command=calcular_triangulo, bg="#4CAF50", fg="white").pack(pady=10)

    ventana.mainloop()  

crear_interfaz()
