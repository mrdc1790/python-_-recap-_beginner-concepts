from PIL import Image

grad_pic_hs = Image.open('C:\\Users\\polla\\OneDrive\\Pictures\\adam-grad.jpg')
print(grad_pic_hs.size)
print(grad_pic_hs.filename)
print(grad_pic_hs.format_description)
colored_pencils = Image.open('C:\\Users\\polla\\OneDrive\\Pictures\\colored-pencils-pens-crayons-colour-pencils.jpg')
print(colored_pencils.size)
halfway = 910/2
x = halfway - 200
w = halfway + 200
y = 300
h = 607
cropped_pencils  = colored_pencils.crop((x, y, w, h))
cropped_pencils.show()
## crop -> (x, y, w, h)