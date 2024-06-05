from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
from io import BytesIO
import textwrap
import requests
import random
import os

load_dotenv()

PIXABAY_API_KEY = os.environ.get("PIXABAY_API_KEY")

print(".env variables loaded")

# get a list of all fonts in the fonts folder
fonts_list = os.listdir("fonts")
fonts = [f[:-4] for f in fonts_list] #remove .ttf from the font name
fonts_size = [45, 70, 80] #sizes of fonts (you will need to change this if you add more fonts by hand)

def get_random_image_url(tags):
    tags = tags.strip()
    tags = tags.lower()
    tags = tags.replace(", ", "+")
    tags = tags.replace(",", "+")
    tags = tags.replace(" ", "+")

    payload = {
        "key": PIXABAY_API_KEY,
        "q": tags,
        "image_type": "photo",
        "min_width": "1080",
        "min_height": "1080"
    }

    url = f"https://pixabay.com/api/"
    
    response = requests.get(url, params=payload)
    data = response.json()
    photos = data["hits"]
    random_photo = random.choice(photos)
    image_url = random_photo["largeImageURL"]
    return image_url


def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    quote = response.json()["content"]
    author = response.json()["author"]
    return f"{quote}\n                                      - {author}" #lolll this is so bad but it works... for now... 


def make_image(image_url, quote_text, fonts_pick:int, background:bool):
    if background:
        image = Image.open(requests.get(image_url, stream=True).raw)
        image = image.resize((1080, 1080))
        image = image.convert("RGB")
    else:
        image = Image.open(("bg.jpg"))
        image = image.convert("RGB")

    quote_font = ImageFont.truetype(f"fonts/{fonts[fonts_pick]}.ttf", fonts_size[fonts_pick])
    quote_lines = textwrap.wrap(quote_text, width=30)

    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textbbox((0, 0), quote_lines[0], font=quote_font)[2:]
    x = (image.width - text_width) // 2
    y = (image.height - text_height * len(quote_lines)) // 2

    # additional font styling
    shadow_color = (0, 0, 0)  # shadow color
    shadow_offset = 3  # shadow offset in pixels

    for line in quote_lines:
        # draw shadow text
        shadow_x = x + shadow_offset
        shadow_y = y + shadow_offset
        draw.text((shadow_x, shadow_y), line, font=quote_font, fill=shadow_color)

        # draw main text
        draw.text((x, y), line, font=quote_font, fill=(255, 255, 255))
        y += text_height

    img_io = BytesIO()
    image.save(img_io, "JPEG", quality=100)
    img_io.seek(0)

    return img_io
