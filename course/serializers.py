from rest_framework import serializers
from .models import Course, Chapter, Resource

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'title', 'url']

class ChapterSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = ['id', 'title', 'resources']


class ChapterSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True)

    class Meta:
        model = Chapter
        fields = ['id', 'title', 'resources']


class CourseSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'chapters']

    def create(self, validated_data):
        chapters_data = validated_data.pop('chapters', [])
        course = Course.objects.create(**validated_data)

        for chapter_data in chapters_data:
            resources_data = chapter_data.pop('resources', [])
            chapter = Chapter.objects.create(course=course, **chapter_data)

            for resource_data in resources_data:
                Resource.objects.create(chapter=chapter, **resource_data)

        return course
