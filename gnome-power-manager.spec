Summary:	GNOME Power Manager
Summary(pl.UTF-8):	Zarządca energii dla GNOME
Name:		gnome-power-manager
Version:	2.19.6
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-power-manager/2.19/%{name}-%{version}.tar.bz2
# Source0-md5:	e8eb02cc9169ba459f4d347110835ef4
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-popt.patch
URL:		http://www.gnome.org/projects/gnome-power-manager/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	gnome-common >= 2.18.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-keyring-devel >= 2.19.91
BuildRequires:	gnome-panel-devel >= 2.19.6
BuildRequires:	gtk+2-devel >= 1:2.10.14
BuildRequires:	gtkunique-devel >= 0.9.1
BuildRequires:	gstreamer-devel >= 0.10.14
BuildRequires:	hal-devel >= 0.5.9
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.19.1
BuildRequires:	libnotify-devel >= 0.4.3
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.19.90
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires:	gnome-session >= 2.19.90
Requires:	notification-daemon >= 0.3.5
Obsoletes:	gnome-power
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
%patch1 -p1

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
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

%find_lang %{name} --all-name --with-gnome

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
%attr(755,root,root) %{_bindir}/gnome-brightness-applet
%attr(755,root,root) %{_bindir}/gnome-inhibit-applet
%attr(755,root,root) %{_bindir}/gnome-power-bugreport.sh
%attr(755,root,root) %{_bindir}/gnome-power-cmd.sh
%attr(755,root,root) %{_bindir}/gnome-power-manager
%attr(755,root,root) %{_bindir}/gnome-power-preferences
%attr(755,root,root) %{_bindir}/gnome-power-statistics
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
%dir %{_omf_dest_dir}/gnome-power-manager
%{_omf_dest_dir}/gnome-power-manager/gnome-power-manager-C.omf
%lang(ca) %{_omf_dest_dir}/gnome-power-manager/gnome-power-manager-ca.omf
%lang(es) %{_omf_dest_dir}/gnome-power-manager/gnome-power-manager-es.omf
%lang(fr) %{_omf_dest_dir}/gnome-power-manager/gnome-power-manager-fr.omf
%lang(hu) %{_omf_dest_dir}/gnome-power-manager/gnome-power-manager-hu.omf
%lang(it) %{_omf_dest_dir}/gnome-power-manager/gnome-power-manager-it.omf
%lang(pa) %{_omf_dest_dir}/gnome-power-manager/gnome-power-manager-pa.omf
%lang(ru) %{_omf_dest_dir}/gnome-power-manager/gnome-power-manager-ru.omf
%lang(sv) %{_omf_dest_dir}/gnome-power-manager/gnome-power-manager-sv.omf
%{_sysconfdir}/gconf/schemas/gnome-power-manager.schemas
