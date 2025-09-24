# urls

from django.urls import path    # pylint: disable=E0401

from . import views

# this key is used when you refer an endpoint by `reverse`
app_name = "django_gauth"  # pylint: disable=C0103

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("login-callback", views.callback, name="callback"),
]

# NOTE : `/` at the end of the route will be taken in cosideration while redirected .
# # if you have strict slashes issues , do take care where to put the `/` or not .
