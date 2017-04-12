from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from web.controller.service import *
# Create your views here.


@csrf_exempt
def login(request):
    result = {}
    try:
        num = request.POST.get('num')
        psw = request.POST.get('psw')
        result = do_login(num, psw)
    except Exception as e:
        print('login_error')
        print(e)
        result = {
            'msg': '登录服务异常',
            'statues': 0
        }
    return HttpResponse(json.dumps(result), content_type="application/json")

@csrf_exempt
def search(request):
    result = {}
    try:
        student_id = int(request.GET.get('student_id'))
        secret_key = request.GET.get('secret_key')
        name = request.GET.get('name')
        date = request.GET.get('date')
        start_time = request.GET.get('start_time')
        end_time = request.GET.get('end_time')
        result = do_search(student_id, secret_key, name, date, start_time, end_time)
    except Exception as e:
        print('search_error')
        print(e)
        result = {
            'msg': '查询服务异常',
            'statues': 0
        }
    return HttpResponse(json.dumps(result), content_type="application/json")

@csrf_exempt
def subscribe(request):
    try:
        student_id = request.POST.get('student_id')
        secret_key = request.POST.get('secret_key')
        seat_name = request.POST.get('seat_name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        result = do_subscribe(student_id, secret_key, seat_name, start_time, end_time)
    except Exception as e:
        print('subscribe_error')
        print(e)
        result = {
            'msg': '预约服务异常',
            'statues': 0
        }
    return HttpResponse(json.dumps(result), content_type="application/json")



