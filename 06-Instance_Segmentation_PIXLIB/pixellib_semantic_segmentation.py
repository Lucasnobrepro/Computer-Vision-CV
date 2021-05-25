import   pixellib
from pixellib.instance import instance_segmentation
import cv2

import argparse

# Realiza a segmentação
def masRcnn_semantic_segmentation(image, weights_path, out_imageName):
    segment_image = instance_segmentation() # Intacia o sementador;
    segment_image.load_model(weights_path) # Carega os pesos para o modelo;
    segment_image.segmentImage(image, output_image_name = out_imageName) # Realiza a segmentação propiamente dita; 

# Organização dos argumentos;
def args_parse(argv=None):
    parser = argparse.ArgumentParser(description='YOLO with OpenCV pre-trained model')
    parser.add_argument("--weights", 
                        default="weights/mask_rcnn_coco.h5", 
                        help="Caminho para os pesos do Mask R-CNN aplicado em CoCo")

    parser.add_argument("--image",
                        default="inputs/cycle.jpg",
                        help="Caminho para imagem")

    parser.add_argument("--out_imageName",
                        default="outputs/out_imageName.jpg",
                        help="Caminho para imagem")

    global args
    args = parser.parse_args(argv)

if __name__ == "__main__":
    args_parse()
    
    masRcnn_semantic_segmentation(args.image, args.weights, args.out_imageName)
    
    print("######################################################################")
    print("Fim da segmetação!!")
