import wx


class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title,
                           size=(800, 800), pos=(100, 100))

        panel = wx.Panel(self, -1, (270, 20), (300, 320),
                         style=wx.SUNKEN_BORDER)
        self.picture = wx.StaticBitmap(panel)
        panel.SetBackgroundColour(wx.WHITE)

        self.images = ['timg.jpg',
                       'feuchtwanger.jpg',
                       'balzac.jpg',
                       'pasternak.jpg',
                       'galsworthy.jpg',
                       'wolfe.jpg',
                       'zweig.jpg']
        authors = ['Leo Tolstoy', 'Lion Feuchtwanger',
                   'Honore de Balzac', 'Boris Pasternak',
                   'John Galsworthy', 'Tom Wolfe',
                   'Stefan Zweig']

        wx.ComboBox(self, -1, pos=(350, 370), size=(150, -1),
                    choices=authors, style=wx.CB_READONLY)
        wx.Button(self, 1, '关 闭', (380, 420))

        self.Bind(wx.EVT_BUTTON, self.OnClose, id=1)
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect)

        self.Center()

    def OnClose(self, event):
        self.Close()

    def OnSelect(self, event):
        item = event.GetSelection()
        self.picture.SetFocus()
        # self.picture.SetBitmap(wx.Bitmap('images/' + self.images[item]))
        self.picture.SetBitmap(wx.Bitmap('D:/project/learned without teacher/zha/'+self.images[item]))

class MyApp(wx.App):
    def OnInit(self):
        dlg = MyDialog(None, -1, 'combobox.py')
        dlg.ShowModal()
        dlg.Destroy()
        return True


app = MyApp(0)
app.MainLoop()