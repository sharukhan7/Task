'''
requirment:
pip install html2image
'''
from html2image import Html2Image

def Html_to_Image(file,width,height):
    hti = Html2Image()
    hti.screenshot(url='file://{}'.format(file), save_as='draw3_test.png',size=(width,height))


w=150
h=65
html="/home/sharukhan/Ionixx/Django/task/testing/file.html"
Html_to_Image(html,w,h)