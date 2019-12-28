from django.urls import path

from apps.accounts import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('remove/<station_abbr>', views.remove_favorite, name='remove_favorite'),
    path('add/<station_abbr>', views.add_favorite, name='add_favorite'),
]
