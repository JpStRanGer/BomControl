import qrcode

img = qrcode.make('test text')

print(type(img))
print(img.size)
# <class 'qrcode.image.pil.PilImage'>
# (290, 290)

img.save('qrcode_test.png')


import cv2 
  
# path 
path = r'qrcode_test.png'
  
# Using cv2.imread() method 
img = cv2.imread(path) 
  
# Displaying the image 
cv2.imshow('image', img) 