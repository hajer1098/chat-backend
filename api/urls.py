from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('', views.getRoutes),

    # Todo URLS
    path("todo/<user_id>/", views.TodoListView.as_view()),
    path("todo-detail/<user_id>/<todo_id>/", views.TodoDetailView.as_view()),


    #Chat URLS
    path("messages/<user_id>/", views.MyInbox.as_view()),
    path("get-messages/<sender_id>/<receiver_id>/", views.GetMessages.as_view()),
    path("send-messages/", views.SendMessage.as_view()),

    #GET_filters_data
    path("profile/<int:pk>", views.ProfileDetails.as_view()),
    path("search/<username>/", views.SearchUser.as_view()),
]
    