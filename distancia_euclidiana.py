import cv2 as cv
from scipy.spatial import distance as dist




######Atenção#########Atenção##########Atenção###################
#O valor do pixel por polegada muda de câmera para câmera, deverá
#ser calibrado se ocorrer troca de equipamento
##################################################################

pixel_polegada = 97


imagem = cv.imread('pessoa2.png')
ponto = []
cv.namedWindow('Imagem')
def pointClick(event, x, y, flags,param):
        
    if event == cv.EVENT_LBUTTONDBLCLK and len(ponto)<2:
        ponto.append([x,y])
        cv.drawMarker(imagem,(x,y),(0,0,0),cv.MARKER_CROSS,30,3,9)
        cv.putText(imagem,'pt'+str(len(ponto)),(x+8,y),3,1,(0,0,0))
        cv.imshow('Imagem',imagem)
        
def calculaDistanciaCM():
    
    if len(ponto)==2:
        distancia_polegada = dist.euclidean(ponto[0],ponto[1])/ pixel_polegada
        distancia_centimetro = '%.2f'%(distancia_polegada * 2.54)
        cv.putText(imagem,'#'+str(distancia_centimetro)+' cm',(ponto[0][0],int(dist.euclidean(ponto[0][1],ponto[1][1])/2)),2,1,(255,100,0))
        cv.imshow('Imagem',imagem)
        cv.waitKey(0)
        
while True:
    
    cv.setMouseCallback('Imagem',pointClick)
    cv.imshow('Imagem',imagem)
    if cv.waitKey(0):
        break



cv.destroyAllWindows()

calculaDistanciaCM()

cv.destroyAllWindows()




