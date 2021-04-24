#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycosat
Version  : 0.6.3
Release  : 13
URL      : https://github.com/ContinuumIO/pycosat/archive/0.6.3.tar.gz
Source0  : https://github.com/ContinuumIO/pycosat/archive/0.6.3.tar.gz
Summary  : bindings to picosat (a SAT solver)
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
Provides: pypi(pycosat)

%description python3
python3 components for the pycosat package.


%prep
%setup -q -n pycosat-0.6.3
cd %{_builddir}/pycosat-0.6.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602133767
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pycosat
cp %{_builddir}/pycosat-0.6.3/LICENSE %{buildroot}/usr/share/package-licenses/pycosat/5dabeed653c76b9f717a5862b7cf1744d3cc8109
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pycosat/5dabeed653c76b9f717a5862b7cf1744d3cc8109

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
