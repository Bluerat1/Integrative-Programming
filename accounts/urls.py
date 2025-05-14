from django.urls import path, include

urlpatterns = [
    path('bisag-unsa/', include ('djoser.urls')),
    path('bisag-unsa/', include('djoser.urls.authtoken')),
]