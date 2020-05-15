from PIL import ImageDraw, Image, ImageFont
import textwrap
import glob

def trendingcat(destination, destination1, leftline, rightline):

    file = glob.glob(destination)[0]
    im = Image.open(file)
    draw = ImageDraw.Draw(im)

    img_w, img_h = im.size

    font = ImageFont.truetype(font="./impact/impact.ttf", size=int(img_h/20))

    left = leftline
    right = rightline

    char_w, char_h =font.getsize('A')

    char_per_section = (img_w/2)//(char_w)

    left_lines = textwrap.wrap(left, width=char_per_section)
    right_lines = textwrap.wrap(right, width=char_per_section)

    print(left_lines)
    print(right_lines)

    #left
    y=char_h*len(left_lines)/2
    for line in left_lines:
        line_w, line_h = font.getsize(line)
        x=40
        draw.text((x,y), line, fill="black", font=font)
        y+=line_h

    #right
    y=char_h*len(right_lines)/2
    for line in right_lines:
        line_w, line_h = font.getsize(line)
        x=(img_w/2)+40
        draw.text((x,y), line, fill="black", font=font)
        y+=line_h

    im.save(destination1)
    im.show()


def trendingyesno(destination, destination1, top, bottom):

    file = glob.glob(destination)[0]
    im = Image.open(file)
    draw = ImageDraw.Draw(im)

    img_w, img_h = im.size
    font = ImageFont.truetype(font="./impact/impact.ttf", size=int(img_h/13))

    top_text = top
    bottom_text = bottom
    print(top_text)
    print(bottom_text)

    char_w, char_h = font.getsize('A')
    char_per_line = ((img_w/2)//char_w) + 2

    top_lines = textwrap.wrap(top_text, width=char_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=char_per_line)

    print(top_lines)

    # y=7
    y = (char_h*len(top_lines)/2)+20
    for line in top_lines:
        line_width,line_height = font.getsize(line)
        x = (img_w/2)+30

        draw.text((x,y), line, fill="white", font=font)
        y+=line_height

    y = (img_h/2)+ (char_h*len(bottom_lines)/2)+20
    for line in bottom_lines:
        line_width,line_height = font.getsize(line)
        x = (img_w/2)+30

        draw.text((x,y), line, fill="white", font=font)
        y+=line_height

    im.save(destination1)
    im.show()
