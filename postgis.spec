%define libname %mklibname lwgeom 1
%define libdevel %mklibname -d lwgeom

Name: postgis
Version: 1.3.1
Release: %mkrel 1
Summary: Geographic objects to the PostgreSQL object-relational database
Source0: %name-%version.tar.gz
URL: http://postgis.refractions.net/
License: GPL
Group: Utilities
Requires: postgresql-plpgsql >= 0.8.0
Requires: %libname = %version
BuildRequires: postgresql-devel >= 0.8.0
BuildRequires: proj-devel
BuildRequires: geos-devel
BuildRequires: flex
BuildRequires: byacc
BuildRequires: libxslt-proc
BuildRequires: bison
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Geographic objects to the PostgreSQL object-relational database

%files
%defattr(-, root, root, 0755)
%doc COPYING README.postgis
%{_bindir}/*
%{_datadir}/*

#---------------------------------------------------------

%package -n %libname
Summary: Postgis library
Group: System/Libraries

%description -n %libname
Postgis library.

%post -n %libname  -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-, root, root, 0755)
%_libdir/liblwgeom.so.*

#---------------------------------------------------------

%package -n %libdevel
Summary: Postgis library
Group: System/Libraries
Requires: %libname = %version
Provides: %name-devel = %version

%description -n %libdevel
Postgis library.

%files -n %libdevel
%defattr(-, root, root, 0755)
%_libdir/liblwgeom.so

#---------------------------------------------------------

%prep
%setup -q -n postgis-cvs 

%build
%configure2_5x \
	--datadir=%_datadir/postgis \
	--with-proj \
	--with-geos

%make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
cp utils/postgis*.pl %{buildroot}/%_bindir

%clean
rm -rf %{buildroot}

