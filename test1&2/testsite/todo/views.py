from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from todo.models import ToDoList
from datetime import date
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))
	else:
   		return redirect(reverse("todo_main"))
    

def login(request):
	if request.user.is_authenticated:
		return redirect(reverse("todo_main"))
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect(reverse("todo_main"))
		else:
			messages.info(request, "invalid username or password")
			return redirect(reverse("login"))
	return render(request, 'login.html')

def register(request):
	return render(request, 'register.html')

def register2(request):	
	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']
	repassword = request.POST['repassword']
	if password == repassword:
		if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
			messages.info(request,'this username or email already exists')
			return redirect(reverse("register"))
		else:
			add_user = User.objects.create_user(
			username = username,
			password = password,
			email = email
			)
			add_user.save()
			subject1 = "signup success!"
			body1 = "Thank you foe registering to own site."
			send_mail(subject=subject1,message=body1,from_email=settings.EMAIL_HOST_USER,recipient_list=[email])
		messages.info(request,'signup success')
		return redirect(reverse("login"))
	else:
		messages.info(request,'password does not match')
		return redirect(reverse("register"))
	return render(request, 'register.html')

def todo_main(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))
	a1=request.POST.get('a1', "");
	a2=request.POST.get('a2', "");
	today = date.today().strftime("%Y-%m-%d")
	if(a1=="1" or a1==""):
		mode = "today"
		a1 = "1"
		query1 = ToDoList.objects.filter(ToDoList_user_id = request.user.id, ToDoList_date = today).exclude(ToDoList_status = 0)
	if(a1=="2"):
		if(a2==""):
			a2 = today
		mode = "date " + a2
		query1 = ToDoList.objects.filter(ToDoList_user_id = request.user.id, ToDoList_date = a2).exclude(ToDoList_status = 0)
	if(a1=="3"):
		mode = "all"
		query1 = ToDoList.objects.filter(ToDoList_user_id = request.user.id).exclude(ToDoList_status = 0)
	query1 = query1.order_by('ToDoList_status','ToDoList_ID')
	return render(request, 'todo_main.html',{"mode":mode,"a1":a1,"a2":a2,"query":query1})

def logout(request):
	auth.logout(request)
	return redirect(reverse("login"))

def todo_add(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))
	return render(request, 'todo_add.html')

def todo_add2(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))
	title=request.POST.get('a1', "");
	date1=request.POST.get('a2', "");
	description=request.POST.get('a3', "");
	if date1 == "":
		date1 = date.today().strftime("%Y-%m-%d")	
	adder = ToDoList(
		ToDoList_user_id = request.user.id,
		ToDoList_title = title,
		ToDoList_description = description,
		ToDoList_status = 1,
		ToDoList_date = date1,
		)      
	adder.save()
	messages.info(request,'add activity success')
	return render(request, 'todo_add2.html')

def todo_edit(request,object_id):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))
	query1 = ToDoList.objects.filter(ToDoList_user_id = request.user.id, ToDoList_ID = object_id).exclude(ToDoList_status = 0)
	return render(request, 'todo_edit.html',{"activity":query1[0]})

def todo_delete(request,object_id):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))
	delete_activity = ToDoList.objects.get(ToDoList_ID = object_id,ToDoList_user_id = request.user.id)
	delete_activity.ToDoList_status = 0
	delete_activity.save()
	messages.info(request,'delete activity success')
	return render(request, 'todo_add2.html')

def todo_finish(request,object_id):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))
	finish_activity = ToDoList.objects.get(ToDoList_ID = object_id,ToDoList_user_id = request.user.id)
	finish_activity.ToDoList_status = 2
	finish_activity.save()
	messages.info(request,'finish activity')
	return render(request, 'todo_add2.html')

def todo_edit2(request,object_id):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))
	title=request.POST.get('a1', "");
	date1=request.POST.get('a2', "");
	description=request.POST.get('a3', "");
	if date1 == "":
		date1 = date.today().strftime("%Y-%m-%d")	
	edit_activity = ToDoList.objects.get(ToDoList_ID = object_id,ToDoList_user_id = request.user.id)
	edit_activity.ToDoList_title = title
	edit_activity.ToDoList_date = date1
	edit_activity.ToDoList_description = description
	edit_activity.save()
	messages.info(request,'edit activity success')
	return render(request, 'todo_add2.html')

def testmail(request):
	if request.method == "POST":
		a1 = request.POST["a1"]
		a2 = request.POST["a2"]
		a3 = request.POST["a3"]
		send_mail(subject=a2,message=a3,from_email=settings.EMAIL_HOST_USER,recipient_list=[a1])
		messages.info(request,'send mail success')
	return render(request, 'testmail.html')



"""
def checkLogin(request):
	if request.user.id :
		return HttpResponseRedirect(reverse("register"))

"""