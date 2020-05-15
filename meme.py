from PIL import Image, ImageDraw, ImageFont
import textwrap
import glob
def meme(destination, destination1, top, bottom):

    file = glob.glob(destination)[0]
    im = Image.open(file)
    draw = ImageDraw.Draw(im)

    image_width, image_height = im.size


    font = ImageFont.truetype(font="./impact/impact.ttf", size=int(image_height/13))


    top_text = top
    bottom_text = bottom
    char_width, char_height = font.getsize('A')
    char_per_line = image_width//char_width

    top_lines = textwrap.wrap(top_text, width=char_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=char_per_line)

    print(top_lines)
    print(bottom_lines)

        #finale
    y=10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
   # thicker border
        draw.text((x-2, y-2), line, font=font, fill='black')
        draw.text((x+2, y-2), line, font=font, fill='black')
        draw.text((x-2, y+2), line, font=font, fill='black')
        draw.text((x+2, y+2), line, font=font, fill='black')
######
        draw.text((x,y), line, fill='white', font=font)
        y+=line_height
        
    y= image_height - (char_height*len(bottom_lines))-10
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
           # thicker border
        draw.text((x-2, y-2), line, font=font, fill='black')
        draw.text((x+2, y-2), line, font=font, fill='black')
        draw.text((x-2, y+2), line, font=font, fill='black')
        draw.text((x+2, y+2), line, font=font, fill='black')
        ###
        draw.text((x,y), line, fill='white', font=font)
        y+=line_height

    im.save(destination1)
    # im.show()
 