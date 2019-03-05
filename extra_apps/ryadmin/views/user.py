from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


# Create your views here.
def ry_user(request, object_id):
    User = get_user_model()
    user = User.objects.get(id=object_id)
    return render(request, 'admin/user.html', {'user': user})


def ry_logout(request):
    logout(request)
    return redirect('/admin/login/')



