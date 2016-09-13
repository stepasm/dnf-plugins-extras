%global _summary %{expand:%{1} Plugin for DNF}
%global _description %{expand:%{summary}. %{1}.}

%{!?dnf_lowest_compatible: %global dnf_lowest_compatible 2.0}
%{!?dnf_not_compatible: %global dnf_not_compatible 3.0}

%bcond_with py3_kickstart

Name:           dnf-plugins-extras
Version:        0.10
Release:        1%{?dist}
Summary:        Extras Plugins for DNF
License:        GPLv2+
URL:            https://github.com/rpm-software-management/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  gettext

BuildRequires:  python2-devel
BuildRequires:  python2-dnf >= %{dnf_lowest_compatible}
BuildRequires:  python2-dnf < %{dnf_not_compatible}
BuildRequires:  python2-nose
%if 0%{?fedora} && 0%{?fedora} < 24
BuildRequires:  python-sphinx
BuildRequires:  pykickstart
%else
BuildRequires:  python-kickstart
BuildRequires:  python2-sphinx
%endif

BuildRequires:  python3-devel
BuildRequires:  python3-dnf >= %{dnf_lowest_compatible}
BuildRequires:  python3-dnf < %{dnf_not_compatible}
BuildRequires:  python3-nose
BuildRequires:  python3-sphinx
BuildRequires:  python3-kickstart

%description
%{summary}.

%package common
Summary:        Common files for %{name} subpackages
Obsoletes:      %{name} < 0.10

%description common
%{summary}.

%package -n python2-%{name}-common
Summary:        Common files for python2-%{name} subpackages
%{?python_provide:%python_provide python2-%{name}-common}
Requires:       python2-dnf >= %{dnf_lowest_compatible}
Requires:       python2-dnf < %{dnf_not_compatible}

%description -n python2-%{name}-common
%{summary}.

%package -n python3-%{name}-common
Summary:        Common files for python3-%{name} subpackages
%{?python_provide:%python_provide python3-%{name}-common}
Requires:       python3-dnf >= %{dnf_lowest_compatible}
Requires:       python3-dnf < %{dnf_not_compatible}

%description -n python3-%{name}-common
%{summary}.

%package -n python2-%{name}-debug
Summary:        %{_summary Debug}
Requires:       python2-%{name}-common = %{?epoch:%{epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python2-%{name}-debug}

%description -n python2-%{name}-debug
%{_description Writes system RPM configuration to a dump file and restores it.}

%package -n python3-%{name}-debug
Summary:        %{_summary Debug}
Requires:       python3-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-debug}
Provides:       dnf-command(debug-dump)
Provides:       dnf-command(debug-restore)
Provides:       %{name}-debug = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}-debug
%{_description Writes system RPM configuration to a dump file and restores it.}


%package -n python2-%{name}-leaves
Summary:        %{_summary Leaves}
Requires:       python2-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python2-%{name}-leaves}

%description -n python2-%{name}-leaves
%{_description List all installed packages not required by any other installed package.}

%package -n python3-%{name}-leaves
Summary:        %{_summary Leaves}
Requires:       python3-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-leaves}
Provides:       dnf-command(leaves)
Provides:       %{name}-leaves = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}-leaves
%{_description List all installed packages not required by any other installed package.}


%package -n python2-%{name}-local
Summary:        %{_summary Local}
Requires:       python2-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python2-%{name}-local}

%description -n python2-%{name}-local
%{_description Automatically copy all downloaded packages to a repository on the local filesystem and generating repo metadata.}

%package -n python3-%{name}-local
Summary:        %{_summary Local}
Requires:       python3-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-local}
Provides:       dnf-command(local)
Provides:       %{name}-local = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}-local
%{_description Automatically copy all downloaded packages to a repository on the local filesystem and generating repo metadata.}


%package -n python2-%{name}-migrate
Summary:        %{_summary Migrate}
Requires:       python2-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python2-%{name}-migrate}

