from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField
from rest_framework.fields import CharField
from sections.models import Question, Section


class QuestionSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Question
        fields = ('id', 'section', 'description', 'question', 'answer')


class QuestionSectionSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())
    members_answer = CharField(required=False, allow_blank=True)

    class Meta:
        model = Question
        fields = ('id', 'section', 'description', 'question', 'answer', 'members_answer')
