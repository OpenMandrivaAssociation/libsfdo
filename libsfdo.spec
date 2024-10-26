%define major 0
%define libname %mklibname sfdo
%define devname %mklibname -d sfdo

Name:           libsfdo
Version:        0.1.3
Release:        1
Summary:        A collection of libraries implementing freedesktop.org specifications
Group:          Libraries
License:        BSD-2-Clause
URL:            https://gitlab.freedesktop.org/vyivel/libsfdo
Source:         https://gitlab.freedesktop.org/vyivel/libsfdo/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  meson

%description
%{summary}.

%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
This package contains the shared library files.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
%{summary}.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%meson
%meson_build

%install
%meson_install
%files -n %{libname}

%license LICENSE
%doc README.md
%{_libdir}/libsfdo-*.so.%{major}

%files -n %{devname}
%{_includedir}/sfdo-*.h
%{_libdir}/libsfdo-*.so
%{_libdir}/pkgconfig/libsfdo-*.pc
