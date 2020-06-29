# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"图像阅读器", pos = wx.DefaultPosition, size = wx.Size( 821,712 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_timer2 = wx.Timer()
		self.m_timer2.SetOwner( self, wx.ID_ANY )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"打开", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button4, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"平移", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"缩放", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"取图", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"重置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, u"标记", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_radioBtn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_splitter2 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_LIVE_UPDATE )
		self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )

		self.m_scrolledWindow3 = wx.ScrolledWindow( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer5.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.broadcaster = wx.ScrolledWindow( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.broadcaster.SetScrollRate( 5, 5 )
		bSizer5.Add( self.broadcaster, 1, wx.EXPAND |wx.ALL, 5 )

		self.pixelinfor = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.pixelinfor, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow3.SetSizer( bSizer5 )
		self.m_scrolledWindow3.Layout()
		bSizer5.Fit( self.m_scrolledWindow3 )
		self.m_scrolledWindow4 = wx.ScrolledWindow( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow4.SetScrollRate( 5, 5 )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter4 = wx.SplitterWindow( self.m_scrolledWindow4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter4.Bind( wx.EVT_IDLE, self.m_splitter4OnIdle )

		self.m_scrolledWindow6 = wx.ScrolledWindow( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow6.SetScrollRate( 5, 5 )
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow6, wx.ID_ANY, u"Message" ), wx.VERTICAL )

		self.Message = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH2 )
		sbSizer5.Add( self.Message, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow6.SetSizer( sbSizer5 )
		self.m_scrolledWindow6.Layout()
		sbSizer5.Fit( self.m_scrolledWindow6 )
		self.m_scrolledWindow7 = wx.ScrolledWindow( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow7.SetScrollRate( 5, 5 )
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow7, wx.ID_ANY, u"Position" ), wx.VERTICAL )

		self.Post = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH )
		sbSizer6.Add( self.Post, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow7.SetSizer( sbSizer6 )
		self.m_scrolledWindow7.Layout()
		sbSizer6.Fit( self.m_scrolledWindow7 )
		self.m_splitter4.SplitHorizontally( self.m_scrolledWindow6, self.m_scrolledWindow7, 310 )
		bSizer7.Add( self.m_splitter4, 1, wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow4, wx.ID_ANY, u"globle" ), wx.VERTICAL )

		self.m_panel3 = wx.Panel( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer4.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer7.Add( sbSizer4, 1, wx.EXPAND, 5 )


		self.m_scrolledWindow4.SetSizer( bSizer7 )
		self.m_scrolledWindow4.Layout()
		bSizer7.Fit( self.m_scrolledWindow4 )
		self.m_splitter2.SplitVertically( self.m_scrolledWindow3, self.m_scrolledWindow4, 0 )
		bSizer3.Add( self.m_splitter2, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_TIMER, self.UpdateUI, id=wx.ID_ANY )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OpenImage )
		self.m_button5.Bind( wx.EVT_BUTTON, self.SaveImage )
		self.m_button6.Bind( wx.EVT_BUTTON, self.MoveImage )
		self.m_button7.Bind( wx.EVT_BUTTON, self.ImageScale )
		self.m_button9.Bind( wx.EVT_BUTTON, self.cutwindows )
		self.m_button10.Bind( wx.EVT_BUTTON, self.ResetImage )
		self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.PickPoint )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def UpdateUI( self, event ):
		event.Skip()

	def OpenImage( self, event ):
		event.Skip()

	def SaveImage( self, event ):
		event.Skip()

	def MoveImage( self, event ):
		event.Skip()

	def ImageScale( self, event ):
		event.Skip()

	def cutwindows( self, event ):
		event.Skip()

	def ResetImage( self, event ):
		event.Skip()

	def PickPoint( self, event ):
		event.Skip()

	def m_splitter2OnIdle( self, event ):
		self.m_splitter2.SetSashPosition( 0 )
		self.m_splitter2.Unbind( wx.EVT_IDLE )

	def m_splitter4OnIdle( self, event ):
		self.m_splitter4.SetSashPosition( 310 )
		self.m_splitter4.Unbind( wx.EVT_IDLE )


