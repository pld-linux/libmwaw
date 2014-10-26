#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Library for reading and converting ClarisWorks, MacWrite, WriteNow word processor documents
Summary(pl.UTF-8):	Biblioteka do odczytu i konwersji dokumentów tekstowych ClarisWorks, MacWrite i WriteNow
Name:		libmwaw
Version:	0.3.3
Release:	1
License:	MPL v2.0 or LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libmwaw/%{name}-%{version}.tar.xz
# Source0-md5:	de4963d833142ce690ca9518a916e888
URL:		http://sourceforge.net/projects/libmwaw
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	librevenge-devel >= 0.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for reading and converting ClarisWorks, MacWrite, WriteNow
word processor documents.

%description -l pl.UTF-8
Biblioteka do odczytu i konwersji dokumentów tekstowych pochodzących z
procesorów tekstu ClarisWorks, MacWrite i WriteNow.

%package devel
Summary:	Header files for libmwaw
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmwaw
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	librevenge-devel >= 0.0
Requires:	libstdc++-devel

%description devel
Header files for libmwaw.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmwaw.

%package static
Summary:	Static libmwaw library
Summary(pl.UTF-8):	Statyczna biblioteka libmwaw
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmwaw library.

%description static -l pl.UTF-8
Statyczna biblioteka libmwaw.

%package apidocs
Summary:	libmwaw API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libmwaw
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API and internal documentation for libmwaw library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libmwaw.

%package tools
Summary:	Tools to transform Macintosh documents into other formats
Summary(pl.UTF-8):	Programy przekształcania dokumentów z Macintosha do innych formatów
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform ClarisWorks, MacWrite, WriteNow word processor
documents into other formats.

%description -l pl.UTF-8
Biblioteka do odczytu i konwersji dokumentów tekstowych pochodzących z
procesorów tekstu ClarisWorks, MacWrite i WriteNow.

%description tools -l pl.UTF-8
Narzędzia do przekształcania dokumentów tekstowych z procesorów tekstu
ClarisWorks, MacWrite i WriteNow do innych formatów.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}
#	--with-sharedptr=c++11	not ready for - uses implicit bool cast

%{__make}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README
%attr(755,root,root) %{_libdir}/libmwaw-0.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmwaw-0.3.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmwaw-0.3.so
%{_includedir}/libmwaw-0.3
%{_pkgconfigdir}/libmwaw-0.3.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmwaw-0.3.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/%{name}

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mwaw2csv
%attr(755,root,root) %{_bindir}/mwaw2html
%attr(755,root,root) %{_bindir}/mwaw2raw
%attr(755,root,root) %{_bindir}/mwaw2svg
%attr(755,root,root) %{_bindir}/mwaw2text
%attr(755,root,root) %{_bindir}/mwawFile
%attr(755,root,root) %{_bindir}/mwawZip
