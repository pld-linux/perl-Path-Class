#
# Conditional build:
# Tests fail because our perl does not contain File::Spec::Win32 and
# other "foreign" modules
%bcond_with	tests	# perform "./Build test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Path
%define	pnam	Class
Summary:	Cross-platform path specification manipulation
Name:		perl-Path-Class
Version:	0.03_01
Release:	1
# same as Perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/K/KW/KWILLIAMS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d5531392cd65c9221e21627ef8dab2a2
Patch0:		%{name}-test-bareword.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Module-Build >= 0.20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
Path::Class is a module for manipulation of file and directory
specifications (strings describing their locations, like
'/home/ken/foo.txt' or 'C:\Windows\Foo.txt') in a cross-platform
manner. It supports pretty much every platform Perl runs on, including
Unix, Windows, Mac, VMS, Epoc, Cygwin, OS/2, and NetWare.

The well-known module File::Spec also provides this service, but it's
sort of awkward to use well, so people sometimes avoid it, or use it
in a way that won't actually work properly on platforms significantly
different than the ones they've tested their code on.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT

./Build
%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Path
%{_mandir}/man3/*
