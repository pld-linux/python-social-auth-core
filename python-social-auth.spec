#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	social-auth
Summary:	Social auth made simple
Name:		python-%{module}
Version:	0.2.19
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	https://pypi.python.org/packages/72/4c/5fb6c9157eb059e662beafbc73c84030741ea30eaaa643ca1cb8b58f1bdc/%{name}-%{version}.tar.gz
# Source0-md5:	65b9c0b77ca2870b5dc586a0c65a0eba
URL:		http://psa.matiasaguirre.net/
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

Crafted using base code from django-social-auth, implements a common
interface to define new authentication providers from third parties.
And to bring support for more frameworks and ORMs.

%package -n python3-%{module}
Summary:	Social auth made simple
Group:		Development/Libraries

%description -n python3-%{module}
Python Social Auth is an easy to setup social
authentication/registration mechanism with support for several
frameworks and auth providers.

Crafted using base code from django-social-auth, implements a common
interface to define new authentication providers from third parties.
And to bring support for more frameworks and ORMs.

%package doc
Summary:	Documentation for Python Social Auth
Group:		Documentation

%description doc
This package contains the documentation for %{name}.

%prep
%setup -q

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
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/social/tests
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/social/apps/django_app/tests.py*
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/social/apps/django_app/me/tests.py*
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/social/apps/django_app/default/tests.py*
%endif

%if %{with python3}
%py3_install

# rm tests (or subpackage?)
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/social/tests
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/social/apps/django_app/tests.py
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/social/apps/django_app/__pycache__/tests.*.pyc
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/social/apps/django_app/me/tests.py
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/social/apps/django_app/me/__pycache__/tests.*.pyc
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/social/apps/django_app/default/tests.py
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/social/apps/django_app/default/__pycache__/tests.*.pyc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py_sitescriptdir}/social
%{py_sitescriptdir}/python_social_auth-%{version}-py2.*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py3_sitescriptdir}/social
%{py3_sitescriptdir}/python_social_auth-%{version}-py3.*.egg-info
%endif

%files doc
%defattr(644,root,root,755)
%doc docs examples
