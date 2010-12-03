%define version	0.3.2
%define release	%mkrel 9

%define scim_version       1.4.5
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
Patch1:		scim-hangul-0.3.2-gcc43.patch
Requires:		scim-client = %{scim_api}
BuildRequires:		scim-devel >= %{scim_version}
BuildRequires:		libhangul-devel >= %{libhangul_version}
BuildRequires:		gettext-devel
BuildRequires:		automake
Obsoletes:	%mklibname %name 0

%description
scim-hangul is a Hangul IMEngine for SCIM, which is 
ported from imhangul project. 
It supports both Hangul and Hanja input.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

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

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_datadir}/scim/icons/*
%{_datadir}/scim/hangul
%scim_plugins_dir/*/*.so
%scim_plugins_dir/*/*.la
