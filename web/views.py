from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from web.controller.service import *
import json
from web.bean.run_mystic_tool import *
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
    try:
        num = request.GET.get('num')
        secret_key = request.GET.get('secret_key')
        name = request.GET.get('name')
        date = request.GET.get('date')
        start_time = request.GET.get('start_time')
        end_time = request.GET.get('end_time')
        result = do_search(num, secret_key, name, date, start_time, end_time)
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
        num = request.POST.get('num')
        secret_key = request.POST.get('secret_key')
        seat_name = request.POST.get('seat_name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        result = do_subscribe(num, secret_key, seat_name, start_time, end_time)
    except Exception as e:
        print('subscribe_error')
        print(e)
        result = {
            'msg': '预约服务异常',
            'statues': 0
        }
    return HttpResponse(json.dumps(result), content_type="application/json")

@csrf_exempt
def mystic_tool(request):
    try:
        num = request.POST.get('num')
        secret_key = request.POST.get('secret_key')
        name = request.POST.get('name')
        email = request.POST.get('mail')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        result = do_mystic_tool(num, secret_key, name, start_time, end_time,email)
    except Exception as e:
        print('mystic_tool_error')
        print(e)
        result = {
            'msg': '特殊工具异常',
            'statues': 0
        }
    return HttpResponse(json.dumps(result), content_type="application/json")




