from django.urls import path
from . import views

urlpatterns = [
    #path('register/', views.register_view, name="register"),
	#path('login/', views.login_view, name="login"),
	#path('logout/', views.logout_view, name="logout"),


    path('', views.home_view, name="home"),
    path('adding_student/', views.adding_student_view, name="adding_student"),
    path('updating_student/<str:pk>/', views.updating_student_view, name="updating_student"),
    path('deleting_student/<str:pk>/', views.deleting_student_view, name="deleting_student"),
    path('student_payment/<str:pk>/', views.student_payment_view, name="student_payment"),
    path('history_of_payment/', views.histories_view, name="history_of_payment"),
    path('records/', views.records_view, name="records"),
    path('user/', views.userPage, name="user"),
]