from rest_framework.permissions import BasePermission


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_teacher:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_teacher:
            return True
        return False


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_student:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_student:
            return True
        return False
