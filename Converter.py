import os
import subprocess


class Converter:
    ffmpeg = ""
    app = None
    validExtensions = [".mp3", ".flac", ".m4a", ".wav"]

    def __init__(self, ff_dir=r"\ffmpeg\bin\ffmpeg"):
        self.ffmpeg =  os.path.abspath(os.getcwd() + ff_dir)

        print(self.ffmpeg)

    

    def convert(self, directory):
        
        
        #this is the directory where ffmpeg is located
        ffmpeg = self.ffmpeg
        i = 0

        #will set the folder to default if no folder is input by the user
        if directory == "":
            self.output("No directory provided. Exiting")
            return False
        
        self.output("Traversing directory: " + directory)

        #loop that traverses the folder iteratively
        outputfile = open(r'log.txt','w')    
        for subdir, dirs, files in os.walk(directory):
            #goes through each file in the subfolder
            self.output("Going through directory: " + subdir)
            for file in files:
                f = os.path.join(subdir, file)
                #get the base name of the file without extension
                basef, ext = os.path.splitext(f)
                if ext not in self.validExtensions:
                    self.output("file: " + f + " is incorrect file type (" + ext + "). Skipping.")
                    continue
                    
                self.output("Converting: " + f)

                #the ffmpeg command that actually does the converting
                command = ffmpeg + " -i \"" + f + "\" -acodec alac \"" + basef + ".m4a\""
                #self.output("Running command: ")
                #self.output(command)

                #runs the actual command
                subprocess.call(command, shell=True, stdout=outputfile)
                i+=1
                self.output("Converted file # " + str(i))
                
            
        outputfile.close()

        self.output ("A total of " + str(i) + " files have been converted")
        return True

    def output(self, txt):
        #for now just print the output
        if self.app == None:
            print(txt)
        else:
            self.app.logString(txt)
            self.app.update()
