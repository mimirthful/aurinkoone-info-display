from .today_forecast_widget import TodayForecastWidget
from backend.weather import get_weather
import wx
import wx.lib.scrolledpanel as scrolled


class ForecastPanel(scrolled.ScrolledPanel):
    def __init__(self, parent, ):
        super().__init__(parent, size=wx.Size(410, 150))
        self.SetupScrolling()
        self.weather_forecast_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.weather_forecast_sizer)

        self.weather_forecast = self.today_weather_forecast()
        for item in self.weather_forecast:
            self.weather_forecast_sizer.Add(
                item, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

    def today_weather_forecast(self) -> list:
        hours_list = ["now", "1_hours_from_now", "2_hours_from_now",
                      "3_hours_from_now", "4_hours_from_now", "5_hours_from_now",
                      "6_hours_from_now", "7_hours_from_now", "8_hours_from_now",
                      "9_hours_from_now", "10_hours_from_now", "11_hours_from_now"]
        widget_list = []

        for item in hours_list:
            widget_list.append(TodayForecastWidget(
                self, get_weather.get_temperature(item)))

        return widget_list
