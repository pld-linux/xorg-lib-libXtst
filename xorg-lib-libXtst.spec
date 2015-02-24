Summary:	Xtst library
Summary(pl.UTF-8):	Biblioteka Xtst
Name:		xorg-lib-libXtst
Version:	1.2.2
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/archive/individual/lib/libXtst-%{version}.tar.bz2
# Source0-md5:	25c6b366ac3dc7a12c5d79816ce96a59
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-lib-libXext-devel >= 1:1.0.99.4
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-recordproto-devel >= 1.13.99.1
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.3
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
Obsoletes:	libXtst
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xtst library - RECORD and XTEST extensions.

%description -l pl.UTF-8
Biblioteka Xtst - rozszerzenia RECORD i XTEST.

%package devel
Summary:	Header files for libXtst library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXtst
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel >= 1:1.0.99.4
Requires:	xorg-lib-libXi-devel
Requires:	xorg-proto-recordproto-devel >= 1.13.99.1
Obsoletes:	libXtst-devel

%description devel
RECORD and XTEST extension library.

This package contains the header files needed to develop programs that
use libXtst.

%description devel -l pl.UTF-8
Biblioteka rozszerzeń RECORD i XTEST.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXtst.

%package static
Summary:	Static libXtst library
Summary(pl.UTF-8):	Biblioteka statyczna libXtst
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXtst-static

%description static
RECORD and XTEST extension library.

This package contains the static libXtst library.

%description static -l pl.UTF-8
Biblioteka rozszerzeń RECORD i XTEST.

Pakiet zawiera statyczną bibliotekę libXtst.

%prep
%setup -q -n libXtst-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--without-fop
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXtst.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXtst.so.6

%files devel
%defattr(644,root,root,755)
%doc specs/*.html
%attr(755,root,root) %{_libdir}/libXtst.so
%{_includedir}/X11/extensions/XTest.h
%{_includedir}/X11/extensions/record.h
%{_libdir}/libXtst.la
%{_pkgconfigdir}/xtst.pc
%{_mandir}/man3/XTest*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXtst.a
