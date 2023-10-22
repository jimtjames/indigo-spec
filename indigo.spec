Name: indigo
Version: 2.0
Release: 248
Summary: INDIGO Astronomy Core Library and Drivers

License: INDIGO Astronomy open source license
URL: https://www.indigo-astronomy.org/
Source0: https://github.com/indigo-astronomy/indigo/archive/refs/tags/%{version}-%{release}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: cmake
BuildRequires: libtool
BuildRequires: libusb1-devel
BuildRequires: avahi-compat-libdns_sd-devel
BuildRequires: libudev-devel
BuildRequires: curl
BuildRequires: curl-devel
BuildRequires: zlib-devel
BuildRequires: gmock
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libcurl)
BuildRequires: patchelf
BuildRequires: sudo

Requires: libtool
Requires: avahi-compat-libdns_sd
Requires: curl
Requires: zlib

%description
INDIGO is the next generation of INDI, based on layered architecture and software bus.

%prep
%autosetup -v -p1 -n indigo-%{version}-%{release}


%build

# We need to patch the Makefile to use relative paths for certain things
sed -i 's/sudo//g' Makefile
sed -i 's/udevadm control --reload-rules/#udevadm control --reload-rules/g' Makefile
sed -i 's/install -d \/sbin/install -d $(INSTALL_ROOT)\/sbin/g' Makefile
sed -i 's/install -d \/usr\/sbin/install -d $(INSTALL_ROOT)\/usr\/sbin/g' Makefile
sed -i 's/install -m 0755 tools\/fxload\/fxload \/sbin/install -m 0755 tools\/fxload\/fxload $(INSTALL_ROOT)\/sbin/g' Makefile
sed -i 's/install -m 0755 tools\/fxload\/fxload \/usr\/sbin/install -m 0755 tools\/fxload\/fxload $(INSTALL_ROOT)\/usr\/sbin/g' Makefile

make all

%install

make INSTALL_ROOT=%{buildroot} INSTALL_BIN=%{buildroot}/usr/bin INSTALL_LIB=%{buildroot}/usr/lib64 INSTALL_INCLUDE=%{buildroot}/include INSTALL_SHARE=%{buildroot}/usr/share install
#make INSTALL_ROOT=%{buildroot} install


%check


%files
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_datadir}/*
%license
%doc

%post
sudo udevadm control --reload-rules

%changelog
%autochangelog

