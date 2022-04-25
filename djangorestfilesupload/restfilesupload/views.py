from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from restfilesupload.serializers import FileSerializer

import os
import zipfile



class FileUploadViewSet(viewsets.ViewSet):

    def create(self, request):
        
        if bool(request.FILES):
            serializer_class = FileSerializer(data=request.data)
            if 'file' not in request.FILES or not serializer_class.is_valid():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                handle_uploaded_file(request.FILES['file'])
                return Response(status=status.HTTP_201_CREATED)

        else:
            if os.path.isdir(request.data['path']):
                fname = str(request.data['path']).split('/')[-1]
                zipf = zipfile.ZipFile(fname+'.zip', 'w', zipfile.ZIP_DEFLATED)
                zipdir(request.data['path'], zipf)
                zipf.close()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)    

def zipdir(path, ziph):
    count=0
    for root, dirs, files in os.walk(path):
        count+=1
        for file in files:
            ziph.write(os.path.join(root, file))
        if count == 6:
            break