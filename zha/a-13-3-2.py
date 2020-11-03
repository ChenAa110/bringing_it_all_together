import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="列表", size=(350, 175), pos=(100, 100))
        panel = wx.Panel(parent=self)

        st1 = wx.StaticText(panel, label='选择你喜欢的编程语言!')
        list1 = ['Python', 'C++', 'Java']
        lb1 = wx.ListBox(panel, choices=list1, style=wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX, self.on_listbox1, lb1)

        st2 = wx.StaticText(panel, label='选择你喜欢的水果!')
        list2 = ['苹果', '橘子', '香蕉']
        lb2 = wx.ListBox(panel, choices=list2, style=wx.LB_EXTENDED)
        self.Bind(wx.EVT_LISTBOX, self.on_listbox2, lb2)

        hbox1 = wx.BoxSizer()
        hbox1.Add(st1, proportion=1, flag=wx.LEFT | wx.RIGHT, border=5)
        hbox1.Add(lb1, proportion=1)

        hbox2 = wx.BoxSizer()
        hbox2.Add(st2, proportion=1, flag=wx.LEFT | wx.RIGHT, border=5)
        hbox2.Add(lb2, proportion=1)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox2, flag=wx.ALL | wx.EXPAND, border=5)
        panel.SetSizer(vbox)

    def on_listbox1(self, event):
        lisbox = event.GetEventObject()
        print('选择{0}'.format(lisbox.GetSelection()))

    def on_listbox2(self, event):
        lisbox = event.GetEventObject()
        print('选择{0}'.format(lisbox.GetSelections()))


app = wx.App()
frm = MyFrame()
frm.Show()

app.MainLoop()
