from web.models import Student, Subscribe, Search, Seat
from web.bean.library_service import *
from web.bean.secretkey import get_secret_key


def do_login(num, psw):
    s = Student.objects.get(num=num,psw=psw)
    if s is not None:
        s.secret_key = get_secret_key()
        s.save()
        statues = 1
        msg = 'OK'
    else:
        statues = 0
        msg = '同户名密码错误'
    result = {
        'statues': statues,
        'msg': msg
    }
    return result


def do_search(student_id, secret_key, name, date, start_time, end_time):
    fs = Student.objects.filter(student_id=student_id,secret_key=secret_key).first()
    if fs:
        s = Search()
        s.student_id = student_id
        s.name = name
        s.save()
        info_list = call_get_seat_infor_list(date, start_time, end_time)
        res_list = []
        if(len(info_list)>0):
            for i in len(info_list):
                if(info_list[i].name=='name'):
                    # if()
                    res_list.append(info_list[i])
                    result = {
                        'data': res_list,
                        'statues': 1,
                        'msg': 'OK'
                    }
                    return result
        result = {
            'data': res_list,
            'statues': 0,
            'msg': '未查询到'
        }
    else:
        result = {
            'data': None,
            'statues': 0,
            'msg': '请登录'
        }
    return result


def do_subscribe(student_id, secret_key, seat_name, start_time, end_time):
    fs = Student.objects.filter(student_id=student_id, secret_key=secret_key).first()
    if fs:
        s = Student.objects.get(student_id=student_id)
        st = Seat.objects.filter(seat_name=seat_name).first()
        if st:
            num = s.num
            psw = s.password
            sb = Subscribe()
            sb.student_id = student_id
            sb.start_time = start_time
            sb.end_time = end_time
            sb.save()
            result = subscribe(num, psw, st.dev_id, start_time, end_time)
            return result
        else:
            result = {
                'statues': 0,
                'msg': '请输入正确座位号'
            }
            return result
    else:
        result = {
            'statues': 0,
            'msg': '请登录'
        }
        return result
