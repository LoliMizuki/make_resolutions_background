import Image

def make_image(name, size, ext):
    targetImage = Image.new("RGB", size, (71,134,21))
    
    innerColorBoundWidth = 1
    centerColorBoundWidth = 2
    
    w = size[0]
    h = size[1]
    
    for x in range(w):
         for y in range(h):
            if x == 0 or y == 0 or x == w -1 or y == h - 1:
               targetImage.putpixel((x,y), (255,0,0))
               
    filename = name + "." + ext
    targetImage.save(filename, "png")
    

if __name__ == '__main__':
    
    w = 480
    h = 320
    
    image_names = ["bg~iphone.png", "bg~ipad.png", "bg@2x~iphone", "bg@2x~ipad"]
    sizes = [(480, 320), (1024, 768), (960, 640), (2048, 1536)]
    
    for i in range(len(image_names)):
        make_image(image_names[i], sizes[i], "png")
    
            
