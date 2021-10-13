from django.contrib.auth import admin
from django.db import models


class Question(models.Model):
    """Вопросы в вопроснике"""
    Text = 'text'
    OneAnswer = 'OneAnswer'
    ManyAnswer = "ManyAnswer"

    ROLE_CHOICES = (
        (Text, 'Текст'),
        (OneAnswer, 'Один ответ'),
        (ManyAnswer, 'Много ответов')
    )

    type = models.CharField(choices=ROLE_CHOICES, blank=True, null=True, max_length=50)
    text = models.CharField(verbose_name='Текст вопроса', max_length=150)

    def __str__(self):
        return self.text


class Survey(models.Model):
    """Опросник"""
    name = models.CharField(verbose_name='Наименование опроса', max_length=150)
    description = models.CharField(verbose_name='Описание', max_length=300, blank=True)
    start = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    stop = models.DateTimeField(verbose_name='Закончен', null=True, blank=True)
    questions = models.ManyToManyField(Question, blank=True, related_name='questions')

    def __str__(self):
        return self.name


class AnswerQuestion(models.Model):
    """Ответы на вопрос"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Ответ на вопрос")

    def __str__(self):
        return self.text


class Answer(models.Model):
    user_id = models.IntegerField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    answer_question = models.ManyToManyField(AnswerQuestion)
    date_end = models.DateTimeField(auto_now_add=True, verbose_name="Время окончания")

    def __str__(self):
        return f"{self.user_id} {self.date_end}"
