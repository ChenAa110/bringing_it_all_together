import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="事件处理", size=(300, 300), pos=(100, 100))
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel, label='请点击按钮', pos=(110, 20))
        b = wx.Button(parent=panel, label='OK', pos=(100, 50))
        self.Bind(wx.EVT_BUTTON, self.on_click, b)

        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(self.statictext, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.FIXED_MINSIZE | wx.TOP, border=30)
        vbox.Add(b, proportion=1, flag=wx.EXPAND | wx.BOTTOM, border=10)
        panel.SetSizer(vbox)

    def on_click(self, event):
        self.statictext.SetLabelText('Hello World')


app = wx.App()
frm = MyFrame()
frm.Show()

app.MainLoop()
