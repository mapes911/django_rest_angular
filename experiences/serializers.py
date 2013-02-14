from rest_framework import serializers
from experiences.models import Experience, Chapter


class ExperienceSerializer(serializers.ModelSerializer):
    user = serializers.Field(source='user.username')

    class Meta:
        model = Experience
        fields = ('user', 'title', 'moral')


class ChapterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('title', 'body')


class ExperienceDetailSerializer(serializers.ModelSerializer):
    user = serializers.Field(source='user.username')
    chapters = ChapterDetailSerializer(many=True)

    class Meta:
        model = Experience
        fields = ('user', 'title', 'moral', 'chapters')
