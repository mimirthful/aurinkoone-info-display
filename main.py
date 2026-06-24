import wx
from frontend.panels import Panel_01
from frontend.ui_bitmaps import UiBitmaps


class FrontFrame(wx.Frame):  # inherits wx.Frame
    def __init__(self, windowTitle):
        super().__init__(parent=None, title=windowTitle)
        # panel and sizer
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        panel.SetSizer(sizer)
        # Notebook
        notebook = wx.Listbook(panel, wx.ID_ANY)
        image_list = wx.ImageList(50, 50)
        notebook.AssignImageList(image_list)
        # Icons
        icons = UiBitmaps()

        # Page 1
        page_one = Panel_01(notebook)
        icon_bitmap = icons.weather
        icon_index = image_list.Add(
            icon_bitmap)

        # Add pages
        notebook.AddPage(page_one, "Weather",
                         True, icon_index)

        # Add to sizer
        sizer.Add(notebook, 1, wx.EXPAND | wx.ALL, border=10)
        sizer.SetSizeHints(self)
        # Show the window
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = FrontFrame("Weather")
    app.MainLoop()
