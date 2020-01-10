Summary:	Hangul Input Method Engine for SCIM
Name:		scim-hangul
Version:	0.4.0
Release:	2
License:	GPLv3+
Group:		System/Internationalization
Url:		http://www.scim-im.org/
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.gz
Patch0:		scim-hangul-0.4.0.gcc47.patch
BuildRequires:	pkgconfig(libhangul)
BuildRequires:	pkgconfig(scim)

%description
Scim-hangul is a SCIM IMEngine module for Korean (Hangul) input support.

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libdir}/scim-1.0/*/IMEngine/hangul.so
%{_libdir}/scim-1.0/*/SetupUI/hangul-imengine-setup.so
%{_datadir}/scim/icons/scim-hangul*.png
%{_datadir}/scim/hangul

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1


%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang %{name}


