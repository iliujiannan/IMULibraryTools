from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from web.controller.service import *
from web.bean.run_mystic_tool import *
from web.bean.JWTest import *
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

@csrf_exempt
def achieve_empty_room(request):
    try:
        zc = str(request.GET.get("zc"))
        xq = str(request.GET.get("xq"))
        jc = str(request.GET.get("jc"))
        j = jwxt()
        data_list1 = j.executeGetEmptyRoomList('002', zc, xq, jc)
        #data_list = [{"jxl": "综合楼", "js": "208", "jslx": "多媒体"}]
        data_list2 = j.executeGetEmptyRoomList('003', zc, xq, jc)
        data_list = data_list1.extend(data_list2)
        if len(data_list1) > 0:
            result = {
                'msg': 'OK',
                'statues': 1,
                'data_list': data_list
            }
            print(len(data_list))
        else:
            result = {
                'msg': '没有空教室',
                'statues': 0,
            }
    except Exception as e:
        print('achieve_empty_room_error')
        print(e)
        result = {
            'msg': '空教室查询异常',
            'statues': 0
        }
    return HttpResponse(json.dumps(result), content_type="application/json")



