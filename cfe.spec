Summary:	Console Font Editor
Summary(pl):	Edytor font�w konsolowych
Name:		cfe
Version:	0.6
Release:	3
License:	GPL
Group:		Utilities/Console
Group(pl):	Narz�dzia/Konsola
Vendor:		Eugene Osintsev <osgene@omskelecom.ru>
Source0:	http://gene.i-connect.com/files/%{name}-%{version}.tar.gz
URL:		http://gene.i-connect.com/files/
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cfe is a Linux console font editor which works well both on the
console and the terminal. It includes such abilities as various glyph
transforming, multi-level undo, and comparing glyphs of two fonts.

%description -l pl
cfe jest edytorem font�w konsolowych dla Linuksa, pracuj�cym zar�wno
na konsoli jak i terminalu. Posiada takie mo�liwo�ci, jak r�ne
przekszta�cenia font�w, wielostopniowe cofanie i por�wnywanie dw�ch
font�w.

%prep
%setup -q

%build

%{__make} CFLAGS="$RPM_OPT_FLAGS -Wall -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install-strip \
	bindir=$RPM_BUILD_ROOT%{_bindir}

gzip -9nf CHANGES TODO AUTHOR

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,TODO,AUTHOR}.gz 

%attr(755,root,root) %{_bindir}/cfe
