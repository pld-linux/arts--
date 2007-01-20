Summary:	Library for handling ARTS data files
Summary(pl):	Biblioteka do obs³ugi plików danych ARTS
Name:		arts++
Version:	1.1.a12
Release:	1
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://www.caida.org/tools/utilities/arts/download/%{name}-%{version}.tar.gz
# Source0-md5:	bb0afcc952c4cf5864342b68380f9ffc
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-printf.patch
URL:		http://www.caida.org/tools/utilities/arts/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/%{name}

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
Requires:	libstdc++-devel

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
%setup -q
%patch0 -p1
%patch1 -p1

find . -name Makefile.in | xargs \
	%{__perl} -pi -e 's/(\@(include|lib|bin|man)dir\@)/\$(DESTDIR)$1/g;
	s/-m 444/-m 644/g;s/-m 555/-m 755/g'

%{__perl} -pi -e 's/-m 644//' classes/src/Makefile.in
%{__perl} -pi -e 's/manl/man1/;s/\.l$/\.1/' apps/*/Makefile.in
%{__perl} -pi -e 's/l LOCAL/1 LOCAL/' apps/*/*.man

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
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/*.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
