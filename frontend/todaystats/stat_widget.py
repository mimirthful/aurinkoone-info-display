import wx


class StatWidget(wx.Panel):
    def __init__(self, parent: wx.Window, icon: wx.Bitmap, info_dict: dict) -> None:
        super().__init__(parent, id=wx.ID_ANY)

        # info to be shown
        info_dict = info_dict
        info_name_label = info_dict["info_name"]
        img_src = icon
        info_label = info_dict["info_label"]

        # weather widget
        sizer = wx.StaticBoxSizer(wx.StaticBox(
            self, style=wx.ALIGN_CENTRE_HORIZONTAL, label=f'{info_name_label}'), wx.VERTICAL)
        self.SetSizer(sizer)
        sizer.SetMinSize(150, -1)

        # content
        static_bmp = wx.StaticBitmap(
            self, wx.ID_ANY, img_src)  # type: ignore
        info_text = wx.StaticText(self, wx.ID_ANY, info_label)

        # Add to sizer
        sizer.AddSpacer(15)
        sizer.Add(static_bmp, flag=wx.ALIGN_CENTER_HORIZONTAL |
                  wx.ALL, border=10)
        sizer.Add(info_text, flag=wx.ALIGN_CENTER_HORIZONTAL |
                  wx.ALL, border=10)
        sizer.AddSpacer(15)
