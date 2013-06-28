Name:           hunspell
Version:        1.3.2
Release:        0
License:        (GPL-2.0+ or LGPL-2.1+ or MPL-1.1+) and LGPL-2.1+
Summary:        Hunspell - a spell checker and morphological analyzer library
Url:            http://hunspell.sourceforge.net/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
Source1001: 	hunspell.manifest
BuildRequires:  autoconf >= 2.59
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel >= 5.0
BuildRequires:  pkg-config
BuildRequires:  readline-devel

%description
Hunspell is a spell checker and morphological analyzer library and
program designed for languages with rich morphology and complex word
compounding or character encoding. Hunspell interfaces: Ispell-like
terminal interface using Curses library, Ispell pipe interface,
LibreOffice or OpenOffice.org UNO module.

%package tools
Summary:        Hunspell tools
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description tools
This package contains munch and unmunch programs.

%package devel
Summary:        Files for developing with hunspell
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       libstdc++-devel
Requires:       pkgconfig

%description devel
Includes and definitions for developing with hunspell.

%package static
Summary:        Static hunspell library
Group:          Development/Libraries/Other
Requires:       %{name}-devel = %{version}

%description static
Static hunspell library.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure \
	--with-ui \
	--with-readline
make %{?_smp_mflags}

%check
make check
%install
%make_install
rm -f %{buildroot}%{_bindir}/example
install -m 644 src/tools/{,un}munch.h %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_mandir}/hu
%find_lang %{name}


%post	-p /sbin/ldconfig -p /sbin/ldconfig

%postun	-p /sbin/ldconfig -p /sbin/ldconfig


%docs_package

%files -f %{name}.lang
%manifest %{name}.manifest
%defattr(644,root,root,755)
%doc COPYING license.hunspell license.myspell
%attr(755,root,root) %{_bindir}/hunspell
%attr(755,root,root) %{_libdir}/libhunspell*.so*
%exclude %{_libdir}/libhunspell*.so

%files tools
%manifest %{name}.manifest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/analyze
%attr(755,root,root) %{_bindir}/chmorph
%attr(755,root,root) %{_bindir}/munch
%attr(755,root,root) %{_bindir}/unmunch
%attr(755,root,root) %{_bindir}/hunzip
%attr(755,root,root) %{_bindir}/hzip
%attr(755,root,root) %{_bindir}/affixcompress
%attr(755,root,root) %{_bindir}/ispellaff2myspell
%attr(755,root,root) %{_bindir}/makealias
%attr(755,root,root) %{_bindir}/wordforms
%attr(755,root,root) %{_bindir}/wordlist2hunspell

%files devel
%manifest %{name}.manifest
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhunspell-*.so
%{_includedir}/%{name}
%{_includedir}/munch.h
%{_includedir}/unmunch.h
%{_libdir}/pkgconfig/hunspell.pc

