from django.urls import path
from ryadmin.views import user

urlpatterns = [
    path('ry_user/<path:object_id>/', user.ry_user, name='ry_user'),
    path('ry_logout/', user.ry_logout, name='ry_logout')
]
