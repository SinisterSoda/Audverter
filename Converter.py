import os
import subprocess


class Converter:
    ffmpeg = ""
    app = None
    validExtensions = [".mp3", ".flac", ".m4a", ".wav", ".mp4", ".flv"]

    #format dictionary. for the tuples, item 0 is codec, item 1 is file extension item 2 is description (for GUI) item 3 is boolean whether or not its a video codec
    convertFormats = {"alac" : ("alac", "m4a", "Apple Lossless Audio Codec(alac)", False), 
    "mp3" : ("mp3", "mp3", "MPEG (mp3)", False), 
    "flac" : ("flac", "flac", "Free Lossless Audio Codec(flac)", False), 
    "wav" : ("pcm_u8", "wav", "Waveform (wav)", False), 
    "wma" : ("wmav2", "wma", "Windows Media Audio (wma)", False), 
    "ogg" : ("libvorbis", "ogg", "Ogg Vorbis (ogg)", False),
    #video formats
    "mp4" : ("", "mp4", "MPEG-4(mp4)", True)}

    def __init__(self, ff_dir=None):
        #r"\ffmpeg\bin\ffmpeg"
        if (ff_dir == None):
            ff_dir = r"" + os.sep + "ffmpeg" + os.sep + "bin" + os.sep + "ffmpeg"
        self.ffmpeg =  os.path.abspath(os.getcwd() + ff_dir)

        #print(self.ffmpeg)

    

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
                k = self.app.getOptionKey()
                tup = self.convertFormats[k]
                codec = tup[0]
                ext = tup[1]
                is_video_format = tup[3]
                #the ffmpeg command that actually does the converting
                if (is_video_format):
                    command = ffmpeg + " -i \"" + f + "\" " + codec + " \"" + basef + "." + ext + "\""
                else:
                    command = ffmpeg + " -i \"" + f + "\" -acodec " + codec + " \"" + basef + "." + ext + "\""
                self.output("Running command: ")
                self.output(command)

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
