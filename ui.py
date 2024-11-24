import tkinter as tk
import customtkinter
from tkinter import scrolledtext
from PIL import Image, ImageTk
from tktooltip import ToolTip
import webbrowser


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
mainFrameTop .pack(fill='x')

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

mainFrameLeft = tk.Frame(root, width=50, height=800, bg = "gray10")
mainFrameLeft.pack_propagate(False)
mainFrameLeft.pack(side="left", fill='both', expand='true')

iconGenerate = ImageTk.PhotoImage(file = "./assets/prompt_icon.png") 
btnGenerateMode = tk.Button(mainFrameLeft, image = iconGenerate, bd = 0, height = 50, width = 50, bg="gray10", font=("Arial", 12))
btnGenerateMode.pack(side = "top")
ToolTip(btnGenerateMode, msg="Prompt to Image")

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


def openweb():
    webbrowser.open("https://prompthero.com/stable-diffusion-prompts",new=1)

btnPromptHero = tk.Button(mainFrameRight, text = "Prompt Help",command=openweb)
btnPromptHero.pack()

lblPrompt= tk.Label(mainFrameRight, text="PROMPT", fg="white", bg="gray60", font=("Arial", 10, "bold"))
lblPrompt.pack()

textPrompt = scrolledtext.ScrolledText(mainFrameRight, wrap=tk.WORD, width=40, height=8, font=("Arial", 12)) 
textPrompt.pack()

lblNegPrompt= tk.Label(mainFrameRight, text="PROMPT NEGATIVO", fg="white", bg="gray60", font=("Arial", 10, "bold"))
lblNegPrompt.pack()

textNegPrompt = scrolledtext.ScrolledText(mainFrameRight, wrap=tk.WORD, width=40, height=8, font=("Arial", 12)) 
textNegPrompt.pack()






