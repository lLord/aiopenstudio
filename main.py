from PIL import Image, ImageTk
from gradio_client import Client, handle_file
from random import randrange
import time
from ui import *


# load from prompt.txt
with open("./config/prompt.txt", 'r') as file:
    content = file.read()
    textPrompt.delete(1.0, tk.END)  # Clear previous content
    textPrompt.insert(tk.END, content)

# load from prompt.txt
with open("./config/negative_prompt.txt", 'r') as file:
    content = file.read()
    textNegPrompt.delete(1.0, tk.END)  # Clear previous content
    textNegPrompt.insert(tk.END, content)

def promt_to_text():
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

buttonGen = tk.Button(text="Generar", fg="black", bg="aquamarine2", command=promt_to_text, font=("Arial", 14))
panelRight.add(buttonGen)
buttonGen.configure(height=30)
root.bind("<Return>", promt_to_text)


################  UPSCALE ################

def Upscaler2X( ):
    client = Client("https://bookbot-image-upscaling-playground.hf.space/")
    result = client.predict(
                    "./result.png",	# str (filepath or URL to image)
                    "modelx5",	# str in 'Choose Upscaler' Radio component
                    api_name="/predict"
    )
    print(result)
    print('Guardando imagen...')
    im=Image.open(result)  
    im.save('./result_upscale.png')
    current_timestamp = time.time()
    im.save( "./history/" + str(current_timestamp) + "_upscale.png")

def Upscaler4X():
    client = Client("https://bookbot-image-upscaling-playground.hf.space/")
    result = client.predict(
                    "./result.png",	# str (filepath or URL to image)
                    "modelx4",	# str in 'Choose Upscaler' Radio component
                    api_name="/predict"
    )
    print(result)
    print('Guardando imagen...')
    im=Image.open(result)  
    im.save('./result_upscale.png')
    current_timestamp = time.time()
    im.save( "./history/" + str(current_timestamp) + "_upscale.png")

def upscaler_window():
    new_window = tk.Toplevel()
    new_window.title('IA Studio ::: Upscaler')
    new_window.iconbitmap("./assets/icon.ico")
    new_window.geometry("950x768+50+50")
    new_window.configure(bg="black")

    upscaleFrameCenter = tk.Frame(new_window, width=768, height=768, bg = "gray40")
    upscaleFrameCenter.pack_propagate(False)
    upscaleFrameCenter.pack( side="left", fill='both', expand='true')

    photo = ImageTk.PhotoImage(Image.open('./result.png'))
    label = tk.Label(upscaleFrameCenter, image=photo)
    label.configure(image=photo)
    label.image = photo
    label.pack()

    upscaleFrameRight = tk.Frame(new_window, width=182, height=768, bg = "gray40", pady=20)
    upscaleFrameRight.pack_propagate(False)
    upscaleFrameRight.pack( side="left", fill='both', expand='true')

    button2x = tk.Button(upscaleFrameRight, text="Upscale X2", fg="black", bg="aquamarine2", command=Upscaler2X, font=("Arial", 14), padx=10, pady=10)
    button2x.pack()

    button4x = tk.Button(upscaleFrameRight, text="Upscale X4", fg="black", bg="aquamarine2", command=Upscaler4X, font=("Arial", 14),padx=10, pady=10)
    button4x.pack()

    lblTexto = tk.Label(upscaleFrameRight, text = "Destino: ./result_upscale.png", fg="white", bg = "gray40")
    lblTexto.pack()
    

iconUpscale = ImageTk.PhotoImage(file = "./assets/upscale_icon.png") 
btnUpscaleMode = tk.Button(mainFrameLeft, image = iconUpscale, bd = 0, command=upscaler_window, height = 50, width = 50, bg="gray10", font=("Arial", 12))
btnUpscaleMode.pack(side = "top")
ToolTip(btnUpscaleMode, msg="Upscaler")

################  INPAINT ################

def Inpainting():
    client = Client("multimodalart/flux-outpainting")
    result = client.predict(
            image=handle_file('./inpainting.png'),
            mask=handle_file('./inpainting_mask.png'),
            width=768,
            height=768,
            overlap_percentage=10,
            num_inference_steps=8,
            resize_option="Full",
            custom_resize_percentage=50,
            prompt_input="Black eyes",
            alignment="Middle",
            overlap_left=True,
            overlap_right=True,
            overlap_top=True,
            overlap_bottom=True,
            api_name="/inpaint_1"
    )

    print(result)
    return

def inpainting_window():
    new_window = tk.Toplevel()
    new_window.title('IA Studio ::: Inpainting')
    new_window.iconbitmap("./assets/icon.ico")
    new_window.geometry("1024x900+50+50")
    new_window.configure(bg="black")

    inpaintingFrameCenter = tk.Frame(new_window, width=1024, height=600, bg="gray60")
    inpaintingFrameCenter.pack( fill='both', expand='true')

    pic = Image.open('./inpainting_mask.png')
    pic = pic.resize((512, 512))
    photo = ImageTk.PhotoImage(pic)
    label = tk.Label(inpaintingFrameCenter, image=photo)
    label.configure(image=photo)
    label.image = photo
    label.pack(side="left")

    pic = Image.open('./inpainting.png')
    pic = pic.resize((512, 512))
    photo2 = ImageTk.PhotoImage(pic)
    label2 = tk.Label(inpaintingFrameCenter, image=photo)
    label2.configure(image=photo2)
    label2.image = photo2
    label2.pack(side="left")

    lblPrompt= tk.Label(inpaintingFrameCenter, text="PROMPT", fg="white", bg="gray60", font=("Arial", 10, "bold"))
    lblPrompt.pack(side="left")
    
    textPrompt = scrolledtext.ScrolledText(inpaintingFrameCenter, wrap=tk.WORD, width=40, height=8, font=("Arial", 12)) 
    textPrompt.pack(side="bottom")
    textPrompt.insert(tk.END, "black eyes")

    iconPaint = ImageTk.PhotoImage(file = "./assets/paint_icon.png") 
    btnPaint = tk.Button(inpaintingFrameCenter, image = iconPaint, bd = 0, height = 50, width = 50, font=("Arial", 12))
    btnPaint.pack(side="bottom")
    ToolTip(btnPaint , msg="Pintar")

icon3 = ImageTk.PhotoImage(file = "./assets/inpaint_icon.png") 
btnGenerateMode3 = tk.Button(mainFrameLeft, image = icon3, bd = 0, command=inpainting_window,  height = 50, width = 50, bg="gray10", font=("Arial", 12))
btnGenerateMode3.pack(side = "top")
ToolTip(btnGenerateMode3, msg="Inpainting")

################  CONTROLNET ################

def controlNET():
    return

def controlnet_window():
    new_window = tk.Toplevel()
    new_window.title('IA Studio ::: ControlNet')
    new_window.iconbitmap("./assets/icon.ico")
    new_window.geometry("1000x900+50+50")
    new_window.configure(bg="black")

icon4 = ImageTk.PhotoImage(file = "./assets/pose_icon.png") 
btnGenerateMode4 = tk.Button(mainFrameLeft, image = icon4, bd = 0, command=controlnet_window,  height = 50, width = 50, bg="gray10", font=("Arial", 12))
btnGenerateMode4.pack(side = "top")
ToolTip(btnGenerateMode4, msg="ControlNET")

def cleanImage():  #AuraSR-v2
    client = Client("gokaygokay/AuraSR-v2")
    result = client.predict(
            input_image=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
            api_name="/process_image"
    )
    print(result)

# Execute tkinter
tk.mainloop()
