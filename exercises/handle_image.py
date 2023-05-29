from PIL import Image, ImageDraw, ImageOps

print("start")
# Open input image
im = Image.open('./blank.jpg')


# Get rid of existing black border by flood-filling with white from top-left corner
ImageDraw.floodfill(im, xy=(0, 0), value=(255, 255, 255), thresh=10)

# Get bounding box of text and trim to it
bbox = ImageOps.invert(im).getbbox()
trimmed = im.crop(bbox)

# Add new white border, then new black, then new white border
res = ImageOps.expand(trimmed, border=10, fill=(255, 255, 255))
res = ImageOps.expand(res, border=5, fill=(0, 0, 0))
res = ImageOps.expand(res, border=5, fill=(255, 255, 255))
res.save('./result.jpg')
print(res)
