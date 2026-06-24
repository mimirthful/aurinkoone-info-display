import wx

# TODO delete if not needed


def png_to_bitmap(path: str) -> wx.Bitmap:

    img = wx.Image(path, wx.BITMAP_TYPE_PNG)
    converted = wx.Bitmap(img=img)
    return converted
