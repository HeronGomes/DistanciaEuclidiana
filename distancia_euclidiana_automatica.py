# -*- coding: utf-8 -*-

import cv2 as cv
import cv2.data as haar_dir
#Importante para o calculo da distancia euclidiana (no plano)
from scipy.spatial import distance as dist




#####Curiosidade######Curiosidade#############
# Pixel(Picture + Element), a menor unidade de uma imagem, com o qual gera-se uma cor (RGB)
# O tamanho de um pixel é 1(polegada)/96 , aproximadamente 0,26 mm (0,254...)

CONST_PIXEL= 0.254
imagem = cv.imread('pessoa4.png') #Troque o nome para testar outras imagens
haar_path = haar_dir.haarcascades #Forma mais bonita de usar  os modelos ja treinados (estao na pasta do sistema quando instalado)
haar= haar_path + 'haarcascade_fullbody.xml'

classificadorCorpo = cv.CascadeClassifier(haar)

imagemDeteccao = cv.cvtColor(imagem,cv.COLOR_BGR2GRAY) #Mudando para escala de cinza

roi = classificadorCorpo.detectMultiScale(imagemDeteccao)#Deteccao com parametros padroes.

for x,y,w,h in roi:
    tamanho_cm = (dist.euclidean((x,y),(x+w,y+h))*CONST_PIXEL)/10 #Calculo da distancia entre pixels e conversao para centimetros
    dimensoes = imagem[y:y+h,x:x+w].shape
    #Desenho da linha vermelha no centro do quadrado
    cv.line(imagem[y:y+h,x:x+w],
            (int(dimensoes[1]*0.5),0),
            ((int(dimensoes[1]*0.5)),y+h),
            (0,0,255),
            1,
            cv.LINE_4)
    
    #Escreve o tamanho do objeto na imagem
    cv.putText(imagem,str('%.2f'%tamanho_cm) + 'cm',(x,y+h+15),cv.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0))  
    
    #Desenha os quadrados (boundingbox)
    cv.rectangle(imagem,(x,y),((x+w),(y+h)),(255,255,0),1,cv.LINE_4)

#Exibe o resultato ate que uma tecla seja pressionada
cv.imshow("Tamanho", imagem)
cv.waitKey()
cv.destroyAllWindows()