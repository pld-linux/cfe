Summary:	Console Font Editor
Summary(pl):	Edytor fontów konsolowych
Name:		cfe
Version:	0.10
Release:	1
License:	GPL v2
Group:		Applications/Console
Group(de):	Applikationen/Konsole
Group(pl):	Aplikacje/Konsola
Vendor:		Eugene Osintsev <osgene@omskelecom.ru>
Source0:	http://lrn.ru/~osgene/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://lrn.ru/~osgene/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cfe is a Linux console font editor which works well both on the
console and the terminal. It includes such abilities as various glyph
transforming, multi-level undo, and comparing glyphs of two fonts.

%description -l pl
cfe jest edytorem fontów konsolowych dla Linuksa, pracuj±cym zarówno
na konsoli jak i terminalu. Posiada takie mo¿liwo¶ci, jak ró¿ne
przekszta³cenia fontów, wielostopniowe cofanie i porównywanie dwóch
fontów.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
%configure
%{__make} CFLAGS="%{rpmcflags} -Wall -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz 
%attr(755,root,root) %{_bindir}/cfe
%{_mandir}/man1/*.1*
