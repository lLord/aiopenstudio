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

mainPanel = tk.PanedWindow(root,  bg = "black", bd=3)
mainPanel.pack(fill="both", expand="1")



panelCenter = tk.PanedWindow(mainPanel, bg="black", orient ="vertical")
panelCenter.configure(width=1000)

panelRight = tk.PanedWindow(mainPanel, bg="gray60", orient ="vertical", bd=3, width=400)
panelRight.configure(width=400)

mainPanel.add(panelCenter)
mainPanel.add(panelRight)

photo = ImageTk.PhotoImage(Image.open('./result.png'))
label = tk.Label( image=photo)
panelCenter.add(label)


###PANEL RIGHT

def openweb():
    webbrowser.open("https://prompthero.com/stable-diffusion-prompts",new=1)
    
def openhistory():
    os.startfile(os.path.normpath('./history/'))

btnPromptHero = tk.Button(  text = "Prompt Help",command=openweb)
panelRight.add(btnPromptHero)

btnHistory = tk.Button( text = "History",command=openhistory)
panelRight.add(btnHistory)

lblPrompt= tk.Label( text="PROMPT", fg="white", bg="gray60", font=("Arial", 10, "bold"))
panelRight.add(lblPrompt)

textPrompt = scrolledtext.ScrolledText(wrap=tk.WORD, width=40, height=8, font=("Arial", 12)) 
panelRight.add(textPrompt)

lblNegPrompt= tk.Label( text="PROMPT NEGATIVO", fg="white", bg="gray60", font=("Arial", 10, "bold"))
panelRight.add(lblNegPrompt)

textNegPrompt = scrolledtext.ScrolledText( wrap=tk.WORD, width=40, height=8, font=("Arial", 12)) 
panelRight.add(textNegPrompt)


### bottom

lblRightWidth = tk.Label( mainFramebottom,text="Width", fg="white", bg="gray60")
lblRightWidth.pack(side="left")

lblRightHeight = tk.Label( mainFramebottom,text="Height", fg="white", bg="gray60")
lblRightHeight.pack(side="left")

lblRightLoading = tk.Label( mainFramebottom,text="Loading", fg="white", bg="gray60")
lblRightLoading.pack(side="left")

lblRightTime= tk.Label( mainFramebottom,text="Time", fg="white", bg="gray60")
lblRightTime.pack(side="left")


