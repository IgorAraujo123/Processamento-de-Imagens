from PIL import Image
from Utils.utils import createFileExcel, changeColor, VerifyColorPixel
from random import randrange
import Transforms.transformationsGray as transform
import Transforms.filtros as filtros
from tkinter.messagebox import showerror

def Etapa1(image):
    # Chamar função da Etapa 1 do prejeto
    createFileExcel(image)

def Etapa2(image,largura,altura):
    
    # Verificar os parametros largura e altura excede da imagem
    if int(largura) > image.size[0]-1 or int(altura) > image.size[1]-1:
        return 'Erro, largura excede da imagem ou altura excede da imagem'
    elif largura.isdigit() and altura.isdigit():
        # Converter parametros x e y para int
        X_convert = int(largura)
        Y_convert = int(altura)

        # Chamar função da Etapa 2 do prejeto
        color = VerifyColorPixel(image, X_convert, Y_convert)

        # Retornar uma mensagem indicando a cor do pixel na largura x e altura y
        return f'A cor do pixel  {X_convert, Y_convert}  é  {color}'
    # Se não for numero retornar mensagem de erro
    else:
        return 'Error, as entradas dos valores acima tem que ser numericos'

def Etapa3(image,color):
    # Separar altura e largura da imagem
    width, height = image.size

    # Criar uma nova imagem toda branca
    new_image = Image.new('RGB',(width,height))

    # Criar valores aleatorias entre 0 , largura imagem
    i = randrange(0, image.size[0])

    # Criar valores aleatorias entre 0 , altura imagem 
    j = randrange(0, image.size[1])

    # Atribuir uma variavel para a imagem com cores alteradas
    new_image = changeColor(image,color,VerifyColorPixel(image,i,j))

    # retorna imagem
    return new_image

def Etapa5(image,medida):
    # Separar altura e largura da imagem
    width, height = image.size

    # Criar uma nova imagem toda branca
    new_image = Image.new('RGB',(width,height))

    # Atribuir uma variavel para a imagem em escala cinza
    new_image = transform.rgbToCiza(image,medida)

    # Retornar imagem
    return new_image

def Etapa6e7(image,fator,imageCinza):
    # Separar altura e largura da imagem
    width, height = image.size

    # Criar uma nova imagem toda branca
    new_image = Image.new('RGB',(width,height))

    # Verificar se é uma imagem cinza ou colorida depois criar uma variavel atribuindo a imagem com contraste
    if imageCinza:
        fator_convert = float(fator)
        new_image = transform.addConstrastGray(image,fator_convert)
    else:
        fator_convert = float(fator)
        new_image = transform.addConstrastColered(image,fator_convert)

    # retornar imagem
    return new_image

def Etapa8(image, valueRed, valueGreen, valueBlue, isRedEnable, isGreenEnable, isBlueEnable):
    # Retorna imagem com canais de cor removidos
    return filtros.remove_RGB(image, valueRed, valueGreen, valueBlue, isRedEnable, isGreenEnable, isBlueEnable)

def Etapa9(image,kernel_size):
    # Retornar imagem  com filtro blur
    return filtros.GaussianBlur(image,kernel_size)
