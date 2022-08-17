from django.shortcuts import render

# Create your views here.
# Register API
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from appJwt.models import Book
from appJwt.serializer import RegisterSerializer, UserSerializer, BookSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class Greeting(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = 'Hey guys welcome  my django app is working'
        return Response(content)


class BookApi(generics.GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request, pk= None):
        if pk is not None:
            book = self.get_object()
            serializer = BookSerializer(book, many=False)
        else:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object()
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        book = self.get_object()
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class BlacklistRefreshView(APIView):
    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response("Success")
