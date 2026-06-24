from .week_forecast_day_widget import WeekForecastDayWidget
from backend.weather import get_weather
from .week_forecast_title_widget import WeekForecastTitleWidget
import wx


class WeekForecastPanel(wx.Panel):
    def __init__(self, parent, ):
        super().__init__(parent)
        sizer = wx.StaticBoxSizer(
            wx.StaticBox(self, label=" - Week Forecast - "), wx.VERTICAL)
        self.SetSizer(sizer)
        weather_forecast = self.days_weather_forecast(sizer)
        for item in weather_forecast:
            sizer.Add(
                item, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

    def days_weather_forecast(self, sizer) -> list:
        target_days = 7
        widget_list = []
        title = WeekForecastTitleWidget(sizer.GetStaticBox())
        widget_list.append(title)
        widget = WeekForecastDayWidget(sizer.GetStaticBox(), get_weather.get_24_forecast(
            0), True)
        widget_list.append(widget)
        i = 1
        while i < target_days:
            widget = WeekForecastDayWidget(
                sizer.GetStaticBox(), get_weather.get_24_forecast(i), False)
            widget_list.append(widget)
            i = i + 1
        print(widget_list)
        return widget_list
