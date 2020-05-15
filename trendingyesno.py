from PIL import Image, ImageDraw, ImageFont
import textwrap
import glob

def trendingyesno(destination, destination1, top, bottom):

    file = glob.glob(destination)[0]
    im = Image.open(file)
    draw = ImageDraw.Draw(im)

    img_w, img_h = im.size
    font = ImageFont.truetype(font="./impact/impact.ttf", size=int(img_h/13))

    top_text = top
    bottom_text = bottom

    char_w, char_h = font.getsize('A')
    char_per_line = ((img_w/2)//char_w) + 5

    top_lines = textwrap.wrap(top_text, width=char_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=char_per_line)

    print(top_lines)

    # y=7
    y = (char_h*len(top_lines)/2)
    for line in top_lines:
        line_width,line_height = font.getsize(line)
        x = (img_w/2)+20

        draw.text((x,y), line, fill="white", font=font)
        y+=line_height

    y = (img_h/2)+ (char_h*len(bottom_lines)/2)
    for line in bottom_lines:
        line_width,line_height = font.getsize(line)
        x = (img_w/2)+20

        draw.text((x,y), line, fill="white", font=font)
        y+=line_height

    im.save(destination1)
    im.show()
