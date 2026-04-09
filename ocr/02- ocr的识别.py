# ocr的识别
# 安装pip install pytesseract
import pytesseract
# 安装pip install pillow
from PIL import Image
from urllib import request
# img = Image.open('aaa.png')
# str_ = pytesseract.image_to_string(img)
# print(str_)
# img = Image.open('bbb.png')
# str_ = pytesseract.image_to_string(img,lang="chi_sim") # ang="chi_sim"指定识别中文
# print(str_)


request.urlretrieve('https://passport.lagou.com/vcode/create?from=register&refresh=1513081451891', 'yzm.png')
img = Image.open('a.jpg')
str_ = pytesseract.image_to_string(img)
print(str_)





















