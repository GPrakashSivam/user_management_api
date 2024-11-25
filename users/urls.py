from django.urls import path
from .views import UserCreateView, UserDetailView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='create_user'), # POST /users
    # GET, PUT, DELETE /users/<user_id>
    path('users/<str:user_id>', UserDetailView.as_view(), name='user_detail'),
]