#
# TODO:
# - Enable more backends
# - Fix requires esp for various backend support
# - Unpackages files? Need for mono macros?

%include	/usr/lib/rpm/macros.mono

%bcond_with eds
%bcond_with hiveminder
%bcond_with icecore
%bcond_with sqlite
%bcond_without dummy
%bcond_without rtm

Summary:	Tasque is a simple task management app
Name:		tasque
Version:	0.1.9
Release:	0.1
License:	- (enter GPL/GPL v2/GPL v3/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/tasque/0.1/%{name}-%{version}.tar.gz
# Source0-md5:	c8c911e1d98843a63d6fb96b180c8af5
URL:		http://live.gnome.org/Tasque
BuildRequires:	dotnet-gnome-sharp-devel
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel
BuildRequires:	dotnet-ndesk-dbus-sharp-devel
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	mono-csharp
BuildRequires:	pkgconfig
Requires:	dotnet-gtk-sharp2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tasque is a simple task management app (TODO list) for the Linux
Desktop.

%package devel
Summary:	Header files for tasque
Group:		Applications

%description devel
Development header files for Tasque

%prep
%setup -q

%build
%configure \
	--%{?with_dummy:en}%{!?with_dummy:dis}able-backend-dummy \
	--%{?with_eds:en}%{!?with_eds:dis}able-backend-eds \
	--%{?with_hiveminder:en}%{!?with_hiveminder:dis}able-backend-hiveminder \
	--%{?with_icecore:en}%{!?with_icecore:dis}able-backend-icecore \
	--%{?with_rtm:en}%{!?with_rtm:dis}able-backend-rtm \
	--%{?with_sqlite:en}%{!?with_sqlite:dis}able-backend-sqlite

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING INSTALL MAINTAINERS NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/Tasque.exe
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.dll
%{_datadir}/dbus-1/services/org.gnome.Tasque.service
%dir %{_datadir}/%{name}/sounds
%{_datadir}/%{name}/sounds/notify.wav
%{_pixmapsdir}/*.png
%{_pixmapsdir}/*.svg
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_desktopdir}/%{name}.desktop

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/%{name}.pc
