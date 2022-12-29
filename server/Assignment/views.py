from rest_framework.response import Response
from .models import Likes
from .serializers import LikeSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def likes(request):
    if request.method == 'GET':
        like = Likes.objects.all()
        serializer = LikeSerializer(like,many=True)
        return Response(serializer.data)
   
@api_view(['GET','PUT'])
def updateLike(request,pk):
    if request.method == 'PUT':
        data = request.data
        like = Likes.objects.get(id=pk)
        serializer = LikeSerializer(instance=like, data=data)
        if serializer.is_valid():
         serializer.save()
        return Response(serializer.data)
    if request.method == 'GET':
        like = Likes.objects.get(id=pk)
        serializer = LikeSerializer(like,many=False)
        return Response(serializer.data)    

