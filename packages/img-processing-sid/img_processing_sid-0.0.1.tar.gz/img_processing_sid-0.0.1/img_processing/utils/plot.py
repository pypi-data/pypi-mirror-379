# Script de utilitários para visualização de imagens usando matplotlib 
import matplotlib.pyplot as plt # Biblioteca para plotagem de gráficos e imagens

def plot_image(image): # Plota uma única imagem
    plt.figure(figsize=(12, 4)) # Define o tamanho da figura
    plt.imshow(image, cmap='gray') # Mostra a imagem em escala de cinza
    plt.axis('off') # Remove os eixos
    plt.show() # Exibe a imagem

def plot_result(*args): # Plota múltiplas imagens lado a lado
    number_images = len(args) # Conta o número de imagens
    fig, axis = plt.subplots(nrows=1, ncols = number_images, figsize=(12, 4)) # Cria subplots
    names_lst = ['Image {}'.format(i) for i in range(1, number_images)] # Nomes padrão para as imagens
    names_lst.append('Result') # Nome para a última imagem como 'Result'
    for ax, name, image in zip(axis, names_lst, args): # Itera sobre os eixos, nomes e imagens
        ax.set_title(name) # Define o título do subplot
        ax.imshow(image, cmap='gray') # Mostra a imagem em escala de cinza
        ax.axis('off') # Remove os eixos
    fig.tight_layout() # Ajusta o layout da figura
    plt.show() # Exibe a figura

def plot_histogram(image): # Plota o histograma de uma imagem colorida
    fig, axis = plt.subplots(nrows=1, ncols = 3, figsize=(12, 4), sharex=True, sharey=True) # Cria subplots para os canais de cor
    color_lst = ['red', 'green', 'blue'] # Lista de cores para os canais
    for index, (ax, color) in enumerate(zip(axis, color_lst)): # Itera sobre os eixos e cores
        ax.set_title('{} histogram'.format(color.title())) # Define o título do subplot
        ax.hist(image[:, :, index].ravel(), bins = 256, color = color, alpha = 0.8) # Plota o histograma do canal de cor
    fig.tight_layout() # Ajusta o layout da figura
    plt.show() # Exibe a figura