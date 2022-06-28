from django.shortcuts import redirect, render
from to_do_app.forms import TasksForm
from .models import Tasks


def all_tasks(request):
    tasks = Tasks.objects.all()
    form = TasksForm()
    if request.method == "POST":
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"tasks":tasks,'form':form}
    return render(request, "to_do_app/tasks.html",context)

def update_task(request,pk):
    task = Tasks.objects.get(id = pk) 
    if request.method == "POST":
        form = TasksForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TasksForm(instance=task)
    context = {'form':form}
    return render(request,"to_do_app/update.html",context)

def delete_task(request,pk):
    task = Tasks.objects.get(id = pk)
    task.delete()
    return redirect('/')
