%define name pmount
%define version 0.9.23
%define release %mkrel 3

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Allow mounting devices without fstab modifications
License:    GPLv2
Group:      System/Base
Url:        http://packages.debian.org/unstable/utils/pmount
Source0:    http://ftp.de.debian.org/debian/pool/main/p/%{name}/%{name}_%{version}.orig.tar.bz2
Patch0:     %{name}-0.9.17-no-user-change-during-install.patch
Buildrequires: glib-gettextize gettext-devel intltool
Buildrequires: pkgconfig(blkid)
Buildrequires: sysfsutils-devel 
Buildrequires: perl-XML-Parser
BuildRequires: libtool

%description
Pmount allow mounting usb, firewire and pcmci media without modifying
/etc/fstab. It's a good base for automount software.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .no-user-change-during-install
autoreconf
libtoolize

%build
%configure2_5x --disable-hal
%make

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/pmount.allow
%attr(4755,root,root) %{_bindir}/pmount
%attr(4755,root,root) %{_bindir}/pumount
