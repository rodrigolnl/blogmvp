from rest_framework import serializers
from .models import BlogPost, Keyword


class KeywordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyword
        fields = [
            'name'
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer(many=True)

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'subtitle',
            'content',
            'published',
            'keywords',
            'author'
        ]

    def create(self, validated_data):
        keywords_data = validated_data.pop("keywords")
        blog_post = BlogPost.objects.create(**validated_data)
        for keyword in keywords_data:
            Keyword.objects.create(blog_post=blog_post, name=keyword['name'])
        return blog_post
