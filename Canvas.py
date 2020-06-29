import wx
from _GUI_ import gui
import cv2
import Motion2 as M

class MyWindows(gui.MyFrame1):

    def __init__(self, parent):
        gui.MyFrame1.__init__(self, parent)
        self.pos = [0, 0]
        self.shown = False
        self.scale = 1
        self.maxScale = 10
        self.minScale = 0.1
        self.init()
        self.init_date()

    def init_date(self):
        self.PosChanged = False
        self.ImScale = False
        self.Input = False
        self.ShowOffset = [0, 0]
        self.LastShowOffset = [0, 0]

    def init_frame(self):
        self.broadcaster.Bind(wx.EVT_PAINT, self.OnPaint)
        self.broadcaster.Bind(wx.EVT_MIDDLE_DOWN, self.OnMidDown)
        self.broadcaster.Bind(wx.EVT_MIDDLE_UP, self.OnMidUp)
        self.broadcaster.Bind(wx.EVT_MOTION, self.OnMotion)
        self.broadcaster.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)
        self.broadcaster.Bind(wx.EVT_MOUSEWHEEL, self.OnWheel)
        pass

    def init(self):
        self.init_frame()
        self.m_timer2.Start(20)
        self.Bind(wx.EVT_TIMER,self.UpdateUI, id=self.m_timer2.GetId())

    def UpdateUI( self, event):
        if self.PosChanged or self.ImScale or self.Input:
            dc = wx.ClientDC(self.broadcaster)
            self.ShowObject(dc)
        self.init_date()

    def OpenImage( self, event ):

        file_wildcard = "All files(*.*)|*.*"
        dlg = wx.FileDialog(self, "Open Video File", wildcard=file_wildcard,
                            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
        dlg.Destroy()

        self.bmp_Org = wx.Bitmap(self.filename)

        if self.bmp_Org.IsOk():
            self.Message.SetValue('图片读入成功')
            self.Input = True
            self.shown = True
            self.bmp = self.bmp_Org
        else:
            self.Message.SetValue('图片读入出错')
            self.Input = False

        # w, h = self.broadcaster.GetSize()
        # x, y = self.bmp.GetSize()
        # self.pos[0] = w/2 - x/2
        # self.pos[1] = h/2 - y/2

    def OnPaint(self, event):
        if self.shown:
            dc = wx.PaintDC(self.broadcaster)
            self.broadcaster.PrepareDC(dc)
            self.ShowObject(dc)

    def ShowObject(self, dc):
        dc.Clear()        #图片显示位置为其：初始位置+上一帧位置+拖拽位置
        memDC = wx.MemoryDC()
        memDC.SelectObject(self.bmp)
        self.pos[0] = self.pos[0] + self.LastShowOffset[0] + self.ShowOffset[0]
        self.pos[1] = self.pos[1] + self.LastShowOffset[1] + self.ShowOffset[1]
        dc.Blit(self.pos[0], self.pos[1],
                self.bmp.GetWidth(), self.bmp.GetHeight(),
                memDC, 0, 0, wx.COPY, True)

    def OnMidDown(self, event):
        IsMouseInImg = self.findImage(event.GetPosition())
        if IsMouseInImg:
            self.MoveStartPos = event.GetPosition()
            self.PosChanged = True
        else:
            self.MoveStartPos = None

    def findImage(self,pt):
        rect = self.GetRect()
        return rect.Contains(pt)

    def GetRect(self):
        return wx.Rect(self.pos[0], self.pos[1],
                       self.bmp.GetWidth(),self.bmp.GetHeight())

    def OnMidUp(self, event):
        self.ShowOffset = [0, 0]
        if self.MoveStartPos != None:
            self.LastShowOffset[0] = event.X - self.MoveStartPos.x
            self.LastShowOffset[1] = event.Y - self.MoveStartPos.y
            self.PosChanged = True
            self.MoveStartPos = None
        event.Skip()

    def OnMotion(self, event):
        tolerance = 1
        if event.middleIsDown and self.MoveStartPos != None:
            dx = abs(event.X - self.MoveStartPos.x)
            dy = abs(event.Y - self.MoveStartPos.y)
            if dx > tolerance and dy > tolerance:
                self.ShowOffset[0] = event.X - self.MoveStartPos.x
                self.ShowOffset[1] = event.Y - self.MoveStartPos.y
                self.MoveStartPos.x = event.X
                self.MoveStartPos.y = event.Y
                self.PosChanged = True
            self.LastShowOffset = [0, 0]

        if self.shown:
            if self.findImage(event.GetPosition()):
                info = '图像坐标: (' + str(int(event.X - self.pos[0])) + ',' + str(int(event.Y - self.pos[1])) + ')'
                self.pixelinfor.SetValue(info)

        self.Update()
        event.Skip()

    def OnLeaveWindow(self,event):
        self.init_date()
        self.MoveStartPos = None
        event.Skip()

    def OnWheel(self,event):
        rotation = event.GetWheelRotation()
        pt = [event.X, event.Y]
        IsMouseInImg = self.findImage(event.GetPosition())
        if IsMouseInImg:
            if rotation > 0:
                self.scale = self.scale * 1.2
                print('up')
            else:
                self.scale = self.scale * 0.8
                print('down')
            self.ImScale = True
            self.ScaleImage(pt)
        event.Skip()

    def ScaleImage(self, pt):

        if self.bmp.GetWidth() * self.scale > self.maxScale * self.bmp_Org.GetWidth():
            self.scale = self.maxScale * self.bmp_Org.GetWidth() / self.bmp.GetWidth()
        if self.bmp.GetWidth() * self.scale < self.minScale * self.bmp_Org.GetWidth():
            self.scale = self.minScale * self.bmp_Org.GetWidth() / self.bmp.GetWidth()
        xo = pt[0] - self.pos[0]
        yo = pt[1] - self.pos[1]
        img = self.bmp.ConvertToImage().Scale(self.bmp.GetWidth()*self.scale, self.bmp.GetHeight()*self.scale)
        self.bmpS = wx.Bitmap(img, wx.BITMAP_SCREEN_DEPTH)
        x_image = xo / self.bmp.GetWidth() * self.bmpS.GetWidth()
        y_image = yo / self.bmp.GetHeight() * self.bmpS.GetHeight()

        fx = self.bmpS.GetWidth() / self.bmp_Org.GetWidth()
        fy = self.bmpS.GetHeight() / self.bmp_Org.GetHeight()
        imm = self.bmp_Org.ConvertToImage().Scale(self.bmp_Org.GetWidth() * fx, self.bmp_Org.GetHeight() * fy)
        self.bmpS = wx.Bitmap(imm, wx.BITMAP_SCREEN_DEPTH)


        self.pos[0] = pt[0] - x_image
        self.pos[1] = pt[1] - y_image
        self.bmp = self.bmpS

    def Pickpoint( self, event ):
        # self.broadcaster.Bind(wx.EVT_LEFT_DCLICK, self.getPoint)
        pass









if __name__=='__main__':
    app = wx.App()
    main_win = MyWindows(None)
    main_win.Show()
    app.MainLoop()
