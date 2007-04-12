%define name pmount
%define version 0.9.9
%define release %mkrel 2

Summary: Pmount allow mounting devices without fstab modifications
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.piware.de/projects/%{name}-%{version}.tar.bz2
Patch0:  pmount-0.9.6-fix-sysfs-detection.patch
# (fc) 0.9.9-2mdv don't use dbus deprecated api
Patch1:  pmount-0.9.9-deprecated.patch

License: GPL
Group: System/Base
Url: http://www.piware.de/projects.shtml
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires: libsysfs-devel 
Buildrequires: hal-devel
Buildrequires: perl-XML-Parser

%description
Pmount allow mounting usb, firewire and pcmci media without modifying
/etc/fstab. It's a good base for automount software.

%prep
%setup -q -n %{name}-%{version}
#%patch0 -p0
%patch1 -p1 -b .deprecated
autoconf

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/pmount.allow
%{_bindir}/pmount-hal
%attr(4755,root,root) %{_bindir}/pmount
%attr(4755,root,root) %{_bindir}/pumount


