import datetime

# 現在の日時を取得する
now = datetime.datetime.now()
print(now)
# 以下は国際規格の表示
print(now.isoformat())
# 自分の好きなフォーマットで表示したい場合は次の通り
# %d : 日 %m : 月 %y : 年（2桁） %H : 時 %M : 分 %S : 秒 %f : マイクロ秒秒
print(now.strftime('%d/%m/%y-%H%M%S%f'))

# 年月日の取得は以下の通り
today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

# 時刻を作成する
t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S_%f'))

#一週間前を求める
print(now)
d = datetime.timedelta(weeks=1)
# d = datetime.timedelta(days=365)
# d = datetime.timedelta(hours=1)
# d = datetime.timedelta(minutes=1)
# d = datetime.timedelta(seconds=1)
# d = datetime.timedelta(microseconds=1)
print(now - d)

import time

# print("###")
# 以下のように書くと2秒止めることができる
# time.sleep(2)
# print("###")
# 1970年1月1日からの時間を出すには以下の通り
# print(time.time())

# ファイルのバックアップを取る
import os
import shutil

file_name = 'test.txt'

if os.path.exists(file_name):
    shutil.copy(file_name, "{},{}".format(
        file_name, now.strftime('%Y_%m_%d_%H_%M_%S')
    ))

with open(file_name, 'w') as f:
    f.write('test')