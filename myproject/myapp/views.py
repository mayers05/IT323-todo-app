from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import Postserializer

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = Postserializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Postserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)


