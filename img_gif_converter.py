# written by Priyesh Kumar Tripathi
# Making gif from images
import glob
from PIL import Image
fp_in = '*.jpg'           # Input filepath 
fp_out = 'test_5.gif'     # Output filepath
imgs = (Image.open(f) for f in sorted(glob.glob(fp_in)))
img = next(imgs)          # extract first image from iterator
img.save(fp=fp_out, format='GIF', append_images=imgs, save_all=True, duration=300, loop=1)
