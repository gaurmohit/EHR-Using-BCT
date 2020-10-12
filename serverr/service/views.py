from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from threading import Thread
from .models import ThreadManage
import time
from .original import start_anon

# for checking whether the service is up or not


def service(request):
    print(request.auth.user)
    return JsonResponse({
        'status': 'UP',
        'auth': request.auth
    })

# to start the anonymization process


def start(request):
    task = ThreadManage()
    task.save()
    anon = Thread(target=anonymus, args=[task.id])
    anon.setDaemon(True)
    anon.start()
    return JsonResponse({'task_id': task.id})

# for checking the status of the process for the anonymization


def status(request, id):
    try:
        task = ThreadManage.objects.get(pk=id)
    except:
        raise Http404
    return JsonResponse({'task': task.task, 'status': task.status})


def anonymus(id):
    # add the anonymization function here or call the function here
    print("Received task", id)
    try:
        # execute the python script for anonymization
        start_anon()
    except Exception as ex:
        print(ex)
    # mark the test as complete
    task = ThreadManage.objects.get(pk=id)
    task.status = True
    task.save()
    print("Finishing task", id)

# To show all the tasks in the database


def show_all(request):
    task = ThreadManage.objects.all()
    return HttpResponse(task)

# To delete all the tasks in database


def del_all(request):
    task = ThreadManage.objects.all()
    task.delete()
    task.save()
    return HttpResponse("all objects deleted")
