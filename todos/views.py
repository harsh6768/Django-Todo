from django.shortcuts import render,redirect
from todos.models import Todo
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
     
    #to get the all todos
    todos=Todo.objects.all()

    return render(request,'index.html',{'todos':todos})

def addTodo(request):

    #to get the data from post method
    title=request.POST['title']
    desc=request.POST['description']

    todo=Todo()
    todo.title=title
    todo.description=desc
    
    print('>>>>>>>')
    print(title)
    print(desc)
    #to save the data into the postgres
    todo.save();
    # return HttpResponseRedirect('')
    return redirect('/')

def editTodo(request,todo_id):

    item_to_edit=Todo.objects.get(id=todo_id)
    print('>>>>>>>>>>>>>>>>...title')
    print(item_to_edit)

    #redirecting to the home page
    return redirect('/')


def deleteTodo(request,todo_id):

    item_to_delete=Todo.objects.get(id=todo_id)
    item_to_delete.delete()

    # return HttpResponseRedirect('')
    #to redirect the data
    return redirect('/')



