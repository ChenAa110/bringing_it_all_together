f_name='timg.jpg'

with open(f_name,'rb') as f:
    b=f.read()
    copy_f_name='logo2.png'
    with open(copy_f_name,'wb') as copy_f:
        copy_f.write(b)
        print("复制成功")


