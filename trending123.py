from PIL import ImageDraw, Image, ImageFont
import textwrap
import glob

def trending123(destination, destination1, leftline, middleline, rightline):
    file = glob.glob(destination)[0]
    im = Image.open(file)
    draw = ImageDraw.Draw(im)

    img_w, img_h = im.size
    font = ImageFont.truetype(font="./impact/impact.ttf", size=int(img_h/13))


    front = leftline
    middle = middleline
    back = rightline

    char_w, char_h = font.getsize('A')

    char_per_section = (img_w/2)//char_w

    front_lines = textwrap.wrap(front, width=char_per_section)
    middle_lines = textwrap.wrap(middle,width=char_per_section/2)
    back_lines = textwrap.wrap(back, width=char_per_section/2+3)

    print(front_lines)
    print(middle_lines)
    print(back_lines)

    #frontdraw
    y = 500
    for line in front_lines:
        line_h , line_w = font.getsize(line)
        x = 250
        # thicker border
        draw.text((x-2, y-2), line, font=font, fill='black')
        draw.text((x+2, y-2), line, font=font, fill='black')
        draw.text((x-2, y+2), line, font=font, fill='black')
        draw.text((x+2, y+2), line, font=font, fill='black')
    ######
        draw.text((x,y), line, fill="white", font=font)
        y+=line_h

    #middledraw
    y = 300
    for line in middle_lines:
        line_h , line_w = font.getsize(line)
        x = 650
        # thicker border
        draw.text((x-2, y-2), line, font=font, fill='black')
        draw.text((x+2, y-2), line, font=font, fill='black')
        draw.text((x-2, y+2), line, font=font, fill='black')
        draw.text((x+2, y+2), line, font=font, fill='black')
    ######
        draw.text((x,y), line, fill="white", font=font)
        y+=line_h

    y = 550
    for line in back_lines:
        line_w , line_h = font.getsize(line)
        x = 900
        # thicker border
        draw.text((x-2, y-2), line, font=font, fill='black')
        draw.text((x+2, y-2), line, font=font, fill='black')
        draw.text((x-2, y+2), line, font=font, fill='black')
        draw.text((x+2, y+2), line, font=font, fill='black')
    ######
        draw.text((x,y), line, fill="white", font=font)
        y+=line_h
    im.save(destination1)
    im.show()