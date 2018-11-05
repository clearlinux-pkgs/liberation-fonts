#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : liberation-fonts
Version  : 2.00.4
Release  : 3
URL      : https://github.com/liberationfonts/liberation-fonts/archive/2.00.4.tar.gz
Source0  : https://github.com/liberationfonts/liberation-fonts/archive/2.00.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : OFL-1.1
Requires: liberation-fonts-data = %{version}-%{release}
Requires: liberation-fonts-license = %{version}-%{release}
BuildRequires : fontforge
BuildRequires : fonttools

%description
1. What's this?
=================
The Liberation Fonts is font collection which aims to provide document
layout compatibility as usage of Times New Roman, Arial, Courier New.

%package data
Summary: data components for the liberation-fonts package.
Group: Data

%description data
data components for the liberation-fonts package.


%package license
Summary: license components for the liberation-fonts package.
Group: Default

%description license
license components for the liberation-fonts package.


%prep
%setup -q -n liberation-fonts-2.00.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541429299
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1541429299
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/liberation-fonts
cp LICENSE %{buildroot}/usr/share/package-licenses/liberation-fonts/LICENSE
%make_install :||
## install_append content
mkdir -p %{buildroot}/usr/share/fonts/truetype/liberation
cp liberation-fonts-ttf-*/*.ttf %{buildroot}/usr/share/fonts/truetype/liberation
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf
/usr/share/fonts/truetype/liberation/LiberationMono-BoldItalic.ttf
/usr/share/fonts/truetype/liberation/LiberationMono-Italic.ttf
/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf
/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf
/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf
/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf
/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf
/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf
/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf
/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf
/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/liberation-fonts/LICENSE
