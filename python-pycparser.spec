# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pycparser
Epoch: 100
Version: 2.21
Release: 1%{?dist}
BuildArch: noarch
Summary: C parser and AST generator written in Python
License: BSD-3-Clause
URL: https://github.com/eliben/pycparser/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
pycparser is a complete parser for the C language, written in pure
Python. It is a module designed to be easily integrated into
applications that need to parse C source code.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500 || 0%{?rhel} == 7
%package -n python%{python3_version_nodots}-pycparser
Summary: C parser and AST generator written in Python
Requires: python3
Provides: python3-pycparser = %{epoch}:%{version}-%{release}
Provides: python3dist(pycparser) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pycparser = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pycparser) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pycparser = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pycparser) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pycparser
pycparser is a complete parser for the C language, written in pure
Python. It is a module designed to be easily integrated into
applications that need to parse C source code.

%files -n python%{python3_version_nodots}-pycparser
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?rhel} == 7)
%package -n python3-pycparser
Summary: C parser and AST generator written in Python
Requires: python3
Provides: python3-pycparser = %{epoch}:%{version}-%{release}
Provides: python3dist(pycparser) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pycparser = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pycparser) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pycparser = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pycparser) = %{epoch}:%{version}-%{release}

%description -n python3-pycparser
pycparser is a complete parser for the C language, written in pure
Python. It is a module designed to be easily integrated into
applications that need to parse C source code.

%files -n python3-pycparser
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
