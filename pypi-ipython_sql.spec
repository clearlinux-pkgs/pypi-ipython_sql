#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-ipython_sql
Version  : 0.5.0
Release  : 57
URL      : https://files.pythonhosted.org/packages/d0/ba/5a396a3b5bda93943479e7e79511ccec00f5b7ac30d0ed9072a1e69ee1a6/ipython-sql-0.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d0/ba/5a396a3b5bda93943479e7e79511ccec00f5b7ac30d0ed9072a1e69ee1a6/ipython-sql-0.5.0.tar.gz
Summary  : RDBMS access via IPython
Group    : Development/Tools
License  : MIT
Requires: pypi-ipython_sql-license = %{version}-%{release}
Requires: pypi-ipython_sql-python = %{version}-%{release}
Requires: pypi-ipython_sql-python3 = %{version}-%{release}
Requires: pypi(ipython_genutils)
Requires: pypi(sqlalchemy)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(ipython)
BuildRequires : pypi(ipython_genutils)
BuildRequires : pypi(prettytable)
BuildRequires : pypi(six)
BuildRequires : pypi(sqlalchemy)
BuildRequires : pypi(sqlparse)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
===========
ipython-sql
===========
:Author: Catherine Devlin, http://catherinedevlin.blogspot.com

%package license
Summary: license components for the pypi-ipython_sql package.
Group: Default

%description license
license components for the pypi-ipython_sql package.


%package python
Summary: python components for the pypi-ipython_sql package.
Group: Default
Requires: pypi-ipython_sql-python3 = %{version}-%{release}

%description python
python components for the pypi-ipython_sql package.


%package python3
Summary: python3 components for the pypi-ipython_sql package.
Group: Default
Requires: python3-core
Provides: pypi(ipython_sql)
Requires: pypi(ipython)
Requires: pypi(ipython_genutils)
Requires: pypi(prettytable)
Requires: pypi(six)
Requires: pypi(sqlalchemy)
Requires: pypi(sqlparse)

%description python3
python3 components for the pypi-ipython_sql package.


%prep
%setup -q -n ipython-sql-0.5.0
cd %{_builddir}/ipython-sql-0.5.0
pushd ..
cp -a ipython-sql-0.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695162223
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ipython_sql
cp %{_builddir}/ipython-sql-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ipython_sql/1c9900f6ca015de4cf1c4f0ef5b9be5361c90a15 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ipython_sql/1c9900f6ca015de4cf1c4f0ef5b9be5361c90a15

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
