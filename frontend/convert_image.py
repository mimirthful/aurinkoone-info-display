import wx

# TODO remove if not needed


def show_png_image(path: str) -> wx.Bitmap:

    img = wx.Image(path, wx.BITMAP_TYPE_PNG)
    converted = wx.Bitmap(img=img)
    return converted
