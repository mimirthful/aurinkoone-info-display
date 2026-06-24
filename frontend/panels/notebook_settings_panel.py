import wx


class NotebookSettingsPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        # Notebook panel's main sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        placeholder = wx.StaticText(
            self, wx.ID_ANY, "⚙️ Settings would go here ⚙️ ")
        sizer.Add(placeholder)
