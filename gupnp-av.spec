Summary:	Library for building UPnP A/V applications
Name:		gupnp-av
Version:	0.12.1
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gupnp-av/0.12/%{name}-%{version}.tar.xz
# Source0-md5:	2d15a94d743720febb400b2cacde1cdc
URL:		http://www.gupnp.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	gupnp-devel >= 0.19.0
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gupnp-av is a small library that aims to easy the handling and
implementation of UPnP A/V profiles.

%package devel
Summary:	Header files for gupnp-av library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gupnp-av library.

%package apidocs
Summary:	gupnp-av library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API and internal documentation for gupnp-av library.

%prep
%setup -q

%build
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgupnp-av-1.0.so.?
%attr(755,root,root) %{_libdir}/libgupnp-av-1.0.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib
%{_datadir}/gupnp-av

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-av-1.0.so
%{_libdir}/libgupnp-av-1.0.la
%{_datadir}/gir-1.0/GUPnPAV-1.0.gir
%{_datadir}/vala/vapi/gupnp-av-1.0.deps
%{_datadir}/vala/vapi//gupnp-av-1.0.vapi
%{_includedir}/gupnp-av-1.0
%{_pkgconfigdir}/gupnp-av-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp-av

