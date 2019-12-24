import string

s = """\

Hi $name.

$contents

Have a good day

"""

# テンプレートを作成する（テンプレートとして読み込めば元データを壊さないで分業もできる）
# tはwithステートメントの外でも使うことができる
with open('design/email_template.txt') as f:
    t = string.Template(f.read())
contents = t.substitute(name='Mike', contents='How are you?')
print(contents)

