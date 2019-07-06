from PIL import Image, ImageDraw, ImageFont
import random
# get an image
base = Image.open('C:\\Users\\denis\\Desktop\\pil-example.png').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
R = random.randint(0,255)
G = random.randint(0,255)
B = random.randint(0,255)
A = random.randint(0,255)

txt = Image.new('RGBA', base.size, (R, G, B, A))

# get a font
fnt = ImageFont.truetype('C:\\Windows\\Fonts\\micross.ttf', 350)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text
letter = input("Write your nickname here:")[0].capitalize()
d.text((120,49), letter, font=fnt, fill= "black")

out = Image.alpha_composite(base, txt)

out.show()