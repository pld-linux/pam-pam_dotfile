Summary:	A PAM module which allows users to have more than one password
Summary(pl):	Modu³ pozwalaj±cy na posiadanie wiêcej ni¿ jednego has³a
Name:		pam-pam_dotfile
Version:	0.7
Release:	1
Epoch:		0
License:	GPL v2
Vendor:		Lennart Poettering <mz70616d646f7466696c65@itaparica.org>
Group:		Applications/System
Source0:	http://www.stud.uni-hamburg.de/users/lennart/projects/pam_dotfile/pam_dotfile-%{version}.tar.gz
# Source0-md5:	3c7249f4e6d8a9bd756bb4e09f2ed907
URL:		http://www.stud.uni-hamburg.de/users/lennart/projects/pam_dotfile/
BuildRequires:	pam-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pam_dotfile is a PAM module which allows users to have more than one
password for a single account, each for a different service.

%description -l pl
pam_dotfile jest modu³em PAM pozwalaj±cym u¿ytkownikom na posiadanie
wiêcej ni¿ jednego has³a do jednego konta, ró¿ne has³a do ró¿nych
serwisów.

%prep
%setup -q

sed -i -e "s#root#$(id -u)#g" src/Makefile*

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) /lib/security/pam_dotfile.so
%attr(755,root,root) %{_bindir}/pam*
%attr(4755,root,root) %{_sbindir}/pam*
%{_mandir}/man?/*
