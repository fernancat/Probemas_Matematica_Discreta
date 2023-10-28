from PIL import Image

Image.CUBIC = Image.BICUBIC
import ttkbootstrap as ttk
import ttkbootstrap
from ttkbootstrap.constants import *




class problemas(ttk.Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
    


        label = ttk.Label(ventana,text="PROYECTO FINAL 2 MATE DISCRETA RESOLVIMIENTO DE PROBLEMAS")
        label.config(font=("Sans Seriff", 16))
        label.pack()


        
        #button problema 1

        boton_1 = ttk.Button(ventana,text="Problema 1", bootstyle= "DARK", command=self.problema1)
        boton_1.pack(fill=X,expand=YES, ipady=30, pady=10)


        boton_2 = ttk.Button(ventana,text="Problema 2",  bootstyle= "DANGER", command=self.problema2)
        boton_2.pack(fill=X,expand=YES, ipady=30, pady=10  )


        boton_3 = ttk.Button(ventana,text="Problema 3",  bootstyle= "SUCCESS", command=self.problema3)
        boton_3.pack(fill=X,expand=YES, ipady=30, pady=10  )

        meter = ttk.Meter(
        metersize=180,
        padding=5,
        amountused=25,
        metertype="semi",
        subtext="Calificacion",
        interactive=True,
        )
        meter.pack()





    def problema1 (self):
        ventana_nueva = ttk.Toplevel("superhero")
        label_Frame_problema = ttk.LabelFrame(ventana_nueva,text="Problema1", bootstyle= "SUCCESS")
        label_Frame_problema.pack(ipadx=100)
        label_problema = ttk.Label(label_Frame_problema, text="""  Tomando en cuenta que los números telefónicos de Guatemala están conformados por 8 dígitos y que el primer digito
no puede ser 0, 1, 8 o 9, ¿cuantos números telefónicos pares pueden existir en Guatemala?""")
        label_problema.pack()
        numeros_telefono_caracteristicas = 6*10**7
        numeros_pares = []

        for i in range(numeros_telefono_caracteristicas):
            if i%2 == 0:
                numeros_pares.append(i)

        numeros_pares = len(numeros_pares)

        label_pasos = ttk.Label(ventana_nueva,text= f"""Paso 1: 10-4 (numero posibilidades que se le quitan al primer digito) \n Paso: 2 Multiplicar por numero de digitos y posibilidades restantes: 6*10**7 \n Paso 3: Resultado {numeros_pares}""")
        label_pasos.pack(pady=20)


        button_resultado = ttk.Button(ventana_nueva, text=f"Los numeros pares que pueden existir en Guatemala con las condiciones son: {numeros_pares}", bootstyle="outline-danger")
        button_resultado.pack()
                
       

    def problema2 (self):
        def calcular():
            mes = set(entrada.get())
            conjunto_b = set('abcdefghij')
            interseccion = mes.intersection(conjunto_b)
            label_pasos = ttk.Label(ventana_nueva, text=f"Primer paso definir primer conjunto \n Conjunto A: {mes} \n Segundo definir el segundo conjunto \n Conjunto B: {conjunto_b} \n Paso 3 calcular la intersección \n la intersección de los dos conjuntos es {interseccion}")
            label_pasos.pack(pady=20)    


        ventana_nueva = ttk.Toplevel("superhero")
        label_Frame_problema = ttk.LabelFrame(ventana_nueva,text="Problema2", bootstyle= "SUCCESS")
        label_Frame_problema.pack(ipadx=100)

        label_problema = ttk.Label(label_Frame_problema, text=""" Cual es el conjunto resultante de la Intersección de los conjuntos conformados por A={x/x letras que conforman el
nombre del mes en el que estamos} B = {x/x primeras 10 letras del abecedario}""")
        label_problema.pack()

        frame_formulario = ttk.Frame(ventana_nueva)
        frame_formulario.pack()
        label_entry = ttk.Label(frame_formulario, text="Ingrese el mes en el que estamos: ")
        label_entry.pack(side=LEFT, pady=20)
        entrada = ttk.Entry(frame_formulario)
        entrada.pack(side=LEFT)
        boton_calcular = ttk.Button(frame_formulario, text="Calcular problema", bootstyle= "SUCCESS", command=calcular)
        boton_calcular.pack(side=LEFT)

        

    def problema3 (self):
        ventana_nueva = ttk.Toplevel("superhero")
        label_Frame_problema = ttk.LabelFrame(ventana_nueva,text="Problema3", bootstyle= "SUCCESS")
        label_Frame_problema.pack(ipadx=100)
        label_problema = ttk.Label(label_Frame_problema, text=""" Por medio del Algoritmo de Euclides calcular el MCD de 24 – 62""")
        label_problema.pack()

        constantes= 24
        constantes_2 = 62
        a = 24
        b = 62

        while b!=0:
            a,b = b, a%b

        label_pasos = ttk.Label(ventana_nueva, text=f"Paso 1 Dividir entre {constantes},{constantes_2} hasta que obtengamos como reiduo 0 y el cociente sera nuestro maximo comun divisor \n Paso 2: Resultado, MCD de {constantes} y {constantes_2} es {a}")
        label_pasos.pack(pady=20)




root = ttk.Window("Proyecto final mate discreta 2", "superhero")

app = problemas(root)

root.mainloop()








        