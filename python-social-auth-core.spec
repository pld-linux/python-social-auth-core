#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define		module		social_core
%define		pypi_name	social-auth-core
%define		egg_name	social_auth_core
Summary:	Python Social Auth - Core
Name:		python-%{pypi_name}
Version:	1.2.0
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	d12b7c872f03d477dcca90c8e14f2844
URL:		http://python-social-auth-docs.readthedocs.io/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python Social Auth is an easy to setup social
authentication/registration mechanism with support for several
frameworks and auth providers.

This is the core component of the python-social-auth ecosystem, it
implements the common interface to define new authentication backends
to third parties services, implement integrations with web frameworks
and storage solutions.

%package -n python3-%{pypi_name}
Summary:	Social auth made simple
Group:		Development/Libraries

%description -n python3-%{pypi_name}
Python Social Auth is an easy to setup social
authentication/registration mechanism with support for several
frameworks and auth providers.

This is the core component of the python-social-auth ecosystem, it
implements the common interface to define new authentication backends
to third parties services, implement integrations with web frameworks
and storage solutions.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean

# rm tests (or subpackage?)
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/social_core/tests
%endif

%if %{with python3}
%py3_install

# rm tests (or subpackage?)
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/social_core/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc README.md LICENSE
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
