%define libname %mklibname lwgeom 1
%define libdevel %mklibname -d lwgeom

Name: postgis
Version: 1.3.2
Release: %mkrel 6
Summary: Geographic objects to the PostgreSQL object-relational database
Source0: %name-%version.tar.gz
Patch0: postgis-1.3.2-libsonamesql.patch
URL: http://postgis.refractions.net/
License: GPL
Group: Sciences/Geosciences
Requires: postgresql-plpgsql-virtual >= 0.8.0
Requires: %libname = %version
Requires: proj
BuildRequires: postgresql-devel >= 0.8.0
BuildRequires: proj
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

%if %mdkversion < 200900
%post -n %libname  -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-, root, root, 0755)
%_libdir/liblwgeom.so.*

#---------------------------------------------------------

%package -n %libdevel
Summary: Postgis library
Group: Development/Other
Requires: %libname = %version
Provides: %name-devel = %version

%description -n %libdevel
Postgis library.

%files -n %libdevel
%defattr(-, root, root, 0755)
%_libdir/liblwgeom.so

#---------------------------------------------------------

%prep
%setup -q 
%patch0 -p1

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

