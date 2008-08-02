%define name torsmo
%define version 0.18
%define release %mkrel 5

Name: %{name}
Summary: System monitor like gkrellm, but lightweight
Version: %{version}
Release: %{release}
Source0: http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
URL: http://torsmo.sourceforge.net/
Group: Monitoring
License: BSD
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: X11-devel

%description
Torsmo is a system monitor that sits in the corner of your desktop. It's very
simple, customizable and it renders only text on the desktop (and
percentagebars if you want it to ;) and the only lib it uses is Xlib.
Torsmo can show various information about your system and it's peripherals.

%prep

%setup -q

%build

%configure

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING README torsmorc.sample
%{_mandir}/man1/torsmo.1*
%{_bindir}/torsmo

