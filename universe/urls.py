from rest_framework.routers import DefaultRouter

from django.urls import path, include

from universe.views import QuizletViewSet, PlanetViewSet, QuestionViewSet, UserAnswerViewSet, AnswerViewSet, \
    QuestionWithAnswerViewSet, AlphabetViewSet

router = DefaultRouter()

router.register("quizlet", QuizletViewSet, basename="quizlet"),
router.register("planet", PlanetViewSet, basename="planet"),
router.register("question", QuestionViewSet, basename="question"),
router.register("answer", AnswerViewSet, basename="answer"),
router.register("user_answer", UserAnswerViewSet, basename="user_answer"),
router.register("question_with_answer", QuestionWithAnswerViewSet, basename="question_with_answer")
router.register("alphabet", AlphabetViewSet, basename="alphabet")


urlpatterns = [path("", include(router.urls))]

app_name = "universe"
