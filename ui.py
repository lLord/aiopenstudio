import tkinter as tk
import customtkinter
from tkinter import scrolledtext
from PIL import Image, ImageTk
from tktooltip import ToolTip
import webbrowser
import os, platform, subprocess
from pathlib import Path


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


############# MAIN WINDOW ########################################################################################################

root = tk.Tk()
root.title('IA Studio')
root.iconbitmap("./assets/icon.ico")
root.geometry("1600x900+0+0")
root.configure(bg="black")

############# MAIN FRAME TOP

mainFrameTop = tk.Frame(root, width=1600, height=50, bg = "black")
mainFrameTop.pack_propagate(False)
mainFrameTop .pack(fill='x', expand='false')

logoTop = Image.open('./assets/logo.jpg')
logo_Tk = ImageTk.PhotoImage(logoTop)
labelLogo = tk.Label(mainFrameTop, text="", image = logo_Tk, bg = "black")
labelLogo.pack(side="left")

lblTopCategory = tk.Label(mainFrameTop, text="Computer Vision >", fg="PaleGreen3", bg="black", font=('Arial', 14))
lblTopCategory.pack(side="left")
lblTopTask = tk.Label(mainFrameTop, text="Image-to-Text", fg="white", bg="black", font=('Arial', 12))
lblTopTask.pack(side="left")

lblTopProjectName = tk.Label(mainFrameTop, text="project: My First IA Project ", fg="white", bg="black", font=('Arial', 12))
lblTopProjectName.pack(side="right")

############# MAIN FRAME LEFT ()

mainFrameLeft = tk.Frame(root, width=60, height=800, bg = "gray10", pady=5, padx=5)
mainFrameLeft.pack_propagate(False)
mainFrameLeft.pack(side="left", fill='y', expand='false')

iconGenerate = ImageTk.PhotoImage(file = "./assets/prompt_icon.png") 
btnGenerateMode = tk.Button(mainFrameLeft, image = iconGenerate, bd = 0, height = 50, width = 50, bg="gray10", font=("Arial", 12))
btnGenerateMode.pack(side = "top")
ToolTip(btnGenerateMode, msg="Prompt to Image")

mainFramebottom = tk.Frame(root, width=1600, height=30, bg = "gray60", pady=5, padx=5)
mainFramebottom.pack_propagate(False)
mainFramebottom.pack(side="bottom", fill='x', expand='false')

############# MAIN FRAME CENTER

mainPanel = tk.PanedWindow(root,  bg ="black", bd=3)
mainPanel.pack(fill="both", expand="1")

panelCenter = tk.PanedWindow( bg="black", orient ="vertical")
panelCenter.configure(width=1000)

panelRight = tk.PanedWindow( bg="gray10", orient ="vertical", bd=3, width=400)
panelRight.configure(width=400)

mainPanel.add(panelCenter)
mainPanel.add(panelRight)

photo = ImageTk.PhotoImage(Image.open('./result.png'))
label = tk.Label( image=photo, bg="black")
panelCenter.add(label)

###PANEL RIGHT

settingsFrame = tk.Frame(  height= 350, bg = "black", pady=5, padx=5)
settingsFrame.pack_propagate(False)
settingsFrame.pack(side="top", fill='x', expand='true')
panelRight.add(settingsFrame)

lblGuide= tk.Label( settingsFrame,text="MODEL:", fg="white", bg="gray40", font=("Arial", 10, "bold"))
lblGuide.pack()

options = [
    "stable-diffusion-3.5-large-turbo",
    "alimama-creative-FLUX.1-Turbo-Alpha",
    "Flux-Midjourney-Mix-LoRA"
]

value_inside = tk.StringVar(root) 
value_inside.set("Stable-Diffusion-3.5-large-turbo")
dropModles = tk.OptionMenu(settingsFrame, value_inside, *options)
dropModles.pack()

lblGuide= tk.Label( settingsFrame,text="Width", fg="white", bg="gray40", font=("Arial", 10, "bold"))
lblGuide.pack()

lblGuide= tk.Label( settingsFrame,text="Height", fg="white", bg="gray40", font=("Arial", 10, "bold"))
lblGuide.pack()

lblGuide= tk.Label( settingsFrame,text="Guidance Scale", fg="white", bg="gray40", font=("Arial", 10, "bold"))
lblGuide.pack()


lblGuide= tk.Label( settingsFrame,text="Inference steps", fg="white", bg="gray40", font=("Arial", 10, "bold"))
lblGuide.pack()


lblGuide= tk.Label( settingsFrame,text="Seed", fg="black", bg="gray40", font=("Arial", 10, "bold"))
lblGuide.pack()

promptsFrame = tk.Frame(  height= 410, bg= "black", pady=5, padx=5)
promptsFrame.pack_propagate(False)
promptsFrame.pack(side="right", fill='x', expand='true')
panelRight.add(promptsFrame)

bottomFrame = tk.Frame(height=32, bg = "black", pady=5, padx=5)
bottomFrame.pack_propagate(True)
bottomFrame.pack(side="bottom", fill='x', expand='false')
panelRight.add(bottomFrame)
bottomFrame.configure(height=32)

def openweb():
    webbrowser.open("https://prompthero.com/stable-diffusion-prompts",new=1)
    
def openhistory():
    os.startfile(os.path.normpath('./history/'))

imgUndo = tk.PhotoImage(file = "./assets/undo_icon.png") 
btnUndo = tk.Button( bottomFrame, image = imgUndo, bg="black", borderwidth=0, padx=5)
btnUndo.pack(side="left")
btnUndo.configure(height=34)

imgHero = tk.PhotoImage(file = "./assets/redo_icon.png") 
btnHistory = tk.Button( bottomFrame, image = imgHero, bg="black", borderwidth=0 , padx=5)
btnHistory.pack(side="left")
btnHistory.configure(height=34)

btnHistory = tk.Button( bottomFrame, text = "History",command=openhistory, padx=5)
btnHistory.pack(side="left")
btnHistory.configure(height=34)

lblPrompt= tk.Label( promptsFrame, text="PROMPT", fg="white", bg="gray40", font=("Arial", 10, "bold"))
lblPrompt.pack(fill='x', expand='false')

textPrompt = scrolledtext.ScrolledText(promptsFrame ,wrap=tk.WORD, width=40, height=8, font=("Arial", 12)) 
textPrompt.pack(fill='x', expand='false')

lblNegPrompt= tk.Label(promptsFrame , text="PROMPT NEGATIVO", fg="black", bg="gray60", font=("Arial", 10, "bold"))
lblNegPrompt.pack(fill='x', expand='false')

textNegPrompt = scrolledtext.ScrolledText(promptsFrame , wrap=tk.WORD, width=40, height=8, font=("Arial", 12)) 
textNegPrompt.pack(fill='x', expand='false')

### bottom

lblBottomStatus = tk.Label( mainFramebottom,text="[IDLE] ", fg="white", bg="gray60")
lblBottomStatus.pack(side="left")

lblBottomSize = tk.Label( mainFramebottom,text="768x768 píxeles", fg="white", bg="gray60")
lblBottomSize .pack(side="left")

lblBottomTime= tk.Label( mainFramebottom,text="", fg="white", bg="gray60")
lblBottomTime.pack(side="left")


