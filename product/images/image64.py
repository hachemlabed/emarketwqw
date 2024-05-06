import base64

with open("C:/Users/SBG/OneDrive/Documents/Bureau/apple-iphone-15-1.jpg", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read())

print('the image :' ,base64_image)