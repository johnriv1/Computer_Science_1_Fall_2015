from PIL import Image
import panoramio as pan
from check2_helper import make_square

address = raw_input('Type an address ==> ')

urls = pan.getPhotos(address,4)

if len(urls) >= 4:
    
    background = Image.new('RGB', (512,512), 'white')
    
    im1 = pan.openphoto(urls[0])
    im1 = make_square(im1)
    im1 = im1.resize((256,256))
    background.paste(im1,(0,0))
    
    im2 = pan.openphoto(urls[1])
    im2 = make_square(im2)
    im2 = im2.resize((256,256))
    background.paste(im2,(256,0))
    
    im3 = pan.openphoto(urls[2])
    im3 = make_square(im3)
    im3 = im3.resize((256,256))
    background.paste(im3,(0,256))
    
    im4 = pan.openphoto(urls[3])
    im4 = make_square(im4)
    im4 = im4.resize((256,256))
    background.paste(im4,(256,256))
    background.show()
else:
    print "Could not find sufficent number of pictures"
    

    