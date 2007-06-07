Summary:	X tst library
Summary(pl.UTF-8):	Biblioteka X tst
Name:		xorg-lib-libXtst
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/archive/individual/lib/libXtst-%{version}.tar.bz2
# Source0-md5:	032d5c1d3914fc0224837328c88aef96
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-recordproto-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXtst
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X tst extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia X tst.

%package devel
Summary:	Header files for libXtst library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXtst
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-recordproto-devel
Obsoletes:	libXtst-devel

%description devel
X extension library.

This package contains the header files needed to develop programs that
use libXtst.

%description devel -l pl.UTF-8
Biblioteka rozszerzeń X.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXtst.

%package static
Summary:	Static libXtst library
Summary(pl.UTF-8):	Biblioteka statyczna libXtst
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXtst-static

%description static
X extension library.

This package contains the static libXtst library.

%description static -l pl.UTF-8
Biblioteka rozszerzeń X.

Pakiet zawiera statyczną bibliotekę libXtst.

%prep
%setup -q -n libXtst-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXtst.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXtst.so
%{_libdir}/libXtst.la
%{_pkgconfigdir}/xtst.pc
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXtst.a
