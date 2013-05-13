%define name torsmo
%define version 0.18
%define release %mkrel 6

Name: %{name}
Summary: System monitor like gkrellm, but lightweight
Version: %{version}
Release: %{release}
Source0: http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0: torsmo-0.18-link.patch
URL: http://torsmo.sourceforge.net/
Group: Monitoring
License: BSD
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: pkgconfig(x11)

%description
Torsmo is a system monitor that sits in the corner of your desktop. It's very
simple, customizable and it renders only text on the desktop (and
percentagebars if you want it to ;) and the only lib it uses is Xlib.
Torsmo can show various information about your system and it's peripherals.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING README torsmorc.sample
%{_mandir}/man1/torsmo.1*
%{_bindir}/torsmo



%changelog
* Fri Jan 28 2011 Funda Wang <fwang@mandriva.org> 0.18-6mdv2011.0
+ Revision: 633655
- fix linkage

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.18-2mdv2008.1
+ Revision: 171147
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.18-1mdv2008.1
+ Revision: 128536
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import torsmo


* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.com> 0.18-1mdk
- 0.17


* Tue Jul 27 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.17-1mdk
- from Robert Weiler <mdk-rpms@robwei.de> :
	- First build of torsmo for Mandrake
