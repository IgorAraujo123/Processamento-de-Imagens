import PySimpleGUI as sg

# Fazer varias funções onde cada função sera os elementos dentro da janela
def saiadaExcel():
    layout = [
        [sg.Button('Create Excel',size=(25,1), font=('Arial', 11),pad=(15,20))]
    ]

    return layout

def colorPixel():
    layout = [
        [sg.Text('largura', font=('Arial', 12), text_color='Black',pad=(15,20)), sg.Input(key='largura_value', tooltip="Digite o valor de x", size=(25,15), font=('Arial', 12))],
        [sg.Text('altura', font=('Arial', 12), text_color='Black',pad=(15,10)), sg.Input(key='altura_value', tooltip="Digite o valor de y", size=(25,15), font=('Arial', 12))],
        [sg.Text('Resultado', font=('Arial', 12), text_color='Black',pad=(15,25),key='result')],
        [sg.Button('show color',size=(25,1), font=('Arial', 11),pad=(15,10))]
    ]

    return layout

def changeColorPixel():
    layout = [
        [sg.Button('Change Color',size=(25,1), font=('Arial', 11),pad=(15,20))]
    ]

    return layout


def escalaCinza():
    layout = [
        [sg.OptionMenu(values=['Media Ponderada','Luminosidade','Decomposicao Minima','Decomposicao Maxima'],default_value='Media Ponderada', key='medias',pad=(15,20))],
        [sg.Button('Aplicar Escala Cinza',size=(25,1), font=('Arial', 11),pad=(15,5))]
    ]
        
    return layout

def contrastImage():
    layout = [
        [sg.Text('Fator', font=('Arial', 12), text_color='Black',pad=(10,10)),sg.Input(key='fator', tooltip='Digite o valor do fator de cotraste', size=(25,15), font=('Arial', 12))],
        [sg.Radio('Image Cinza', group_id=1, default=True, key='ImageCinza'), sg.Radio('Image Colored', group_id=1, default=False)],
        [sg.Button('add contrast image',size=(25,1), font=('Arial', 11),pad=(10,10))]
    ]

    return layout

def removeCanaisDeCor():
    layout = [
        [sg.Text()],
        [sg.Text('Red'),sg.Slider(range=(0,150),key='valueRed',tooltip='valor de aumento red', orientation='horizontal'), sg.Button('Enable/Desable red')],
        [sg.Text()],
        [sg.Text('Green'),sg.Slider(range=(0,150),key='valueGreen',tooltip='valor de aumento green', orientation='horizontal'), sg.Button('Enable/Desable green')],
        [sg.Text()],
        [sg.Text('Blue'),sg.Slider(range=(0,150),key='valueBlue',tooltip='valor de aumento blue', orientation='horizontal'), sg.Button('Enable/Desable blue')],
        [sg.Button('Aplicar remocao dos canais de cores',size=(25,2), font=('Arial', 11),pad=(15,20))]
    ]

    return layout

def filtroBlur():
    layout = [
        [sg.Text('Kernel Size', font=('Arial', 12), text_color='Black',pad=(10,10)),sg.Input(key='kernel_size', tooltip='Digite o tamnho do kernel', size=(25,15), font=('Arial', 12))],
        [sg.Button('Aplicar Filtro Blur',size=(25,1), font=('Arial', 11),pad=(15,20))]
    ]

    return layout

def changeImage():
    layout = [
        [sg.Text('Patch Image', font=('Arial', 12), text_color='Black',pad=(10,10)),sg.Input(key='patch', tooltip='Digite o tamnho do kernel', size=(25,15), font=('Arial', 12))],
        [sg.Button('change image',size=(25,1), font=('Arial', 11),pad=(15,20))]
    ]

    return layout