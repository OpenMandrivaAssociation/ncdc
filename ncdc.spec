Summary:	Lightweight Direct Connect Client
Name:		ncdc
Version:	1.16.1
Release:	1
Group:		Networking/File transfer
License:	MIT
Url:		http://dev.yorhel.nl/ncdc
Source0:	http://dev.yorhel.nl/download/ncdc-%{version}.tar.gz
Source1:	ncdc.desktop
BuildRequires:	libtool
BuildRequires:	bzip2-devel
BuildRequires:	gdbm-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(sqlite3)

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

