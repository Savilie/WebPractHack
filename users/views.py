from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .permissions import CanEditTeammateProfile
from .serializers import CustomUserSerializer

# Create your views here.

class CustomUserAPIView(APIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()

    def get(self, request):
        cu = CustomUser.objects.all()
        team_id = self.request.query_params.get('team_id')

        if team_id:
            cu = cu.filter(team_id=team_id)

        return Response({'users': CustomUserSerializer(cu, many=True).data})

    def patch(self, request, pk, *args, **kwargs):
        user = request.user

        if not pk:
            return Response({"error": "Patch method is not allowed"})

        try:
            instance = CustomUser.objects.get(pk=pk)

            if user.is_captain and user.team_id==instance.team_id:
                pass
            else:
                return Response({"error": "Different teams"})
        except CustomUser.DoesNotExist:
            return Response({"error": "Object does not exist"})

        serializer = CustomUserSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user": serializer.data})

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def delete(self, request, pk):
        try:
            product = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)