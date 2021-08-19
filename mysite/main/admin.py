from django.contrib import admin
from .models import ToDoList, Item, Person, MockedLoginUser

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(Person)
admin.site.register(MockedLoginUser)
