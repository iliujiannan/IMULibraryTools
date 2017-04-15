import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IMULibraryTools.settings")# project_name 项目名称
django.setup()

from web.models import *
from web.bean.library_service import *
import web.models
import time



def do_run_mystic_tool():
    student_info_list = call_get_seat_infor_list('', '', '')['data']
    if (len(student_info_list) > 0):
        m = Mystic.objects.filter(is_ok=0).all()
        print(len(m))
        for i in m:
            if datetime.datetime.strptime(i.end_time, '%Y-%m-%d %H:%M')<datetime.datetime.now():
                i.is_ok = 1
                i.save()
        for i in m:
            name = i.tar_name
            fs = web.models.Student.objects.filter(student_id=i.student_id).first()
            for j in range(0, len(student_info_list) - 1):
                if (student_info_list[j].name == name):
                    dev_name = int(str(student_info_list[j].dev_name).split('-')[1])
                    search_list = []
                    if dev_name % 4 == 1:
                        str1 = str(student_info_list[j].dev_name).split('-')[0] + '-{:0>3}'.format(str(dev_name + 1))
                        search_list.append(str1)
                        str1 = str(student_info_list[j].dev_name).split('-')[0] + '-{:0>3}'.format(str(dev_name + 2))
                        search_list.append(str1)
                        str1 = str(student_info_list[j].dev_name).split('-')[0] + '-{:0>3}'.format(str(dev_name + 3))
                        search_list.append(str1)
                    else:
                        if dev_name % 4 == 2:
                            str1 = str(student_info_list[j].dev_name).split('-')[0] + '-{:0>3}'.format(
                                str(dev_name - 1))
                            search_list.append(str1)
                            str1 = str(student_info_list[j].dev_name).split('-')[0] + '-{:0>3}'.format(
                                str(dev_name + 2))
                            search_list.append(str1)
                            str1 = str(student_info_list[j].dev_name).split('-')[0] + '-{:0>3}'.format(
                                str(dev_name + 1))
                            search_list.append(str1)
                        else:
                            if dev_name % 4 == 3:
                                str1 = str(student_info_list[j].dev_name).split('-')[0] + '-{:0>3}'.format(
                                    str(dev_name + 1))
                                search_list.append(str1)
                                str1 = str(student_info_list[j].dev_name).split('-')[0] + '-{:0>3}'.format(
                                    str(dev_name - 2))
                                search_list.append(str1)
                                str1 = str(student_info_list[j].dev_name).split('-')[0] + '-{:0>3}'.format(
                                    str(dev_name - 1))
                                search_list.append(str1)
                            else:
                                str1 = str(student_info_list[j].dev_name).split('-')[0] + '-{:0>3}'.format(
                                    str(dev_name - 1))
                                search_list.append(str1)
                                str1 = str(student_info_list[j].dev_name).split('-')[0] + '-{:0>3}'.format(
                                    str(dev_name - 2))
                                search_list.append(str1)
                                str1 = str(student_info_list[j].dev_name).split('-')[0] + '-{:0>3}'.format(
                                    str(dev_name - 3))
                                search_list.append(str1)
                    for k in search_list:
                        for l in student_info_list:
                            if l.dev_name == k:
                                search_list.remove(k)
                    for k in search_list:
                        fsea = web.models.Seat.objects.filter(seat_name=k).first()
                        res = subscribe(fs.num, fs.password, fsea.seat_id, datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), student_info_list[j].open_end)
                        if res['statues'] == 1:
                            i.is_ok = 1
                            i.save()
                            break
                #         发送邮件
                else:
                    continue
    else:
        return

if __name__ == '__main__':
    while 1:
        do_run_mystic_tool()
        time.sleep(60)

