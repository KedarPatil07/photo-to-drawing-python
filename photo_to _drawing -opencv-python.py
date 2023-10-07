import cv2

image=cv2.imread('')
gr=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert=cv2.bitwise_not(gr)
blur=cv2.GaussianBlur(invert,(21,21),0)
invertedblur=cv2.bitwise_not(blur)
sketch=cv2.divide(gr,invertedblur,scale=256.0)
cv2.imshow('original image',image)
cv2.imshow('sketch image',sketch)
cv2.imwrite('',sketch)
cv2.waitKey(0)