from PIL import Image
import matplotlib.pyplot as plt

def MediaPonderada(rgb):
    # Separar valores dos canais de cor RGB
    r,g,b = rgb

    # Soma valores dos canais de cor RGB e depois dividir por 3
    return (r+g+b)//3

def Luminosidade(rgb):
    # Separar valores dos canais de cor RGB
    r,g,b = rgb

    # Aplicar um peso a cada canal de cor RGB e depois dividir por 3
    return ((r*1.5)+(g*1.5)+(b*1.5))//3

def DecomposicaoMinima(rgb):
    # Pegar menor valor entre os canais de cor RGB
    return min(rgb)

def DecomposicaoMaxima(rgb):
    # Pegar maior valor entre os canais de cor RGB
    return max(rgb)

def rgbToCiza(image, opt):
    # Separar altura e largura da imagem
    width, height = image.size

    # Criar uma nova imagem toda branca
    image_gray = Image.new('RGB',(width,height))

    for i in range(width):
        for j in range(height):
            # Pegar RGB de cada pixel da imagem
            rgb = image.getpixel((i,j))
            
            # Verificar qual vai ser a escala cinza
            if opt == 'Media Ponderada':
                gray = MediaPonderada(rgb)
            elif opt == 'Luminosidade':
                gray = Luminosidade(rgb) 
            elif opt == 'Decomposicao Minima':
                gray = DecomposicaoMinima(rgb)
            elif opt == 'Decomposicao Maxima':
                gray = DecomposicaoMaxima(rgb)
            else:
                return

            # Colocar em cada pixel da imagem toda branca o valor do cauculo de escala escolhido
            image_gray.putpixel((i,j), tuple(int(gray) for i in range(0,3)))

    # Retornar a imagem em escala cinza
    return image_gray

def addConstrastGray(image, fator):
    # Separar altura e largura da imagem
    width, height = image.size

    # Criar uma nova imagem toda branca
    image_Contrast = Image.new('RGB', (width,height))
    
    # Pegar menor valor na imagem cinza
    min_cinza = getMin(image)

    # Pegar maior valor na imagem cinza
    max_cinza = getMax(image)
    
    for i in range(width):
        for j in range(height):
            # Cauculo do contraste de cada pixel da imagem e colocar em uma variavel
            new_pixel = (image.getpixel((i,j))[0] - min_cinza) * (255 / (max_cinza - min_cinza)) * fator

            # Converter variavel do cauculo de contraste em int
            new_pixel = int(new_pixel)

            # Colocar valor da variavel do cauculo de contraste em cada pixel da imagem toda branca
            image_Contrast.putpixel((i,j),(new_pixel,new_pixel,new_pixel))
    
    # Retornar imagem com contraste
    return image_Contrast

def addConstrastColered(image, fator):
    # Separar altura e largura da imagem
    width, height = image.size

    # Criar uma nova imagem toda branca
    image_Contrast = Image.new('RGB', (width,height))
    
    # Pegar menor valor na imagem cinza
    min_cinza = getMin(image)

    # Pegar maior valor na imagem cinza
    max_cinza = getMax(image)
    
    for i in range(width):
        for j in range(height):
            # Cauculo do contraste em cada canal RGB do pixel da imagem e colocar em uma variavel
            red = int((image.getpixel((i,j))[0] - min_cinza) * (255 / (max_cinza - min_cinza)) * fator)
            green = int((image.getpixel((i,j))[1] - min_cinza) * (255 / (max_cinza - min_cinza)) * fator)
            blue = int((image.getpixel((i,j))[2] - min_cinza) * (255 / (max_cinza - min_cinza)) * fator)
            image_Contrast.putpixel((i,j),(red,green,blue))
    
    # Retornar imagem com contraste
    return image_Contrast

def getMin(image):
    # Separar altura e largura da imagem
    width, height = image.size

    # Criar uma nova imagem toda branca
    min_cinza = min(image.getpixel((0,0)))

    for i in range(width):
        for j in range(1,height):
            # Verificar qual o menor valor da imagem
            if min(image.getpixel((i,j))) < min_cinza:
                min_cinza = min(image.getpixel((i,j)))

    # Retornar menor valor
    return min_cinza


def getMax(image):
    # Separar altura e largura da imagem
    width, height = image.size

    # Criar uma nova imagem toda branca
    max_cinza = max(image.getpixel((0,0)))

    for i in range(width):
        for j in range(1,height):
            # Verificar qual o maior valor da imagem
            if max(image.getpixel((i,j))) > max_cinza:
                max_cinza = max(image.getpixel((i,j)))

    # Retornar maior valor
    return max_cinza


