# parametros de arquivo - tamanho desejado pra imagens e disposição no pdf
# lógica abrir pasta de arquivos
# gerar arquivo do PDF 
# loop para leitura, inserção e redimensionamento
# fechar arquivo


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm, mm, inch, pica

from reportlab.lib.pagesizes import A4, cm,landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch


import os , glob
try:
    from PIL import Image
except ImportError:
    import Image




largura_desejada= 200
altura_desejada= 200
nomearquivoPDF = "relatório.pdf"
pasta = "./imagens/"
marcaTemp = "_tempNPCIC.jpg"
imagens = []
run =1

def limpaTemp():
    for path, subdirs, files in os.walk(r"."):
           for filename in files:
                 if(str(marcaTemp) in filename):
                     f = os.path.join(path, filename)
                     os.remove(f)
                     print ("limpou arquivos")
    return
                    
    
def redimensiona():
    with open("error.txt", "w") as a:
        for path, subdirs, files in os.walk(r'.'):
            for filename in files:
                if not(marcaTemp in filename):
                    if(".jpg" in filename) or (".JPG" in filename) or (".jpeg" in filename) or (".JPEG" in filename):                      
                        f = os.path.join(path, filename)
                        print("trabalhando imagem "+f)
                        imagem = Image.open(f)
                        largura_imagem = imagem.size[0]
                       
                        try:
                            altura_imagem = imagem.size[1]
                            percentual_largura = float(largura_desejada) / float(largura_imagem)
                            altura_desejada = int((altura_imagem * percentual_largura))
                            imagem = imagem.resize((largura_desejada, altura_desejada), Image.ANTIALIAS)
                            g = f+marcaTemp
                            imagem.save(g)
                            
                            imagens.append(g)
                        except Exception as ERROR:
                            a.write(str(f) + os.linesep)
                            a.write(str(ERROR) + os.linesep)
                            continue
                        else:
                            continue
                else:                      
                    f = os.path.join(path, filename)
                    print("trabalhando imagem "+f)
                    imagens.append(g)

        return         

def gerarPDF():
    c = canvas.Canvas(nomearquivoPDF, pagesize=letter)

    
    try:
        for i in imagens:
            #print(i)
            #c.drawImage(i, inch, inch * 1)
            a = Image.open(i)  
            a.drawHeight = 2*inch
            a.drawWidth = 2*inch
            data=[['1',a],['3','4']]
            c = canvas.Canvas("Reportlabtest.pdf", pagesize=portrait(A4))
            table = Table(data, colWidths=200, rowHeights=50)
            table.setStyle(TableStyle([
                                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                                       ('BACKGROUND',(0,0),(-1,2),colors.lightgrey)
                                       ]))
            table.wrapOn(c, 200, 400)
            table.drawOn(c,20,50)
            c.save()
            if limpaTemp():
        #c.save()
                print ("PDF criado")
    except:
        print ("PDF não criado")
        limpaTemp()
    return

redimensiona()

gerarPDF()

limpaTemp()

