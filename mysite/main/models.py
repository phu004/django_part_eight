from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    upi = models.CharField(max_length=10, default="")
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(Person, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

class MockedLoginUser(models.Model):
    name = models.CharField(max_length=200)
    upi = models.CharField(max_length=10, default="")



