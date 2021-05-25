## 05 - Semantic Segmentation

Neste projeto é feito a segmentaao semantica de objetos em uma imagem. O objetos são detectados pelo utilizando a bilioteca  PIXELLIB utilizando o modelo MASK R-CNN destaca objetos.

## PIXELLIB
PixelLib é uma biblioteca criada para realizar a segmentação de imagens e vídeos usando poucas linhas de código. É uma biblioteca flexível criada para permitir fácil integração da segmentação de imagem e vídeo em soluções de software.

### Requisitos
Os recursos necessarios para realizar a construção desse projeto foram:
    
    * python3.
    * pip
    * tensorflow
    * imgaug

Para instalar, digite no terminal:
```
sudo apt update

pip3 install pip 

pip3 install tensorflow

pip3 install imgaug

pip3 install pixellib --upgrade
```
Baixe os pesos do Mask R-CNN para a pasta weights, digite os comandos abaixo no terminal, na pasta raiz do projeto:

``` shell
# Entre na pasta
cd weights

# Baixe os pesos, yolov4.weights > 200MB
wget https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.2/mask_rcnn_coco.h5

```
### You only look once (YOLO)
Outros sistemas de detecção adaptam classificadores ou localizadores para realizar a detecção. Eles aplicam o modelo a uma imagem em vários locais e escalas. As regiões de alta pontuação da imagem são consideradas detecções.

O YOLO utiliza uma abordagem totalmente diferente. Aplicando uma única rede neural à imagem completa. Essa rede divide a imagem em regiões e prevê caixas delimitadoras e probabilidades para cada região. Essas caixas delimitadoras são ponderadas pelas probabilidades previstas.

Exemplo de uma detecção utilizando YOLO:

<img src="/Figuras/Semantic_seg_1_PIXELIB.jpg"/>

### Para executar
Digite no terminal o comando abaixo:
```
python pixellib_semantic_segmentation.py
```


## Referências

Pixellib Docs: <a href="url">https://pixellib.readthedocs.io/en/latest/</a>

Pixellib GitHub: <a href="url">https://github.com/ayoolaolafenwa/PixelLib</a>