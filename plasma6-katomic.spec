Name:		plasma6-katomic
Version:	24.01.85
Release:	1
Epoch:		1
Summary:	Build complex atoms with a minimal amount of moves
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=katomic
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/katomic-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6KDEGames)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6DBusAddons)

%description
KAtomic is a fun educational game built around molecular geometry.
It employs simplistic two-dimensional looks at different chemical elements.

%files -f katomic.lang
%{_datadir}/knsrcfiles/katomic.knsrc
%{_bindir}/katomic
%{_datadir}/metainfo/org.kde.katomic.appdata.xml
%{_datadir}/applications/org.kde.katomic.desktop
%{_iconsdir}/hicolor/*/apps/katomic.png
%{_datadir}/katomic
%{_datadir}/kconf_update/katomic-levelset*
%{_datadir}/qlogging-categories6/katomic.categories

#------------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang katomic --with-html