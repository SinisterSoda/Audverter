from Converter import *
from GUI import *

app = None

def main():
    con = Converter()
    #this is the default folder it traverses
    #rootdir = input("Input the Directory (Or leave blank for default directory): ")
    #r = con.convert(rootdir)
    app = ApplicationGUI()
    app.mainloop()
    
    

main()
