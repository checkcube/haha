from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Problem
from .serializers import ProblemSerializer

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # 로그를 추가하여 author가 올바르게 설정되는지 확인
        import logging
        logging.debug(f"Creating problem with data: {serializer.validated_data}")
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def approved(self, request):
        difficulty = request.query_params.get('difficulty', None)
        if difficulty:
            approved_problems = Problem.objects.filter(approved=True, difficulty=difficulty)
        else:
            approved_problems = Problem.objects.filter(approved=True)
        serializer = self.get_serializer(approved_problems, many=True)
        return Response(serializer.data)
