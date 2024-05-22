import PySimpleGUI as sg
from tkinter.colorchooser import askcolor
from tkinter.messagebox import showerror
import Utils.layouts as layouts
from Utils.utils import imageOriginal
import Utils.chamadaDeFunçõesEtapas as funcEtapas
import io 

class Window():

    def initLayout(self):     
        # Inicializar layout da janela   
        layout = [[sg.TabGroup([[sg.Tab("Saida em Excel", layouts.saiadaExcel()), sg.Tab("Color pixel", layouts.colorPixel()), sg.Tab("Change color pixel", layouts.changeColorPixel()),
                                 sg.Tab("Escala Cinza", layouts.escalaCinza()), sg.Tab("contrast Image", layouts.contrastImage()),sg.Tab("remove Canais De Cor", layouts.removeCanaisDeCor()), 
                                 sg.Tab("filtro Blur", layouts.filtroBlur()), sg.Tab("Change Image", layouts.changeImage())]], focus_color='black',size=(500,350))],
                  [sg.Image(self.newImage(),key='-IMAGE-')],
                  [sg.Button('Reset Image')]
        ]
        
        # Retornar layout da janela
        return layout

    def __init__(self):
        # Incializar imagem original
        self.image = imageOriginal()
        self.patch_image = 'image2.jpg'

        # Criar janela
        self.window = sg.Window('Playlist', self.initLayout())
        self.isEnableRed = True
        self.isEnableGreen = True
        self.isEnableBlue = True

    def newImage(self):
        # Redimesionando imagem
        self.image.thumbnail((500,300))
        bio = io.BytesIO()

        # Salvar imagem no formato PNG
        self.image.save(bio, format='PNG')

        # Retornar imagem
        return bio.getvalue()
    
    def updateImage(self):
        # Atualizar imagem da janela para uma nova imagem
        self.window['-IMAGE-'].update(self.newImage())
        

    def openWindon(self):
        # Inicializando janela
        while True:
            # Eventos e valores dos campos da janela
            evento,values = self.window.read()

            # Fechar Janela
            if evento == sg.WIN_CLOSED:
                break
            
            # Verificar eventos da janela e Chamar etapas em cada verficação de evento
            elif evento == 'Create Excel':
                funcEtapas.Etapa1(self.image)
            elif evento == 'show color':
                message = funcEtapas.Etapa2(self.image,values['largura_value'],values['altura_value'])
                self.window['result'].update(message) 
            elif evento == 'Change Color':
                self.image = funcEtapas.Etapa3(self.image,askcolor()[0])
                self.updateImage()   
            elif evento == 'Aplicar Escala Cinza':
                self.image = funcEtapas.Etapa5(self.image,values['medias'])
                self.updateImage()
            elif evento == 'add contrast image':
                self.image = funcEtapas.Etapa6e7(self.image,values['fator'],values['ImageCinza'])
                self.updateImage()
            elif evento == 'Aplicar remocao dos canais de cores':
                # Pegar valores dos campos Red, Blue e Green
                red = int(values['valueRed'])
                green = int(values['valueGreen'])
                blue = int(values['valueBlue'])

                self.image = funcEtapas.Etapa8(self.image,red,green,blue,self.isEnableRed,self.isEnableGreen,self.isEnableBlue)
                self.updateImage()
            elif evento == 'Aplicar Filtro Blur':
                kernel_size = float(values['kernel_size'])
                self.image = funcEtapas.Etapa9(self.image,kernel_size)
                self.updateImage()
            elif evento == 'change image':
                try:
                    self.patch_image = values['patch']
                    self.image = imageOriginal(values['patch'])
                    self.updateImage()
                except FileNotFoundError:
                    showerror('Error', 'Patch image incorrect')
                except FileExistsError as file:
                    showerror('Error', file)
                except:
                    showerror('Error', 'Veja os inputs')

            # Voltar a imagem para forma inicial
            elif evento == 'Reset Image':
                self.image = imageOriginal(self.patch_image)
                self.window['-IMAGE-'].update(self.newImage())
            
            # Verificar eventos de desabilitar campos
            elif evento == 'Enable/Desable red':
                if self.isEnableRed:
                    self.window['valueRed'].update(0,disabled=True)
                    self.isEnableRed = False
                else:
                    self.window['valueRed'].update(disabled=False)
                    self.isEnableRed = True
            elif evento == 'Enable/Desable green':
                if self.isEnableGreen:
                    self.window['valueGreen'].update(0,disabled=True)
                    self.isEnableGreen = False
                else:
                    self.window['valueGreen'].update(disabled=False)
                    self.isEnableGreen = True
            elif evento == 'Enable/Desable blue':
                if self.isEnableBlue:
                    self.window['valueBlue'].update(0,disabled=True)
                    self.isEnableBlue = False
                else:
                    self.window['valueBlue'].update(disabled=False)
                    self.isEnableBlue = True
            
            # Evento para sair da janela
            elif evento == 'Sair':
                break
            

# Verificar se o arquivo executado e esse mesmo
if __name__ == '__main__':
    mainWindow = Window()
    mainWindow.openWindon()



