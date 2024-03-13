import random
import PIL
from PIL import Image
imagetails = Image.open("tails.jpeg")
imageheads = Image.open("heads.jpg")
a=random.randint(1,3)
if(a<2):
    imageheads.show()
else:
    imagetails.show()


