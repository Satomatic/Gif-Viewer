from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import linecache
import threading
import webbrowser
import pygame
import time
import sys
import os

# This was written by Satomatic (Brian Thomson)
# github.com/Satomatic
# Clear temp on startup

for item in os.listdir("Temp"):
	if ".ignore" in item:
		continue
	else:
		os.remove("Temp/" + item)

def Close(event):
	if messagebox.askyesno("Sure", "Are you sure you would\nlike to quit?"):
		for item in os.listdir("Temp"):
			if ".ignore" in item:
				continue
			else:
				os.remove("Temp/" + item)
				
		sys.exit(1)
	else:
		passs
		
window = Tk()

window.title("Gif Viewer")
window.geometry("500x500")
window.protocol('WM_DELETE_WINDOW', Close)
window.resizable(0,0)
window.iconbitmap("icon.ico")
		
def extractFrames(inGif, outFolder):
	frame = Image.open(inGif)
	nframes = 0
	while frame:
		frame.save('%s/%s-%s.gif' % (outFolder, os.path.basename(inGif), nframes ), 'PNG')
		nframes += 1
		try:
			frame.seek(nframes)
		except EOFError:
			break;
	return True
	
def RunFrame():
	while True:
		for item in os.listdir("Temp"):
			if ".gif" in item:
				imagename = "Temp/" + item

				ImageObject = PhotoImage(file=imagename)
				PhotoFrame.config(image=ImageObject)
				time.sleep(0.1)
			else:
				continue
	
def LoadGithub():
	webbrowser.open_new(r"https://www.github.com/Satomatic")

def Open(event):
	try:
		filepath = filedialog.askopenfilename(filetypes = (("gif animation","*.gif"),("all files","*.*")))
		
		if filepath == "":
			pass
		else:
			filename = os.path.basename(filepath)

			if filename.endswith(".gif"):
				print("File type gif")

				# Clear temp if failed on startup
				for item in os.listdir("Temp"):
					if ".ignore" in item:
						continue
					else:
						os.remove("Temp/" + item)
					
				extractFrames(filepath, 'Temp')
				window.title("Gif Viewer :: " + filename)
				img = pygame.image.load(filepath)
				width = img.get_width()
				height = img.get_height()
				window.geometry(str(width) + "x" + str(height))
				
				RunThread = threading.Thread(target=RunFrame)
				RunThread.daemon = True
				RunThread.start()
			else:
				print("Bad file type")
				messagebox.showerror("Error", "Unsupported file type,\nPlease use '.gif'")
	except:
		messagebox.showerror("Error", "An unknown error has occurred :/")
		
# Menu Bar
menubar = Menu(window)
window.config(menu=menubar)

# File Menu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command= lambda: Open("penis lol"))
filemenu.add_command(label="Exit", command= lambda: Close("dak jimbles"))

# Other stuff
menubar.add_command(label="github", command=LoadGithub)
menubar.add_command(label="exit", command= lambda: Close(">:O"))

PhotoFrame = Label(window)
PhotoFrame.pack(fill=BOTH)

# Key Binds
window.bind("<Control-o>", Open)
window.bind("<Control-O>", Open)
window.bind("<Escape>", Close)

window.mainloop()
