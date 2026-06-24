import wx
from frontend import show_svg_image


class WeekForecastDayWidget(wx.Panel):
    def __init__(self, parent: wx.Window, info_function, is_today: bool):
        super().__init__(parent, id=wx.ID_ANY)
        # weather widget

        sizer = wx.GridSizer(0, 3, 0, 0)
        self.SetSizer(sizer)
        # info to be shown
        info = info_function

        img_src_day = info["image_day"]
        img_src_night = info["image_night"]
        temp_day_label = info["temperature_day"]
        temp_night_label = info["temperature_night"]
        weekday_label = info["weekday"]

        if is_today:
            weekday_label = "Today"

        weekday_panel = wx.Panel(self)
        weekday_sizer = wx.BoxSizer(wx.HORIZONTAL)
        weekday_panel.SetSizer(weekday_sizer)
        weekday = wx.StaticText(weekday_panel, wx.ID_ANY, label=weekday_label)
        weekday_sizer.Add(weekday, 1, wx.LEFT, 5)

        day_info_panel = wx.Panel(self)
        day_info_sizer = wx.GridSizer(2)
        day_info_panel.SetSizer(day_info_sizer)
        image_day = show_svg_image(day_info_panel, img_src_day, 40)
        temp_day = wx.StaticText(day_info_panel, wx.ID_ANY, temp_day_label)
        day_info_sizer.AddMany(
            [(image_day, 1, wx.LEFT, 10), (temp_day, 2, wx.RIGHT, 10)])

        night_info_panel = wx.Panel(self)
        night_info_sizer = wx.GridSizer(2)
        night_info_panel.SetSizer(night_info_sizer)
        image_night = show_svg_image(night_info_panel, img_src_night, 40)
        temp_night = wx.StaticText(
            night_info_panel, wx.ID_ANY, label=temp_night_label)
        night_info_sizer.AddMany(
            [(image_night, 1, wx.LEFT, 10), (temp_night,  2, wx.RIGHT, 10)])
        # add to sizers

        sizer.Add(weekday_panel, flag=wx.EXPAND |
                  wx.LEFT, border=10)
        sizer.Add(day_info_panel, flag=wx.EXPAND |
                  wx.RIGHT, border=10)
        sizer.Add(night_info_panel, flag=wx.EXPAND | wx.RIGHT, border=10)
