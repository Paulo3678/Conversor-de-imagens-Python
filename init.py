# Importing Library
from PIL import Image
 
# Loading the image
for i in range (1,18):
    image = Image.open('./imgs/{}.ashx'.format(i))
    # Specifying the RGB mode to the image
    image = image.convert('RGB')
    
    # Converting an image from PNG to JPG format
    image.save("./converted/{}.jpg".format(i))
    print("Image successfully converted!")
 