import urllib.request

url='https://image.baidu.com/'

req=urllib.request.Request(url)
with urllib.request.urlopen(url) as response:
    data=response.read()
    # print(data)
    f_name='img.peg'
    with open(f_name,'wb')as f:
        f.write(data)
        print('下载成功')