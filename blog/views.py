from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer

class ArticleView(APIView):
    # def get(self, request):
    #     articles = Article.objects.all()
    #     serializer = ArticleSerializer(articles, many=True)
    #     return Response(serializer.data)


    def get(self, request, slug=None):
        if slug is None:
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
        else:
            article = Article.objects.get(slug=slug)
            serializer = ArticleSerializer(article)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # def get(self, request, slug):
    #     article = Article.objects.get(slug=slug)
    #     serializer = ArticleSerializer(article)
    #     return Response(serializer.data)