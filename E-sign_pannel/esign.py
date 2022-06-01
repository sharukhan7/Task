'''
requirments:
pip install GrabzIt
Application key:   ZmFmNWY1MTI4NDU0NDg2YjgyOTE0MmEwNjQzZjBjNDM=
Application secret: Pz8/Pz8aUz8/cD8/aWoNPz8/Hz9TcGVVPz8/Pz8/az8=
'''
from GrabzIt import GrabzItImageOptions
from GrabzIt import GrabzItClient



def replace_id(image,unique_id):
    with open(r'resource/file.html', 'r') as file:
        data = file.read()
        data = data.replace("src", image)
        data = data.replace("unique_id", unique_id)   
    with open(r'resource/temp.html', 'w') as file:
        file.write(data)

def Html_to_Image():
    grabzIt = GrabzItClient.GrabzItClient("ZmFmNWY1MTI4NDU0NDg2YjgyOTE0MmEwNjQzZjBjNDM=", "Pz8/Pz8aUz8/cD8/aWoNPz8/Hz9TcGVVPz8/Pz8/az8=")
    options = GrabzItImageOptions.GrabzItImageOptions()
    options.format = "png"
    grabzIt.FileToImage("./resource/temp.html", options)
    grabzIt.SaveTo("./resource/media/result.png")



img_src='src = "https://storage.googleapis.com/blockesign_staging/InkPaper__05_12_2022_10_24_58_966288?Expires=1654081511&GoogleAccessId=inkpaper-gcs-prod-access%40probable-pager-261221.iam.gserviceaccount.com&Signature=gwWgoqbM2%2FpkjbTuUnisMu%2BR1eEtolGDo2lCF6NZhKTpM5sHuYwgXxEkW37OpR7oIqq4hc4GGIWi1d3GFe%2FS9wS3D7uAOl14oJr0UfeK0uJerlXWTRyrCUUBXu1v14KEOgktL%2FU02KKVLb13Kmg5fP%2BhlnXe4y968ULTfAGS%2BaT6z6AlJYCpTPxsQ1KLyhSHGVKIbB9vtaBP%2B77lgycNqvSN9RXI3s8tA3tgfneKaiaJGzUWoya%2FL8LfhkYLKuNTQmfF7ZZczR%2BfgPeOkba7gaCBmFIkwDPYpYQOE1SS0R1peQNKWX8%2BKVPnHx5Rtcu11ZIhngvL0cpaqq2US4QOLQ%3D%3D"'
unq_id='sdjkfhb4brbsnbfjhjskartvck'
replace_id(img_src,unq_id)
Html_to_Image()