from rest_framework import permissions

class IsCaptainOfTeam(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.is_captain and user.team == obj  # Проверяем, является ли пользователь капитаном и относится ли к команде объекта

