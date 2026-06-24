import wx
from frontend.panels import NotebookWeatherPanel, NotebookBusPanel, NotebookSettingsPanel
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
        page_one = NotebookWeatherPanel(notebook)
        icon_one_bitmap = icons.weather
        icon_one_index = image_list.Add(
            icon_one_bitmap)
        # Page 2
        page_two = NotebookBusPanel(notebook)
        icon_two_bitmap = icons.bus_stop
        icon_two_index = image_list.Add(icon_two_bitmap)
        # Page 3
        page_three = NotebookSettingsPanel(notebook)
        icon_three_bitmap = icons.settings
        icon_three_index = image_list.Add(icon_three_bitmap)
        # Add pages
        notebook.AddPage(page_one, "Weather",
                         True, icon_one_index)
        notebook.AddPage(page_two, "Bus-stops", False, icon_two_index)
        notebook.AddPage(page_three, "Settings", False, icon_three_index)

        # Add to sizer
        sizer.Add(notebook, 1, wx.EXPAND | wx.ALL, border=20)
        sizer.SetSizeHints(self)
        # Show the window
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = FrontFrame("Weather")
    app.MainLoop()
