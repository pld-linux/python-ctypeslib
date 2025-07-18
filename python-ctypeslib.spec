%define	svnrev	r89065
%define	snap	20100119
%define	rel	4
Summary:	ctypeslib - useful additions to the ctypes FFI library
Summary(pl.UTF-8):	ctypeslib - przydatne dodatki do biblioteki FFI ctypes
Name:		python-ctypeslib
Version:	0.5.6
Release:	0.%{snap}.%{rel}
License:	MIT
Group:		Libraries/Python
# svn co http://svn.python.org/projects/ctypes/trunk/ctypeslib
Source0:	ctypeslib-%{svnrev}.tar.xz
# Source0-md5:	5ca5986339426eda062818a8b9a5e379
# http://blog.gmane.org/gmane.comp.python.ctypes/month=20100501
Patch0:		%{name}-cv.patch
URL:		https://pypi.python.org/pypi/ctypeslib
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gccxml
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ctypeslib - useful additions to the ctypes FFI library.

ctypeslib contains these packages:
- ctypeslib.codegen - a code generator
- ctypeslib.contrib - various contributed modules
- ctypeslib.util - assorted small helper functions
- ctypeslib.test - unittests

%description -l pl.UTF-8
ctypeslib - przydatne dodatki do biblioteki FFI ctypes.

ctypeslib zawiera następujące pakiety:
- ctypeslib.codegen - generator kodu
- ctypeslib.contrib - różne moduły dostarczone przez użytkowników
- ctypeslib.util - różne małe funkcje pomocnicze
- ctypeslib.test - testy jednostkowe

%prep
%setup -q -n ctypeslib
%patch -P0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/{h2xml.py,h2xml}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/{xml2py.py,xml2py}

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/ctypeslib/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE.txt TODO docs/codegen.txt
%attr(755,root,root) %{_bindir}/h2xml
%attr(755,root,root) %{_bindir}/xml2py
%{py_sitescriptdir}/ctypeslib
%{py_sitescriptdir}/ctypeslib-%{version}-py*.egg-info
