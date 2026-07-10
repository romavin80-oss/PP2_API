from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from sections.models import Section, Content, Question, Test
from sections.permissions import IsModerator, IsSuperuser
from sections.serializers.section_serializers import SectionSerializer, SectionListSerializer
from sections.serializers.content_serializers import ContentSerializer, ContentSectionSerializer, ContentListSerializer
from sections.serializers.question_serializers import QuestionSerializer, QuestionSectionSerializer
from sections.paginators import SectionPaginator, ContentPaginator, QuestionPaginator
from sections.serializers.test_serializers import TestSerializer, TestDetailSerializer


class SectionListApiView(ListAPIView):
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = SectionPaginator


class SectionCreateApiView(CreateAPIView):
    serializer_class = SectionSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated,)


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsSuperuser)

class ContentListApiView(ListAPIView):
    serializer_class = ContentListSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = ContentPaginator


class ContentCreateApiView(CreateAPIView):
    serializer_class = ContentSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)


class ContentRetrieveAPIView(RetrieveAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)

class ContentUpdateAPIView(UpdateAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)


class ContentDestroyAPIView(DestroyAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsSuperuser)

class QuestionListApiView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = QuestionPaginator

class QuestionRetrieveApiView(RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            question = Question.objects.get(pk=self.kwargs.get('pk'))
        except Question.DoesNotExist:
            return Response({'error': 'Question not found'}, status=404)

        answer = question.answer.title.strip().lower()
        member_answer = request.data.get('member_answer', '').strip().lower()

        is_correct = member_answer == answer
        return Response({'is_correct': is_correct})

class QuestionCreateApiView(CreateAPIView):
    serializer_class = QuestionSerializer

from rest_framework.permissions import AllowAny

class TestListApiView(ListAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.filter(is_active=True)
    permission_classes = [AllowAny]
    pagination_class = SectionPaginator


class TestCreateApiView(CreateAPIView):
    serializer_class = TestSerializer
    permission_classes = [AllowAny]


class TestRetrieveAPIView(RetrieveAPIView):
    serializer_class = TestDetailSerializer
    queryset = Test.objects.all()
    permission_classes = [AllowAny]


class TestUpdateAPIView(UpdateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = [AllowAny]


class TestDestroyAPIView(DestroyAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = [AllowAny]
