from django.contrib import admin
from django.urls import path
from .views import LoginView, RegisterView, UserView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view())
    # path('upload/',)
    # path('logout/', LogoutView.as_view())
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
