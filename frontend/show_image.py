import wx
from wx.svg import SVGimage


def show_svg_image(parent_component: wx.Window, path: str, size: int) -> wx.StaticBitmap:

    img = SVGimage.CreateFromFile(path)
    bmp = img.ConvertToScaledBitmap(wx.Size(size, size))
    converted = wx.StaticBitmap(parent_component, wx.ID_ANY, bmp)
    return converted
