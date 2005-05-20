Summary:	GNOME Power Manager
Name:		gnome-power
Version:	0.0.3
Release:	0.2
Epoch:		0
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnome-power/%{name}-%{version}.tar.gz
# Source0-md5:	0f352d463b251a7b8b8a90a82627bb52
URL:		http://gnome-power.sourceforge.net/
BuildRequires:	hal-devel >= 0.5.2
BuildRequires:	libgnomeui-devel >= 2.10.0
BuildRequires:	libwnck-devel >= 2.10.0
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

%prep
%setup -q -n %{name}

%build
autoreconf -i
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-power.schemas

%preun
%gconf_schema_uninstall gnome-power.schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_datadir}/%{name}
%{_desktopdir}/*
