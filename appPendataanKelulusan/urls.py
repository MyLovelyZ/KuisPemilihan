# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserManageViewSet, QuestionViewSet, SubmitQuizView

router = DefaultRouter()
router.register(r'users', UserManageViewSet, basename='user-manage')
router.register(r'questions', QuestionViewSet, basename='question')

urlpatterns = [
    # Endpoint Autentikasi (Login untuk dapat Token)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Endpoint Aplikasi
    path('api/', include(router.urls)),
    path('api/quiz/submit/', SubmitQuizView.as_view(), name='quiz-submit'),
]