# permissions.py
from rest_framework import permissions

class IsSuperAdmin(permissions.BasePermission):
    """Hanya untuk Super Admin (bisa hapus/ban user)"""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'superadmin')

class IsAdmin(permissions.BasePermission):
    """Hanya untuk Admin (bisa CRUD soal) atau Super Admin"""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role in ['admin', 'superadmin'])

class IsNormalUser(permissions.BasePermission):
    """Hanya untuk User biasa yang tidak di-banned (bisa ikut kuis)"""
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.role == 'user' and not user.is_banned)