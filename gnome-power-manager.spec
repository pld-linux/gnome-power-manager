Summary:	GNOME Power Manager
Summary(pl.UTF-8):	Zarządca energii dla GNOME
Name:		gnome-power-manager
Version:	2.23.91
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-power-manager/2.23/%{name}-%{version}.tar.bz2
# Source0-md5:	ec1b6a0ead759ff43b268597eb17f2af
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/projects/gnome-power-manager/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.1
BuildRequires:	gnome-keyring-devel >= 2.22.0
BuildRequires:	gnome-panel-devel >= 2.22.0
BuildRequires:	gtk+2-devel >= 1:2.12.8
BuildRequires:	gstreamer-devel >= 0.10.14
BuildRequires:	hal-devel >= 0.5.10
BuildRequires:	intltool >= 0.37.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.22.0
BuildRequires:	libnotify-devel >= 0.4.3
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.22.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
Requires(post,preun):	GConf2
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires:	gnome-session >= 2.22.0
Requires:	notification-daemon >= 0.3.5
Obsoletes:	gnome-power
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uses of GNOME Power Manager infrastructure
- A dialogue that warns the user when on UPS power, that automatically
  begins a kind shutdown when the power gets critically low.
- An icon that allows a user to dim the LCD screen with a slider, and
  does do automatically when going from mains to battery power on a
  laptop.
- An icon, that when an additional battery is inserted, updates it's
  display to show two batteries and recalculates how much time
  remaining. Would work for wireless mouse and keyboards, UPS's and
  PDA's.
- A daemon that does a clean shutdown when the battery is critically
  low or does a soft-suspend when you close the lid on your laptop (or
  press the "suspend" button on your PC).
- Tell Totem to use a codec that does low quality processing to
  conserve battery power.
- Postpone indexing of databases (e.g. up2date) or other heavy
  operations until on mains power.
- Presentation programs / movie players don't want the screensaver
  starting or screen blanking.

%description -l pl.UTF-8
Zastosowania infrastruktury zarządcy energii GNOME:
- okno dialogowe ostrzegające użytkownika o zasilaniu z UPS-a,
  automatycznie rozpoczynające uprzejme zamykanie systemu, kiedy
  zasilanie jest w stanie krytycznym
- ikona umożliwiająca użytkownikowi przyciemnienie ekranu LCD przy
  użyciu suwaka i robi to automatycznie przy przełączaniu z głównego
  źródła zasilania na baterie w laptopie
- ikona, która po dołożeniu dodatkowej baterii uaktualnia wskaźnik,
  aby pokazywał dwie baterie i przelicza ilość pozostałego czasu;
  powinna działać dla bezprzewodowych myszy i klawiatur, UPS-ów i PDA
- demon wykonujący czyste zamknięcie systemu kiedy bateria jest w
  stanie krytycznym i wykonujący zamrożenie systemu (soft-suspend)
  przy zamykaniu pokrywy laptopa (albo naciśnięciu przycisku
  "suspend")
- informowanie Totema, aby używał kodeka o niższej jakości w celu
  zaoszczędzenia energii baterii
- wstrzymywanie indeksowania baz danych (np. up2date) i innych
  ciężkich operacji do czasu podłączenia głównego źródła zasilania
- zapobieganie uruchomienia screensaverów i wygaszaniu ekranu podczas
  działania programów prezentacyjnych i odtwarzaczy filmów

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--enable-xevents \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	autostartdir=%{_datadir}/gnome/autostart

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-power-manager.schemas
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall gnome-power-manager.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-power-bugreport.sh
%attr(755,root,root) %{_bindir}/gnome-power-cmd.sh
%attr(755,root,root) %{_bindir}/gnome-power-manager
%attr(755,root,root) %{_bindir}/gnome-power-preferences
%attr(755,root,root) %{_bindir}/gnome-power-statistics
%attr(755,root,root) %{_libdir}/gnome-brightness-applet
%attr(755,root,root) %{_libdir}/gnome-inhibit-applet
%{_libdir}/bonobo/servers/GNOME_BrightnessApplet.server
%{_libdir}/bonobo/servers/GNOME_InhibitApplet.server
%{_datadir}/gnome/autostart/gnome-power-manager.desktop
%{_datadir}/dbus-1/services/gnome-power-manager.service
%{_datadir}/gnome-2.0/ui/GNOME_BrightnessApplet.xml
%{_datadir}/gnome-2.0/ui/GNOME_InhibitApplet.xml
%{_mandir}/man1/*.1*
%{_datadir}/gnome-power-manager
%{_desktopdir}/gnome-power-preferences.desktop
%{_desktopdir}/gnome-power-statistics.desktop
%{_iconsdir}/hicolor/*/*/*
%{_sysconfdir}/gconf/schemas/gnome-power-manager.schemas
