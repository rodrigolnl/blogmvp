from .serializers import BlogPostSerializer
from user_api.serializers import UserSerializer
from .models import BlogPost
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class BlogPostView(APIView):
    parser_classes = [JSONParser]
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user_serializer = UserSerializer(request.user, many=False)
        request.data['author'] = user_serializer.data['id']

        post_serializer = BlogPostSerializer(data=request.data, many=False)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,  pk):
        post = BlogPost.objects.get(id=pk)
        serializer = BlogPostSerializer(post, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request,  pk):
        post = BlogPost.objects.get(id=pk)
        if post.deleted:
            return Response('Already deleted.', status=status.HTTP_204_NO_CONTENT)
        post.deleted = True
        post.save()
        return Response('', status=status.HTTP_200_OK)


class AllBlogPostView(APIView):
    parser_classes = [JSONParser]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        posts = BlogPost.objects.filter(deleted=False)
        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
