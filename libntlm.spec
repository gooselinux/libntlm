Name:           libntlm
Version:        1.0
Release:        3%{?dist}
Summary:        NTLM authentication library 

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://josefsson.org/libntlm/
Source0:        http://josefsson.org/libntlm/releases/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  pkgconfig

%description
A library for authenticating with Microsoft NTLM challenge-response,
derived from Samba sources.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
touch -r NEWS $RPM_BUILD_ROOT%{_includedir}/ntlm.h
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README THANKS
%{_libdir}/libntlm.so.*

%files devel
%defattr(-,root,root,-)
%doc COPYING 
%{_includedir}/ntlm.h
%{_libdir}/libntlm.so
%{_libdir}/pkgconfig/libntlm.pc


%changelog
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Apr 19 2008 Nikolay Vladimirov <nikolay@vladimiroff.com> - 1.0-1
- new upstream release

* Thu Mar 6 2008 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.4.2-1
- new upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.1-2
- Autorebuild for GCC 4.3

* Wed Jan 23 2008  Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.4.1-1
- new upstrem release

* Wed Aug 29 2007  Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.3.13-5
- rebuild for ppc32 selinux fix

* Thu Aug 2 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.3.13-4
- License tag changed

* Thu Jun 21 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.3.13-3
- minor mixed-use-of-spaces-and-tabs fix

* Thu Jun 21 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.3.13-2
- fixed summary
- fixed requires and buildrequires for pkgconfig
- fixed the timestamp of ntlm.h

* Wed Jun 20 2007 Nikolay Vladimirov <nikolay@vladimiroff.com> - 0.3.13-1
- initial release
