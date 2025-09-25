# Script de transformação de imagens: redimensionamento
from skimage.transform import resize # Função para redimensionar imagens

def resize_image(image, proportion): # Redimensiona a imagem pela proporção especificada
    assert 0 <= proportion <= 1, "Specify a valid proportion between 0 and 1." # Verifica se a proporção está entre 0 e 1
    # Calcula as novas dimensões
    height = round(image.shape[0] * proportion) # Calcula a nova altura
    width = round(image.shape[1] * proportion) # Calcula a nova largura
    # Redimensiona a imagem
    image_resized = resize(image, (height, width), anti_aliasing=True)  # Redimensiona a imagem com anti-aliasing
    return image_resized # Retorna a imagem redimensionada