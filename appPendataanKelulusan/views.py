from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser, Question, QuizResult
from .serializers import UserSerializer, QuestionSerializer, QuizResultSerializer
from .permissions import IsSuperAdmin, IsAdmin, IsNormalUser

# --- ENDPOINT SUPER ADMIN ---
class UserManageViewSet(viewsets.ModelViewSet):
    """
    Super Admin dapat melakukan CRUD pada User.
    Bisa mengubah is_banned menjadi True atau menghapus user (DELETE).
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperAdmin] # Kunci keamanan: Hanya Super Admin

# --- ENDPOINT ADMIN ---
class QuestionViewSet(viewsets.ModelViewSet):
    """
    Admin dapat menambahkan, mengubah, atau menghapus soal kuis.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdmin] # Kunci keamanan: Hanya Admin & Super Admin

# --- ENDPOINT USER BIASA ---
class SubmitQuizView(APIView):
    """
    User biasa submit hasil kuis di sini.
    """
    permission_classes = [IsNormalUser] # Kunci keamanan: Hanya User tidak di-banned

    def post(self, request):
        # Dalam aplikasi nyata, kamu akan menerima array jawaban dan menghitungnya di sini.
        # Untuk contoh ini, mari kita asumsikan frontend mengirimkan total poin yang didapat 
        # (atau kamu menghitungnya secara internal).
        total_points = request.data.get('total_points', 0)
        
        try:
            total_points = int(total_points)
        except ValueError:
            return Response({"error": "Poin harus berupa angka."}, status=status.HTTP_400_BAD_REQUEST)

        # Logika Penilaian (Sesuai permintaanmu)
        if 50 <= total_points <= 70:
            grade = 'A'
        elif 71 <= total_points <= 90:
            grade = 'B'
        else:
            # Fallback jika poin di luar rentang tersebut
            grade = 'Lainnya' 

        # Simpan hasil ke database
        result = QuizResult.objects.create(
            user=request.user,
            total_points=total_points,
            grade=grade
        )

        serializer = QuizResultSerializer(result)
        return Response({
            "message": "Kuis berhasil diselesaikan!",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)