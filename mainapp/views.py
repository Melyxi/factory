import json
from django.db import transaction
from django.utils import timezone
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Survey, Question, AnswerQuestion, Answer
from .serializers import SurveyListSerializer, QuestionSerializer, SurveyUserSerializer, AnswerSerializer, \
    SurveyDetailSerializer


class IsAdminPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class SurveyViewSet(ModelViewSet):
    permission_classes = [IsAdminPermissions]
    queryset = Survey.objects.all()
    serializer_class = SurveyListSerializer


class QuestionViewSet(ModelViewSet):
    permission_classes = [IsAdminPermissions]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SurveyUserView(ListAPIView, RetrieveAPIView):
    serializer_class = SurveyListSerializer

    def get_queryset(self):
        queryset = Survey.objects.filter(stop__gte=timezone.now())
        return queryset


class SurveyDetailView(RetrieveAPIView):
    serializer_class = SurveyDetailSerializer

    def get_queryset(self):
        queryset = Survey.objects.filter(stop__gte=timezone.now())
        return queryset


class AnswerSurvey(APIView):

    def get_object_survey(self, pk):
        obj = get_object_or_404(Survey, stop__gte=timezone.now(), pk=pk)
        return obj

    def get(self, request, **kwargs):
        obj = self.get_object_survey(kwargs['pk'])
        serializer = SurveyUserSerializer(obj)
        return Response(serializer.data)

    # валидация по типу ответа
    @staticmethod
    def valid_answer(answer):
        if isinstance(answer, list):
            if len(answer) == 1:
                return 'OneAnswer'
            else:
                return 'ManyAnswer'
        if isinstance(answer, str):
            return 'text'

    @transaction.atomic
    def post(self, request, **kwargs):
        data = request.data
        obj = self.get_object_survey(kwargs['pk'])
        obj_answer = Answer(user_id=data['user_id'], survey=obj)
        obj_answer.save()
        question = data['question']

        for item in question:
            answer_q = AnswerQuestion()
            id_question = item['id_question']
            quest = Question.objects.filter(pk=id_question).first()
            survey_question = obj.questions.all()

            answer = item['answer']
            type_answer = self.valid_answer(answer)

            # валидация на соотвествия вопроса в опроснике
            if quest in survey_question:
                if quest.type == type_answer:
                    answer_q.question = quest
                    answer_q.text = json.dumps(answer)
                    answer_q.save()
                else:
                    answer_q.question = quest
                    answer_q.text = "Неверный тип ответа!"
                    answer_q.save()
                obj_answer.answer_question.add(answer_q)
                obj_answer.save()

        obj_answer.date_end = timezone.now()
        obj_answer.save()
        answer_serialiser = AnswerSerializer(obj_answer)

        return Response(answer_serialiser.data)


class ResultAnswerView(APIView, PageNumberPagination):
    serializer_class = AnswerSerializer

    def get(self, request, **kwargs):
        queryset = Answer.objects.filter(user_id=kwargs["id_user"])
        results = self.paginate_queryset(queryset, request, view=self)
        serializer = self.serializer_class(results, many=True)
        return self.get_paginated_response(serializer.data)

#Заполнение ответов на вопросы
"""
{
    "user_id": 1,
    "question": 
        [
                {"id_question": 8,
                "answer": ["0"]
                },
                {"id_question": 9,
                "answer": ["1","3","5"]
                },
                {"id_question": 10,
                "answer": ["1","3","5"]
                },
                {"id_question": 11,
                "answer": ["1","3","5"]
                },
                {"id_question": 12,
                "answer": ["1","3","5"]
                },
                {"id_question": 13,
                "answer": ["1","3","5"]
                }
        ]
}
"""
