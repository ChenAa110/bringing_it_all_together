import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title="第一个python程序",size=(1020,300),pos=(100,100))
        panel=wx.Panel(parent=self)
        statictext=wx.StaticText(parent=panel,label='Hello World!',pos=(10,10))


app=wx.App()
frm=MyFrame()
frm.Show()

app.MainLoop()