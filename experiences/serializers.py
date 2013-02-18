from rest_framework import serializers
from experiences.models import Experience, Chapter


class ChapterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'body')


class ExperienceSerializer(serializers.ModelSerializer):
    user = serializers.Field(source='user.username')
    chapters = ChapterDetailSerializer(many=True)

    class Meta:
        model = Experience
        fields = ('id', 'user', 'title', 'moral', 'chapters')
