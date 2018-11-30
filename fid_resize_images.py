import time
import pathlib
from PIL import Image
from PIL import ImageFile
from resizeimage import resizeimage

ImageFile.LOAD_TRUNCATED_IMAGES = True
start_time = time.time()
path = '/share/wandell/data/NN_Camera_Generalization/dataset/FID_score/data_city_scape_2/'
path = pathlib.Path(path)
files = list(path.glob('*.jpg')) + list(path.glob('*.png'))
'take only 400 images'
files = files[0:1000]
'resize images: size of images should be the same'
for fi in files:
    with open(str(fi), 'r+b') as f:
        with Image.open(f) as input_img:
            img_new = resizeimage.resize_cover(input_img, [1280, 720], validate=False)
            img_new.save(str(fi), input_img.format)

print(time.time()-start_time)