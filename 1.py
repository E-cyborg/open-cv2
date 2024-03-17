import cv2


# path of image
image_path='images\\image.jpg'


# loading the image
img = cv2.imread(image_path, -1)



#resizing the image
img=cv2.resize(img,(1000,1000))
#img=cv2.resize(img,(0,0), fx=0.5,fy=0.5)
#througth this we can half ,2x,... as much we can increase the size


img=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
#using rotate method we can rotate the img in any diraction we want


# cv2.imwrite('newimage.jpg',img)
#to save the updated image


#displaying the the image , window name image name
cv2.imshow('image',img)



#to wait the display the image
cv2.waitKey(0)
cv2.destroyAllWindows()
