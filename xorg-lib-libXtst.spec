
#
Summary:	X tst library
Summary(pl):	Biblioteka X tst
Name:		xorg-lib-libXtst
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXtst-%{version}.tar.bz2
# Source0-md5:	210f8cecebe1839a2b8aeb9bee925bcb
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-proto-recordproto-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/libXtst-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
X extension library.

%description -l pl
Biblioteka rozszerzeñ X.


%package devel
Summary:	Header files libXtst development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXtst
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXtst = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-recordproto-devel

%description devel
X extension library.

This package contains the header files needed to develop programs that
use these libXtst.

%description devel -l pl
Biblioteka rozszerzeñ X.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXtst.


%package static
Summary:	Static libXtst libraries
Summary(pl):	Biblioteki statyczne libXtst
Group:		Development/Libraries
Requires:	xorg-lib-libXtst-devel = %{version}-%{release}

%description static
X extension library.

This package contains the static libXtst library.

%description static -l pl
Biblioteka rozszerzeñ X.

Pakiet zawiera statyczn± bibliotekê libXtst.


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
%doc ChangeLog
%attr(755,root,wheel) %{_libdir}/libXtst.so.*


%files devel
%defattr(644,root,root,755)
%{_libdir}/libXtst.la
%attr(755,root,wheel) %{_libdir}/libXtst.so
%{_pkgconfigdir}/xtst.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libXtst.a
