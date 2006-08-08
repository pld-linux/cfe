Summary:	Console Font Editor
Summary(pl):	Edytor fontów konsolowych
Name:		cfe
Version:	0.12
Release:	4
License:	GPL v2
Group:		Applications/Console
Vendor:		Eugene Osintsev <osgene@omskelecom.ru>
Source0:	http://lrn.ru/~osgene/files/%{name}-%{version}.tar.gz
# Source0-md5:	c37cca14cacd6c6be27f8fa6cc10e89b
Patch0:		%{name}-DESTDIR.patch
URL:		http://lrn.ru/~osgene/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
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
%patch0 -p0

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} CFLAGS="%{rpmcflags} -Wall -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/cfe
%{_mandir}/man1/*.1*
