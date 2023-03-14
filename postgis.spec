Summary:	Geographic objects to the PostgreSQL object-relational database
Name:		postgis
Version:	3.3.2
Release:	1
License:	GPLv2+
Group:		Sciences/Geosciences
Url:		http://www.postgis.net
Source0:	http://download.osgeo.org/postgis/source/%{name}-%{version}.tar.gz
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	libxslt-proc
BuildRequires:	proj
BuildRequires:	gdal-devel
BuildRequires:	geos-devel
BuildRequires:	protobuf-c
BuildRequires:	pkgconfig(cunit)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libpq)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(proj)
BuildRequires:	pkgconfig(libpq)
BuildRequires:	pkgconfig(libprotobuf-c)
BuildRequires:	protobuf-c
Requires: 	postgresql-plpgsql
Requires:	proj
# Used to exist in postgis 2.x
%define libname %mklibname lwgeom %{version}
%define devname %mklibname lwgeom -d
Obsoletes:	%{libname} < %{EVRD}
Obsoletes:	%{devname} < %{EVRD}

%description
Geographic objects to the PostgreSQL object-relational database.

%files
%doc COPYING README.postgis
%{_bindir}/*
%{_datadir}/*
%{_libdir}/postgresql/*.so

%prep
%autosetup -p1
export CC=%{__cc}
export CXX=%{__cxx}
export CFLAGS="%{optflags} -DPROTOBUF_USE_DLLS"
export CXXFLAGS="%{optflags} -DPROTOBUF_USE_DLLS -std=gnu++17"
# FIXME figure out why using %%configure here breaks the build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--datadir=%{_datadir}/postgis \
	--with-pgconfig=%{_bindir}/pg_config

%build
%make_build

%install
%make_install

cp utils/postgis*.pl %{buildroot}/%{_bindir}

rm -f %{buildroot}%{_libdir}/liblwgeom.a
