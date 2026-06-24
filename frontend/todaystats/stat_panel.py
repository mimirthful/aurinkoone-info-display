from .stat_widget import StatWidget
from backend.weather import get_rain_change, get_UV, get_wind_speed
from frontend.ui_bitmaps import UiBitmaps
import wx


class StatPanel(wx.Panel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        bitmaps = UiBitmaps()

        self.SetSizer(sizer)

        # UV
        uv_info = get_UV()
        uv_widget = StatWidget(self, bitmaps.uv, uv_info)

        # Rain change
        rain_info = get_rain_change("now")
        rain_widget = StatWidget(self, bitmaps.umbrella, rain_info)

        # wind speed
        wind_info = get_wind_speed()
        wind_widget = StatWidget(self, bitmaps.wind, wind_info)

        sizer.Add(uv_widget, flag=wx.ALIGN_CENTER |
                  wx.LEFT | wx.RIGHT, border=5)
        sizer.Add(rain_widget, flag=wx.ALIGN_CENTER |
                  wx.LEFT | wx.RIGHT, border=5)
        sizer.Add(wind_widget, flag=wx.ALIGN_CENTER |
                  wx.LEFT | wx.RIGHT, border=5)
