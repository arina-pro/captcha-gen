import random
from captcha.image import ImageCaptcha

chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'

def randomString():
    rndLetters = (random.choice(chars) for i in range(4))
    return "".join(rndLetters)

image = ImageCaptcha(fonts=['./gentium/GenBkBasB.ttf', './gentium/GenBkBasBI.ttf', \
    './gentium/GenBkBasI.ttf', './gentium/GenBkBasR.ttf'])

text = randomString()
image.write(text, './generated_captcha/' + text + '.png')