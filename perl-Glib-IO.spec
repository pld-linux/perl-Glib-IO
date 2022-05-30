#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pnam	Glib-IO
Summary:	Perl GIO (Glib IO) bindings
Summary(pl.UTF-8):	Wiązania GIO (Glib IO) dla Perla
Name:		perl-Glib-IO
Version:	0.002
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	https://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	6fc3325815d13f01545966313d8ae506
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	glib2-devel >= 1:2.24.0
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-Glib-Object-Introspection >= 0.014
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	perl-Glib-Object-Introspection >= 0.014
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl access to GIO (Glib IO) library.

%description -l pl.UTF-8
Ten moduł daje dostęp z poziomu Perla do biblioteki GIO (Glib IO).

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%dir %{perl_vendorlib}/Glib
%{perl_vendorlib}/Glib/IO.pm
%{_mandir}/man3/Glib::IO.3pm*
