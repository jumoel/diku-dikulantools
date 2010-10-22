

import uuid
import Image, ImageDraw, ImageFont

max = 64

serials = []

for i in range(0, max):
    im = Image.open("billet_raw.png")
    txt = Image.new('L', (1011, 638))
    draw = ImageDraw.Draw(txt)
    f = ImageFont.truetype("consolas.ttf", 55)
    serial = "-".join(str(uuid.uuid4()).split('-')[1:4]).upper()
    draw.text((15,560), serial, font=f, fill=255)
    im.paste(txt, mask=txt)
    im.save("billet" + serial + ".png", "PNG")
    serials.append(serial)

for i in range(0, len(serials)):
    print serials[i]


