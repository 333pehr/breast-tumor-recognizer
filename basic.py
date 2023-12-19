import cv2 as cv

img = cv.imread('Photos/foto1.jpg')
#cv.imshow('Zeynep', img)

#resize the image
def rescaleFrame(frame, scale=0.18):
    width= int(frame.shape[1]* scale)
    height= int(frame.shape[0]* scale)

    dimensions = (width,height)

    return cv.resize(frame ,dimensions,interpolation=cv.INTER_AREA)

resized_image=rescaleFrame(img)
#cv.imshow('Image', resized_image)


#converting to grayscale
gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

#blur
blur=cv.GaussianBlur(gray , (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#Edge Cascade
canny = cv.Canny(blur , 110 , 130)
cv.imshow('Canny Edges', canny)

#dilating İmage
dilated = cv.dilate(canny,(7,7), iterations=3)
cv.imshow('Dilated',dilated)

#resize
#resized= cv.resize(img , (500,500) , interpolation=cv.INTER_AREA)
#cv.imshow('Resized' , resized)

#Cropping
#cropped= img[50:200 , 200:400]
#cv.imshow('Cropped', cropped)


cv.waitKey(0)