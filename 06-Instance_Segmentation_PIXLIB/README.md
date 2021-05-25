## 06 - Semantic Segmentation com PixelLib

Neste projeto é feito a segmentaao semantica de objetos em uma imagem. O objetos são detectados pelo utilizando a bilioteca  PIXELLIB utilizando o modelo MASK R-CNN destaca objetos.



### Requisitos
Os recursos necessarios para realizar a construção desse projeto foram:
    
    * python3.
    * pip
    * tensorflow
    * imgaug

Para instalar, digite no terminal:
``` shell
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

# Baixe os pesos, mask r-cnn > 250MB
wget https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.2/mask_rcnn_coco.h5

```
## PIXELLIB
PixelLib é uma biblioteca criada para realizar a segmentação de imagens e vídeos usando poucas linhas de código. É uma biblioteca flexível criada para permitir fácil integração da segmentação de imagem e vídeo em soluções de software.

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