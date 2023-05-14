Summary:	GNOME Power Manager
Summary(pl.UTF-8):	Zarządca energii dla GNOME
Name:		gnome-power-manager
Version:	43.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-power-manager/43/%{name}-%{version}.tar.xz
# Source0-md5:	c7e33249b59c6082312909f65739912e
URL:		https://gitlab.gnome.org/GNOME/gnome-power-manager
BuildRequires:	cairo-devel >= 1.0.0
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.46.0
BuildRequires:	gtk+3-devel >= 3.3.8
BuildRequires:	meson >= 0.46.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	upower-devel >= 0.99.8
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.46.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	cairo >= 1.0.0
Requires:	glib2 >= 1:2.46.0
Requires:	gnome-session >= 3.0.0
Requires:	gtk+3 >= 3.3.8
Requires:	hicolor-icon-theme
Requires:	upower >= 0.99.8
Obsoletes:	gnome-power < 0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Uses of GNOME Power Manager infrastructure
- A dialogue that warns the user when on UPS power, that automatically
  begins a kind shutdown when the power gets critically low.
- An icon that allows a user to dim the LCD screen with a slider, and
  does do automatically when going from mains to battery power on a
  laptop.
- An icon, that when an additional battery is inserted, updates its
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
  użyciu suwaka i robiąca to automatycznie przy przełączaniu z głównego
  źródła zasilania na baterie w laptopie
- ikona, która po dołożeniu dodatkowej baterii uaktualnia wskaźnik,
  aby pokazywał dwie baterie i przelicza ilość pozostałego czasu;
  powinna działać dla bezprzewodowych myszy i klawiatur, UPS-ów i PDA
- demon wykonujący czyste zamknięcie systemu, kiedy bateria jest w
  stanie krytycznym i wykonujący zamrożenie systemu (soft-suspend) przy
  zamykaniu pokrywy laptopa (albo naciśnięciu przycisku "suspend")
- informowanie Totema, aby używał kodeka o niższej jakości w celu
  zaoszczędzenia energii baterii
- wstrzymywanie indeksowania baz danych (np. up2date) i innych
  ciężkich operacji do czasu podłączenia głównego źródła zasilania
- zapobieganie uruchomieniu wygaszacza ekranu i samemu wygaszaniu
  ekranu podczas działania programów prezentacyjnych i odtwarzaczy
  filmów

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COMMITMENT MAINTAINERS README.md
%attr(755,root,root) %{_bindir}/gnome-power-statistics
%{_datadir}/glib-2.0/schemas/org.gnome.power-manager.gschema.xml
%{_datadir}/metainfo/org.gnome.PowerStats.appdata.xml
%{_desktopdir}/org.gnome.PowerStats.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.PowerStats.png
%{_iconsdir}/hicolor/scalable/apps/org.gnome.PowerStats.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.PowerStats-symbolic.svg
%{_mandir}/man1/gnome-power-statistics.1*
