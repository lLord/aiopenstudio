import tkinter as tk
from tkinter import scrolledtext
from tktooltip import ToolTip
from PIL import Image, ImageTk
from gradio_client import Client, handle_file
from random import randrange
import time

root = tk.Tk()
root.title('IA Studio')
root.iconbitmap("icon.ico")
root.geometry("1600x900+0+0")
root.configure(bg="black")



############# MAIN FRAME TOP

mainFrameTop = tk.Frame(root, width=1600, height=50, bg = "black")
mainFrameTop.pack_propagate(False)
mainFrameTop .pack(fill='x')

logoTop = Image.open('logo.jpg')
logo_Tk = ImageTk.PhotoImage(logoTop)
labelLogo = tk.Label(mainFrameTop, text="", image = logo_Tk, bg = "black")
labelLogo.pack(side="left")

lblTopCategory = tk.Label(mainFrameTop, text="Computer Vision >", fg="PaleGreen3", bg="black", font=('Arial', 14))
lblTopCategory.pack(side="left")
lblTopTask = tk.Label(mainFrameTop, text="Image-to-Text", fg="white", bg="black", font=('Arial', 12))
lblTopTask.pack(side="left")

lblTopProjectName = tk.Label(mainFrameTop, text="project: My First IA Project ", fg="white", bg="black", font=('Arial', 12))
lblTopProjectName.pack(side="right")

############# MAIN FRAME LEFT

mainFrameLeft = tk.Frame(root, width=50, height=800, bg = "gray10")
mainFrameLeft.pack_propagate(False)
mainFrameLeft.pack(side="left", fill='both', expand='true')

btnGenerateMode = tk.Button(mainFrameLeft, text="Generar", fg="white", bg="gray10", font=("Arial", 12))
btnGenerateMode.pack()
ToolTip(btnGenerateMode, msg="Hover info")

btnGenerateMode = tk.Button(mainFrameLeft, text="In-painting", fg="white", bg="gray10", font=("Arial", 12))
btnGenerateMode.pack()
ToolTip(btnGenerateMode, msg="In-painting")

btnGenerateMode = tk.Button(mainFrameLeft, text="Upscaler", fg="white", bg="gray10", font=("Arial", 12))
btnGenerateMode.pack()
ToolTip(btnGenerateMode, msg="Upscaler")

############# MAIN FRAME CENTER

mainFrameCenter = tk.Frame(root, width=1200, height=800, bg = "gray40")
mainFrameCenter.pack_propagate(False)
mainFrameCenter.pack( side="left", fill='both', expand='true')

photo = ImageTk.PhotoImage(Image.open('./result.png'))
label = tk.Label(mainFrameCenter, image=photo)
label.pack()

############# MAIN FRAME RIGHT

mainFrameRight = tk.Frame(root, width=350, height=800, bg="gray60")
mainFrameRight.pack_propagate(False)
mainFrameRight.pack(side="right", fill='both', expand='true')

lblRightWidth = tk.Label(mainFrameRight, text="Width", fg="white", bg="gray60")
lblRightWidth.pack()

lblRightHeight = tk.Label(mainFrameRight, text="Height", fg="white", bg="gray60")
lblRightHeight.pack()

lblRightLoading = tk.Label(mainFrameRight, text="Loading", fg="white", bg="gray60")
lblRightLoading.pack()

lblRightTime= tk.Label(mainFrameRight, text="Time", fg="white", bg="gray60")
lblRightTime.pack()

lblPrompt= tk.Label(mainFrameRight, text="PROMPT", fg="white", bg="gray60", font=("Arial", 10, "bold"))
lblPrompt.pack()

textPrompt = scrolledtext.ScrolledText(mainFrameRight, wrap=tk.WORD, width=40, height=8, font=("Arial", 12)) 
textPrompt.pack()

# load from prompt.txt
with open("./config/prompt.txt", 'r') as file:
    content = file.read()
    textPrompt.delete(1.0, tk.END)  # Clear previous content
    textPrompt.insert(tk.END, content)

lblNegPrompt= tk.Label(mainFrameRight, text="PROMPT NEGATIVO", fg="white", bg="gray60", font=("Arial", 10, "bold"))
lblNegPrompt.pack()

textNegPrompt = scrolledtext.ScrolledText(mainFrameRight, wrap=tk.WORD, width=40, height=8, font=("Arial", 12)) 
textNegPrompt.pack()

# load from prompt.txt
with open("./config/negative_prompt.txt", 'r') as file:
    content = file.read()
    textNegPrompt.delete(1.0, tk.END)  # Clear previous content
    textNegPrompt.insert(tk.END, content)

def cosas():
    #save prompts
    texto_positivo = textPrompt.get('1.0', tk.END)
    fl = open("./config/prompt.txt", "w")
    fl.write(texto_positivo)
    fl.close()
    texto_negativo = textNegPrompt.get('1.0', tk.END)
    fl = open("./config/negative_prompt.txt", "w")
    fl.write(texto_negativo)
    fl.close()

    print("Cargar")
    tiempo = generate(texto_positivo, texto_negativo)
    lblRightTime.config(text="Generado en" + str(tiempo))

    print("Cargado")

def generate(texto_positivo, texto_negativo):
    PROMPT= texto_positivo
    NEG_PROMPT= texto_negativo
    start_time = time.time()
    client = Client("doevent/stable-diffusion-3.5-large-turbo")
    print('generando')
    result = client.predict(
            prompt=PROMPT,
            negative_prompt=NEG_PROMPT,
            seed=0,
            randomize_seed=True,
            width=768,
            height=768,
            guidance_scale=0,
            num_inference_steps=4,
            api_name="/infer"
    )
    print('Guardando imagen...')
    im=Image.open(result[0])  
    im.save('./result.png')
    im=Image.open('./result.png')  
    current_timestamp = time.time()
    im.save( "./history/" + str(current_timestamp) + ".png")
    tiempo = time.time() - start_time
    photo2 = ImageTk.PhotoImage(Image.open('./result.png'))
    label.configure(image=photo2)
    label.image = photo2
    print("%s" % (tiempo))
    return tiempo

button = tk.Button(mainFrameRight, text="Generar", fg="white", bg="gray20", command=cosas, font=("Arial", 14))
button.pack()
root.bind("<Return>", cosas)

# Execute tkinter
tk.mainloop()
