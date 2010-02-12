Name: postgis
Version: 1.5.0
Release: %mkrel 1
Summary: Geographic objects to the PostgreSQL object-relational database
Source0: http://postgis.refractions.net/download/%{name}-%{version}.tar.gz
URL: http://postgis.refractions.net/
License: GPLv2+
Group: Sciences/Geosciences
Requires: postgresql-plpgsql-virtual >= 0.8.0
Requires: proj
BuildRequires: postgresql-devel >= 0.8.0
BuildRequires: proj
BuildRequires: proj-devel
BuildRequires: geos-devel
BuildRequires: flex
BuildRequires: byacc
BuildRequires: libxslt-proc
BuildRequires: bison
BuildRequires: libxml2-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Geographic objects to the PostgreSQL object-relational database

%prep
%setup -q 

%build
%configure2_5x \
	--datadir=%_datadir/postgis \
	--with-proj \
	--with-geos

make

%install
rm -rf %buildroot
%makeinstall_std
cp utils/postgis*.pl %buildroot/%_bindir

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README.postgis
%{_bindir}/*
%{_datadir}/*
%{_libdir}/postgresql/postgis-1.5.so
