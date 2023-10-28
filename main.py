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
        subtext="miles per hour",
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
        ventana_nueva = ttk.Toplevel("superhero")
        label_Frame_problema = ttk.LabelFrame(ventana_nueva,text="Problema1", bootstyle= "SUCCESS")
        label_Frame_problema.pack(ipadx=100)

        label_problema = ttk.Label(label_Frame_problema, text=""" Cual es el conjunto resultante de la Intersección de los conjuntos conformados por A={x/x letras que conforman el
nombre del mes en el que estamos} B = {x/x primeras 10 letras del abecedario}""")
        label_problema.pack()

        frame_formulario = ttk.Frame(ventana_nueva)
        label_entry = ttk.Label(ventana_nueva, text="Ingrese el mes en el que estamos: ")
        label_entry.pack(side=LEFT, pady=20)
        entrada = ttk.Entry(ventana_nueva)
        entrada.pack(side=LEFT)

    def problema3 (self):
        ventana_nueva = ttk.Toplevel("superhero")




root = ttk.Window("Proyecto final mate discreta 2", "superhero")

app = problemas(root)

root.mainloop()








        