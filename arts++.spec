Summary:	Library for handling ARTS data files
Name:		arts++
Version:	1.1.a8
Release:	1
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.caida.org/pub/arts++/arts++-1-1-a8.tar.gz
# Source0-md5:	3527ba0fa7ab6fb579573969967d1059
BuildRequires:	perl-base
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arts++ is a set of C++ classes and applications for handling ARTS data
files produced by CAIDA software (cflowd and skitter).

%package devel
Summary:	Header files and develpment documentation for arts++
Group:		Development/Libraries
#Requires:	%{name} = %{epoch}:%{version}

%description devel
Header files and develpment documentation for arts++.

%package static
Summary:	Static arts++ library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Static arts++ library.

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

%{makeinstall}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/*.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
