from rest_framework import serializers




class FileListSerializer (serializers.Serializer ) :
    image = serializers.ListField(
                       child=serializers.FileField( max_length=100000,
                                         allow_empty_file=False,
                                         use_url=False )
                                )
    def create(self, validated_data):
        blogs=Blogs.objects.latest('created_at')
        image=validated_data.pop('image')
        for img in image:
            photo=Photo.objects.create(image=img,blogs=blogs,**validated_data)
        return photo
class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        read_only_fields = ("blogs",)
