Summary:	Library for handling ARTS data files
Summary(pl):	Biblioteka do obs³ugi plików danych ARTS
Name:		arts++
Version:	1.1.a9
Release:	1
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.caida.org/pub/arts++/arts++-1-1-a9.tar.gz
# Source0-md5:	210dc2110d0177a98d15c557ee97fe4f
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arts++ is a set of C++ classes and applications for handling ARTS data
files produced by CAIDA software (cflowd and skitter).

%description -l pl
arts++ to zbiór klas C++ i aplikacji do obs³ugi plików danych ARTS
tworzonych przez oprogramowanie CAIDA (cflowd i skitter).

%package devel
Summary:	Header files and development documentation for arts++
Summary(pl):	Pliki nag³ówkowe i dokumentacja programisty dla arts++
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and development documentation for arts++.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja programisty dla arts++.

%package static
Summary:	Static arts++ library
Summary(pl):	Statyczna biblioteka arts++
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static arts++ library.

%description static -l pl
Statyczna biblioteka arts++.

%prep
%setup  -q -n %{name}-1-1-a8

%build
chmod u+w *.m4 configure
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/net \
	$RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man3}

perl -pi -e 's#/usr/include#\$\(includedir\)/%{name}#g' Makefile* */Makefile* */*/Makefile*
perl -pi -e 's#/usr/lib#\$\(libdir\)#g' Makefile* */Makefile* */*/Makefile*
perl -pi -e 's#/usr/bin#\$\(bindir\)#g' Makefile* */Makefile* */*/Makefile*
perl -pi -e 's#/usr/share/man#\$\(mandir\)#g' Makefile* */Makefile* */*/Makefile*

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/*.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
