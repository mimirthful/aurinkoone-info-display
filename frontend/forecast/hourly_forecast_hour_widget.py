import wx
from frontend import show_svg_image


class HourlyForecastHourWidget(wx.Panel):
    def __init__(self, parent: wx.Window, info_function):
        super().__init__(parent, id=wx.ID_ANY)
        # weather widget
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        sizer.SetMinSize(wx.Size(100, 100))
        # info to be shown
        info = info_function
        hour_label = info["hour"]
        text_label = info["label"]
        img_src = info["image"]

        # content
        hour = wx.StaticText(self, wx.ID_ANY, hour_label)
        image = show_svg_image(self, img_src, 64)
        label = wx.StaticText(self, wx.ID_ANY, text_label)

        sizer.Add(hour, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)
        sizer.Add(image, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)
        sizer.Add(label, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)
