Name:		ncdc
Version:	1.16.1
Release:	1
Summary:	Lightweight Direct Connect Client
Source0:	http://dev.yorhel.nl/download/ncdc-%{version}.tar.gz
Source1:	ncdc.desktop
URL:		http://dev.yorhel.nl/ncdc
Group:		Networking/File transfer
License:	MIT
BuildRequires:	ncurses-devel
BuildRequires:	bzip2-devel
BuildRequires:	glib2-devel
BuildRequires:	sqlite3-devel	
BuildRequires:	ncursesw-devel
BuildRequires:	libxml2-devel
BuildRequires:	gdbm-devel
BuildRequires:	gnutls-devel
BuildRequires:	sqlite-devel
BuildRequires:	gcc make glibc-devel pkgconfig
BuildRequires:	autoconf automake libtool

%description
Ncdc is a modern and lightweight direct connect client with a friendly ncurses
interface. 

%prep
%setup -q

%build
%configure2_5x --enable-db-upgrade
%make

%install
%makeinstall_std
install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc ChangeLog COPYING README
%{_bindir}/ncdc
%{_datadir}/applications/%{name}.desktop
%doc %{_mandir}/man1/ncdc.1*


%changelog
* Mon Jul 16 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.12-1
+ Revision: 809815
- version update 1.12

* Sat May 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.11-1
+ Revision: 799689
- version update 1.1.1

* Wed May 09 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.10-1
+ Revision: 797634
- BR: gnutls-devel
- version update 1.10

* Mon Mar 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.9-1
+ Revision: 785754
- Broken archive
- version update 1.9

* Tue Feb 14 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.7-1
+ Revision: 773920
- version update 1.7
- sqlite3-devel package 2011 fix

* Wed Dec 28 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.6-1.1
+ Revision: 745911
- BR fix
- imported package ncdc

