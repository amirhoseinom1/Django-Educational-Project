from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoCreateForm,TodoUpdateForm


def home(request):
    todos = Todo.objects.all()
    return render(request,'home.html',{'todos':todos})

def detail(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request,"detail.html",{"todo":todo})

def delete(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request,"object deleted successfully","success")
    return redirect('home')

def create(request):
    if request.method == "POST":
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd["title"], body=cd["body"], created_at=cd["created_at"])
            messages.success(request,"Todo created successfully","success")
            return redirect('home')
    else:
        form = TodoCreateForm()
    return render(request,'create.html',{"form":form})


def update(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,"Todo updated successfully","success")
            return redirect('detail',todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request,'update.html',{"form":form})
