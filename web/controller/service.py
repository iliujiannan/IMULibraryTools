from web.models import Student, Subscribe, Search, Seat
import web.models
from web.bean.library_service import *
from web.bean.secretkey import get_secret_key
import datetime


def do_login(num, psw):
    s = web.models.Student.objects.filter(num=num,password=psw).first()
    if s is not None:
        secret_key = get_secret_key()
        s.secret_key = secret_key
        s.save()
        statues = 1
        msg = 'OK'
    else:
        statues = 0
        msg = '同户名密码错误'
        secret_key = ''
    result = {
        'statues': statues,
        'msg': msg,
        'secret_key': secret_key
    }
    return result


def do_search(num, secret_key, name, date, start_time, end_time):
    fs = web.models.Student.objects.filter(num=num,secret_key=secret_key).first()
    if fs:

        s = Search()
        s.student_id = fs.student_id
        s.name = name
        s.search_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        s.save()
        info_list = call_get_seat_infor_list(date, start_time, end_time)['data']
        res_list = []
        if(len(info_list)>0):
            for i in range(0, len(info_list)-1):
                if(info_list[i].name == name):
                    array = {
                        'name': name,
                        'dev_name': info_list[i].dev_name,
                        'open_start': info_list[i].open_start,
                        'open_end': info_list[i].open_end
                    }
                    res_list.append(array)
                    dev_name = int(str(info_list[i].dev_name).split('-')[1])
                    search_list = []
                    if dev_name % 4 == 1:
                        str1 = str(info_list[i].dev_name).split('-')[0]+ '-{:0>3}'.format(str(dev_name+1))
                        search_list.append(str1)
                        str1 = str(info_list[i].dev_name).split('-')[0] + '-{:0>3}'.format(str(dev_name + 2))
                        search_list.append(str1)
                        str1 = str(info_list[i].dev_name).split('-')[0] + '-{:0>3}'.format(str(dev_name + 3))
                        search_list.append(str1)
                    else:
                        if dev_name % 4 == 2:
                            str1 = str(info_list[i].dev_name).split('-')[0] + '-{:0>3}'.format(str(dev_name - 1))
                            search_list.append(str1)
                            str1 = str(info_list[i].dev_name).split('-')[0] + '-{:0>3}'.format(str(dev_name + 1))
                            search_list.append(str1)
                            str1 = str(info_list[i].dev_name).split('-')[0] + '-{:0>3}'.format(str(dev_name + 2))
                            search_list.append(str1)
                        else:
                            if dev_name % 4 == 3:
                                str1 = str(info_list[i].dev_name).split('-')[0] + '-{:0>3}'.format(str(dev_name - 1))
                                search_list.append(str1)
                                str1 = str(info_list[i].dev_name).split('-')[0] + '-{:0>3}'.format(str(dev_name + 1))
                                search_list.append(str1)
                                str1 = str(info_list[i].dev_name).split('-')[0] + '-{:0>3}'.format(str(dev_name - 2))
                                search_list.append(str1)
                            else:
                                str1 = str(info_list[i].dev_name).split('-')[0] + '-{:0>3}'.format(str(dev_name - 1))
                                search_list.append(str1)
                                str1 = str(info_list[i].dev_name).split('-')[0] + '-{:0>3}'.format(str(dev_name - 3))
                                search_list.append(str1)
                                str1 = str(info_list[i].dev_name).split('-')[0] + '-{:0>3}'.format(str(dev_name - 2))
                                search_list.append(str1)
                    for j in search_list:
                        for k in info_list:
                            if j == k.dev_name:
                                array = {
                                    'name': k.name,
                                    'dev_name': k.dev_name,
                                    'open_start': k.open_start,
                                    'open_end': k.open_end
                                }
                                search_list.remove(j)
                                res_list.append(array)
                    for l in search_list:
                        array = {
                            'name': '',
                            'dev_name': l,
                            'open_start': '',
                            'open_end': ''
                        }
                        res_list.append(array)
                    result = {
                        'data': res_list,
                        'statues': 1,
                        'msg': 'OK'
                    }
                    return result
        result = {
            'data': [],
            'statues': 0,
            'msg': '未查询到'
        }
    else:
        result = {
            'data': [],
            'statues': 0,
            'msg': '请登录'
        }
    return result


def do_subscribe(num, secret_key, seat_name, start_time, end_time):
    fs = web.models.Student.objects.filter(num=num, secret_key=secret_key).first()
    if fs:
        st = Seat.objects.filter(seat_name=seat_name).first()
        if st:
            num = fs.num
            psw = fs.password
            print(fs.num)
            sb = web.models.Subscribe()
            sb.student_id = fs.student_id
            sb.start_time = start_time
            sb.end_time = end_time
            sb.save()
            result = subscribe(num, psw, st.seat_id, start_time, end_time)
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


def do_mystic_tool(num, secret_key, name, start_time, end_time, mail):
    fs = web.models.Student.objects.filter(num=num, secret_key=secret_key).first()
    if fs:
        m = web.models.Mystic()
        m.student_id = fs.student_id
        m.tar_name = name
        m.start_time = start_time
        m.end_time = end_time
        m.mail = mail
        m.save()
    else:
        result = {
            'statues': 0,
            'msg': '请登录'
        }
        return result