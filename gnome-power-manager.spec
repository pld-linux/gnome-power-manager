Summary:	GNOME Power Manager
Summary(pl):	Zarz±dca energii dla GNOME
Name:		gnome-power
Version:	0.1.0
Release:	1
Epoch:		0
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnome-power/%{name}-%{version}.tar.gz
# Source0-md5:	38bffb73974c355a1d602470b0c92d9d
Patch0:		%{name}-desktop.patch
URL:		http://gnome-power.sourceforge.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	hal-devel >= 0.5.2
BuildRequires:	libgnomeui-devel >= 2.10.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.10.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
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
Zastosowania infrastruktury zarz±dcy energii GNOME:
- okno dialogowe ostrzegaj±ce u¿ytkownika o zasilaniu z UPS-a,
  automatycznie rozpoczynaj±ce uprzejme zamykanie systemu, kiedy
  zasilanie jest w stanie krytycznym
- ikona umo¿liwiaj±ca u¿ytkownikowi przyciemnienie ekranu LCD przy
  u¿yciu suwaka i robi to automatycznie przy prze³±czaniu z g³ównego
  ¼ród³a zasilania na baterie w laptopie
- ikona, która po do³o¿eniu dodatkowej baterii uaktualnia wska¼nik,
  aby pokazywa³ dwie baterie i przelicza ilo¶æ pozosta³ego czasu;
  powinna dzia³aæ dla bezprzewodowych myszy i klawiatur, UPS-ów i PDA
- demon wykonuj±cy czyste zamkniêcie systemu kiedy bateria jest w
  stanie krytycznym i wykonuj±cy zamro¿enie systemu (soft-suspend)
  przy zamykaniu pokrywy laptopa (albo naci¶niêciu przycisku
  "suspend")
- informowanie Totema, aby u¿ywa³ kodeka o ni¿szej jako¶ci w celu
  zaoszczêdzenia energii baterii
- wstrzymywanie indeksowania baz danych (np. up2date) i innych
  ciê¿kich operacji do czasu pod³±czenia g³ównego ¼ród³a zasilania
- zapobieganie uruchomienia screensaverów i wygaszaniu ekranu podczas
  dzia³ania programów prezentacyjnych i odtwarzaczy filmów

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-power.schemas

%preun
%gconf_schema_uninstall gnome-power.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_datadir}/%{name}
%{_desktopdir}/*
