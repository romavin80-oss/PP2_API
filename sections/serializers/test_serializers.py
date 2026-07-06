from rest_framework import serializers
from sections.models import Test, Question, Section

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class TestDetailSerializer(serializers.ModelSerializer):
    section = serializers.SlugRelatedField(slug_field='title', queryset=Section.objects.all())
    questions = serializers.SlugRelatedField(slug_field='question', many=True, queryset=Question.objects.all())

    class Meta:
        model = Test
        fields = '__all__'
