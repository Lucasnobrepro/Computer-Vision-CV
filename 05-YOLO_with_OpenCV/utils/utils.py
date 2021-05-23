import cv2
import matplotlib.pyplot as plt

# FUNÇÕES UTEIS;
def showImage(img):
    fig = plt.gcf()
    fig.set_size_inches(16,10)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

def resizeImage(image, width_max = 600):
    if image.shape[1] > width_max:
        proportion = image.shape[1] / image.shape[0] # Calculando a propoção da imagem;
        image_width = width_max
        image_height = int(image_width / proportion)
        image = cv2.resize(image, (image_width, image_height)) # Redimensionando imagens;

    return image
