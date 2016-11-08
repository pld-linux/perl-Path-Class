#
# Conditional build:
%bcond_with	tests	# perform "./Build test"
			# (tests fail because our perl doesn't contain
			# File::Spec::Win32 and other "foreign" modules)

%define		pdir	Path
%define		pnam	Class
%include	/usr/lib/rpm/macros.perl
Summary:	Path::Class - cross-platform path specification manipulation
Summary(pl.UTF-8):	Path::Class - wieloplatformowe operacje na ścieżkach plików
Name:		perl-Path-Class
Version:	0.37
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/K/KW/KWILLIAMS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	13e6db714f6d5a0e62ca1c4a7fc4d0f3
URL:		http://search.cpan.org/dist/Path-Class/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-Module-Build >= 0.3601
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 3.26
BuildRequires:	perl-File-Temp
BuildRequires:	perl-Test-Simple
%endif
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

%description -l pl.UTF-8
Path::Class to moduł do operacji na specifikacjach plików i katalogów
(łańcuchach opisujących ich położenie, takich jak '/home/ken/foo.txt'
czy 'C:\Windows\Foo.txt') w sposób wieloplatformowy. Obsługuje
większość platform na których działa Perl, w tym: Unix, Windows, Mac,
VMS, Epoc, Cygwin, OS/2, NetWare.

Podobne operacje są udostępniane przez dobrze znany moduł File::Spec,
ale jest on nieco niewygodny, więc ludzie czasem go unikają lub
używają w sposób nie działający poprawnie na platformach znacząco
różnych od tych, na których testują kod.

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
%doc Changes README
%dir %{perl_vendorlib}/Path
%{perl_vendorlib}/Path/Class.pm
%{perl_vendorlib}/Path/Class
%{_mandir}/man3/Path::Class*.3pm*
