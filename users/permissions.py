from rest_framework import permissions


class CanEditTeammateProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        teammate = obj  # Объект профиля сокомандника
        # Возвращаем True, если пользователь - капитан и сокомандник принадлежит к его команде
        return user.is_captain and user.team_id == teammate.team_id