%description -n python2-%{name}-migrate
%{_description Migrates yum's history, group and yumdb data to dnf.}


%package -n python2-%{name}-kickstart
Summary:        %{_summary Kickstart}
Requires:       python2-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python2-%{name}-kickstart}

%description -n python2-%{name}-kickstart
%{_description Install packages listed in a Kickstart file.}

%package -n python3-%{name}-kickstart
Summary:        %{_summary Kickstart}
Requires:       python3-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-kickstart}
Requires:       python3-kickstart
Provides:       dnf-command(kickstart)
Provides:       %{name}-kickstart = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}-kickstart
%{_description Install packages listed in a Kickstart file.}


%package -n python2-%{name}-repoclosure
Summary:        %{_summary Repoclosure}
Requires:       python2-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python2-%{name}-repoclosure}

%description -n python2-%{name}-repoclosure
%{_description Display a list of unresolved dependencies for repositories.}

%package -n python3-%{name}-repoclosure
Summary:        %{_summary Repoclosure}
Requires:       python3-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-repoclosure}
Provides:       dnf-command(repoclosure)
Provides:       %{name}-repoclosure = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}-repoclosure
%{_description Display a list of unresolved dependencies for repositories.}


%package -n python2-%{name}-repograph
Summary:        %{_summary Repograph}
Requires:       python2-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python2-%{name}-repograph}

%description -n python2-%{name}-repograph
%{_description Output a full package dependency graph in dot format.}

%package -n python3-%{name}-repograph
Summary:        %{_summary Repograph}
Requires:       python3-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-repograph}
Provides:       dnf-command(repograph)
Provides:       %{name}-repograph = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}-repograph
%{_description Output a full package dependency graph in dot format.}


%package -n python2-%{name}-repomanage
Summary:        %{_summary Repomanage}
Requires:       python2-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python2-%{name}-repomanage}

%description -n python2-%{name}-repomanage
%{_description Manage a directory of rpm packages.}

%package -n python3-%{name}-repomanage
Summary:        %{_summary Repomanage}
Requires:       python3-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-repomanage}
Provides:       dnf-command(repomanage)
Provides:       %{name}-repomanage = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}-repomanage
%{_description Manage a directory of rpm packages.}


%package -n python3-%{name}-rpmconf
Summary:        %{_summary RpmConf}
Requires:       python3-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-rpmconf}
Provides:       dnf-command(rpmconf)
Provides:       %{name}-rpmconf = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}-rpmconf
%{_description Handles .rpmnew, .rpmsave every transaction.}


%package -n python2-%{name}-show-leaves
Summary:        %{_summary Leaves}
Requires:       python2-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
Requires:       python2-%{name}-leaves = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python2-%{name}-show-leaves}

%description -n python2-%{name}-show-leaves
%{_description List all installed packages that are no longer required by any other installed package after a transaction.}

%package -n python3-%{name}-show-leaves
Summary:        %{_summary Leaves}
Requires:       python3-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
Requires:       python3-%{name}-leaves = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-show-leaves}
Provides:       dnf-command(show-leaves)
Provides:       %{name}-show-leaves = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}-show-leaves
%{_description List all installed packages that are no longer required by any other installed package after a transaction.}


%package -n python2-%{name}-snapper
Summary:        %{_summary Repomanage}
Requires:       python2-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
Requires:       dbus-python
Requires:       snapper
%{?python_provide:%python_provide python2-%{name}-snapper}

%description -n python2-%{name}-snapper
%{_description Creates snapshot every transaction.}

%package -n python3-%{name}-snapper
Summary:        %{_summary Repomanage}
Requires:       python3-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
Requires:       python3-dbus
Requires:       snapper
%{?python_provide:%python_provide python3-%{name}-snapper}
Provides:       dnf-command(snapper)
Provides:       %{name}-snapper = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}-snapper
%{_description Creates snapshot every transaction.}


