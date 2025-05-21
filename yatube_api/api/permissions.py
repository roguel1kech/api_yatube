from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    """
    Позволяет редактировать/удалять только автору объекта, 
    всем остальным — только чтение.
    """
    def has_permission(self, request, view):
        return True  # листинг и создание проверяется на уровне view

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user