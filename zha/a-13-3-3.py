import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="静态图片控制", size=(300, 300), pos=(100, 100))
        self.panel = wx.Panel(parent=self)

        self.bmps = [wx.Bitmap('D:/project/learned without teacher/zha/0.gif', wx.BITMAP_TYPE_GIF),
                     wx.Bitmap('D:/project/learned without teacher/zha/timg.gif', wx.BITMAP_TYPE_GIF)]
        b1 = wx.Button(self.panel, id=1, label='Button1')
        b2 = wx.Button(self.panel, id=2, label='Button2')
        self.Bind(wx.EVT_BUTTON, self.on_click, id=1, id2=2)

        self.image = wx.StaticBitmap(self.panel, bitmap=self.bmps[1])

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(b1, proportion=1, flag=wx.EXPAND, border=5)
        vbox.Add(b2, proportion=1, flag=wx.EXPAND, border=5)
        vbox.Add(self.image, proportion=3, flag=wx.EXPAND, border=5)
        self.panel.SetSizer(vbox)

    def on_click(self, event):
        eventid = event.GetId()
        if eventid == 1:
            self.image.SetBitmap(self.bmps[1])
        else:
            self.image.SetBitmap(self.bmps[0])
        self.panel.Layout()



app = wx.App()
frm = MyFrame()
frm.Show()

app.MainLoop()
