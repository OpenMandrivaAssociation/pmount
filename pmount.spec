Summary:	Pmount allow mounting devices without fstab modifications
Name:		pmount
Version:	0.9.23
Release:	5
License:	GPLv2+
Group:		System/Base
Url:		https://packages.debian.org/unstable/utils/pmount
Source0:	http://ftp.de.debian.org/debian/pool/main/p/%{name}/%{name}_%{version}.orig.tar.bz2
Patch0:		pmount-0.9.17-no-user-change-during-install.patch
Buildrequires:	glib-gettextize
Buildrequires:	intltool
BuildRequires:	libtool
Buildrequires:	perl-XML-Parser
Buildrequires:	gettext-devel
Buildrequires:	sysfsutils-devel
Buildrequires:	pkgconfig(blkid)

%description
Pmount allow mounting usb, firewire and pcmci media without modifying
/etc/fstab. It's a good base for automount software.

%files -f %{name}.lang
%{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/pmount.allow
%attr(4755,root,root) %{_bindir}/pmount
%attr(4755,root,root) %{_bindir}/pumount

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .no-user-change-during-install

%build
autoreconf -fi
libtoolize
%configure2_5x --disable-hal
%make

%install
%makeinstall_std

%find_lang %{name}

