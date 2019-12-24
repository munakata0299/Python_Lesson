# Pythonからターミナルコマンドを実行する
import os
import subprocess

# Macの場合は以下のように
# subprocess.run(['ls', '-al'])
# 以下のように書くことも可能
# subprocess.run('ls -al', shell=True)
# Windowsの場合はfind
# 以下のようにパイプを使うこともできるが、セキュリティ的に非推奨
subprocess.run('ls -al | grep test', shell=True)
'''
このようにファイルをすべて消されてしまう可能性もある
cmd = 'rm -rf *'
Windowsの場合はdelコマンド
subprocess.run(cmd, shell=True)

subprocess.run('ls -al', shell=True)
'''

# r = subprocess.run('ls -al', shell=True)
# returncodeは処理が正常にされれば0が返ってきて、
# 正常に実行されなければエラーコードが返ってくる
# print(r.returncode)
# print('###')

# 以下のようにcheck=Trueという引数を渡すと正常に処理されない場合、エラーを出す
# r = subprocess.run('l -al', shell=True, check=True)

p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(
    ['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE
)
p1.stdout.close()
output = p2.communicate()[0]
print(output)

# 以下は古い書き方（非推奨）
# os.system('ls')

# Windowsの場合は以下のように
# subprocess.run(['dir', 'ah'])

