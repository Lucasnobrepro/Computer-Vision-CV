## 04 - Rastreamento de objetos.

Neste projeto é feito o rastreamento de um objeto ao decorrer do vídeo. O objeto é selecionado a partir do primeiro frame de vídeo e então rastreado até que deixe a área de captura ou o vídeo termine.

### O que é rastreamento
Simplificando, localizar um objeto em quadros sucessivos de um vídeo é chamado de rastreamento.


### Recursos Utilizados 
Os recursos necessarios para realizar a construção desse projeto foram:
    
    * Python3, foi a linguagem utilizada para desenvolver o projeto.
    * OpenCV, uma das bibliotecas mais conhecidas para desenvolvimento de Visão Computacional;    
    * CSRT, é um algoritmo de rastreamento que está presente no OpenCV.
### CSR
No Filtro de *Discriminative Correlation Filter with Channel and Spatial Reliability* (DCF-CSR), usamos o mapa de confiabilidade espacial para ajustar o suporte do filtro à parte da região selecionada do quadro para rastreamento. Isso garante a ampliação e a localização da região selecionada e o rastreamento aprimorado das regiões ou objetos não retangulares. Ele usa apenas 2 recursos padrão (HoGs e Colornames). Ele também opera a fps comparativamente mais baixo (25 fps, mas oferece maior precisão para rastreamento de objetos.

<img src="/Figuras/rastreamento1.gif" width="800" height="562" />

### Para executar
Digite no terminal o comando abaixo:
```
python tracker_object_CSRT.py
```

