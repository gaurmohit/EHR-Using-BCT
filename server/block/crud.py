from django.http import JsonResponse as jr
from django.forms.models import model_to_dict
from django.urls import path
from .models import Block
from .apps import Chain
from pprint import pprint
import json


def create_user(request):
    try:
        a = Block.objects.all().order_by('-UserId')[0]
        b = Block(UserId=int(a.UserId) + 1)
        b.save()
        return jr({
            'error': False,
            'message': 'User created with UserId:' + str(b.UserId),
            'result': model_to_dict(b)
        })
    except Exception as e:
        return jr({
            'error': True,
            'message': 'Exception occurred, cant create field'
        })


def fetch(request, uid):
    chain = Chain(Block, uid)
    if len(chain.blocks) == 0:
        return jr({
            'error': True,
            'message': 'The user with uid:' + str(uid) + ' not found'
        })
    return jr({
        'error': False,
        'result': chain.to_list()
    })


def update(request, uid):
    chain = Chain(Block, uid)
    data = json.loads(request.body.decode('utf-8'))
    # pprint()
    chain.add_updates(**data)
    return jr({
        'error': False,
        'result': chain.to_list()
    })


urls = [
    path('create-user/', create_user),
    path('fetch/<int:uid>/', fetch),
    path('update/<int:uid>/', update)
]
