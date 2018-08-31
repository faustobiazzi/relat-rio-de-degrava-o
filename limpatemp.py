import os , glob
marcaTemp = "_tempNPCIC.jpg"

for path, subdirs, files in os.walk(r"."):
           for filename in files:
                 if(str(marcaTemp) in filename):
                     f = os.path.join(path, filename)
                     os.remove(f)
                     print ("limpou arquivos")
    
                   
