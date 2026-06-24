from .hourly_forecast_hour_widget import HourlyForecastHourWidget
from backend.weather import get_weather
import wx
import wx.lib.scrolledpanel as scrolled


class HourlyForecastPanel(wx.Panel):
    def __init__(self, parent, ):
        super().__init__(parent, size=wx.Size(450, 200))

        sizer = wx.StaticBoxSizer(
            wx.StaticBox(self, label=" Day Forecast"), wx.HORIZONTAL)
        self.SetSizer(sizer)

        self.scroll_panel = scrolled.ScrolledPanel(
            self, size=(wx.Size(450, 200)))
        self.scroll_panel.SetupScrolling()

        sizer.Add(self.scroll_panel)
        child_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.scroll_panel.SetSizer(child_sizer)
        weather_forecast = self.today_weather_forecast()
        for item in weather_forecast:
            child_sizer.Add(
                item, proportion=1, flag=wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=5)

    def today_weather_forecast(self) -> list:
        hours_list = ["now", "1_hours_from_now", "2_hours_from_now",
                      "3_hours_from_now", "4_hours_from_now", "5_hours_from_now",
                      "6_hours_from_now", "7_hours_from_now", "8_hours_from_now",
                      "9_hours_from_now", "10_hours_from_now", "11_hours_from_now"]
        widget_list = []

        for item in hours_list:
            widget_list.append(HourlyForecastHourWidget(
                self.scroll_panel, get_weather.get_temperature(item)))

        return widget_list
