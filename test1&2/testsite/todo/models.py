from django.db import models

# Create your models here.
class ToDoList(models.Model):
	ToDoList_ID = models.BigAutoField(auto_created=True, primary_key=True)
	ToDoList_user_id = models.CharField(max_length=20 ,null=True)
	ToDoList_title = models.TextField(null=True)
	ToDoList_description = models.TextField(null=True)	
	ToDoList_status = models.IntegerField(null=True)
	ToDoList_date = models.CharField(max_length=20 ,null=True)
	#ToDoList_finishdate = models.IntegerField(null=True)

