#
# Conditional build:
%bcond_with	tests	# perform "./Build test"
			# (tests fail because our perl doesn't contain
			# File::Spec::Win32 and other "foreign" modules)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Path
%define	pnam	Class
Summary:	Path::Class - cross-platform path specification manipulation
Summary(pl):	Path::Class - wieloplatformowe operacje na ¶cie¿kach plików
Name:		perl-Path-Class
Version:	0.05
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/K/KW/KWILLIAMS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	09a47e595b39998b2ab64904327f0958
BuildRequires:	perl-Module-Build >= 0.20
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
Path::Class to modu³ do operacji na specifikacjach plików i katalogów
(³añcuchach opisuj±cych ich po³o¿enie, takich jak '/home/ken/foo.txt'
czy 'C:\Windows\Foo.txt') w sposób wieloplatformowy. Obs³uguje
wiêkszo¶æ platform na których dzia³a Perl, w tym: Unix, Windows, Mac,
VMS, Epoc, Cygwin, OS/2, NetWare.

Podobne operacje s± udostêpniane przez dobrze znany modu³ File::Spec,
ale jest on nieco niewygodny, wiêc ludzie czasem go unikaj± lub
u¿ywaj± w sposób nie dzia³aj±cy poprawnie na platformach znacz±co
ró¿nych od tych, na których testuj± kod.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