%package -n python2-%{name}-tracer
Summary:        %{_summary Tracer}
Requires:       python2-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
Requires:       tracer
%{?python_provide:%python_provide python2-%{name}-tracer}

%description -n python2-%{name}-tracer
%{_description Finds outdated running applications in your system every transaction.}

%package -n python3-%{name}-tracer
Summary:        %{_summary Tracer}
Requires:       python3-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
Requires:       tracer
%{?python_provide:%python_provide python3-%{name}-tracer}
Provides:       dnf-command(tracer)
Provides:       %{name}-tracer = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}-tracer
%{_description Finds outdated running applications in your system every transaction.}


%package -n python2-%{name}-versionlock
Summary:        %{_summary Versionlock}
Requires:       python2-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python2-%{name}-versionlock}

%description -n python2-%{name}-versionlock
%{_description Versionlock plugin takes a set of name/versions for packages and excludes all other versions of those packages. This allows you to e.g. protect packages from being updated by newer versions.}

%package -n python3-%{name}-versionlock
Summary:        %{_summary Versionlock}
Requires:       python3-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-versionlock}
Provides:       dnf-command(versionlock)
Provides:       %{name}-versionlock = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}-versionlock
%{_description Versionlock plugin takes a set of name/versions for packages and excludes all other versions of those packages. This allows you to e.g. protect packages from being updated by newer versions.}


%package -n python2-%{name}-system-upgrade
Summary:        %{_summary System Upgrade}
Requires:       python2-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python2-%{name}-system-upgrade}

%description -n python2-%{name}-system-upgrade
%{_description This package provides the "system-upgrade" command.}

