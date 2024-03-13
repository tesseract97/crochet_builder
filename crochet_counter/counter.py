from PIL import Image, ImageColor


#Take image, resize to 25x25 if not

def open_image():
    im = Image.open('/Users/tessacondon/crochet_builder/methods/desert.png',"r")
    #im = im.convert("P")
    #im = im.convert("P", palette=ADAPTIVE, colors = 16)
    
    im.show()
    width, height = im.size
    im1= im.resize((25, 25))
    #add resampling filter?
    
    pix_val = list(im1.getdata())
    colors= im1.getcolors()
    print(colors)

    pix = im1.getpixel((0,0))
    print(pix)

    with open("pix.txt", 'w') as text_file:
        for line in pix_val:
            text_file.write(f"{line}\n")

    #palette = list(im.getpalette())
    
    #print("palette:", palette)
            
    #grab dominant color and palette from an image
    


if __name__== "__main__":
    open_image()
    


#<blockquote class="pix-embed-wrap"><div class="pix-embed-activity" data-id="sr285c3d7d76daws3" data-width="25" data-height="25" data-type="art" data-theme="light" data-show-edit="1">Pixilart Embed</div></blockquote><script async="async" src="https://www.pixilart.com/js/embed.js?v=1.0.4"></script>