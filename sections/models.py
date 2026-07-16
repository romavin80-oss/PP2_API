from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import NULLABLE


class Section(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'), unique=True)
    description = models.TextField(verbose_name=_('Description'), **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        ordering = ['id']


class Content(models.Model):
    section = models.ForeignKey(Section, verbose_name=_('Section'), on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name=_('Title'), unique=True)
    content = models.TextField(verbose_name=_('Content'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Content')
        verbose_name_plural = _('Content')
        ordering = ['id']


class Question(models.Model):
    section = models.ForeignKey(Section, verbose_name=_('Section'), on_delete=models.CASCADE)
    description = models.TextField(verbose_name=_('Description'), **NULLABLE)
    question = models.TextField(verbose_name=_('Question'), **NULLABLE)
    answer = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name=_('Answer'), **NULLABLE)
    members_answer = models.TextField(verbose_name=_('Members Answer'), **NULLABLE)

    def __str__(self):
        return f"Вопросы по курсу {self.section}"

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['section']


class Test(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_('Section'), related_name='tests')
    title = models.CharField(max_length=150, verbose_name=_('Test Title'))
    description = models.TextField(verbose_name=_('Test Description'), **NULLABLE)
    questions = models.ManyToManyField(Question, verbose_name=_('Questions'), related_name='tests', blank=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))

    def __str__(self):
        return f"{self.title} ({self.section.title})"

    class Meta:
        verbose_name = _('Test')
        verbose_name_plural = _('Tests')
        ordering = ['id']
