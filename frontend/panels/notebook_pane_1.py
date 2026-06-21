import wx
from frontend.forecast import ForecastPanel


class NotebookPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        # Notebook panel's main sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)

        # Lower and half sizers
        self.upper_half_sizer = wx.GridBagSizer(10, 10)
        self.lower_half_sizer = wx.GridBagSizer(10, 10)
        self.sizer.AddMany([self.upper_half_sizer, self.lower_half_sizer])

        self.forecast_panel = ForecastPanel(self)
        self.lower_half_sizer.Add(self.forecast_panel, (0, 0))
