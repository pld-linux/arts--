Summary:	Library for handling ARTS data files
Name:		arts++
Version:	1.1.a8
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.caida.org/pub/arts++/arts++-1-1-a8.tar.gz
# Source0-md5:	d41d8cd98f00b204e9800998ecf8427e
BuildRequires:	motif-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arts++ is a set of C++ classes and applications for handling ARTS data
files produced by CAIDA software (cflowd and skitter).

%package devel
Summary:	Header files and develpment documentation for arts++
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

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
install %{_datadir}/automake/config.* .
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/net \
	$RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man3}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES CREDITS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_includedir}/net/*.h
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
