from rest_framework.decorators import action
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import CustomUserSerializer, RegisterSerializer
from .models import CustomUser

class UserProfileViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get', 'put'], permission_classes=[permissions.IsAuthenticated])
    def profile(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = CustomUserSerializer(user)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomUserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response({"detail": "회원가입 성공", "user_id": user.id}, status=status.HTTP_201_CREATED, headers=headers)

