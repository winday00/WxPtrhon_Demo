///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Dec 21 2016)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyFrame1::MyFrame1( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxVERTICAL );
	
	wxBoxSizer* bSizer2;
	bSizer2 = new wxBoxSizer( wxHORIZONTAL );
	
	
	bSizer2->Add( 0, 0, 1, wxEXPAND, 5 );
	
	m_button4 = new wxButton( this, wxID_ANY, wxT("打开"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer2->Add( m_button4, 0, wxALL, 5 );
	
	m_button5 = new wxButton( this, wxID_ANY, wxT("保存"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer2->Add( m_button5, 0, wxALL, 5 );
	
	m_button6 = new wxButton( this, wxID_ANY, wxT("平移"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer2->Add( m_button6, 0, wxALL, 5 );
	
	m_button7 = new wxButton( this, wxID_ANY, wxT("缩放"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer2->Add( m_button7, 0, wxALL, 5 );
	
	m_button8 = new wxButton( this, wxID_ANY, wxT("取点"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer2->Add( m_button8, 0, wxALL, 5 );
	
	m_button9 = new wxButton( this, wxID_ANY, wxT("取图"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer2->Add( m_button9, 0, wxALL|wxALIGN_CENTER_VERTICAL, 5 );
	
	m_button10 = new wxButton( this, wxID_ANY, wxT("重置"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer2->Add( m_button10, 0, wxALL|wxALIGN_CENTER_VERTICAL, 5 );
	
	
	bSizer2->Add( 0, 0, 1, wxEXPAND, 5 );
	
	
	bSizer1->Add( bSizer2, 0, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer3;
	bSizer3 = new wxBoxSizer( wxHORIZONTAL );
	
	m_splitter2 = new wxSplitterWindow( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxSP_LIVE_UPDATE );
	m_splitter2->Connect( wxEVT_IDLE, wxIdleEventHandler( MyFrame1::m_splitter2OnIdle ), NULL, this );
	
	m_scrolledWindow3 = new wxScrolledWindow( m_splitter2, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxHSCROLL|wxVSCROLL );
	m_scrolledWindow3->SetScrollRate( 5, 5 );
	wxBoxSizer* bSizer5;
	bSizer5 = new wxBoxSizer( wxVERTICAL );
	
	Broadcaster = new wxPanel( m_scrolledWindow3, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	bSizer5->Add( Broadcaster, 1, wxEXPAND | wxALL, 5 );
	
	
	m_scrolledWindow3->SetSizer( bSizer5 );
	m_scrolledWindow3->Layout();
	bSizer5->Fit( m_scrolledWindow3 );
	m_scrolledWindow4 = new wxScrolledWindow( m_splitter2, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxHSCROLL|wxVSCROLL );
	m_scrolledWindow4->SetScrollRate( 5, 5 );
	wxBoxSizer* bSizer4;
	bSizer4 = new wxBoxSizer( wxVERTICAL );
	
	m_splitter4 = new wxSplitterWindow( m_scrolledWindow4, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxSP_3D );
	m_splitter4->Connect( wxEVT_IDLE, wxIdleEventHandler( MyFrame1::m_splitter4OnIdle ), NULL, this );
	
	m_scrolledWindow6 = new wxScrolledWindow( m_splitter4, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxHSCROLL|wxVSCROLL );
	m_scrolledWindow6->SetScrollRate( 5, 5 );
	wxBoxSizer* bSizer6;
	bSizer6 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText1 = new wxStaticText( m_scrolledWindow6, wxID_ANY, wxT("坐标点"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText1->Wrap( -1 );
	bSizer6->Add( m_staticText1, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	wxArrayString m_checkList1Choices;
	m_checkList1 = new wxCheckListBox( m_scrolledWindow6, wxID_ANY, wxDefaultPosition, wxDefaultSize, m_checkList1Choices, 0 );
	bSizer6->Add( m_checkList1, 1, wxALL|wxEXPAND, 5 );
	
	
	m_scrolledWindow6->SetSizer( bSizer6 );
	m_scrolledWindow6->Layout();
	bSizer6->Fit( m_scrolledWindow6 );
	m_scrolledWindow7 = new wxScrolledWindow( m_splitter4, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxHSCROLL|wxVSCROLL );
	m_scrolledWindow7->SetScrollRate( 5, 5 );
	wxStaticBoxSizer* sbSizer1;
	sbSizer1 = new wxStaticBoxSizer( new wxStaticBox( m_scrolledWindow7, wxID_ANY, wxT("预览") ), wxVERTICAL );
	
	
	m_scrolledWindow7->SetSizer( sbSizer1 );
	m_scrolledWindow7->Layout();
	sbSizer1->Fit( m_scrolledWindow7 );
	m_splitter4->SplitHorizontally( m_scrolledWindow6, m_scrolledWindow7, 0 );
	bSizer4->Add( m_splitter4, 1, wxEXPAND, 5 );
	
	
	m_scrolledWindow4->SetSizer( bSizer4 );
	m_scrolledWindow4->Layout();
	bSizer4->Fit( m_scrolledWindow4 );
	m_splitter2->SplitVertically( m_scrolledWindow3, m_scrolledWindow4, 0 );
	bSizer3->Add( m_splitter2, 1, wxEXPAND, 5 );
	
	
	bSizer1->Add( bSizer3, 1, wxEXPAND, 5 );
	
	
	this->SetSizer( bSizer1 );
	this->Layout();
	
	this->Centre( wxBOTH );
	
	// Connect Events
	m_button4->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::OpenImage ), NULL, this );
	m_button5->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::SaveImage ), NULL, this );
	m_button6->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::MoveImage ), NULL, this );
	m_button7->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::ImageScale ), NULL, this );
	m_button8->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::Pickpoint ), NULL, this );
	m_button9->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::cutwindows ), NULL, this );
	m_button10->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::ResetImage ), NULL, this );
}

MyFrame1::~MyFrame1()
{
	// Disconnect Events
	m_button4->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::OpenImage ), NULL, this );
	m_button5->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::SaveImage ), NULL, this );
	m_button6->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::MoveImage ), NULL, this );
	m_button7->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::ImageScale ), NULL, this );
	m_button8->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::Pickpoint ), NULL, this );
	m_button9->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::cutwindows ), NULL, this );
	m_button10->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::ResetImage ), NULL, this );
	
}
