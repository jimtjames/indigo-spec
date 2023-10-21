Name: indigo
Version: 248
Release: %autorelease
Summary: INDIGO Astronomy Core Library and Drivers

License: INDIGO-Astronomy-open-source-license
URL: https://www.indigo-astronomy.org/
Source0: https://github.com/indigo-astronomy/indigo/archive/refs/tags/2.0-%{version}.tar.gz

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



%description
INDIGO is the next generation of INDI, based on layered architecture and software bus.

%prep
%autosetup -v -p1 -n indigo


%build
%configure
%make_build


%install
%make_install


%check


%files
%license
%doc


%changelog
%autochangelog

