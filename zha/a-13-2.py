import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="布局管理器嵌套", size=(300, 120), pos=(100, 100))
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel, label='请点击按钮', pos=(110, 20))
        b1 = wx.Button(parent=panel, id=10, label='Botton1', pos=(100, 50))
        b2 = wx.Button(parent=panel, id=11, label='Botton2', pos=(100, 50))

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(b1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hbox.Add(b2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(self.statictext, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE | wx.TOP, border=10)
        vbox.Add(hbox, proportion=1, flag=wx.CENTER)
        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.on_click, id=10,id2=20)

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
