from rest_framework import serializers 

class PostSerializer(serializers.ModelField):
    class Mets:
        models = Post
        field = '__all__'
