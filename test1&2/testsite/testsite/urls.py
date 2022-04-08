"""testsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#import other views.py
from todo import views as views1

urlpatterns = [
    path('admin/', admin.site.urls),

### todo app
	path('',views1.index, name='index'),
	path('login/',views1.login, name='login'),
	path('register/',views1.register, name='register'),
	path('register2/',views1.register2, name='register2'),
	path('todo_main/',views1.todo_main, name='todo_main'),
	path('logout/',views1.logout, name='logout'),
	path('todo_add/',views1.todo_add, name='todo_add'),	
	path('todo_add2/',views1.todo_add2, name='todo_add2'),
	path('todo_edit/<int:object_id>/',views1.todo_edit, name='todo_edit'),
	path('todo_delete/<int:object_id>/',views1.todo_delete, name='todo_delete'),
	path('todo_finish/<int:object_id>/',views1.todo_finish, name='todo_finish'),
	path('todo_edit2/<int:object_id>/',views1.todo_edit2, name='todo_edit2'),
	path('testmail/',views1.testmail, name='testmail'),
]

	
	
	
