import wx
from _GUI_ import gui
import Motion2 as M

class DragShape:
    def __init__(self, bmp):
        self.bmp = bmp
        self.pos = (0,0)
        self.shown = True
        self.text = None
        self.fullscreen = False

    def HitTest(self, pt):
        rect = self.GetRect()
        return rect.Contains(pt)

    def GetRect(self):
        return wx.Rect(self.pos[0], self.pos[1],
                      self.bmp.GetWidth(), self.bmp.GetHeight())

    def Draw(self, dc, op = wx.COPY):
        if self.bmp.IsOk():
            memDC = wx.MemoryDC()
            memDC.SelectObject(self.bmp)

            dc.Blit(self.pos[0], self.pos[1],
                    self.bmp.GetWidth(), self.bmp.GetHeight(),
                    memDC, 0, 0, op, True)

            return True
        else:
            return False

class MyWindows(gui.MyFrame1):
    def __init__(self, parent):
        gui.MyFrame1.__init__(self, parent)

        self.shapes = []
        self.dragShape = None
        self.hiliteShape = None
        self.dragImage = None


    def OpenImage( self, event ):

        file_wildcard = "All files(*.*)|*.*"
        dlg = wx.FileDialog(self, "Open Video File", wildcard=file_wildcard,
                            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
        dlg.Destroy()

        self.bmp = wx.Bitmap(self.filename)

        if self.bmp.IsOk():
            self.Message.SetValue('图片读入成功')
        else:
            self.Message.SetValue('图片读入出错')
            return

        # 读入图片
        canvas = DragCanvas(self.Broadcaster, -1, self.bmp)
        canvas.Update()
        def onSize(evt, panel=self.Broadcaster, canvas=canvas):
            canvas.SetSize(panel.GetSize())
        self.Broadcaster.Bind(wx.EVT_SIZE, onSize)
        # self.Position.SetValue(canvas.position)




class DragCanvas(wx.ScrolledWindow):
    def __init__(self, parent, ID, bmp1):
        wx.ScrolledWindow.__init__(self, parent, ID)
        self.shapes = []
        self.position = 0
        self.dragImage = None
        self.dragShape = None
        self.hiliteShape = None
        self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
        shape = DragShape(bmp1)
        shape.pos = (200, 5)
        self.shapes.append(shape)

        text = "Some Text"
        bg_colour = wx.Colour(115, 115, 115)  # matches the bg image
        font = wx.Font(15, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        textExtent = self.GetFullTextExtent(text, font)

        bmp = wx.Bitmap(textExtent[0], textExtent[1])

        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.SetBackground(wx.Brush(bg_colour, wx.BRUSHSTYLE_SOLID))
        dc.Clear()

        dc.SelectObject(wx.NullBitmap)
        mask = wx.Mask(bmp, bg_colour)
        bmp.SetMask(mask)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_MIDDLE_DOWN, self.OnMidDown)
        self.Bind(wx.EVT_MIDDLE_UP, self.OnMidUp)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)
        self.Bind(wx.EVT_MOUSEWHEEL, self.OnWheel)
##########################################################
    def OnWheel(self,evt):

        pass

    def OnLeaveWindow(self, evt):
        if not self.dragImage or not self.dragShape:
            self.dragImage = None
            self.dragShape = None
            return
        # Hide the image, end dragging, and nuke out the drag image.
        self.dragImage.Hide()
        self.dragImage.EndDrag()
        self.dragImage = None

        if self.hiliteShape:
            self.RefreshRect(self.hiliteShape.GetRect())
            self.hiliteShape = None

        self.dragShape.pos = (
            self.dragShape.pos[0] + evt.GetPosition()[0] - self.dragStartPos[0],
            self.dragShape.pos[1] + evt.GetPosition()[1] - self.dragStartPos[1]
            )

        self.dragShape.shown = True
        self.RefreshRect(self.dragShape.GetRect())
        self.dragShape = None

    def DrawShapes(self, dc):
        for shape in self.shapes:
            if shape.shown:
                shape.Draw(dc)

    def FindShape(self, pt):
        for shape in self.shapes:
            if shape.HitTest(pt):
                return shape
        return None


    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        self.PrepareDC(dc)
        self.DrawShapes(dc)

    def OnMidDown(self, evt):
        shape = self.FindShape(evt.GetPosition())
        if shape:
            self.dragShape = shape
            self.dragStartPos = evt.GetPosition()

    def OnMidUp(self, evt):
        if not self.dragImage or not self.dragShape:
            self.dragImage = None
            self.dragShape = None
            return

        self.dragImage.Hide()
        self.dragImage.EndDrag()
        self.dragImage = None

        if self.hiliteShape:
            self.RefreshRect(self.hiliteShape.GetRect())
            self.hiliteShape = None

        self.dragShape.pos = (
            self.dragShape.pos[0] + evt.GetPosition()[0] - self.dragStartPos[0],
            self.dragShape.pos[1] + evt.GetPosition()[1] - self.dragStartPos[1]
            )

        self.dragShape.shown = True
        self.RefreshRect(self.dragShape.GetRect())
        self.dragShape = None


    def OnMotion(self, evt):

        if not self.dragShape or not evt.Dragging() or not evt.MiddleIsDown:
            return
        if self.dragShape and not self.dragImage:

            tolerance = 2
            pt = evt.GetPosition()
            self.position = pt
            dx = abs(pt.x - self.dragStartPos.x)
            dy = abs(pt.y - self.dragStartPos.y)
            if dx <= tolerance and dy <= tolerance:
                return
            self.dragShape.shown = False
            self.RefreshRect(self.dragShape.GetRect(), True)
            self.Update()

            item = self.dragShape.text if self.dragShape.text else self.dragShape.bmp
            self.dragImage = wx.DragImage(item,
                                         wx.Cursor(wx.CURSOR_HAND))

            hotspot = self.dragStartPos - self.dragShape.pos
            self.dragImage.BeginDrag(hotspot, self, self.dragShape.fullscreen)

            self.dragImage.Move(pt)
            self.dragImage.Show()

        elif self.dragShape and self.dragImage:
            onShape = self.FindShape(evt.GetPosition())
            unhiliteOld = False
            hiliteNew = False

            if self.hiliteShape:
                if onShape is None or self.hiliteShape is not onShape:
                    unhiliteOld = True

            if onShape and onShape is not self.hiliteShape and onShape.shown:
                hiliteNew = True

            if unhiliteOld or hiliteNew:
                self.dragImage.Hide()

            if unhiliteOld:
                dc = wx.ClientDC(self)
                self.hiliteShape.Draw(dc)
                self.hiliteShape = None

            if hiliteNew:
                dc = wx.ClientDC(self)
                self.hiliteShape = onShape
                self.hiliteShape.Draw(dc, wx.INVERT)

            self.dragImage.Move(evt.GetPosition())
            if unhiliteOld or hiliteNew:
                self.dragImage.Show()



if __name__=='__main__':
    app = wx.App()
    main_win = MyWindows(None)
    main_win.Show()
    app.MainLoop()