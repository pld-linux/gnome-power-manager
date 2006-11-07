Summary:	GNOME Power Manager
Summary(pl):	Zarz�dca energii dla GNOME
Name:		gnome-power-manager
Version:	2.16.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/gnome-power-manager/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	6798ee24e5e94befab5a7584c19771cb
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/projects/gnome-power-manager/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	glib2-devel >= 1:2.12.4
BuildRequires:	gnome-doc-utils
BuildRequires:	hal-devel >= 0.5.7.1
BuildRequires:	libgnomeui-devel >= 2.16.0
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.16.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Obsoletes:	gnome-power
Requires(post,preun):	GConf2
Requires(post,postun):	gtk+2 >= 2:2.10.5
Requires(post,postun):	scrollkeeper
Requires:	gnome-session >= 2.16.1
Requires:	notification-daemon >= 0.3.5
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

%description -l pl
Zastosowania infrastruktury zarz�dcy energii GNOME:
- okno dialogowe ostrzegaj�ce u�ytkownika o zasilaniu z UPS-a,
  automatycznie rozpoczynaj�ce uprzejme zamykanie systemu, kiedy
  zasilanie jest w stanie krytycznym
- ikona umo�liwiaj�ca u�ytkownikowi przyciemnienie ekranu LCD przy
  u�yciu suwaka i robi to automatycznie przy prze��czaniu z g��wnego
  �r�d�a zasilania na baterie w laptopie
- ikona, kt�ra po do�o�eniu dodatkowej baterii uaktualnia wska�nik,
  aby pokazywa� dwie baterie i przelicza ilo�� pozosta�ego czasu;
  powinna dzia�a� dla bezprzewodowych myszy i klawiatur, UPS-�w i PDA
- demon wykonuj�cy czyste zamkni�cie systemu kiedy bateria jest w
  stanie krytycznym i wykonuj�cy zamro�enie systemu (soft-suspend)
  przy zamykaniu pokrywy laptopa (albo naci�ni�ciu przycisku
  "suspend")
- informowanie Totema, aby u�ywa� kodeka o ni�szej jako�ci w celu
  zaoszcz�dzenia energii baterii
- wstrzymywanie indeksowania baz danych (np. up2date) i innych
  ci�kich operacji do czasu pod��czenia g��wnego �r�d�a zasilania
- zapobieganie uruchomienia screensaver�w i wygaszaniu ekranu podczas
  dzia�ania program�w prezentacyjnych i odtwarzaczy film�w

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
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
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/*
%{_datadir}/gnome/autostart/gnome-power-manager.desktop
%{_datadir}/dbus-1/services/*.service
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*
%dir %{_omf_dest_dir}/gnome-power-manager
%{_omf_dest_dir}/gnome-power-manager/gnome-power-manager-C.omf
%lang(ru) %{_omf_dest_dir}/gnome-power-manager/gnome-power-manager-ru.omf
%lang(sv) %{_omf_dest_dir}/gnome-power-manager/gnome-power-manager-sv.omf
%{_sysconfdir}/gconf/schemas/gnome-power-manager.schemas
