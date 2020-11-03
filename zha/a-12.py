f = open('text.txt', 'w+')
f.write('no world')
print('创建text文件，world写入')

f = open('text.txt', 'r+')
f.write('no hello')
print('打开text文件，hello覆盖')

f = open('text.txt', 'a')
f.write(' ')
print('打开text文件，文件尾部追加空格')

file = 'D:\\project\\learned without teacher\\zha\\text.txt'
f = open(file, 'a+')
f.write('no world')
print('打开text文件，文件尾部追加world')

f_name = 'text.txt'
f = None
try:
    f = open(f_name)
    print('打开成功')
    content = f.read()
    print(content)
except FileNotFoundError as e:
    print("文件不存在")
except OSError as e:
    print('处理OSError异常')
finally:
    if f is not None:
        f.close()
        print('关闭文件成功')

f_name = 'text.txt'
with open(f_name) as   f:
    content = f.read()
    print(content)
