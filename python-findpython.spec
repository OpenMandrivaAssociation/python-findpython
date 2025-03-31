%define module findpython

Name:		python-findpython
Version:	0.6.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/f/findpython/findpython-%{version}.tar.gz
Summary:	A utility to find python versions on your system
URL:		https://pypi.org/project/findpython/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildRequires:	python%{pyver}dist(packaging)

%description
A utility to find python versions on your system


%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install


%files
%{_bindir}/%{module}
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-*.*-info
