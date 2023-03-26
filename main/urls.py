from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("opportunity/", views.opport, name="opportExc"),
    path("opportunity/university", views.opportUniv, name="opportUniv"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit", views.edit, name="edit"),
    path("opportunity/company1", views.company1, name="company"),
    path("signup/", views.signup, name="signup"),
    path('login/', views.login, name='login'),
    path("logout/", views.logout, name="logout"),
]