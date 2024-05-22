import openpyxl
import matplotlib.pyplot as plt
from PIL import Image

def VerifyColorPixel(image,x,y):
    # Retornar o RGB da imagem no pixel com os valores da altura e largura no parametro
    return image.getpixel((x,y))

def changeColor(image,rgb,colorChange):
    # Separar altura e largura da imagem
    width, height = image.size

     # Criar uma nova imagem toda branca
    new_imgem = Image.new('RGB', (width,height))

    for i in range(width):
        for j in range(height):
            # Pegar RGB de cada pixel da imagem
            color_pixel = image.getpixel((i,j))

            # Verificar se o RGB atual do pixel é igual ao RGB do parametro
            if color_pixel == colorChange:
                new_imgem.putpixel((i,j), rgb)
            # Se não colocar RGB do pixel atual
            else:
                new_imgem.putpixel((i,j), color_pixel)

    #Retornar imagem com cor mudada
    return new_imgem

def createFileExcel(image):
    # Criando pagina Excel
    book = openpyxl.Workbook()

    # Separar altura e largura da imagem
    width, height = image.size

    # Criar variavel para auxiliar na atribuição de valores no Excel
    auxiliar = []

    for i in range(width):
        for j in range(height):
            # Pegar RGB de cada pixel da imagem
            pixel = image.getpixel((i,j))

            # Adicionar RGB no lista auxiliar com o formato de R(valor red), G(valor green), B(valor blue)
            auxiliar.append(str(f'R({pixel[0]}), G({pixel[1]}), B({pixel[2]})'))
        
        # Adicionar no Excel lista auxiliar
        book['Sheet'].append(auxiliar)

        # Esvaziar lista auxiliar
        auxiliar = []

    # Salvar Excel
    book.save('igor.xlsx')


def imageOriginal(patch = 'Image2.jpg'):
    # Inicializando imagem
    image = Image.open(patch)

    # Retornando imagem
    return image

def showImage(matriz):
    # Mostrar imagem
    plt.imshow(matriz)
    plt.show()
