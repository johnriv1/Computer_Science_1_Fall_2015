from PIL import Image

background = Image.new('RGB', (512,512), 'white')

im1 = Image.open('ca.jpg')
im1 = im1.resize((256,256))
background.paste(im1,(0,0))

im2 = Image.open('im.jpg')
im2 = im2.resize((256,256))
background.paste(im2,(256,0))

im3 = Image.open('hk.jpg')
im3 = im3.resize((256,256))
background.paste(im3,(0,256))

im4 = Image.open('bw.jpg')
im4 = im4.resize((256,256))
background.paste(im4,(256,256))

background.show()