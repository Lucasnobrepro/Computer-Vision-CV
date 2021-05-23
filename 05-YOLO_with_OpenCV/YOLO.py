# Importando bibliotecas;
from ast import parse
import cv2
import numpy as np

import time
import argparse

import matplotlib.pyplot as plt

from utils.utils import resizeImage, showImage



def configure():
    # DEFINES
    threshold = float(args.threshold) # threshold para classificar probabilidades;
    threshold_NMS = float(args.threshold_NMS) # threshold para o NON-MAX SUPRESSION;

    # DEFININDO CONFIGURAÇÕES DA DETECÃO
    LABELS = open("cfg/coco.names").read().strip().split('\n') # Ler o conteudo do arquivo no caminho, retira os espaços e separa por ENTER;
    COLORS = np.random.randint(0, 255, size=(len(LABELS),3)) # Definindo palheta de cores;

    return threshold, threshold_NMS, LABELS, COLORS

def blobImage(yoloNet, image,layer_name_outputs ,show_text = True):

    start = time.time()

    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False) # Preprocessando a imagem;
    yoloNet.setInput(blob) # Passando para entrada da rede neural;
    layers_outPuts = yoloNet.forward(layer_name_outputs) # Pegando o resultado das camadas de saída do YOLO;

    end = time.time()
    if show_text:
        print("YOLO levou {:.2f} segundos".format(end - start))
    return yoloNet, image, layers_outPuts

# TRABALHANDO COM DETECÇÕES
def detections(detection, threshold, boxs, confiances, IDClasses, W, H):
    scores = detection[5:] # Pegar apenas as probabilidades;
    classID = np.argmax(scores) # Pegando o ID da maior probabilidade;
    confiance = scores[classID] # Recebe o valor da probabilidade;

    if confiance > threshold:

        box = detection[0:4] * np.array([W, H, W, H]) # Redimensionar a dimensionalidade;
        center_X, center_Y, width, height = box.astype('int') # Valores da caixas delimitadoras;

        x = int(center_X - width/2) # Encontrando coodenada inicial;
        y = int(center_Y - height/2) # Encontrando coodenada inicial;

        boxs.append([x, y, int(width), int(height)]) # Salvando as coodenadas das caixas;
        confiances.append(float(confiance)) # Salvando a confiança;
        IDClasses.append(classID) # Salvando o Id das classes;

    return boxs, confiances, IDClasses

def check_negative(n):
    if n < 0:
        return 0
    else:
        return n

def boundBoxDraw(image, i, confiances, IDClasses, boxs, LABELS, COLORS,show_text="False"):
    x, y = boxs[i][0], boxs[i][1] # Pegando coodenadas X e Y;
    w, h = boxs[i][2], boxs[i][3] # Pegando Width e Height;
    
    color = [int(c) for c in COLORS[IDClasses[i]]] # Pegando a cor de acordo com a classe do objeto;

    cv2.rectangle(image, (x, y), (x+w, y+h), color, 2) # Desenhando Bound Boxes;
    text = "{}: {:4f}".format(LABELS[IDClasses[i]], confiances[i]) # Estruturando texto para inserir na imagem;
    cv2.putText(image, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2) # Inserindo texto na imagem;
    if show_text == "True":
        print("> " + text)
        print("X: {}, Y: {}".format(x,y))
        print("WIDTH: {}, HEIGHT: {}".format(w,h))
    else:
        pass
    
    return image, x, y, w, h

def yolo(image):
    # VETORES
    boxs = []
    confiances =[]
    IDClasses = []

    threshold, threshold_NMS, LABELS, COLORS = configure()
    
    resize = args.resize
    if resize:
        image = resizeImage(image)
    
    H, W = image.shape[:2]

    # Carregando detector da rede neura;
    yoloNet = cv2.dnn.readNet(args.weights, args.cfg)
    
    layer_name_outputs = yoloNet.getLayerNames() # Nomes das camadas de saída da rede neural;
    layer_name_outputs = [layer_name_outputs[i[0] - 1] for i in yoloNet.getUnconnectedOutLayers()] # Camadas de saídas;

    yoloNet, image, layers_outPuts = blobImage(yoloNet=yoloNet,image=image, layer_name_outputs=layer_name_outputs)

    for outputs in layers_outPuts: # Pecorrer todas as camadas de saída;
        for detection in outputs: # Pecorrer todas as detecções;
            boxs, confiances, IDClasses = detections(detection, threshold, boxs, confiances, IDClasses, W, H)
    
    # Aplicando NON-MAX Supression
    objts = cv2.dnn.NMSBoxes(boxs, confiances, threshold, threshold_NMS) # Diminui o numero de Bound Boxes;

    if len(objts) > 0: # Se possuir pelo menos um objeto detectado;
        for i in objts.flatten():
            image, x, y, w, h = boundBoxDraw(image, i, confiances, IDClasses, boxs, LABELS, COLORS, show_text=args.show_text)
    
    print("FIM!!")
    
    cv2.imwrite("resultado.jpg", image)
    return image


def args_parse(argv=None):
    parser = argparse.ArgumentParser(description='YOLO with OpenCV pre-trained model')
    parser.add_argument("--weights", 
                        default="weights/yolov4.weights", 
                        help="Caminho para os pesos do YOLO4")
    parser.add_argument("--cfg",
                        default="cfg/yolov4.cfg",
                        help="Caminho para as configurações da CNN do YOLO")
    parser.add_argument("--labels",
                        default="cfg/coco.names",
                        help="Caminho para as configurações da CNN do YOLO")
    parser.add_argument("--resize",
                        default=True,
                        help="Realizar redimensionamento da imagem")
    parser.add_argument("--show_text", 
                        default=False,
                        help="Mostra saídas")
    parser.add_argument("--image",
                        default="image.jpg",
                        help="Caminho para imagem")
    parser.add_argument("--show_image",
                        default=False,
                        help="Mostra a imagem ao final da detecção")               
    parser.add_argument("--threshold",
                        default=0.5,
                        help="threshold para probabilidade de existir um objeto")

    parser.add_argument("--threshold_NMS",
                        default=0.3,
                        help="threshold para NON-MAX SUPRESSION")

    global args
    args = parser.parse_args(argv)


if __name__ == "__main__":
    args_parse()
    np.random.seed(10) # Fixa a a semente aleatoria;

    image = cv2.imread(args.image)
    image = yolo(image)    
    
    if args.show_image == "True":
        showImage(image)
    
    




















