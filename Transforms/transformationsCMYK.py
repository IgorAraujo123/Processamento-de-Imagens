from PIL import Image

def createMatriz(image_rgb):
    # Separar altura e largura da imagem 
    width, height = image_rgb.size

    # Criar uma nova imagem toda branca
    image_cmyk = Image.new('CMYK',(width,height))
    
    for i in range(width):
        for j in range(height):
            # Pegar as cores RGB de cada pixel
            rgb = image_rgb.getpixel((i,j))

            # Criar variavel com valores CMKY
            cmyk = RGBtoCMY(rgb)

            # Colocar cores CMKY em cada pixel da imagem toda branca
            image_cmyk.putpixel((i,j),tuple(int(valor * 255) for valor in cmyk))

    # Retornar Imagem CMKY
    return image_cmyk

def RGBtoCMY(rgb):
    # Criar três variáveis com valores red, green e blue da imagem
    r,g,b = rgb

    # Dividir cada canal de cor por 255 e colocar em uma variavel
    c = 1 - (r/255.0)
    m = 1 - (g/255.0)
    y = 1 - (b/255.0)

    # Pegar menor valor entre as variaveis criadas acima
    k = min(c,m,y)

    if k == 1:
        return 0,0,0,1

    # Subtrair a variavel cada canal de cor CMKY por preto
    c = c - k 
    m = m - k 
    y = y - k 

    # Retornar CMKY
    return c,m,y,k