# Bibliotecas
import cv2

# Criando rastreador;
tracker = cv2.TrackerCSRT_create()

# Capturando video;
video = cv2.VideoCapture('video1.mp4')

# Lendo video
ok, frame = video.read()

# Selecionando bounding box do objeto a ser rastreado;
bbox = cv2.selectROI(frame)

# Iinicia o rastreador
ok = tracker.init(frame,bbox)
print(ok)


# Para ler todos os frames do video;
while True:
    ok, frame = video.read()

    # Se o video terminar sai do while;
    if not ok:
        break

    # Atualizando bbox;=
    ok, bbox = tracker.update(frame)

    if ok:
        # Pegando informação de rastreio;
        (x, y, w, h) = [int(v) for v in bbox]
        
        # Desenha um retangulo verdr ao redor do objeto rastreado;
        cv2.rectangle(frame, # Imagem que será desenhada;
                     (x,y), (x+w, y+h), # Posição que será desenhado o retangulo;
                     (0,255,0)) # Cor do retangulo está em BGR;
    else:
        # Adicona o texto caso não possa mais fazer o rastreamento do objeto;
        cv2.putText(frame, "Fail in tracking..", (100,80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2) 

    # Plota a imagem
    cv2.imshow("Tracking", frame)
    # fecha o ploty com o botão ESC;
    if cv2.waitKey(1) & 0xFF == 27:
        break

