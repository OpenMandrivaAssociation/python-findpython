%define module findpython

Name:		python-findpython
Version:	0.8.0
Release:	2
Summary:	A utility to find python versions on your system
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/findpython
Source0:	https://files.pythonhosted.org/packages/source/f/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(wheel)

%description
A utility to find python versions on your system

%files
%doc README.md
%{_bindir}/%{module}
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
