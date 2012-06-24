#
# Conditional build:
%bcond_without	gamin	# build without file monitoring
#
Summary:	gMUTOO - elegant service launcher/stopper/monitor
Summary(pl):	gMUTOO - eleganckie narz�dzie do uruchamiania/zatrzymywania/monitorowania us�ug
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

%description -l pl
gMUTOO to eleganckie narz�dzie do uruchamiania, zatrzymywania i
monitorowania us�ug mieszcz�ce si� w zasobniku zarz�dcy okien. By�o
pomy�lane przede wszystkim do uruchamiania demon�w (httpd, ftpd, sshd
itp.), ale mo�e by� u�ywane do uruchamiania i zatrzymywania prawie
wszystkiego.

Dla ka�dego wpisu w menu uruchamiania mo�na poda� plik do
monitorowania (zwykle plik PID). Stan tego pliku (czy istnieje) jest
monitorowany przy u�yciu Gamina (reimplementacji FAM-a); zmiany w
pliku stanu wp�ywaj� na zachowanie gMUTOO, kt�ry wy�wietla stan
us�ugi i umo�liwia szybkie uruchomienie jej je�li jest wy��czona lub
zatrzymanie je�li jest w��czona.

gMUTOO mo�na �atwo zbudowa� bez obs�ugi Gamina, ale wtedy nie ma
monitorowania plik�w (dla ka�dego wpisu w menu gMUTOO udost�pnia wtedy
przyciski start/stop, a u�ytkownik decyduje, czy us�uga powinna by�
w��czona, czy wy��czona).

%prep
%setup -q

%build
%configure \
%if %{without gamin}
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
