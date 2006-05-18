%define 	modulename pam_dotfile
Summary:	A PAM module which allows users to have more than one password
Summary(pl):	Modu³ pozwalaj±cy na posiadanie wiêcej ni¿ jednego has³a
Name:		pam-%{modulename}
Version:	0.7
Release:	3
Epoch:		0
License:	GPL v2
Group:		Applications/System
Source0:	http://0pointer.de/lennart/projects/pam_dotfile/%{modulename}-%{version}.tar.gz
# Source0-md5:	3c7249f4e6d8a9bd756bb4e09f2ed907
URL:		http://0pointer.net/lennart/projects/pam_dotfile/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	lynx
BuildRequires:	pam-devel
BuildRequires:	sed >= 4.0
Obsoletes:	pam_dotfile
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pam_dotfile is a PAM module which allows users to have more than one
password for a single account, each for a different service.

%description -l pl
pam_dotfile jest modu³em PAM pozwalaj±cym u¿ytkownikom na posiadanie
wiêcej ni¿ jednego has³a do jednego konta, ró¿ne has³a do ró¿nych
serwisów.

%prep
%setup -q -n %{modulename}-%{version}

sed -i -e "s#root#$(id -u)#g" src/Makefile*
sed -i -e "s#/lib/security#/%{_lib}/security#g" configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_lib}/security/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) /%{_lib}/security/pam_dotfile.so
%attr(755,root,root) %{_bindir}/pam*
%attr(4755,root,root) %{_sbindir}/pam*
%{_mandir}/man?/*
