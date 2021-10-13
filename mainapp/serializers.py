from rest_framework import serializers
from .models import Survey, Question, Answer, AnswerQuestion


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class SurveyListSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = ('id', "name", 'description', 'start', 'stop', 'questions')


class SurveyUserSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = ('id', "name", 'description', 'start', 'stop', 'questions')


class AnswerQuestionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = AnswerQuestion
        fields = ('question', 'text')


class AnswerSerializer(serializers.ModelSerializer):
    answer_question = AnswerQuestionSerializer(many=True)

    class Meta:
        model = Answer
        fields = ('id', 'user_id', 'survey', 'date_end', 'answer_question')
