from os import path as p

from django.urls import path
from rest_framework.routers import DefaultRouter

from sections.apps import SectionsConfig
from sections.views import (
    SectionListApiView, SectionCreateApiView, SectionRetrieveAPIView, SectionUpdateAPIView, SectionDestroyAPIView,
    ContentListApiView, ContentCreateApiView, ContentRetrieveAPIView, ContentUpdateAPIView, ContentDestroyAPIView,
    QuestionListApiView, QuestionRetrieveApiView, TestListApiView, TestCreateApiView, TestRetrieveAPIView, TestUpdateAPIView, TestDestroyAPIView
)

app_name = SectionsConfig.name

router = DefaultRouter()

section = 'section/'
content = 'content/'
question = 'question/'
create = 'create/'
update = 'update/'
delete = 'delete/'
int_pk = '<int:pk>/'
test_path = 'test/'

urlpatterns = [
    # section urlpatterns
    path(p.join(section), SectionListApiView.as_view(), name='section_list'),
    path(p.join(section, create), SectionCreateApiView.as_view(), name='section_create'),
    path(p.join(section, int_pk), SectionRetrieveAPIView.as_view(), name='section_detail'),
    path(p.join(section, int_pk, update), SectionUpdateAPIView.as_view(), name='section_update'),
    path(p.join(section, int_pk, delete), SectionDestroyAPIView.as_view(), name='section_delete'),

    # content urlpatterns
    path(p.join(content), ContentListApiView.as_view(), name='content_list'),
    path(p.join(content, create), ContentCreateApiView.as_view(), name='content_create'),
    path(p.join(content, int_pk), ContentRetrieveAPIView.as_view(), name='content_detail'),
    path(p.join(content, int_pk, update), ContentUpdateAPIView.as_view(), name='content_update'),
    path(p.join(content, int_pk, delete), ContentDestroyAPIView.as_view(), name='content_delete'),

    # question urlpatterns
    path(p.join(question), QuestionListApiView.as_view(), name='question_list'),
    path(p.join(question, int_pk), QuestionRetrieveApiView.as_view(), name='question'),

    # test urlpatterns
    path(p.join(test_path), TestListApiView.as_view(), name='test_list'),
    path(p.join(test_path, create), TestCreateApiView.as_view(), name='test_create'),
    path(p.join(test_path, int_pk), TestRetrieveAPIView.as_view(), name='test_detail'),
    path(p.join(test_path, int_pk, update), TestUpdateAPIView.as_view(), name='test_update'),
    path(p.join(test_path, int_pk, delete), TestDestroyAPIView.as_view(), name='test_delete'),

] + router.urls
