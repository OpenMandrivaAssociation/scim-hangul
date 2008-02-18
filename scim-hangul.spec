%define version	0.3.2
%define release	%mkrel 2

%define scim_version       1.4.5
%define skim_version       1.4.5
%define libhangul_version  0.0.4

Name:		scim-hangul
Summary:	Hangul IMEngine for SCIM
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
URL:		http://sourceforge.net/projects/scim/
Source:		http://dfn.dl.sourceforge.net/sourceforge/scim/%name-%version.tar.gz
Patch0:		scim-hangul-fix-build.diff
Requires:		scim-client = %{scim_api}
BuildRequires:		scim-devel >= %{scim_version}
BuildRequires:		libskim-devel >= %{skim_version}
BuildRequires:		libhangul-devel >= %{libhangul_version}
BuildRequires:		gettext-devel
BuildRequires:		automake
BuildRequires:		libskim-devel >= %{skim_version}
Obsoletes:	%mklibname %name 0

%description
scim-hangul is a Hangul IMEngine for SCIM, which is 
ported from imhangul project. 
It supports both Hangul and Hanja input.

%package skim
Summary:	Skim setup plugin for scim-hangul
Group:		System/Internationalization
Requires:	%{name} = %{version} 
Requires:	skim >= %{skim_version}
Conflicts:	%{mklibname %name 0} < 0.3.1-2

%description skim
This package contains skim setup plugin for scim-hangul.


%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --disable-static --disable-rpath
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unnecessary files
# note: skim loads some *.la files. Don't remove them.
rm -f %{buildroot}/%{_libdir}/scim-1.0/*/*.a

%find_lang %{name}
%find_lang skim-scim-hangul

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_datadir}/scim/icons/*
%{_datadir}/scim/hangul
%scim_plugins_dir/*/*.so
%scim_plugins_dir/*/*.la

%files skim -f skim-scim-hangul.lang
%defattr(-,root,root)
%doc COPYING
%{_libdir}/kde3/*
%{_datadir}/apps/skim/pics/scim-hangul.png
%{_datadir}/config.kcfg/scim_hangul.kcfg
%{_datadir}/services/skimconfiguredialog/skimplugin_scim_hangul_config.desktop
