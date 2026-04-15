%define module pyscard
%bcond tests 1

Name:		python-pyscard
Version:	2.3.1
Release:	1
Summary:	Smartcard module for Python
License:	LGPL-2.1-or-later
Group:		Development/Python
URL:		https://pypi.org/project/pyscard
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(libpcsclite)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	swig
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
Smartcard module for Python.

%prep -a
# Remove bundled egg-info
rm -rf src/%{module}.egg-info
# We dont need colour output in CI
sed -i '/addopts = "--color=yes"/d' pyproject.toml

%build -p
export LDFLAGS="%{ldflags} -lpython%{py_ver}"

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
pytest
%endif

%files
%{python_sitearch}/smartcard
%{python_sitearch}/%{module}-%{version}.dist-info
