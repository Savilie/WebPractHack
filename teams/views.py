from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Team
from .permissions import IsCaptainOfTeam
from .serializers import *


# Create your views here.

class TeamAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsCaptainOfTeam]
    queryset = Team.objects.all()  # Установите queryset вашей модели Product

    def get(self, request):
        t = Team.objects.all()

        return Response({'teams': TeamSerializer(t, many=True).data})

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def delete(self, request, pk):
        try:
            product = Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
