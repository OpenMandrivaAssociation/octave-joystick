%global octpkg joystick

Summary:	Provides basic joystick functions for GNU Octave
Name:		octave-joystick
Version:	0.0.3
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/joystick/
Source0:	https://downloads.sourceforge.net/project/octave-joystick/v%{version}/joystick-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:	pkgconfig(sdl2)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The Octave joystick package provides basic joystick read/write functions.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

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

