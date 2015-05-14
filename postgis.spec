%define libname %mklibname lwgeom %{version}
%define devname %mklibname lwgeom -d

Summary:	Geographic objects to the PostgreSQL object-relational database
Name:		postgis
Version:	2.1.7
Release:	1
License:	GPLv2+
Group:		Sciences/Geosciences
Url:		http://www.postgis.net
Source0:	http://download.osgeo.org/postgis/source/%{name}-%{version}.tar.gz
Patch0:		postgis-2.1.0-linkage.patch
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	libxslt-proc
BuildRequires:	proj
BuildRequires:	gdal-devel
BuildRequires:	geos-devel
BuildRequires:	pkgconfig(cunit)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libpq)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(proj)
Requires: 	postgresql-plpgsql
Requires:	proj

%description
Geographic objects to the PostgreSQL object-relational database.

%files
%doc COPYING README.postgis
%{_bindir}/*
%{_datadir}/*
%{_libdir}/postgresql/*.so

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
Shared library for %{name}.

%files -n %{libname}
%{_libdir}/liblwgeom-%{version}.so

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_includedir}/liblwgeom.h
%{_libdir}/liblwgeom.so

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
	--datadir=%{_datadir}/postgis
%make

%install
%makeinstall_std

cp utils/postgis*.pl %{buildroot}/%{_bindir}

rm -f %{buildroot}%{_libdir}/liblwgeom.a

