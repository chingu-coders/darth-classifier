from PIL import ImageEnhance
import os
size_256 = (256,256)
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f).convert('RGB')
        fn, fext = os.path.splitext(f)
        enhancer = ImageEnhance.Brightness(i)
        i = enhancer.enhance(1.5)
        img = i.resize(size_256, Image.ANTIALIAS)
        img.save('Clean_darth vader/{}_clean{}'.format(fn, fext))
        
