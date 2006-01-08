Summary:	Frontend to the movies section of sublimedirectory.com
Summary(pl):	Frontend do sekcji filmów z sublimedirectory.com
Name:		gnaughty
Version:	1.1.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.sourceforge.net/gnaughty/%{name}-%{version}.tar.gz
# Source0-md5:	60b83c4aa814838688e1697411ed9cbe
URL:		http://gnaughty.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnaughty is a frontend to the movies section of sublimedirectory.com,
written in GTK+2 for the Linux operating system.

%description -l pl
gnaughty to frontend do sekcji filmów z sublimedirectory.com napisany
w GTK+2 dla systemu operacyjnego Linux.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install gnaughty.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
