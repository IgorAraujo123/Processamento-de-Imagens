from PIL import Image,ImageFilter
import numpy as np

# Função que faz  a remoção dos canais RGB
def remove_RGB(image, valueRed, valueGreen, valueBlue, isRedEnable, isGreenEnable, isBlueEnable):

    # Separar altura e largura da imagem
    width, height = image.size

    # Criar uma nova imagem toda branca
    new_image = Image.new('RGB',(width,height))

    for i in range(width):
        for j in range(height):
            # Pegar as cores RGB de cada pixel
            pixel = image.getpixel((i,j))

            newRed = 0
            newGreen = 0
            newBlue = 0

            # Verificar se vai remover o red
            if isRedEnable:
                newRed = pixel[0] + valueRed
            # Verificar se vai remover o green
            if isGreenEnable:
                newGreen = pixel[1] + valueGreen
            # Verificar se vai remover o blue
            if isBlueEnable:
                newBlue = pixel[2] + valueBlue
            
            # Colocar cores RGB em cada pixel da imagem toda branca 
            new_image.putpixel((i,j), (newRed,newGreen,newBlue))

    # Retornar imagem com canais removidos
    return new_image

#Função que faz a aplição do filtro blur Gaussian
def GaussianBlur(image, kernel_size):
    # Aplicando o filtro blur na imagem passada como parametro
    # GaussianBlur(kernel_size) é uma função da Biblioteca PIL.ImageFilter
    filtered_image = image.filter(ImageFilter.GaussianBlur(kernel_size))

    #Retornando a imagem com filtro blur
    return filtered_image