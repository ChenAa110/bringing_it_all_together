import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="文本输入控制", size=(300, 260), pos=(100, 100))
        panel = wx.Panel(parent=self)

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        userid=wx.StaticText(panel,label='用户ID：')
        pwd=wx.StaticText(panel,label='密码：')
        content=wx.StaticText(panel,label='多行文本')

        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(userid, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(pwd, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc2, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(content, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc3, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(vbox)

        tc1.SetValue('tony')
        tc2.SetValue('123456')
        tc3.SetValue('你想输入什么!')
        print('读取用户ID：{}'.format(tc1.GetValue()))
        print('读取密码：{}'.format(tc2.GetValue()))
        print('读取消息：{}'.format(tc3.GetValue()))

    def on_click(self, event):
        event_id = event.GetId()
        print(event_id)
        if event_id == 10:
            self.statictext.SetLabelText('Botton1单击')
        else:
            self.statictext.SetLabelText('Botton2单击')


app = wx.App()
frm = MyFrame()
frm.Show()

app.MainLoop()
