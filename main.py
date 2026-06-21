import wx
from frontend.panels import Panel_01
from frontend.ui_bitmaps import UiBitmaps


class FrontFrame(wx.Frame):  # inherits wx.Frame
    def __init__(self, windowTitle):
        super().__init__(parent=None, title=windowTitle)
        # panel and sizer
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.panel.SetSizer(self.sizer)
        # Notebook
        self.notebook = wx.Listbook(self.panel, wx.ID_ANY)
        self.image_list = wx.ImageList(50, 50)
        self.notebook.AssignImageList(self.image_list)
        # Icons
        self.icons = UiBitmaps()

        # Page 1
        self.page_one = Panel_01(self.notebook)
        self.icon_bitmap = self.icons.weather
        self.icon_index = self.image_list.Add(
            self.icon_bitmap)

        # Add pages
        self.notebook.AddPage(self.page_one, "Weather",
                              True, self.icon_index)

        # Add to sizer
        self.sizer.Add(self.notebook, 1, wx.EXPAND)

        # Show the window
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = FrontFrame("Weather")
    app.MainLoop()
