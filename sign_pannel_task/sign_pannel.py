'''
requirment:
pip install html2image
'''
import os
from html2image import Html2Image

def Html_to_Image(file,width,height,output_path):
    hti = Html2Image()
    hti.output_path = output_path
    hti.screenshot(url='file://{}'.format(file),save_as='test_op6.png',size=(width,height))


def replace_id(image,unique_id):
    with open(r'resource/test1.html', 'r') as file:
        data = file.read()
        #print(data)
        data = data.replace("src", image)
        #print(data)
        data = data.replace("unique_id", unique_id)
        
    with open(r'resource/temp.html', 'w') as file:
        file.write(data)
        Html_to_Image(html,w,h,path)


w=200
h=100
html="/home/sharukhan/Ionixx/Django/task/testing/test/resource/temp.html"
path='/home/sharukhan/Ionixx/Django/task/testing/test/media'
#Html_to_Image(html,w,h,path)

img_src='src ="https://storage.googleapis.com/blockesign_staging/InkPaper__05_10_2022_09_04_57_360749"'
unq_id='sdjkfhb4brbsnbfjhjskartvc'
replace_id(img_src,unq_id)

