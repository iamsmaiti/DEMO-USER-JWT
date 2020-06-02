from django.urls import path
from .views import CreateUserAPIView  # UserRetrieveUpdateAPIView
from .views import authenticate_user


urlpatterns = [
    path('create/', CreateUserAPIView.as_view() , name="create"),
    #path('update/', UserRetrieveUpdateAPIView.as_view()),
    path('obtain_token/', authenticate_user),
    
]