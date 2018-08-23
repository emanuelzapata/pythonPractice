import wx

#app = wx.App()
"""
frame = wx.Frame(None, -1, 'Main')
frame.Show()

app.MainLoop()
"""
class windowClass(wx.Frame):
    def __init__(self, parent, title):
        super(windowClass, self).__init__(parent,title=title, size=(800,600))

        self.Centre
        self.Show()

app = wx.App()
windowClass(None, title="Main")
app.MainLoop()
