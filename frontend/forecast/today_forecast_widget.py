import wx
from wx.svg import SVGimage


class TodayForecastWidget(wx.Panel):
    def __init__(self, parent: wx.Window, info_function):
        super().__init__(parent, id=wx.ID_ANY, style=wx.BORDER_SIMPLE)
        # weather widget
        sizer = wx.GridBagSizer()
        self.SetSizer(sizer)
        # info to be shown
        self.info = info_function
        self.hour_label = self.info["hour"]
        self.text_label = self.info["label"]
        self.img_src = self.info["image"]

        # content
        self.hour = wx.StaticText(self, wx.ID_ANY, self.hour_label)
        self.image = self.show_image(self, self.img_src)
        self.label = wx.StaticText(self, wx.ID_ANY, self.text_label)

        sizer.Add(self.hour, pos=(1, 0),
                  flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=1)
        sizer.Add(self.image, pos=(2, 0), span=(3, 0),
                  flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=1)
        sizer.Add(self.label, pos=(5, 0),
                  flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=1)

    def show_image(self, parent_component: wx.Window, path: str) -> wx.StaticBitmap:

        img = SVGimage.CreateFromFile(path)
        bmp = img.ConvertToScaledBitmap(wx.Size(64, 64))
        converted = wx.StaticBitmap(parent_component, wx.ID_ANY, bmp)
        return converted
