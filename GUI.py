import tkinter as tk
from tkinter.filedialog import askdirectory

class ApplicationGUI(tk.Frame):
    master=None
    directory=""
    def __init__(self):
        master=tk.Tk()
        tk.Frame.__init__(self, master)
        #set size
        master.minsize(width=300, height=500)

        
        self.pack()
        self.createComponents()

    def createComponents(self):
        #file name text box
        self.fileName = tk.Entry(self)
        self.fileName.pack(side="top")

        #select file button
        self.selectFile = tk.Button(self)
        self.selectFile["text"] = "Select File"
        self.selectFile["command"] = self.getFile
        self.selectFile.pack(side="top")
        
        
        
    def getFile(self):
        fn = askdirectory()
        self.fileName.delete(0, tk.END)
        self.fileName.insert(0, fn)

        self.directory = fn
