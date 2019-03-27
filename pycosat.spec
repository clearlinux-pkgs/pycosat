#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycosat
Version  : 0.6.3
Release  : 1
URL      : https://github.com/ContinuumIO/pycosat/archive/0.6.3.tar.gz
Source0  : https://github.com/ContinuumIO/pycosat/archive/0.6.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: pycosat-license = %{version}-%{release}
Requires: pycosat-python = %{version}-%{release}
Requires: pycosat-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
===========================================
pycosat: bindings to picosat (a SAT solver)
===========================================

%package license
Summary: license components for the pycosat package.
Group: Default

%description license
license components for the pycosat package.


%package python
Summary: python components for the pycosat package.
Group: Default
Requires: pycosat-python3 = %{version}-%{release}

%description python
python components for the pycosat package.


%package python3
Summary: python3 components for the pycosat package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pycosat package.


%prep
%setup -q -n pycosat-0.6.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1553709724
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pycosat
cp LICENSE %{buildroot}/usr/share/package-licenses/pycosat/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pycosat/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
