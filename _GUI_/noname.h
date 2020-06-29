///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Dec 21 2016)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/button.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/sizer.h>
#include <wx/panel.h>
#include <wx/scrolwin.h>
#include <wx/stattext.h>
#include <wx/checklst.h>
#include <wx/statbox.h>
#include <wx/splitter.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class MyFrame1
///////////////////////////////////////////////////////////////////////////////
class MyFrame1 : public wxFrame 
{
	private:
	
	protected:
		wxButton* m_button4;
		wxButton* m_button5;
		wxButton* m_button6;
		wxButton* m_button7;
		wxButton* m_button8;
		wxButton* m_button9;
		wxButton* m_button10;
		wxSplitterWindow* m_splitter2;
		wxScrolledWindow* m_scrolledWindow3;
		wxPanel* Broadcaster;
		wxScrolledWindow* m_scrolledWindow4;
		wxSplitterWindow* m_splitter4;
		wxScrolledWindow* m_scrolledWindow6;
		wxStaticText* m_staticText1;
		wxCheckListBox* m_checkList1;
		wxScrolledWindow* m_scrolledWindow7;
		
		// Virtual event handlers, overide them in your derived class
		virtual void OpenImage( wxCommandEvent& event ) { event.Skip(); }
		virtual void SaveImage( wxCommandEvent& event ) { event.Skip(); }
		virtual void MoveImage( wxCommandEvent& event ) { event.Skip(); }
		virtual void ImageScale( wxCommandEvent& event ) { event.Skip(); }
		virtual void Pickpoint( wxCommandEvent& event ) { event.Skip(); }
		virtual void cutwindows( wxCommandEvent& event ) { event.Skip(); }
		virtual void ResetImage( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		MyFrame1( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("图像阅读器"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 821,623 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		~MyFrame1();
		
		void m_splitter2OnIdle( wxIdleEvent& )
		{
			m_splitter2->SetSashPosition( 0 );
			m_splitter2->Disconnect( wxEVT_IDLE, wxIdleEventHandler( MyFrame1::m_splitter2OnIdle ), NULL, this );
		}
		
		void m_splitter4OnIdle( wxIdleEvent& )
		{
			m_splitter4->SetSashPosition( 0 );
			m_splitter4->Disconnect( wxEVT_IDLE, wxIdleEventHandler( MyFrame1::m_splitter4OnIdle ), NULL, this );
		}
	
};

#endif //__NONAME_H__
