from datetime import datetime, timedelta
from django.http import JsonResponse, HttpResponse
from .models import Block
from threading import Thread
from collections import deque
import random
import string
import time
from .anonymous.dataframe_anoymizer import anonymize
from .apps import Chain


processes = deque([])  # {request: request, df, type, pk}
processing = {}
finished = {}
status = {
    'running': False,
    'threadObject': None,
    'forceStop': False,
    'ids': {}
}

print(type(finished))


class ProcessThread(Thread):
    @classmethod
    def status(cls, pk):
        if pk in finished:
            return 1
        if pk in processing:
            return 2
        if len(list(filter(lambda x: x['id'] == pk, processes))) != 0:
            return 3
        return 4

    @classmethod
    def generateKey(cls):
        letters = string.ascii_lowercase
        while True:
            x = ''.join(random.choice(letters) for i in range(10))
            if cls.status(x) == 4:
                return x

    @classmethod
    def startProcess(cls):
        if status['threadObject'] is not None and status['threadObject'].is_alive():
            # print(status['threadObject'])
            return
        else:
            th = ProcessThread()
            th.start()
            status['threadObject'] = th

    def run(self):
        try:
            while status['forceStop'] is False and len(processes) != 0:
                print("I am inside", processes, processing, finished)

                process = processes.popleft()
                processing[process['id']] = process
                df = Block.prepare(process['df'], process['type'])
                df = anonymize(df, process['type'])
                # print("Got result", df.iloc[:2, :].head())
                del processing[process['id']]
                res = {'result': df}
                res.update(process)
                finished[process['id']] = res

                for pid in finished:
                    if finished[pid]['downloaded'] == -1:
                        continue
                    if finished[pid]['downloaded'] > 2:
                        print('Before del', finished.keys(), pid)
                        try:
                            del finished[pid]
                        except Exception as e:
                            pass
                        print('After del', finished.keys())
                        print("-----------")
                    else:
                        time.sleep(2)
                        finished[pid]['downloaded'] += 1

                print("Thread Loop parsed")
        except Exception as e:
            print("An error occurred", str(e))
        del status['threadObject']
        status['threadObject'] = None


def add_process(request):
    user, t = request.json.get('user', 'all'), request.json.get('type', 'k')
    print('\n' * 4 + ' ... adding process')
    print(user, t)
    if user == 'all':
        t = '123'
    # return

    if t not in ['k', 'l', 't']:
        return JsonResponse({
            'error': True,
            'message': 'Invalid type(k/l/t)/user(id/all)'
        })
    process = {}
    if user == 'all':
        process = {
            'df': Chain.compile_all(),
            'id': ProcessThread.generateKey(),
            'type': t
        }
    else:
        df = Chain.compile_id(user)
        print(df.head())
        process = {
            'df': df,
            'id': ProcessThread.generateKey(),
            'type': t,
            'downloaded': -1
        }

    processes.append(process)
    ProcessThread.startProcess()
    return JsonResponse({
        'id': process['id']
    })


def get_status(request):
    print('\n' * 4 + ' ... getting status')

    ProcessThread.startProcess()
    pid = request.GET.get('id', None)
    print(pid, finished.keys(), processing.keys())
    # print("I am inside", processes, processing, finished)

    if pid is None:
        print(processes, processing, finished)
        return JsonResponse({
            'error': True,
            'message': 'Please provide a process id'
        })
    else:
        return JsonResponse({
            'error': False,
            'status': ProcessThread.status(pid)
        })


def download_finished(request):
    pid = request.GET.get('id', None)
    if pid is None:
        print(processes, processing, finished)
        return JsonResponse({
            'error': True,
            'message': 'Please provide a process id'
        })
    else:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=filename.csv'
        result = finished[pid]['result']
        result.to_csv(path_or_buf=response,
                      float_format='%.2f')
        finished[pid]['downloaded'] = 0
        # del finished[pid]
        # del processing[pid]
        return response


def intOrNone(i):
    try:
        return int(i)
    except Exception as e:
        return None


def some_users(request):
    obj = list(Block.objects.all()[
        intOrNone(request.GET.get('start', None)):
        intOrNone(request.GET.get('end', None))
    ].values('id', 'UserId'))
    print(obj[0])
    ProcessThread.startProcess()
    return JsonResponse(obj, safe=False)


def download_data(request):
    ProcessThread.startProcess()

    return JsonResponse({
        'K': {
            'available': [
                {
                    'created_on': str(datetime.now() - timedelta(days=3)),
                    'num_entries': 0,
                    'size': 0,
                    'url': 'http://localhost:8000'
                }
            ]
        },
        'L': {
            'available': []
        },
        'T': {
            'available': []
        }
    })
