from django.urls import path, include
# from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage, TaskReorder
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, SignUpView, TaskReorder, RegisterPage

from django.contrib.auth.views import LogoutView
from . import views


# from django.urls import path
# from account.api.views import(
#   registration_view,
# )

# from rest_framework.authtoken.views import obtain_auth_token
# app_name = "account"


from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),


    path('login/', CustomLoginView.as_view(), name='login'),
    path('accounts/login/', CustomLoginView.as_view(), name='accounts-login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    # path('register/', views.register_user, name='register'),

    path("signup/", SignUpView.as_view(), name="signup"),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),

    # path('api/account/login', obtain_auth_token , name="api-login"),
    # path('api/account/register', registration_view, name="api-register"),
]

urlpatterns += staticfiles_urlpatterns()