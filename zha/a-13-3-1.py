import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="复选框和单选框", size=(330, 120), pos=(100, 100))
        panel = wx.Panel(parent=self)

        st1 = wx.StaticText(panel, label='选择你喜欢的编程语言!')
        cb1 = wx.CheckBox(panel, id=1, label='Python')
        cb2 = wx.CheckBox(panel, id=2, label='Java')
        cb2.SetValue(True)
        cb3 = wx.CheckBox(panel, id=3, label='C++')
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=1, id2=3)

        st2 = wx.StaticText(panel, label='选择性别：')
        radio1 = wx.RadioButton(panel, id=4, label='男', style=wx.RB_GROUP)
        radio2 = wx.RadioButton(panel, id=5, label='女')
        self.Bind(wx.EVT_RADIOBUTTON, self.on_radiol_click, id=4, id2=5)

        hbox1 = wx.BoxSizer()
        hbox1.Add(st1, flag=wx.LEFT | wx.RIGHT, border=5)
        hbox1.Add(cb1)
        hbox1.Add(cb2)
        hbox1.Add(cb3)

        hbox2 = wx.BoxSizer()
        hbox2.Add(st2, flag=wx.LEFT | wx.RIGHT, border=5)
        hbox2.Add(radio1)
        hbox2.Add(radio2)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1, flag=wx.ALL, border=10)
        vbox.Add(hbox2, flag=wx.ALL, border=10)
        panel.SetSizer(vbox)

    def on_checkbox_click(self, event):
        cb = event.GetEventObject()
        print('选择{0}，状态{1}'.format(cb.Getlabel(), event.IsChecked()))

    def on_radiol_click(self, event):
        rb = event.GetEventObject()
        print('第一组{}被选中'.format(rb.Getlabel()))


app = wx.App()
frm = MyFrame()
frm.Show()

app.MainLoop()
