#encoding=utf-8
import os
import sys
import time
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from db_info import db_tpms
from mydb import MysqlControl

class TimelineControl:
    def get_statuses(self, uid, Api):
        # GET /statuses/user_timeline
        # 每次抓取20条
        w_list = list()
        t_list = Api.get.statuses__user_timeline(format="json", name=uid, pageflag=0, pagetime=0, reqnum=20,
                                                 lastid=0, type=0, contenttype=0x80)
        time.sleep(3.6)
        if t_list.data is None:
            curTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            print "%s no statuses list! %s" % (uid, curTime)
            return []
        else:
            w_list.extend(t_list.data.info)
            msc = MysqlControl()
            msc.insert_r_list(100, w_list, uid)
            return w_list