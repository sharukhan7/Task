from rest_framework import serializers

class FileSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False,)
    #file = serializers.FileField(upload_to='your directory name/')
