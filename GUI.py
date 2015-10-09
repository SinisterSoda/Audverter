import tkinter as tk
from tkinter.filedialog import askdirectory
from Converter import *

class ApplicationGUI(tk.Frame):
    master=None
    directory=""
    converter=None

    def __init__(self, c):
        master=tk.Tk()
        tk.Frame.__init__(self, master)
        self.converter = c
        self.grid(row=0, column=0, sticky="nsew")
        self.converter.app = self
        
        
        self.pack()
        self.createWM()
        self.createComponents()

    def createComponents(self):
        #start topframe
        self.frameRow1 = tk.Frame(self)
        self.frameRow1.grid(row=0, column=0)
        
        #label
        self.fileLabel = tk.Label(self.frameRow1, text="Directory: ", font = "Helvetica 14")
        self.fileLabel.grid(row=0, padx=(0, 10), sticky=tk.NW)
        
        #file name text box
        self.fileName = tk.Entry(self.frameRow1, font = "Helvetica 14", state='disabled')
        self.fileName.grid(row=0, column=1, sticky=tk.NW, padx=(0,5))
        
        #select file button
        #button image
        self.selectFileImage = tk.PhotoImage(file="img/button2.gif")
        self.selectFile = tk.Button(self.frameRow1, text="Select Folder", height=1)
        self.selectFile["command"] = self.getFile
        self.selectFile.grid(row=0, column=2, sticky=tk.NW)
        self.selectFile.config(image=self.selectFileImage, width="128",height="25", compound=tk.CENTER, borderwidth=0)

        #end top frame
        #start middle frame
        self.frameRow2 = tk.Frame(self)
        self.frameRow2.grid(row=1, column=0, sticky=tk.NW, pady=10)

        #convert button
        self.convertButtonImage = tk.PhotoImage(file="img/button.gif")
        self.convertButton = tk.Button(self.frameRow2, text="Convert", fg="#000000")
        self.convertButton["command"] = self.convert
        self.convertButton.grid(row=0, sticky=tk.NW, padx=(5,0))
        self.convertButton.config(image=self.convertButtonImage, width="125",height="25", compound=tk.CENTER, borderwidth=0)

        #end middle frame

        #start log frame
        self.frameLog = tk.Frame(self)
        self.frameLog.grid(row=2, column=0)
        #log
        self.log = tk.Text(self.frameLog, width=60, height=20, font = "Helvetica 8")
        self.logString("Activity Monitor:")
        self.logString("Select a Folder to begin Converting")
        self.log.grid(row=1)
        

    def createWM(self):
        self.master.title("Audverter")
        self.master.minsize(width=300, height=500)
        self.master.maxsize(width=600, height=1000)        
        
        
        
    def getFile(self):
        fn = askdirectory()
        self.fileName.configure(state='normal')
        self.fileName.delete(0, tk.END)
        self.fileName.insert(0, fn)
        self.fileName.configure(state='disabled')
        self.directory = fn

    def convert(self):
        self.logString("Converting all files in folder: " + self.directory)
        self.converter.convert(self.directory)

    def logString(self, text):
        self.log.insert(tk.END, text + "\n")

        
