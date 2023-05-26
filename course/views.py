from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Chapter
from .serializers import CourseSerializer, ChapterSerializer

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):
    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # def put(self, request, pk):
    #     try:
    #         course = Course.objects.get(pk=pk)
    #         serializer = CourseSerializer(course, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except Course.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    # def patch(self, request, pk):
    #     try:
    #         course = Course.objects.get(pk=pk)
    #         serializer = CourseSerializer(course, data=request.data, partial=True)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except Course.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ChapterListView(APIView):
    def get(self, request, course_id):
        chapters = Chapter.objects.filter(course_id=course_id)
        serializer = ChapterSerializer(chapters, many=True)
        return Response(serializer.data)