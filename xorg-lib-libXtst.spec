#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Xtst library
Summary(pl.UTF-8):	Biblioteka Xtst
Name:		xorg-lib-libXtst
Version:	1.2.4
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/archive/individual/lib/libXtst-%{version}.tar.xz
# Source0-md5:	02f128fbf809aa9c50d6e54c8e57cb2e
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-lib-libX11-devel >= 1.6
BuildRequires:	xorg-lib-libXext-devel >= 1:1.0.99.4
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-recordproto-devel >= 1.13.99.1
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.3
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
BuildRequires:	xz
Requires:	xorg-lib-libX11 >= 1.6
Obsoletes:	libXtst < 6.5
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
Requires:	xorg-lib-libX11-devel >= 1.6
Requires:	xorg-lib-libXext-devel >= 1:1.0.99.4
Requires:	xorg-lib-libXi-devel
Requires:	xorg-proto-recordproto-devel >= 1.13.99.1
Requires:	xorg-proto-xextproto-devel >= 7.0.99.3
Obsoletes:	libXtst-devel < 6.5

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
Obsoletes:	libXtst-static < 6.5

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
	%{!?with_static_libs:--disable-static} \
	--without-fop
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXtst.la

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/libXtst/{recordlib,xtestlib}.*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libXtst.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXtst.so.6

%files devel
%defattr(644,root,root,755)
%doc specs/*.html
%attr(755,root,root) %{_libdir}/libXtst.so
%{_includedir}/X11/extensions/XTest.h
%{_includedir}/X11/extensions/record.h
%{_pkgconfigdir}/xtst.pc
%{_mandir}/man3/XTest*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libXtst.a
%endif
