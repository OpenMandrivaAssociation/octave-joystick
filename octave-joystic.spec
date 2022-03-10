%global octpkg joystick

Summary:	Basic matlab-like api for reading a joystick in GNU Octave 
Name:		octave-%{octpkg}
Version:	0.0.1
Release:	1
Source0:	https://downloads.sourceforge.net/octave-joystick/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://sourceforge.net/projects/%{octpkg}

BuildRequires:	octave-devel >= 3.6.0
BuildRequires:	pkgconfig(sdl2)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The Octave joystick package provides basic joystick read/write functions.

%files
%license %{octpkg}-%{version}/COPYING
%doc %{octpkg}-%{version}/NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -c

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build -T

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

