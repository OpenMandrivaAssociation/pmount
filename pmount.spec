%define name pmount
%define version 0.9.20
%define release %mkrel 1

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Pmount allow mounting devices without fstab modifications
License:    GPLv2
Group:      System/Base
Url:        http://packages.debian.org/unstable/utils/pmount
Source0:    http://ftp.de.debian.org/debian/pool/main/p/%{name}/%{name}_%{version}.orig.tar.gz
Patch0:     %{name}-0.9.17-no-user-change-during-install.patch
Buildrequires: glib-gettextize gettext-devel intltool
Buildrequires: libblkid-devel
Buildrequires: libsysfs-devel 
Buildrequires: hal-devel
Buildrequires: perl-XML-Parser
BuildRequires: libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Pmount allow mounting usb, firewire and pcmci media without modifying
/etc/fstab. It's a good base for automount software.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .no-user-change-during-install
autoreconf
libtoolize

%build
%configure2_5x
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


