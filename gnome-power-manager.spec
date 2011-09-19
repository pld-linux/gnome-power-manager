Summary:	GNOME Power Manager
Summary(pl.UTF-8):	Zarządca energii dla GNOME
Name:		gnome-power-manager
Version:	3.1.92
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-power-manager/3.1/%{name}-%{version}.tar.xz
# Source0-md5:	4f191b5571c3e7d8782858ce8a3fffba
URL:		http://www.gnome.org/projects/gnome-power-manager/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.0.0
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-utils
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	scrollkeeper
BuildRequires:	tar >= 1:1.22
BuildRequires:	upower-devel >= 0.9.1
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.28.0
Requires(post,postun):	scrollkeeper
Requires:	gnome-icon-theme
Requires:	gnome-session >= 3.0.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	upower >= 0.9.1
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
  użyciu suwaka i robiąca to automatycznie przy przełączaniu z
  głównego źródła zasilania na baterie w laptopie
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
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-silent-rules \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_icon_cache hicolor
%update_icon_cache gnome
%glib_compile_schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor
%update_icon_cache gnome
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-power-statistics
%{_mandir}/man1/*.1*
%{_datadir}/glib-2.0/schemas/org.gnome.power-manager.gschema.xml
%{_datadir}/gnome-power-manager
%{_desktopdir}/gnome-power-statistics.desktop
%{_iconsdir}/hicolor/*/*/*
