import os
import wx


class UiBitmaps:
    def __init__(self):
        self.bus_stop = self._set_bitmaps("icons8-bus-stop-100")
        self.info = self._set_bitmaps("icons8-info-squared-100")
        self.weather = self._set_bitmaps(
            "icons8-partly-cloudy-day-100")
        self.settings = self._set_bitmaps("icons8-settings-100")
        self.uv = self._set_bitmaps("icons8-sun-100")
        self.sunrise = self._set_bitmaps("icons8-sunrise-100")
        self.sunset = self._set_bitmaps("icons8-sunset-100")
        self.umbrella = self._set_bitmaps("icons8-umbrella-100")
        self.wind = self._set_bitmaps("icons8-wind-100")

    def _set_bitmaps(self, icon_name: str) -> wx.Bitmap:
        try:
            path = os.path.join("icons_ui", f'{icon_name}.png')
            img = wx.Image(path)
            img.Rescale(50, 50)
            bmp = wx.Bitmap(img)
            return bmp
        except Exception:
            img = wx.Image()
            img.Rescale(50, 50)
            bmp = wx.Bitmap(img)
            return bmp
