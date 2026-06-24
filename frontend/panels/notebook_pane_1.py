import wx
from frontend.forecast import HourlyForecastPanel, WeekForecastPanel
from frontend.todaystats import MainTempPanel, StatPanel


class NotebookPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        # Notebook panel's main sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        # Lower and half sizers
        upper_half_sizer = wx.GridBagSizer(10, 10)
        maintemp_panel = MainTempPanel(self)

        upper_half_sizer.Add(maintemp_panel, (0, 0))

        lower_half_sizer = wx.GridBagSizer(0, 10)

        sizer.Add(upper_half_sizer)
        sizer.Add(lower_half_sizer)

        hourly_forecast_panel = HourlyForecastPanel(self)
        week_forecast_panel = WeekForecastPanel(self)
        stat_panel = StatPanel(self)

        lower_half_sizer.Add(
            stat_panel, (0, 0), (2, 1), flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)

        lower_half_sizer.Add(
            hourly_forecast_panel, (2, 0), flag=wx.EXPAND | wx.ALL, border=5)

        lower_half_sizer.Add(
            week_forecast_panel, (0, 1), (3, 2), flag=wx.EXPAND | wx.ALL, border=5)
