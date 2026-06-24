import wx
from backend.weather import get_temperature
from frontend import show_svg_image


class MainTempPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(sizer)

        weather_info = get_temperature("now")

        temperature_label = weather_info["label"]
        font = wx.Font(pointSize=60, family=wx.FONTFAMILY_DECORATIVE,
                       style=wx.FONTSTYLE_NORMAL, weight=wx.FONTWEIGHT_SEMIBOLD)
        temperature = wx.StaticText(self, wx.ID_ANY, f'{temperature_label}')
        temperature.SetFont(font)

        icon = weather_info["image"]
        svg_icon = show_svg_image(self, f'{icon}', 256)

        sizer.Add(temperature, 1, flag=wx.ALIGN_CENTRE_VERTICAL |
                  wx.ALL, )
        sizer.Add(svg_icon, 1, flag=wx.ALIGN_CENTRE_VERTICAL |
                  wx.ALL,)
