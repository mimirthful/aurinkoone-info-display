import wx
from frontend.panels import Panel_01


class FrontFrame(wx.Frame):  # inherits wx.Frame
    def __init__(self, windowTitle):
        super().__init__(parent=None, title=windowTitle)
        # panel and sizer
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.panel.SetSizer(self.sizer)
        # Notebook
        self.notebook = wx.Notebook(self.panel, wx.ID_ANY)
        # Page 1
        self.page_one = Panel_01(self.notebook)
        self.notebook.AddPage(self.page_one, "Page One")

        # Add to sizer
        self.sizer.Add(self.notebook, 1, wx.EXPAND)

        # Show the window
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = FrontFrame("Weather")
    app.MainLoop()
