Name:		ncdc
Version:	1.12
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
%{_bindir}/ncdc-db-upgrade
%{_datadir}/applications/%{name}.desktop
%doc %{_mandir}/man1/ncdc.1*
%doc %{_mandir}/man1/ncdc-db-upgrade.1*
