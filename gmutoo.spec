#
# Conditional build:
%bcond_without	gamin	# build without file monitoring
#
Summary:	gMUTOO - elegant service launcher/stopper/monitor
Summary(pl.UTF-8):	gMUTOO - eleganckie narzędzie do uruchamiania/zatrzymywania/monitorowania usług
Name:		gmutoo
Version:	0.1
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.develia.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	44453caf4551682a957eb3fe48d9de76
URL:		http://www.develia.org/
%if %{with gamin}
BuildRequires:	gamin-devel >= 0.1.7
%endif
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	gtk+2-devel >= 2:2.6
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gMUTOO is an elegant service launcher/stopper/monitor that resides in
the window manager tray. It has been mostly thought for the launch of
daemons (httpd, ftpd, sshd and so on), but it can be used to
start/stop pretty anything.

For each entry of its launch menu, a monitored file can be specified
(usually a PID file). The status of this file (exists/doesn't exist)
is monitored with Gamin (a FAM re-implementation); changes in the file
status influence the behaviour of gMUTOO, that displays the status of
the service and allows to quickly start it if the status is 'off' and
to stop it if the status is 'on'.

gMUTOO can also be compiled without Gamin support, but the file
monitor won't be available in this case (for each entry in its menu,
gMUTOO will then provide start/stop buttons so the user can decide if
a service should be started or stopped).

%description -l pl.UTF-8
gMUTOO to eleganckie narzędzie do uruchamiania, zatrzymywania i
monitorowania usług mieszczące się w zasobniku zarządcy okien. Było
pomyślane przede wszystkim do uruchamiania demonów (httpd, ftpd, sshd
itp.), ale może być używane do uruchamiania i zatrzymywania prawie
wszystkiego.

Dla każdego wpisu w menu uruchamiania można podać plik do
monitorowania (zwykle plik PID). Stan tego pliku (czy istnieje) jest
monitorowany przy użyciu Gamina (reimplementacji FAM-a); zmiany w
pliku stanu wpływają na zachowanie gMUTOO, który wyświetla stan
usługi i umożliwia szybkie uruchomienie jej jeśli jest wyłączona lub
zatrzymanie jeśli jest włączona.

gMUTOO można łatwo zbudować bez obsługi Gamina, ale wtedy nie ma
monitorowania plików (dla każdego wpisu w menu gMUTOO udostępnia wtedy
przyciski start/stop, a użytkownik decyduje, czy usługa powinna być
włączona, czy wyłączona).

%prep
%setup -q

%build
%configure \
%if !%{with gamin}
	--disable-monitor
%endif


%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%lang(it) %doc README.it
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}_icon.xpm
