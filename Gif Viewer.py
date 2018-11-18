from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
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

def Close():
	for item in os.listdir("Temp"):
		if ".ignore" in item:
			continue
		else:
			os.remove("Temp/" + item)
			
	sys.exit(1)
	
def LoadGithub():
	webbrowser.open_new(r"https://www.github.com/Satomatic")
	
window = Tk()

window.title("Gif Viewer")
window.geometry("500x500")
window.protocol('WM_DELETE_WINDOW', Close)
window.resizable(0,0)
window.iconbitmap("icon.ico")

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

menubar = Menu(window)
menubar.add_command(label="open", command= lambda: Open("penis lol"))
menubar.add_command(label="github", command=LoadGithub)
menubar.add_command(label="exit", command=Close)
window.config(menu=menubar)

PhotoFrame = Label(window)
PhotoFrame.pack(fill=BOTH)

# Key Binds
window.bind("<Control-o>", Open)

window.mainloop()
