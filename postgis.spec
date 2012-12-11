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


%changelog
* Sun Jun 26 2011 Funda Wang <fwang@mandriva.org> 1.5.3-1mdv2011.0
+ Revision: 687198
- update to new version 1.5.3

* Wed Dec 22 2010 Paulo Andrade <pcpa@mandriva.com.br> 1.5.2-1mdv2011.0
+ Revision: 623743
- Update to latest upstream release

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-2mdv2011.0
+ Revision: 614606
- the mass rebuild of 2010.1 packages

* Thu Apr 29 2010 Emmanuel Andry <eandry@mandriva.org> 1.5.1-1mdv2010.1
+ Revision: 541001
- Nw version 1.5.1

* Fri Feb 12 2010 Funda Wang <fwang@mandriva.org> 1.5.0-1mdv2010.1
+ Revision: 504765
- BR pgsql 8.4 (main package)
- BR xml2
- New version 1.5.0

* Thu Dec 31 2009 Frederik Himpe <fhimpe@mandriva.org> 1.4.1-1mdv2010.1
+ Revision: 484259
- Disable parallel build
- Update to new version 1.4.1
- Remove literal patch: not needed anymore

* Mon Sep 14 2009 Frederik Himpe <fhimpe@mandriva.org> 1.3.6-1mdv2010.0
+ Revision: 440768
- Update to new version 1.3.6

* Wed Feb 18 2009 Helio Chissini de Castro <helio@mandriva.com> 1.3.5-1mdv2009.1
+ Revision: 342613
- Minor update 1.3.5

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.3.2-6mdv2009.0
+ Revision: 259240
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.3.2-5mdv2009.0
+ Revision: 247148
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Apr 01 2008 Helio Chissini de Castro <helio@mandriva.com> 1.3.2-3mdv2008.1
+ Revision: 191459
- Fix invalid library pointers in .sql files, leading postgis to be unable to handle functions.

* Fri Feb 15 2008 Helio Chissini de Castro <helio@mandriva.com> 1.3.2-2mdv2008.1
+ Revision: 168979
- Adding "virtual" in requires of postgres pgplsql

* Sun Feb 10 2008 Helio Chissini de Castro <helio@mandriva.com> 1.3.2-1mdv2008.1
+ Revision: 164980
- Update for stable version 1.3.2

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 24 2007 Helio Chissini de Castro <helio@mandriva.com> 1.3.1-1mdv2008.0
+ Revision: 71039
- Proper groups
- Right provides
- import postgis-1.3.1-1mdv2008.0


