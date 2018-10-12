from tkinter import *
from tkinter import filedialog
from PIL import Image
import threading
import webbrowser
import pygame
import time
import sys
import os

# This was written by Satomatic (Brian Thomson)
# github.com/Satomatic

def extractFrames(inGif, outFolder):
	frame = Image.open(inGif)
	nframes = 0
	while frame:
		frame.save( '%s/%s-%s.gif' % (outFolder, os.path.basename(inGif), nframes ) , 'PNG')
		nframes += 1
		try:
			frame.seek( nframes )
		except EOFError:
			break;
	return True
	
def RunFrame():
	while True:
		for item in os.listdir("Temp"):
			imagename = "Temp/" + item
			
			ImageObject = PhotoImage(file=imagename)
			PhotoFrame.config(image=ImageObject)
			time.sleep(0.1)

def Close():    
	sys.exit(1)
	
def LoadGithub(event):
	webbrowser.open_new(r"https://www.github.com/Satomatic")
	
window = Tk()

window.title("Gif Viewer")
window.geometry("500x500")
window.protocol('WM_DELETE_WINDOW', Close)
window.resizable(0,0)
window.iconbitmap("icon.ico")
		
try:
	filepath = filedialog.askopenfilename(filetypes = (("gif animation","*.gif"),("all files","*.*")))
except:
	Close()

# Clear temp #
for item in os.listdir("Temp"):
	os.remove("Temp/" + item)

extractFrames(filepath, 'Temp')
filename = os.path.basename(filepath)
window.title("Gif Viewer :: " + filename)
img = pygame.image.load(filepath)
width = img.get_width()
height = img.get_height()
window.geometry(str(width) + "x" + str(height))

PhotoFrame = Label(window)
PhotoFrame.pack(fill=BOTH)

RunThread = threading.Thread(target=RunFrame)
RunThread.daemon = True
RunThread.start()

window.mainloop()
