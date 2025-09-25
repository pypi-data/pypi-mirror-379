# Combinação de imagens: encontrar diferenças e transferir histogramas

import numpy as np # Biblioteca para manipulação de arrays
from skimage.color import rgb2gray # Função para converter imagens RGB para escala de cinza
from skimage.exposure import match_histograms # Função para igualar histogramas
from skimage.metrics import structural_similarity # Função para calcular similaridade estrutural

def find_difference(image1, image2): # Encontra diferenças entre duas imagens
    assert image1.shape == image2.shape, "Specify 2 images with de same shape." # Verifica se as imagens têm o mesmo formato
    # Converte para escala de cinza
    gray_image1 = rgb2gray(image1) # Converte para escala de cinza
    gray_image2 = rgb2gray(image2) # Converte para escala de cinza
    
    # Define data_range para imagens float
    if np.issubdtype(gray_image1.dtype, np.floating):# Verifica se o tipo de dado é float
        data_range = gray_image1.max() - gray_image1.min() # Calcula o intervalo de dados
        score, difference_image = structural_similarity(gray_image1, gray_image2, full=True, data_range=data_range) # Calcula similaridade estrutural
    else:
        score, difference_image = structural_similarity(gray_image1, gray_image2, full=True) # Calcula similaridade estrutural
    print("Similarity of the images:", score) # Imprime a similaridade das imagens
    # Normaliza a imagem de diferença para o intervalo [0, 1]
    normalized_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image)) # Normaliza a imagem de diferença
    return normalized_difference_image # Retorna a imagem de diferença normalizada

def transfer_histogram(image1, image2): # Transfere o histograma de image2 para image1
    matched_image = match_histograms(image1, image2, multichannel=True) # Igualação de histogramas
    return matched_image # Retorna a imagem com histograma transferido