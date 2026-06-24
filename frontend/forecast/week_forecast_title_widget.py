import wx


class WeekForecastTitleWidget(wx.Panel):
    def __init__(self, parent: wx.Window):
        super().__init__(parent, id=wx.ID_ANY)
        sizer = wx.GridSizer(3)
        self.SetSizer(sizer)

        # Day title
        image_cal = wx.Panel(self)
        image_cal.SetBackgroundColour(wx.Colour(135, 0, 88, 200))
        image_cal_sizer = wx.BoxSizer(wx.VERTICAL)
        image_cal.SetSizer(image_cal_sizer)
        image_day_text = wx.StaticText(
            image_cal, wx.ID_ANY | wx.ALL, "🗓️",)
        image_cal_sizer.AddSpacer(5)
        image_cal_sizer.Add(
            image_day_text, flag=wx.ALIGN_CENTER_HORIZONTAL, border=1)
        image_cal_sizer.AddSpacer(5)
        # Day title
        image_day = wx.Panel(self)
        image_day.SetBackgroundColour(wx.Colour(224, 169, 79, 200))
        image_day_sizer = wx.BoxSizer(wx.VERTICAL)
        image_day.SetSizer(image_day_sizer)
        image_day_text = wx.StaticText(
            image_day, wx.ID_ANY | wx.ALL, "🌞",)
        image_day_sizer.AddSpacer(5)
        image_day_sizer.Add(
            image_day_text, flag=wx.ALIGN_CENTER_HORIZONTAL, border=1)
        image_day_sizer.AddSpacer(5)
        # Night title
        image_night = wx.Panel(
            self)
        image_night.SetBackgroundColour(wx.Colour(107, 178, 236, 200))
        image_night_sizer = wx.BoxSizer(wx.VERTICAL)
        image_night.SetSizer(image_night_sizer)
        image_night_text = wx.StaticText(
            image_night, wx.ID_ANY, "🌛",)
        image_night_sizer.AddSpacer(5)
        image_night_sizer.Add(
            image_night_text, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=1)
        image_night_sizer.AddSpacer(5)

        sizer.Add(image_cal, flag=wx.EXPAND | wx.LEFT, border=5)
        sizer.Add(image_day, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=2)
        sizer.Add(image_night, flag=wx.EXPAND | wx.RIGHT, border=5)
