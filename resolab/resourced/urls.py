from resourced.api import views
from django.urls import include, path
from rest_framework import routers

app_name = "resource"

'''router = routers.DefaultRouter()
router.register(r'users', views.UserListCreate.as_view())
router.register(r'usersupdate', views.UserRetrieveDestroyUpdate.as_view())
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]'''

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('new_user/', views.RegisterNewUser.as_view()),
    path('users/<int:pk>/', views.UserRetrieveDestroyUpdate.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]