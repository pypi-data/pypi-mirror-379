# Script de utilitários para leitura e salvamento de imagens usando skimage
from skimage.io import imread, imsave # Funções para ler e salvar imagens

def read_image(path, is_gray = False): # Lê uma imagem do caminho especificado
    image = imread(path, as_gray = is_gray) # Lê a imagem, opcionalmente em escala de cinza
    return image # Retorna a imagem lida

def save_image(image, path): # Salva a imagem no caminho especificado
    imsave(path, image)  # Salva a imagem no arquivo
    print(f'Image saved in: {path}') # Mensagem de confirmação  