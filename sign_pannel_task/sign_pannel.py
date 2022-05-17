'''
requirment:
pip install html2image
'''
from html2image import Html2Image




def replace_id(image,unique_id):
    with open(r'resource/file.html', 'r') as file:
        data = file.read()
        data = data.replace("src", image)
        data = data.replace("unique_id", unique_id)   
    with open(r'resource/temp.html', 'w') as file:
        file.write(data)
        
        

def Html_to_Image():
    hti = Html2Image()
    hti.output_path = 'resource/media/'
    hti.screenshot(url='resource/temp.html',save_as='test_op6.png',size=(200,100))


#img_src='src ="https://storage.googleapis.com/blockesign_staging/InkPaper__05_10_2022_09_04_57_360749"'
img_src='src ="/home/sharukhan/Documents/Local/Task/sign_pannel_task/resource/test1.png"'

unq_id='sdjkfhb4brbsnbfjhjskartvck'
replace_id(img_src,unq_id)
Html_to_Image()

