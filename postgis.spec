Name: postgis
Version: 1.5.3
Release: %mkrel 1
Summary: Geographic objects to the PostgreSQL object-relational database
Source0: http://postgis.refractions.net/download/%{name}-%{version}.tar.gz
URL: http://postgis.refractions.net/
License: GPLv2+
Group: Sciences/Geosciences
Requires: postgresql-plpgsql
Requires: proj
BuildRequires: cunit-devel
BuildRequires: postgresql-devel
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
	--datadir=%_datadir/postgis
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
