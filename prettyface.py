#
# prettyface.py
#
import matplotlib.pyplot as plt 
from scipy import ndimage
from scipy import misc
import numpy as np

face = misc.face(gray=True) 
plt.imshow(face)
plt.imshow(face, cmap=plt.cm.gray) 
shifted_face = ndimage.shift(face, (50,50))
plt.imshow(shifted_face)
rotated_face = ndimage.rotate(face, 30)
plt.imshow(rotated_face)
cropped_face = face[100:-100,100:-100]
plt.imshow(cropped_face)
print(np.shape(face)) # (768, 1024)
plt.imshow(face)
pixel_face = face[::10,::10]
plt.imshow(pixel_face)
pixel_face2 = face[::50,::50]
plt.imshow(pixel_face2)
plt.show()