%package -n python3-%{name}-system-upgrade
Summary:        %{_summary System Upgrade}
Requires:       python3-%{name}-common = %{?epoch:%{?epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python3-%{name}-system-upgrade}
Provides:       dnf-command(system-upgrade)
Provides:       %{name}-system-upgrade = %{?epoch:%{epoch}:}%{version}-%{release}

Provides:   fedup = %{?epoch:%{epoch}}%{version}-%{release}
Obsoletes:  fedup < 0.10
Obsoletes:  fedup-dracut

Obsoletes:  dnf-plugin-system-upgrade < 0.10
Obsoletes:  python3-dnf-plugin-system-upgrade < 0.10
Conflicts:  PackageKit < 1.0.8

BuildRequires:  python3-systemd
Requires:       python3-systemd

%description -n python3-%{name}-system-upgrade
%{_description This package provides the "system-upgrade" command.}


%prep
%autosetup
mkdir python2 python3

%build
pushd python2
  %cmake ..
  %make_build
  make doc-man
popd
pushd python3
  %cmake -DPYTHON_DESIRED:str=3 ..
  %make_build
  make doc-man
popd

%install
pushd python2
  %make_install
popd
pushd python3
  %make_install
popd

%find_lang %{name}

%check
PYTHONPATH="%{buildroot}%{python2_sitelib}:%{buildroot}%{python2_sitelib}/dnf-plugins/" nosetests-%{python2_version} -s tests/
PYTHONPATH="%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitelib}/dnf-plugins/" nosetests-%{python3_version} -s tests/

%files common -f %{name}.lang
%license COPYING
%doc README.rst
%{_mandir}/man8/dnf.plugin.*

%files -n python2-%{name}-common
%{python2_sitelib}/dnfpluginsextras/

%files -n python3-%{name}-common
%{python3_sitelib}/dnfpluginsextras/

%files -n python2-%{name}-debug
%{python2_sitelib}/dnf-plugins/debug.*

%files -n python3-%{name}-debug
%{python3_sitelib}/dnf-plugins/debug.py
%{python3_sitelib}/dnf-plugins/__pycache__/debug.*

%files -n python2-%{name}-leaves
%{python2_sitelib}/dnf-plugins/leaves.*

%files -n python3-%{name}-leaves
%{python3_sitelib}/dnf-plugins/leaves.py
%{python3_sitelib}/dnf-plugins/__pycache__/leaves.*

%files -n python2-%{name}-local
%config %{_sysconfdir}/dnf/plugins/local.conf
%{python2_sitelib}/dnf-plugins/local.*

%files -n python3-%{name}-local
%config %{_sysconfdir}/dnf/plugins/local.conf
%{python3_sitelib}/dnf-plugins/local.py
%{python3_sitelib}/dnf-plugins/__pycache__/local.*

%files -n python2-%{name}-migrate
%{python2_sitelib}/dnf-plugins/migrate.*

%files -n python2-%{name}-kickstart
%{python2_sitelib}/dnf-plugins/kickstart.py*

%files -n python3-%{name}-kickstart
%{python3_sitelib}/dnf-plugins/kickstart.py
%{python3_sitelib}/dnf-plugins/__pycache__/kickstart.*

%files -n python2-%{name}-repoclosure
%{python2_sitelib}/dnf-plugins/repoclosure.*

%files -n python3-%{name}-repoclosure
%{python3_sitelib}/dnf-plugins/repoclosure.py
%{python3_sitelib}/dnf-plugins/__pycache__/repoclosure.*

%files -n python2-%{name}-repograph
%{python2_sitelib}/dnf-plugins/repograph.*

%files -n python3-%{name}-repograph
%{python3_sitelib}/dnf-plugins/repograph.py
%{python3_sitelib}/dnf-plugins/__pycache__/repograph.*

%files -n python2-%{name}-repomanage
%{python2_sitelib}/dnf-plugins/repomanage.*

%files -n python3-%{name}-repomanage
%{python3_sitelib}/dnf-plugins/repomanage.py
%{python3_sitelib}/dnf-plugins/__pycache__/repomanage.*

%files -n python3-%{name}-rpmconf
%config(noreplace) %{_sysconfdir}/dnf/plugins/rpmconf.conf
%{python3_sitelib}/dnf-plugins/rpm_conf.py
%{python3_sitelib}/dnf-plugins/__pycache__/rpm_conf.*

%files -n python2-%{name}-show-leaves
%{python2_sitelib}/dnf-plugins/show_leaves.*

%files -n python3-%{name}-show-leaves
%{python3_sitelib}/dnf-plugins/show_leaves.py
%{python3_sitelib}/dnf-plugins/__pycache__/show_leaves.*

%files -n python2-%{name}-snapper
%{python2_sitelib}/dnf-plugins/snapper.*

%files -n python3-%{name}-snapper
%{python3_sitelib}/dnf-plugins/snapper.py
%{python3_sitelib}/dnf-plugins/__pycache__/snapper.*

%files -n python2-%{name}-tracer
%{python2_sitelib}/dnf-plugins/tracer.*

%files -n python3-%{name}-tracer
%{python3_sitelib}/dnf-plugins/tracer.py
%{python3_sitelib}/dnf-plugins/__pycache__/tracer.*

%files -n python2-%{name}-versionlock
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.list
%{python2_sitelib}/dnf-plugins/versionlock.*

%files -n python3-%{name}-versionlock
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.list
%{python3_sitelib}/dnf-plugins/versionlock.py
%{python3_sitelib}/dnf-plugins/__pycache__/versionlock.*

%files -n python2-%{name}-system-upgrade
%{python2_sitelib}/dnf-plugins/system_upgrade.*
%{_unitdir}/dnf-system-upgrade.service
%dir %{_unitdir}/system-update.target.wants
%{_unitdir}/system-update.target.wants/dnf-system-upgrade.service

%files -n python3-%{name}-system-upgrade
%{python3_sitelib}/dnf-plugins/system_upgrade.py
%{python3_sitelib}/dnf-plugins/__pycache__/system_upgrade.*
%{_unitdir}/dnf-system-upgrade.service
%dir %{_unitdir}/system-update.target.wants
%{_unitdir}/system-update.target.wants/dnf-system-upgrade.service

%changelog
