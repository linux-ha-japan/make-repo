###############################################################################
###############################################################################
##
##  Copyright (C) 2004-2011 Red Hat, Inc.  All rights reserved.
##
##  This copyrighted material is made available to anyone wishing to use,
##  modify, copy, or redistribute it subject to the terms and conditions
##  of the GNU General Public License v.2.
##
###############################################################################
###############################################################################

# keep around ready for later user
## global alphatag git0a6184070

%global bundled_lib_dir    bundled

# google cloud
# python-google-api-client bundle
%global googleapiclient		google-api-python-client
%global googleapiclient_version	1.6.3
%global googleapiclient_dir	%{bundled_lib_dir}/gce/%{googleapiclient}
# python-oauth2client bundle
%global oauth2client		oauth2client
%global oauth2client_version	4.0.0
%global oauth2client_dir	%{bundled_lib_dir}/gce/%{oauth2client}
# python-httplib2 bundle
%global httplib2		httplib2
%global httplib2_version	0.9.1
%global httplib2_dir		%{bundled_lib_dir}/gce/%{httplib2}
# python-fasteners bundle
%global fasteners		fasteners
%global fasteners_version	0.9.0
%global fasteners_dir		%{bundled_lib_dir}/gce/%{fasteners}
# python-keyring bundle
%global keyring			keyring
%global keyring_version		5.0
%global keyring_dir		%{bundled_lib_dir}/gce/%{keyring}
# python-gflags bundle
%global gflags			gflags
%global gflags_version		2.0
%global gflags_dir		%{bundled_lib_dir}/gce/%{gflags}
# python-uritemplate bundle
%global uritemplate		uritemplate
%global uritemplate_version	3.0.0
%global uritemplate_dir		%{bundled_lib_dir}/gce/%{uritemplate}

# alibaba
# python-pycryptodome bundle
%global pycryptodome		pycryptodome
%global pycryptodome_version	3.6.4
%global pycryptodome_dir	%{bundled_lib_dir}/aliyun/%{pycryptodome}
# python-aliyun-sdk-core bundle
%global aliyunsdkcore		aliyun-python-sdk-core
%global aliyunsdkcore_version	2.8.5
%global aliyunsdkcore_dir	%{bundled_lib_dir}/aliyun/%{aliyunsdkcore}
# python-aliyun-sdk-ecs bundle
%global aliyunsdkecs		aliyun-python-sdk-ecs
%global aliyunsdkecs_version	4.9.3
%global aliyunsdkecs_dir	%{bundled_lib_dir}/aliyun/%{aliyunsdkecs}
# python-aliyun-sdk-vpc bundle
%global aliyunsdkvpc		aliyun-python-sdk-vpc
%global aliyunsdkvpc_version	3.0.2
%global aliyunsdkvpc_dir	%{bundled_lib_dir}/aliyun/%{aliyunsdkvpc}

Name: fence-agents
Summary: Fence Agents for Red Hat Cluster
Version: 4.2.1
Release: 11%{?alphatag:.%{alphatag}}%{?dist}.8
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
URL: https://github.com/ClusterLabs/fence-agents
Source0: https://fedorahosted.org/releases/f/e/fence-agents/%{name}-%{version}.tar.gz
Source1: https://pypi.python.org/packages/16/00/a6913a2e6eb3d5b1cc3538c3492ccd2b39a6d79367432d46cea1ec74170d/%{googleapiclient}-%{googleapiclient_version}.tar.gz
Source2: https://github.com/google/%{oauth2client}/archive/v%{oauth2client_version}.tar.gz#/%{oauth2client}-%{oauth2client_version}.tar.gz
Source3: https://pypi.python.org/packages/source/h/%{httplib2}/%{httplib2}-%{httplib2_version}.tar.gz
Source4: https://codeload.github.com/harlowja/fasteners/tar.gz/%{fasteners_version}#/%{fasteners}-%{fasteners_version}.tar.gz
Source5: http://pypi.python.org/packages/source/k/keyring/%{keyring}-%{keyring_version}.zip
Source6: https://github.com/gflags/python-gflags/archive/python-%{gflags}-%{gflags_version}.tar.gz#/python-%{gflags}-%{gflags_version}.tar.gz
Source7: https://github.com/sigmavirus24/%{uritemplate}/archive/%{uritemplate_version}/%{uritemplate}-%{uritemplate_version}.tar.gz
Source8: %{pycryptodome}-%{pycryptodome_version}.tar.gz
Source9: %{aliyunsdkcore}-%{aliyunsdkcore_version}.tar.gz
Source10: %{aliyunsdkecs}-%{aliyunsdkecs_version}.tar.gz
Source11: %{aliyunsdkvpc}-%{aliyunsdkvpc_version}.tar.gz
Patch0: bz1579391-fence_impilan-fence_ilo_ssh-add-ilo5-support.patch
Patch1: bz1504202-fence_mpath-watchdog-support.patch
Patch2: bz1236395-1-fence_scsi-fence_scsi_check.pl-link.patch
Patch3: bz1236395-2-fence_ilo3-fence_ipmilan-show-correct-default-method.patch
Patch4: bz1549699-1-fence_evacuate-fix-evacuable-tag-mix-issue.patch
Patch5: bz1549699-2-fence_compute-fence_evacuate-fix-compute-domain.patch
Patch6: bz1568753-1-fence_gce-stackdriver-logging-default-method-cycle.patch
Patch7: bz1568753-2-fence_gce-filter-aggregatedlist.patch
Patch8: bz1568753-3-fence_gce-stackdriver-logging-note.patch
Patch9: bz1568742-1-fence_aliyun.patch
Patch10: bz1568742-2-fence_aliyun.patch
Patch11: bz1568742-3-fence_aliyun-logging.patch
Patch12: bz1568742-4-fence_aliyun-bundled.patch
Patch13: bz1236395-3-fix-version.patch
Patch14: bz1622229-1-fence_aliyun-list-instance-names.patch
Patch15: bz1622229-2-fence_aliyun-correct-help-indentation.patch
Patch16: bz1625164-fence_cisco_ucs-encode-POSTFIELDS.patch
Patch17: bz1647522-fence_scsi-fix-incorrect-SCSI-key-node-ID-10-or-higher.patch
Patch18: bz1654172-1-fence_scsi-watchdog-retry-support.patch
Patch19: bz1654172-2-build-fix-check_used_options.patch
Patch20: bz1652115-fence_hpblade-fix-log_expect-syntax.patch
Patch21: bz1666848-1-fence_redfish.patch
Patch22: bz1666848-2-fence_redfish-fail-invalid-cert.patch
Patch23: bz1708547-fence_rhevm-RHEV-v4-API-support.patch
Patch24: bz1709110-fence_azure_arm-skip_shutdown.patch
# bundle patches
Patch1000: bz1568753-4-fence_gce-bundled-libs.patch
Patch1001: bz1568753-5-%{oauth2client}-docs-build-fix.patch
Patch1002: bz1568753-6-%{oauth2client}-python-rsa-to-cryptography.patch
Patch1003: python-%{httplib2}.certfile.patch
Patch1004: python-%{httplib2}.getCertHost.patch
Patch1005: python-%{httplib2}.rfc2459.patch
Patch1006: python-%{httplib2}-0.9-proxy-http.patch
Patch1007: python-%{httplib2}-0.9-cve-2013-2037.patch
Patch1008: bz1568753-7-%{keyring}-fix-gnome-version-warning.patch

%if 0%{?rhel}
%global supportedagents amt_ws apc apc_snmp bladecenter brocade cisco_mds cisco_ucs compute drac5 eaton_snmp emerson eps evacuate hpblade ibmblade ifmib ilo ilo_moonshot ilo_mp ilo_ssh intelmodular ipdu ipmilan mpath kdump redfish rhevm rsa rsb sbd scsi vmware_rest vmware_soap wti
%ifarch x86_64
%global testagents virsh heuristics_ping aliyun aws azure_arm gce
%endif
%ifarch ppc64le
%global testagents virsh lpar heuristics_ping
%endif
%ifarch s390x
%global testagents virsh zvm heuristics_ping
%endif
%ifnarch x86_64 ppc64le s390x
%global testagents virsh heuristics_ping
%endif

%global allfenceagents fence-agents-amt-ws fence-agents-apc fence-agents-apc-snmp fence-agents-bladecenter fence-agents-brocade fence-agents-cisco-mds fence-agents-cisco-ucs fence-agents-compute fence-agents-drac5 fence-agents-eaton-snmp fence-agents-emerson fence-agents-eps fence-agents-heuristics-ping fence-agents-hpblade fence-agents-ibmblade fence-agents-ifmib fence-agents-ilo2 fence-agents-ilo-moonshot fence-agents-ilo-mp fence-agents-ilo-ssh fence-agents-intelmodular fence-agents-ipdu fence-agents-ipmilan fence-agents-mpath fence-agents-kdump fence-agents-redfish fence-agents-rhevm fence-agents-rsa fence-agents-rsb fence-agents-sbd fence-agents-scsi fence-agents-vmware-rest fence-agents-vmware-soap fence-agents-wti
%endif

## Setup/build bits

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# Build dependencies
BuildRequires: glibc-devel
BuildRequires: gnutls-utils
BuildRequires: libxslt
BuildRequires: python pexpect python-pycurl python-suds python-requests python-boto3
BuildRequires: net-snmp-utils
BuildRequires: autoconf automake libtool
BuildRequires: iputils

# python-google-api-client bundle
BuildRequires:  python-devel >= 2.7
BuildRequires:  python-setuptools
BuildRequires:  python-six >= 1.6.1

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1 -F2
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1 -F2
%patch24 -p1

%ifarch x86_64
# bundles
mkdir -p %{bundled_lib_dir}/aliyun
mkdir -p %{bundled_lib_dir}/gce

# python-google-api-client bundle
tar -xzf %SOURCE1 -C %{bundled_lib_dir}
mv %{bundled_lib_dir}/%{googleapiclient}-%{googleapiclient_version} %{googleapiclient_dir}
cp %{googleapiclient_dir}/LICENSE %{googleapiclient}_LICENSE

# python-oauth2client bundle
tar -xzf %SOURCE2 -C %{bundled_lib_dir}
mv %{bundled_lib_dir}/%{oauth2client}-%{oauth2client_version} %{oauth2client_dir}
cp %{oauth2client_dir}/LICENSE %{oauth2client}_LICENSE
cp %{oauth2client_dir}/README.md %{oauth2client}_README.md

# python-httplib2 bundle
tar -xzf %SOURCE3 -C %{bundled_lib_dir}
mv %{bundled_lib_dir}/%{httplib2}-%{httplib2_version} %{httplib2_dir}

# python-fasteners bundle
tar -xzf %SOURCE4 -C %{bundled_lib_dir}
mv %{bundled_lib_dir}/%{fasteners}-%{fasteners_version} %{fasteners_dir}
cp %{fasteners_dir}/LICENSE %{fasteners}_LICENSE
cp %{fasteners_dir}/README.rst %{fasteners}_README.rst

# python-keyring bundle
unzip %SOURCE5 -d %{bundled_lib_dir}
mv %{bundled_lib_dir}/%{keyring}-%{keyring_version} %{keyring_dir}
cp %{keyring_dir}/README.rst %{keyring}_README.rst

# python-gflags bundle
tar -xzf %SOURCE6 -C %{bundled_lib_dir}
mv %{bundled_lib_dir}/python-%{gflags}-%{gflags_version} %{gflags_dir}
cp %{gflags_dir}/README %{gflags}_README

# python-uritemplate bundle
tar -xzf %SOURCE7 -C %{bundled_lib_dir}
mv %{bundled_lib_dir}/%{uritemplate}-%{uritemplate_version} %{uritemplate_dir}
cp %{uritemplate_dir}/LICENSE %{uritemplate}_LICENSE
cp %{uritemplate_dir}/LICENSE.APACHE %{uritemplate}_LICENSE.APACHE
cp %{uritemplate_dir}/LICENSE.BSD %{uritemplate}_LICENSE.BSD
cp %{uritemplate_dir}/README.rst %{uritemplate}_README.rst

# python-pycryptodome bundle
tar -xzf %SOURCE8 -C %{bundled_lib_dir}
mv %{bundled_lib_dir}/%{pycryptodome}-%{pycryptodome_version} %{pycryptodome_dir}
cp %{pycryptodome_dir}/README.rst %{pycryptodome}_README.rst
cp %{pycryptodome_dir}/LICENSE.rst %{pycryptodome}_LICENSE.rst

# python-aliyun-sdk-core bundle
tar -xzf %SOURCE9 -C %{bundled_lib_dir}
mv %{bundled_lib_dir}/%{aliyunsdkcore}-%{aliyunsdkcore_version} %{aliyunsdkcore_dir}
cp %{aliyunsdkcore_dir}/README.rst %{aliyunsdkcore}_README.rst

# python-aliyun-sdk-ecs bundle
tar -xzf %SOURCE10 -C %{bundled_lib_dir}
mv %{bundled_lib_dir}/%{aliyunsdkecs}-%{aliyunsdkecs_version} %{aliyunsdkecs_dir}
cp %{aliyunsdkecs_dir}/README.rst %{aliyunsdkecs}_README.rst

# python-aliyun-sdk-vpc bundle
tar -xzf %SOURCE11 -C %{bundled_lib_dir}
mv %{bundled_lib_dir}/%{aliyunsdkvpc}-%{aliyunsdkvpc_version} %{aliyunsdkvpc_dir}
cp %{aliyunsdkvpc_dir}/README.rst %{aliyunsdkvpc}_README.rst

# fence_gce: append bundled-directory to search path
%patch1000 -p1

# python-google-api-client bundle
pushd %{googleapiclient_dir}
# remove egg info
rm -rf google_api_python_client.egg-info
# remove shebang without touching timestamp
for lib in googleapiclient/*.py; do
 sed '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
popd

# python-oauth2client bundle
pushd %{oauth2client_dir}
%patch1001 -p1 -b .doc
# replace python-rsa with python-cryptography
%patch1002 -p1

# Remove the version constraint on httplib2.  From reading upstream's git log,
# it seems the only reason they require a new version is to force python3
# support.  That doesn't affect us on EPEL7, so we can loosen the constraint.
sed -i 's/httplib2>=0.9.1/httplib2/' setup.py

# We do not have the package for google.appengine support
# This is removed because it breaks the docs build otherwise
rm -f docs/source/oauth2client.contrib.appengine.rst oauth2client/appengine.py
popd

# python-httplib2 bundle
pushd %{httplib2_dir}
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1
%patch1006 -p1
%patch1007 -p1
popd

# python-keyring bundle
pushd %{keyring_dir}
%patch1008 -p1
rm -frv keyring.egg-info
# Drop redundant shebangs.
sed -i '1{\@^#!/usr/bin/env python@d}' keyring/cli.py
# Drop slags from upstream of using his own versioning system.
sed -i -e "\@use_vcs_version@s/^.*$/\tversion = \"%{version}\",/g" \
       -e "/'hgtools'/d" setup.py
popd

# python-gflags bundle
pushd %{gflags_dir}
sed -i '1s|^#!/usr/bin/env python$|#!%{__python2}|' gflags2man.py
sed -i '/^#!\/usr\/bin\/env python$/,+1 d' gflags*.py
popd

# python-uritemplate bundle
pushd %{uritemplate_dir}
# remove egg info
rm -rf uritemplate.egg-info
popd
%endif

%build
./autogen.sh
%{configure} --with-agents='%{supportedagents} %{testagents}'
CFLAGS="$(echo '%{optflags}')" make %{_smp_mflags}

%ifarch x86_64
# python-google-api-client bundle
pushd %{googleapiclient_dir}
%{__python2} setup.py build
popd

# python-oauth2client bundle
pushd %{oauth2client_dir}
%{__python2} setup.py build
popd

# python-httplib2 bundle
pushd %{httplib2_dir}
%{__python2} setup.py build
popd

# python-fasteners bundle
pushd %{fasteners_dir}
%{__python2} setup.py build
popd

# python-keyring bundle
pushd %{keyring_dir}
%{__python2} setup.py build
popd

# python-gflags bundle
pushd %{gflags_dir}
%{__python2} setup.py build
popd

# python-uritemplate bundle
pushd %{uritemplate_dir}
%{__python2} setup.py build
popd

# python-pycryptodome bundle
pushd %{pycryptodome_dir}
%{__python2} setup.py build
popd

# python-aliyun-sdk-core bundle
pushd %{aliyunsdkcore_dir}
%{__python2} setup.py build
popd

# python-aliyun-sdk-ecs bundle
pushd %{aliyunsdkecs_dir}
%{__python2} setup.py build
popd

# python-aliyun-sdk-vpc bundle
pushd %{aliyunsdkvpc_dir}
%{__python2} setup.py build
popd
%endif

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%ifarch x86_64
# python-google-api-client bundle
pushd %{googleapiclient_dir}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/gce
popd

# python-oauth2client bundle
pushd %{oauth2client_dir}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/gce
popd

# python-httplib2 bundle
pushd %{httplib2_dir}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/gce
popd

# python-fasteners bundle
pushd %{fasteners_dir}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/gce
popd

# python-keyring bundle
pushd %{keyring_dir}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/gce
popd

# python-gflags bundle
pushd %{gflags_dir}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/gce
mv %{buildroot}%{_bindir}/gflags2man.py  %{buildroot}%{_bindir}/gflags2man
chmod +x %{buildroot}%{_bindir}/gflags2man
popd

# python-uritemplate bundle
pushd %{uritemplate_dir}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/gce
popd

# python-pycryptodome bundle
pushd %{pycryptodome_dir}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/aliyun
popd

# python-aliyun-sdk-core bundle
pushd %{aliyunsdkcore_dir}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/aliyun
popd

# python-aliyun-sdk-ecs bundle
pushd %{aliyunsdkecs_dir}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/aliyun
popd

# python-aliyun-sdk-vpc bundle
pushd %{aliyunsdkvpc_dir}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot} --install-lib /usr/lib/fence-agents/%{bundled_lib_dir}/aliyun
popd
%endif

## tree fix up
# remove docs
rm -rf %{buildroot}/usr/share/doc/fence-agents

%clean
rm -rf %{buildroot}

%description
Red Hat Fence Agents is a collection of scripts to handle remote
power management for several devices.

%package common
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Common utilities for fence agents
Requires: python pexpect python-pycurl policycoreutils-python selinux-policy-targeted
%description common
Red Hat Fence Agents is a collection of scripts and libraries to handle remote power management for various devices.
%post common
/usr/sbin/semanage boolean -S targeted -N -m --on fenced_can_ssh
/usr/sbin/semanage boolean -S targeted -N -m --on fenced_can_network_connect
%files common
%defattr(-,root,root,-)
%doc doc/COPYING.* doc/COPYRIGHT doc/README.licence
%{_datadir}/fence
%{_datadir}/cluster
%exclude %{_datadir}/cluster/fence_mpath_check*
%exclude %{_datadir}/cluster/fence_scsi_check*
%exclude %{_sbindir}/fence_tripplite_snmp
%exclude %{_mandir}/man8/fence_tripplite_snmp.8.gz

%package all
License: GPLv2+ and LGPLv2+ and ASL 2.0
Group: System Environment/Base
Summary: Fence agents
Requires: %(echo "%{allfenceagents}" | sed "s/\( \|$\)/ >= %{version}-%{release}\1/g")
%ifarch i686 x86_64
Requires: fence-virt
%endif
%ifarch ppc64le
Requires: fence-agents-lpar >= %{version}-%{release}
%endif
%ifarch s390x
Requires: fence-agents-zvm >= %{version}-%{release}
%endif
Provides: fence-agents = %{version}-%{release}
Obsoletes: fence-agents < 3.1.13
%description all
Red Hat Fence Agents is a collection of all supported fence agents.
%files all

%ifarch x86_64
%package aliyun
License: GPLv2+ and LGPLv2+ and ASL 2.0 and BSD and MIT
Group: System Environment/Base
Summary: Fence agent for Alibaba Cloud (Aliyun)
Requires: fence-agents-common >= %{version}-%{release}
# python-pycryptodome bundle
Provides: bundled(python-%{pycryptodome}) = %{pycryptodome_version}
# python-aliyun-sdk-core bundle
Provides: bundled(python-aliyun-sdk-core) = %{aliyunsdkcore_version}
# python-aliyun-sdk-ecs bundle
Provides: bundled(python-aliyun-sdk-ecs) = %{aliyunsdkecs_version}
# python-aliyun-sdk-vpc bundle
Provides: bundled(python-aliyun-sdk-vpc) = %{aliyunsdkvpc_version}
Obsoletes: fence-agents
%description aliyun
The fence-agents-aliyun package contains a fence agent for Alibaba Cloud (Aliyun) instances.
%files aliyun
%defattr(-,root,root,-)
# bundled libraries
%doc pycryptodome_README.rst aliyun*_README*
%license pycryptodome_LICENSE.rst
%{_sbindir}/fence_aliyun
%{_mandir}/man8/fence_aliyun.8*
# bundled libraries
/usr/lib/fence-agents/%{bundled_lib_dir}/aliyun
%endif

%package amt-ws
License: ASL 2.0
Group: System Environment/Base
Summary: Fence agent for AMT (WS-Man) devices
Requires: fence-agents-common >= %{version}-%{release}
Requires: openwsman-python >= 2.6.3-1.git4391e5c.el7
Obsoletes: fence-agents
%description amt-ws
The fence-agents-amt-ws package contains a fence agent for AMT (WS-Man) devices.
%files amt-ws
%defattr(-,root,root,-)
%{_sbindir}/fence_amt_ws
%{_mandir}/man8/fence_amt_ws.8*

%package apc
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for APC devices
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description apc
The fence-agents-apc package contains a fence agent for APC devices that are accessed via telnet or SSH. 
%files apc 
%defattr(-,root,root,-)
%{_sbindir}/fence_apc
%{_mandir}/man8/fence_apc.8*

%package apc-snmp
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for APC devices (SNMP)
Requires: fence-agents-common >= %{version}-%{release}
Requires: net-snmp-utils
Obsoletes: fence-agents
%description apc-snmp
The fence-agents-apc-snmp package contains a fence agent for APC devices that are accessed via the SNMP protocol. 
%files apc-snmp
%defattr(-,root,root,-)
%{_sbindir}/fence_apc_snmp
%{_mandir}/man8/fence_apc_snmp.8*

%ifarch x86_64
%package aws
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Amazon AWS
Requires: fence-agents-common >= %{version}-%{release}
Requires: python-boto3
Obsoletes: fence-agents
%description aws
The fence-agents-aws package contains a fence agent for Amazon AWS instances. 
%files aws
%defattr(-,root,root,-)
%{_sbindir}/fence_aws
%{_mandir}/man8/fence_aws.8*
%endif

%ifarch x86_64
%package azure-arm
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Azure Resource Manager
Requires: fence-agents-common >= %{version}-%{release}
Requires: python-azure-sdk >= 4.0.0
Obsoletes: fence-agents
%description azure-arm
The fence-agents-azure-arm package contains a fence agent for Azure instances. 
%files azure-arm
%defattr(-,root,root,-)
%{_sbindir}/fence_azure_arm
%{_mandir}/man8/fence_azure_arm.8*
%{_datadir}/fence/azure_fence.py
%endif

%package bladecenter
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM BladeCenter 
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description bladecenter
The fence-agents-bladecenter package contains a fence agent for IBM BladeCenter devices that are accessed via telnet or SSH.
%files bladecenter
%defattr(-,root,root,-)
%{_sbindir}/fence_bladecenter
%{_mandir}/man8/fence_bladecenter.8*

%package brocade
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP Brocade
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description brocade
The fence-agents-brocade package contains a fence agent for HP Brocade devices that are accessed via telnet or SSH.
%files brocade
%defattr(-,root,root,-)
%{_sbindir}/fence_brocade
%{_mandir}/man8/fence_brocade.8*

%package cisco-mds
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Cisco MDS 9000 series
Requires: fence-agents-common >= %{version}-%{release}
Requires: net-snmp-utils
Obsoletes: fence-agents
%description cisco-mds
The fence-agents-cisco-mds package contains a fence agent for Cisco MDS 9000 series devices that are accessed via the SNMP protocol.
%files cisco-mds
%defattr(-,root,root,-)
%{_sbindir}/fence_cisco_mds
%{_mandir}/man8/fence_cisco_mds.8*

%package cisco-ucs
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Cisco UCS series
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description cisco-ucs
The fence-agents-cisco-ucs package contains a fence agent for Cisco UCS series devices that are accessed via the SNMP protocol.
%files cisco-ucs
%defattr(-,root,root,-)
%{_sbindir}/fence_cisco_ucs
%{_mandir}/man8/fence_cisco_ucs.8*

%package compute
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Nova compute nodes
Requires: fence-agents-common >= %{version}-%{release}
Requires: python-requests
Obsoletes: fence-agents
%description compute
The fence-agents-compute package contains a fence agent for Nova compute nodes.
%files compute
%defattr(-,root,root,-)
%{_sbindir}/fence_compute
%{_sbindir}/fence_evacuate
%{_mandir}/man8/fence_compute.8*
%{_mandir}/man8/fence_evacuate.8*

%package drac5
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Dell DRAC 5
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description drac5
The fence-agents-drac5 package contains a fence agent for Dell DRAC 5 series devices that are accessed via telnet or SSH.
%files drac5
%defattr(-,root,root,-)
%{_sbindir}/fence_drac5
%{_mandir}/man8/fence_drac5.8*

%package eaton-snmp
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Eaton network power switches
Requires: fence-agents-common >= %{version}-%{release}
Requires: net-snmp-utils
Obsoletes: fence-agents
%description eaton-snmp
The fence-agents-eaton-snmp package contains a fence agent for Eaton network power switches that are accessed via the SNMP protocol.
%files eaton-snmp
%defattr(-,root,root,-)
%{_sbindir}/fence_eaton_snmp
%{_mandir}/man8/fence_eaton_snmp.8*

%package emerson
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Emerson devices (SNMP)
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description emerson
The fence-agents-emerson package contains a fence agent for Emerson devices that are accessed via the SNMP protocol.
%files emerson
%defattr(-,root,root,-)
%{_sbindir}/fence_emerson
%{_mandir}/man8/fence_emerson.8*

%package eps
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for ePowerSwitch 8M+ power switches
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description eps
The fence-agents-eps package contains a fence agent for ePowerSwitch 8M+ power switches that are accessed via the HTTP(s) protocol.
%files eps
%defattr(-,root,root,-)
%{_sbindir}/fence_eps
%{_mandir}/man8/fence_eps.8*

%ifarch x86_64
%package gce
License: GPLv2+ and LGPLv2+ and ASL 2.0 and BSD and MIT
Group: System Environment/Base
Summary: Fence agent for GCE (Google Cloud Engine)
Requires: fence-agents-common >= %{version}-%{release}
Requires: python-cryptography >= 1.7.2
# python-google-api-client bundle
Provides: bundled(python-google-api-client) = %{googleapiclient_version}
# python-oauth2client bundle
Provides: bundled(python-%{oauth2client}) = %{oauth2client_version}
# python-httplib2 bundle
Provides: bundled(python-%{httplib2}) = %{httplib2_version}
# python-fasteners bundle
Provides: bundled(python-%{fasteners}) = %{fasteners_version}
# python-keyring bundle
Provides: bundled(python-%{keyring}) = %{keyring_version}
# python-uritemplate bundle
Provides: bundled(python-%{uritemplate}) = %{uritemplate_version}
Obsoletes: fence-agents
%description gce
The fence-agents-gce package contains a fence agent for GCE (Google Cloud Engine) instances.
%files gce
%defattr(-,root,root,-)
# bundled libraries
%doc %{oauth2client}_README.md %{fasteners}_README.rst %{keyring}_README.rst %{gflags}_README %{uritemplate}_README.rst
%license %{googleapiclient}_LICENSE %{oauth2client}_LICENSE %{fasteners}_LICENSE %{uritemplate}_LICENSE*
%{_sbindir}/fence_gce
%{_mandir}/man8/fence_gce.8*
# bundled libraries
/usr/lib/fence-agents/%{bundled_lib_dir}/gce
%exclude %{_bindir}/keyring
%exclude %{_bindir}/gflags2man
%endif

%package heuristics-ping
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent used to control other fence agents based on ping-heuristics
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description heuristics-ping

The fence-agents-heuristics-ping package contains fence agent used to control other fence agents based on ping-heuristics
%files heuristics-ping
%defattr(-,root,root,-)
%{_sbindir}/fence_heuristics_ping
%{_mandir}/man8/fence_heuristics_ping.8*

%package hpblade
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP BladeSystem devices
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description hpblade
The fence-agents-hpblade package contains a fence agent for HP BladeSystem devices that are accessed via telnet or SSH.
%files hpblade
%defattr(-,root,root,-)
%{_sbindir}/fence_hpblade
%{_mandir}/man8/fence_hpblade.8*

%package ibmblade
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM BladeCenter
Requires: fence-agents-common >= %{version}-%{release}
Requires: net-snmp-utils
Obsoletes: fence-agents
%description ibmblade
The fence-agents-ibmblade package contains a fence agent for IBM BladeCenter devices that are accessed via the SNMP protocol.
%files ibmblade
%defattr(-,root,root,-)
%{_sbindir}/fence_ibmblade
%{_mandir}/man8/fence_ibmblade.8*

%package ifmib
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for devices with IF-MIB interfaces
Requires: fence-agents-common >= %{version}-%{release}
Requires: net-snmp-utils
Obsoletes: fence-agents
%description ifmib
The fence-agents-ifmib package contains a fence agent for IF-MIB interfaces that are accessed via the SNMP protocol.
%files ifmib
%defattr(-,root,root,-)
%{_sbindir}/fence_ifmib
%{_mandir}/man8/fence_ifmib.8*

%package ilo2
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP iLO2 devices
Requires: fence-agents-common >= %{version}-%{release}
Requires: gnutls-utils
Obsoletes: fence-agents
%description ilo2
The fence-agents-ilo2 package contains a fence agent for HP iLO2 devices that are accessed via the HTTP(s) protocol.
%files ilo2
%defattr(-,root,root,-)
%{_sbindir}/fence_ilo
%{_sbindir}/fence_ilo2
%{_mandir}/man8/fence_ilo.8*
%{_mandir}/man8/fence_ilo2.8*

%package ilo-moonshot
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP iLO Moonshot devices
Requires: telnet openssh-clients
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description ilo-moonshot
The fence-agents-ilo-moonshot package contains a fence agent for HP iLO Moonshot devices that are accessed via telnet or SSH.
%files ilo-moonshot
%defattr(-,root,root,-)
%{_sbindir}/fence_ilo_moonshot
%{_mandir}/man8/fence_ilo_moonshot.8*

%package ilo-mp
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP iLO MP devices
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description ilo-mp
The fence-agents-ilo-mp package contains a fence agent for HP iLO MP devices that are accessed via telnet or SSH.
%files ilo-mp
%defattr(-,root,root,-)
%{_sbindir}/fence_ilo_mp
%{_mandir}/man8/fence_ilo_mp.8*

%package ilo-ssh
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP iLO devices via SSH
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description ilo-ssh
The fence-agents-ilo-ssh package contains a fence agent for HP iLO devices that are accessed via SSH.
%files ilo-ssh
%defattr(-,root,root,-)
%{_sbindir}/fence_ilo_ssh
%{_mandir}/man8/fence_ilo_ssh.8*
%{_sbindir}/fence_ilo3_ssh
%{_mandir}/man8/fence_ilo3_ssh.8*
%{_sbindir}/fence_ilo4_ssh
%{_mandir}/man8/fence_ilo4_ssh.8*
%{_sbindir}/fence_ilo5_ssh
%{_mandir}/man8/fence_ilo5_ssh.8*

%package intelmodular
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for devices with Intel Modular interfaces
Requires: fence-agents-common >= %{version}-%{release}
Requires: net-snmp-utils
Obsoletes: fence-agents
%description intelmodular
The fence-agents-intelmodular package contains a fence agent for Intel Modular interfaces that are accessed via the SNMP protocol.
%files intelmodular
%defattr(-,root,root,-)
%{_sbindir}/fence_intelmodular
%{_mandir}/man8/fence_intelmodular.8*

%package ipdu
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM iPDU network power switches
Requires: fence-agents-common >= %{version}-%{release}
Requires: net-snmp-utils
Obsoletes: fence-agents
%description ipdu
The fence-agents-ipdu package contains a fence agent for IBM iPDU network power switches that are accessed via the SNMP protocol.
%files ipdu
%defattr(-,root,root,-)
%{_sbindir}/fence_ipdu
%{_mandir}/man8/fence_ipdu.8*

%package ipmilan
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for devices with IPMI interface
Requires: fence-agents-common >= %{version}-%{release}
Requires: /usr/bin/ipmitool
Obsoletes: fence-agents
%description ipmilan
The fence-agents-ipmilan package contains a fence agent for devices with IPMI interface. 
%files ipmilan
%defattr(-,root,root,-)
%{_sbindir}/fence_ipmilan
%{_mandir}/man8/fence_ipmilan.8*
%{_sbindir}/fence_idrac
%{_mandir}/man8/fence_idrac.8*
%{_sbindir}/fence_ilo3
%{_mandir}/man8/fence_ilo3.8*
%{_sbindir}/fence_ilo4
%{_mandir}/man8/fence_ilo4.8*
%{_sbindir}/fence_ilo5
%{_mandir}/man8/fence_ilo5.8*
%{_sbindir}/fence_imm
%{_mandir}/man8/fence_imm.8*

%package mpath
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for reservations over Device Mapper Multipath
Requires: fence-agents-common >= %{version}-%{release}
Requires: device-mapper-multipath
Obsoletes: fence-agents
%description mpath
The fence-agents-mpath package contains fence agent for SCSI persisent reservation over Device Mapper Multipath
%files mpath
%defattr(-,root,root,-)
%{_sbindir}/fence_mpath
%{_datadir}/cluster/fence_mpath_check*
%{_mandir}/man8/fence_mpath.8*

%package kdump
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for use with kdump crash recovery service
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description kdump
The fence-agents-kdump package contains a fence agent for use with kdump crash recovery service.
%files kdump
%defattr(-,root,root,-)
%{_sbindir}/fence_kdump
%{_libexecdir}/fence_kdump_send
%{_mandir}/man8/fence_kdump.8*
%{_mandir}/man8/fence_kdump_send.8*

%ifarch ppc64le
%package lpar
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM LPAR
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description lpar
The fence-agents-lpar package contains a fence agent for IBM LPAR devices that are accessed via telnet or SSH.
%files lpar
%defattr(-,root,root,-)
%{_sbindir}/fence_lpar
%{_mandir}/man8/fence_lpar.8*
%endif

%package redfish
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Redfish
Requires: fence-agents-common >= %{version}-%{release}
Requires: python-requests
Obsoletes: fence-agents
%description redfish
The fence-agents-redfish package contains a fence agent for Redfish
%files redfish
%defattr(-,root,root,-)
%{_sbindir}/fence_redfish
%{_mandir}/man8/fence_redfish.8*

%package rhevm
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for RHEV-M
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description rhevm
The fence-agents-rhevm package contains a fence agent for RHEV-M via REST API
%files rhevm
%defattr(-,root,root,-)
%{_sbindir}/fence_rhevm
%{_mandir}/man8/fence_rhevm.8*

%package rsa
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM RSA II
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description rsa
The fence-agents-rsa package contains a fence agent for IBM RSA II devices that are accessed via telnet or SSH.
%files rsa
%defattr(-,root,root,-)
%{_sbindir}/fence_rsa
%{_mandir}/man8/fence_rsa.8*

%package rsb
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Fujitsu RSB
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description rsb
The fence-agents-rsb package contains a fence agent for Fujitsu RSB devices that are accessed via telnet or SSH.
%files rsb
%defattr(-,root,root,-)
%{_sbindir}/fence_rsb
%{_mandir}/man8/fence_rsb.8*

%if 0
%package sanbox2
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for QLogic SANBox2 FC switches
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet
Obsoletes: fence-agents
%description sanbox2
The fence-agents-sanbox2 package contains a fence agent for QLogic SANBox2 switches that are accessed via telnet.
%files sanbox2
%defattr(-,root,root,-)
%{_sbindir}/fence_sanbox2
%{_mandir}/man8/fence_sanbox2.8*
%endif

%package sbd
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for SBD (storage-based death)
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description sbd
The fence-agents-sbd package contains fence agent for SBD (storage-based death)
%files sbd
%defattr(-,root,root,-)
%{_sbindir}/fence_sbd
%{_mandir}/man8/fence_sbd.8*

%package scsi
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for SCSI persisent reservations
Requires: sg3_utils fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description scsi
The fence-agents-scsi package contains fence agent for SCSI persisent reservations
%files scsi
%defattr(-,root,root,-)
%{_sbindir}/fence_scsi
%{_datadir}/cluster/fence_scsi_check.pl
%{_datadir}/cluster/fence_scsi_check
%{_datadir}/cluster/fence_scsi_check_hardreboot
%{_mandir}/man8/fence_scsi.8*

%package virsh
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for virtual machines based on libvirt
Requires: fence-agents-common >= %{version}-%{release}
Requires: openssh-clients /usr/bin/virsh
Obsoletes: fence-agents
%description virsh
The fence-agents-virsh package contains a fence agent for virtual machines that are accessed via SSH.
%files virsh
%defattr(-,root,root,-)
%{_sbindir}/fence_virsh
%{_mandir}/man8/fence_virsh.8*

%package vmware-rest
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for VMWare with REST API
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description vmware-rest
The fence-agents-vmware-rest package contains a fence agent for VMWare with REST API
%files vmware-rest
%defattr(-,root,root,-)
%{_sbindir}/fence_vmware_rest
%{_mandir}/man8/fence_vmware_rest.8*

%package vmware-soap
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for VMWare with SOAP API v4.1+
Requires: fence-agents-common >= %{version}-%{release}
Requires: python-suds python-requests
Obsoletes: fence-agents
%description vmware-soap
The fence-agents-vmware-soap package contains a fence agent for VMWare with SOAP API v4.1+
%files vmware-soap
%defattr(-,root,root,-)
%{_sbindir}/fence_vmware_soap
%{_mandir}/man8/fence_vmware_soap.8*

%package wti
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for WTI Network power switches
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description wti
The fence-agents-wti package contains a fence agent for WTI network power switches that are accessed via telnet or SSH.
%files wti
%defattr(-,root,root,-)
%{_sbindir}/fence_wti
%{_mandir}/man8/fence_wti.8*

%ifarch s390x
%package zvm
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for z/VM hypervisors
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description zvm
The fence-agents-zvm package contains a fence agent for z/VM hypervisors
%files zvm
%defattr(-,root,root,-)
%{_sbindir}/fence_zvmip
%{_mandir}/man8/fence_zvmip.8*
%exclude %{_sbindir}/fence_zvm
%exclude %{_mandir}/man8/fence_zvm.8*
%endif

%changelog
* Thu May 16 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-11.8
- fence_rhevm: add RHEV v4 API support and auto-detection
  Resolves: rhbz#1708547
- fence_azure_arm: use skip_shutdown feature
  Resolves: rhbz#1709110

* Thu Jan 17 2019 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-11.7
- fence_redfish: new fence agent
  Resolves: rhbz#1666848

* Thu Dec  6 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-11.5
- fence_scsi: add watchdog retry support
  Resolves: rhbz#1654172

* Wed Nov 28 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-11.4
- fence_hpblade: fix log_expect syntax
  Resolves: rhbz#1652115

* Thu Nov  8 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-11.1
- fence_scsi: fix incorrect SCSI-key when node ID is 10 or higher
  Resolves: rhbz#1647522

* Tue Sep  4 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-11
- fence_cisco_ucs: fix missing encode for POSTFIELDS
  Resolves: rhbz#1625164

* Thu Aug 30 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-10
- fence_aliyun: show instances names in list-action
  Resolves: rhbz#1622229

* Mon Aug 20 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-9
- Fix --version
  Resolves: rhbz#1236395

* Tue Aug 14 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-8
- fence_aliyun: add logging
  Resolves: rhbz#1568742
- fence_gce: add stackdriver-logging support, improve logging and
  set default mode to cycle
  Resolves: rhbz#1568753

* Tue Jul 24 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-5
- fence_aliyun: new fence agent
  Resolves: rhbz#1568742

* Mon Jul 16 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-3
- fence_evacuate: fix evacuable tag mix issue
  Resolves: rhbz#1549699

* Thu Jun 28 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.2.1-1
- rebase to v4.2.1
  Resolves: rhbz#1236395
- fence_mpath: add watchdog support
  Resolves: rhbz#1504202

* Mon Jun 25 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-90
- fence_gce: new fence agent
  Resolves: rhbz#1568753
- fence_rhevm: dont require --ssl parameter when using --ssl-insecure
  Resolves: rhbz#1544093
- fence_mpath: fix preemptive abort
  Resolves: rhbz#1556857
- fence-agents-all: dont show manpage-tags in metadata
  Resolves: rhbz#1553908
- fence_scsi: dont write duplicates to .dev-file
  Resolves: rhbz#1575973
- fence_impilan: add iLO5-support
  Resolves: rhbz#1579391

* Thu Apr 12 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-88
- fence_azure_arm: fix subscriptionId from metadata
  Resolves: rhbz#1566154

* Tue Apr 10 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-87
- fence_azure_arm: add network-fencing
  Resolves: rhbz#1553904
- fence_compute/fence_evacuate: fix parameters
  Resolves: rhbz#1559977

* Wed Feb  7 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-86
- fence-agents-all: remove fence-agents-aws and fence-agents-azure-arm
  dependencies
  Resolves: rhbz#1476009

* Tue Feb  6 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-85
- fence_aws: add python-boto3 dependency
  Resolves: rhbz#1540700

* Mon Jan 22 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-84
- fence_azure_arm: new fence agent
  Resolves: rhbz#1476009

* Thu Jan 11 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-83
- fence_compute/fence_evacuate: add support for keystone v3 authentication
  Resolves: rhbz#1533170
- fence_ilo3: default to onoff
  Resolves: rhbz#1519370

* Tue Nov 28 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-82
- fence_vmware_rest: new fence agent
  Resolves: rhbz#1396050

* Tue Nov  7 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-81
- common: add selinux-policy-targeted dependency
  Resolves: rhbz#1509327

* Fri Nov  3 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-80
- fence_ipmilan: fix default method inconsistency (help/man page)
  Resolves: rhbz#1465436

* Wed Nov  1 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-78
- fence_heuristics_ping: new fence agent
  Resolves: rhbz#1476401

* Thu Oct 26 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-77
- fence_ilo_ssh: fix "hard reset"
  Resolves: rhbz#1490475

* Wed Oct 25 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-76
- fence_ipmilan: add support for hexadecimal key authentication
  Resolves: rhbz#1449183

* Tue Oct 24 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-75
- fence_aws: new fence agent
  Resolves: rhbz#1451776

* Fri Oct  6 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-72
- fence_amt_ws: new fence agent
  Resolves: rhbz#1296201

* Fri Sep 29 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-70
- fence-agents-all: require agents to be the same version
  Resolves: rhbz#1484128

* Fri Sep 29 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-69
- fence_scsi: add FIPS support
  Resolves: rhbz#1455383

* Thu Sep 28 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-68
- fence_compute/fence_scsi: fix issue with some parameters
  Resolves: rhbz#1473860
- fence_compute/fence_evacuate: changes to support Instance HA on OSP12
  Resolves: rhbz#1496390
- fence-agents-common: remove fence_scsi_check-files that should only be in
  the scsi subpackage
  Resolves: rhbz#1484128

* Wed Aug  2 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-67
- Remove "list" when not supported
  Resolves: rhbz#1461854

* Fri Jun 16 2017 Marek Grac <mgrac@redhat.com> - 4.0.11-66
- Set SELinux booleans even when SELinux is disabled
  Resolves: rhbz#1457887

* Thu Jun 15 2017 Marek Grac <mgrac@redhat.com> - 4.0.11-65
- Set SELinux booleans even when SELinux is disabled
  Resolves: rhbz#1457887

* Wed Jun  7 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-64
- fence_vmware_soap: fix for self-signed certificates
  Resolves: rhbz#1459199

* Tue May 30 2017 Marek Grac <mgrac@redhat.com> - 4.0.11-63
- Add dependencies on policycoreutils
  Resolves: rhbz#1427986

* Wed May 17 2017 Marek Grac <mgrac@redhat.com> - 4.0.11-62
- Set SELinux booleans required for fence agent integration with cluster
  Resolves: rhbz#1427986

* Thu May  4 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-61
- fence_ipmilan: add target (ipmilan -t <target>) support
  Resolves: rhbz#1377389

* Mon Apr  3 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-60
- fence_compute: fix project_id changed to project_name in Nova API
  Resolves: rhbz#1426693

* Thu Mar 23 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-58
- CI: dont test paths in metadata
  Resolves: rhbz#1377972

* Wed Mar 22 2017 Marek Grac <mgrac@redhat.com> - 4.0.11-57
- Set SELinux booleans required for fence agent integration with cluster
  Resolves: rhbz#1427986
- Add consistency of parameters between STDIN and command-line
  Resolves: rhbz#1403028

* Tue Mar 21 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-56
- fencing: add validate-all action
  Resolves: rhbz#1433948
- fence_rhevm: add "--disable-http-filter" to be able to explicitly
  use oVirt API version 3
  Resolves: rhbz#1422499

* Wed Mar 01 2017 Marek Grac <mgrac@redhat.com> - 4.0.11-54
- fence_lpar: Fix monitor action on IVM systems
  Resolves: rhbz#1376481

* Tue Feb 21 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-53
- fence_compute: Improved FQDN and Nova handling
  Resolves: rhbz#1387590

* Tue Feb 14 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-52
- fence_compute: fix ConnectionError
  Resolves: rhbz#1384073
- fence_lpar: add IVM support and improve error handling
  Resolves: rhbz#1376481
- fence_vmware_soap: suppress warning for --ssl-insecure
  Resolves: rhbz#1393962
- Add support for "s" for seconds for delay, *_timeout, *_wait parameters
  Resolves: rhbz#1377928
- fence-agents-zvm: add to fence-agents-all dependencies for s390x
  Resolves: rhbz#1255700
- Build for ppc64le
  Resolves: rhbz#1402566

* Mon Jan 23 2017 Marek Grac <mgrac@redhat.com>
- fence_cisco_ucs: Change commands send to UCS
  Resolves: rhbz#1410881

* Wed Jan 11 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-50
- fence_sbd: new fence agent
  Resolves: rhbz#1337236

* Wed Nov 23 2016 Marek Grac <mgrac@redhat.com> - 4.0.11-49
- fencing: Fix 'monitor' action for devices with --port-as-ip
  Resolves: rhbz#1390915

* Wed Aug 31 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-47
- fence_rhevm: fix issues on RHEV 4
  Resolves: rhbz#1287059

* Thu Aug 25 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-46
  Resolves: rhbz#1298430

* Thu Aug 25 2016 Marek Grac <mgrac@redhat.com> - 4.0.11-45
- fence_cisco_ucs: Change method for obtaining status
  Resolves: rhbz#1298430

* Wed Aug 17 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-44
- fence_mpath: update info to say unique key per node instead of per
  node/device
  Resolves: rhbz#1280151

* Tue Jul 12 2016 Marek Grac <mgrac@redhat.com> - 4.0.11-43
- change in spec file
  Resolves: rhbz#1353221

* Thu Jul  7 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-42
- fence-agents-common: add dependency on python-pycurl
  Resolves: rhbz#1353221

* Wed Jul  6 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-41
- fence_compute: perform real status operation in record-only mode
  Resolves: rhbz#1287311

* Mon Jul  4 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-40
- fence_compute: improved FQDN handling
  Resolves: rhbz#1334162

* Wed Jun 22 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-39
- fence_apc: fix "Connection timed out" issue
  Resolves: rhbz#1342584

* Wed Jun 15 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-38
- fence_compute: advertise as fabric device
  Resolves: rhbz#1287301

* Tue Jun 14 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-37
- fence_compute: add taggable instance support
  Resolves: rhbz#1285523

* Tue May 31 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-34
- fence_virsh: add --missing-as-off
  Resolves: rhbz#1254821
- fence_ipmilan: fix power_wait regression
  Resolves: rhbz#1275250
- fence_ipmilan: add diag action
  Resolves: rhbz#1286045
- fence_ipmilan: warn that cycle method can report success before node
  is powered off
  Resolves: rhbz#1271780
- fence_scsi: fix persistentl typo in short desc
  Resolves: rhbz#1280139
- fence_scsi: remove /dev/dm-X reference
  Resolves: rhbz#1280151
- fence_rhevm: add Filter header
  Resolves: rhbz#1287059
- fence_compute: fix to locate all instances to be evacuated
  Resolves: rhbz#1313561

* Mon Feb 22 2016 Marek Grac <mgrac@redhat.com> - 4.0.11-33
- fence_cisco_ucs: Obtain status from different attribute
  Resolves: rhbz#1298430

* Tue Feb 09 2016 Marek Grac <mgrac@redhat.com> - 4.0.11-32
- fence_cisco_ucs: Obtain status from different endpoint
  Resolves: rhbz#1298430

* Mon Feb 01 2016 Marek Grac <mgrac@redhat.com> - 4.0.11-31
- fence_cisco_ucs: Obtain status from different endpoint
  Resolves: rhbz#1298430

* Wed Jan 20 2016 Marek Grac <mgrac@redhat.com> - 4.0.11-30
- fence_compute: Replace with current implementation
  Resolves: rhbz#1283084

* Wed Dec 16 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-28
- fence_scsi: Add fence_scsi_check_hardreboot
  Resolves: rhbz#bz1265426

* Mon Oct 26 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-27
- fence_brocade: Fix return status in get_power_status
  Resolves: rhbz#1274431

* Thu Sep 17 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-26
- fence_ipmilan: Fix -i attribute
  Resolves: rhbz#1257137

* Mon Sep 14 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-25
- fence_apc: Support for v6.x
  Resolves: rhbz#1259319

* Wed Sep 02 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-24
- fence_ipmilan: Add removed attributes -i & timeout
  Resolves: rhbz#1257137
- fence_ipmilan: Do not print password in verbose mode
  Resolves: rhbz#1241648
- fence_ilo: Negotiation of TLS1.0 is more automatic
  Resolves: rhbz#1256908

* Mon Aug 17 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-23
- fence_scsi: Fix watchdog script broken by more strict 'monitor'
  Resolves: 1243485

* Wed Aug 12 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-21
- fence_mpath: Fix unfencing after non-cluster reboot
  Resolves: 1102727
- manual pages now describe 'list-status' properly

bz1102727-3-fence_mpath.patch bz1250586-2-list_status.patch
* Tue Aug 11 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-20
- fencing: Fix place where --plug + --port-as-ip are tested
  Resolves: rhbz#1214522

* Mon Aug 10 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-19
- fencing: do not fail when state is None
  Resolves: rhbz#1251491

* Wed Aug 05 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-18
- fence_rsa: Fix login issue
  Resolves: rhbz#1185329
- fencing: support for list-status
  Resolves: rhbz#1250586
- fencing: Fix support for --port-as-ip
  Resolves: rhbz#1214522

* Thu Jul 16 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-17
- fence_scsi: Improve monitoring and add option to force ON
  Resolves: rhbz#1243485

* Mon Jun 29 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-16
- fence_compute: Agent cleanup
  Resolves: rhbz#1214359
- fence_hpblade: Add support for HP Integrity Superdome
  Resolves: rhbz#1216997
- fence_zvmip: Add --missing-as-off and change monitor/status actions
  Resolves: rhbz#1188750
- fence_mpath: new fence agent
  Resolves: rhbz#1102727
- fencing: Option --port-as-ip
  Resolves: rhbz#1214522

* Mon Jun 22 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-15
- fence_zvmip: Connection timeout issues
  Resolves: rhbz#1188750

* Thu Jun 18 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-14
- fence_rhevm: Add authentication via cookies
  Resolves: rhbz#1145769
- fence_ilo_moonshot: New fence agent
  Resolves: rhbz#1152917
- fence_emerson: New fence agent
  Resolves: rhbz#1171732
- fence_rsa: New fence agent
  Resolves: rhbz#1185329

* Wed Jun 17 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-13
- fence_scsi: Add monitor operation
  Resolves: rhbz#1213571
- fence_scsi: Force unfence if any of paths is off
  Resolves: rhbz#1214919
- fence_cisco_ucs: Fix https:// prefix with --ssl-(in)secure
  Resolves: rhbz#1165591
- fence_kdump: Add monitor operation
  Resolves: rhbz#1196068
- fence2rng: Fix problem with quotes
  Resolves: rhbz#1207982

* Mon Jun 08 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-12
- New fence agent fence_compute
  Resolves: rhbz#1214359

* Wed Mar 25 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-11
- fence_ipmilan: Unset default cipher
  Resolves: rhbz#1203877
- fence_ilo2: Add --tls1.0
  Resolves: rhbz#1199970
- update scripts so 'make check' is working again

* Mon Jan 05 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-10
- fence_zvmip: Add fence_zvmip ported to fencing library
  Resolves: rhbz#1173178

* Mon Dec 01 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-9
- fence_ilo_ssh: Fix EOL issue, syslog problem and add fence_ilo_[34]_ssh symlink
  Resolves: rhbz#1121122

* Wed Nov 12 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-8
- fence_zvm: Add 'monitor' support for fence_zvmip
  Resolves: rhbz#1140921

* Mon Nov 10 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-7
- HTTPS connection do not validate certificate (introduced with rebase)
  Resolves: rhbz#1162092

* Thu Oct 16 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-6
- fence_cisco_ucs and fence_vmware_soap should logout even in case of failure
  Resolves: rhbz#1111599
- fence_vmware_soap: Fix issue with import of fail_usage
  Resolves: rhbz#1153059

* Thu Oct 02 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-5
- fence_wti: Fix problem with EOL introduced by rebase
  Resolves: rhbz#1148762
- fence_rsb: Fix issue with new firmware 
  Resolves: rhbz#1111597

* Sat Sep 20 2014 Fabio M. Di Nitto <fdinitto@redhat.com> - 4.0.11-4
- add initial support for IBM z/VM
  Resolves: rhbz#1140921

* Mon Sep 15 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-3
- temporary removes fence-agents-amt because amtterm is missing

* Wed Sep 03 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-2
- add a fence agents for AMT and iLO-ssh
  Resolves: rhbz#1121122 rhbz#1107439

* Wed Sep 03 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-1
- rebase of fence agents
  Resolves: rhbz#1120682
- INFO: fence_scsi_check.pl is now a python script

* Wed Mar 19 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-21
- fencing: Add --ssl-secure and --ssl-insecure for fence_vmware_soap
  Resolves: rhbz#1072564

* Fri Mar 07 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-20
- fencing: Add --ssl-secure and --ssl-insecure for fence_vmware_soap
  Resolves: rhbz#1072564

* Wed Mar 05 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-19
- fencing: Add --ssl-secure and --ssl-insecure
  Resolves: rhbz#1072564

* Thu Feb 27 2014 Fabio M. Di Nitto <fdinitto@redhat.com> - 4.0.2-18
- fence_vmware_soap: fix short/long option parsing traceback
  Resolves: rhbz#1018780

* Wed Feb 26 2014 Fabio M. Di Nitto <fdinitto@redhat.com> - 4.0.2-17
- Fix fence-agents-* Requires on proper fence-agents-common and silence
  suds error
  Resolves: rhbz#1018780

* Thu Feb 20 2014 Fabio M. Di Nitto <fdinitto@redhat.com> - 4.0.2-16
- Allow ssl connections to disable TLS negotiation with "notls" option.
  Resolves: rhbz#990539

* Wed Feb 19 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-15
- Fix dependencies issues

* Mon Feb 17 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-14
- fence_vmware_soap: Fix unexpected exception
  Resolves: rhbz#1018780
- nss_wrapper was replaced by gnutls-cli
  Resolves: rhbz#990539

* Wed Jan 29 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-13
- fencing: Do not use public key if identity file is not defined
  Resolves: rhbz#1048843
- fence_vmware_soap: Add support for --delay option
  Resolves: rhbz#1057299
- fence_wti: Add support for named groups (also for firmware 1.43)
  Resolves: rhbz#1022536

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 4.0.2-12
- Mass rebuild 2014-01-24

* Thu Jan 23 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-11
- fencing: Ensure validity of XML metadata using Relax NG 
  Resolves: rhbz#1022529

* Thu Jan 23 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-10
- fix default action for fabric fencing agents
  Resolves: rhbz#1021392
- modify key generation in fence_scsi to support pacemaker/corosync cluster
  Resolves: rhbz#994466

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.0.2-9
- Mass rebuild 2013-12-27

* Wed Nov 20 2013 Marek Grac <mgrac@redhat.com> - 4.0.2-8
- fence-agents-all now includes fence-virt which is not available everywhere
  Resolves: rhbz#1028940

* Tue Nov 12 2013 Marek Grac <mgrac@redhat.com> - 4.0.2-7
- fence-agents-all now includes fence-virt
  Resolves: rhbz#1028940

* Mon Nov 04 2013 Marek Grac <mgrac@redhat.com> - 4.0.2-6
- fencing: Ensure validity of XML metadata using Relax NG 
  Resolves: rhbz#1022529
- fencing: Fix invalid use of options[".."]
  Resolves: rhbz#1022533
- fence_brocade: Add fence agent
  Resolves: rhbz#1021392

* Mon Nov 04 2013 Marek Grac <mgrac@redhat.com> - 4.0.2-5
- fence_vmware_soap: Report if user privileges are not enough for given operation
  Resolves: rhbz#1018780
- fence_wti: Add support for named groups
  Resolves: rhbz#1022536
- fence_rsb: Update regular expression to match newer firmware version
  Resolves: rhbz#1022538

* Mon Nov 04 2013 Marek Grac <mgrac@redhat.com> - 4.0.2-4
- fence_vmware_soap: Disable cache in SUDS library to resolve SELinux problems
  Resolves: rhbz#1022528
- fencing: Add information that operation 'unfence' should be run automatically after start of the cluster
  Resolves: rhbz#1012994
- Aligned to upstream 4.0.4

* Mon Sep 02 2013 Marek Grac <mgrac@redhat.com> - 4.0.2-3
- fence_bladecenter: Fix telnet login failure
- fence_brocade: Rewrite to fencing library
- fencing_snmp: Fix 'KeyError --a'
- fence_scsi: Fix XML metadata
- fence_scsi: Add a documentation of "delay"
- fence_ilo2: Unable to login when password contains "

* Tue Jul 30 2013 Marek Grac <mgrac@redhat.com> - 4.0.2-2
- new upstream release

* Tue Jul 09 2013 Marek Grac <mgrac@redhat.com> - 4.0.1-1
- new upstream release

* Mon Jun 24 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-5
- fence-agents-all should provide fence-agent for clean update path

* Wed Apr 03 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-4
- minor changes in spec file

* Thu Mar 21 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-3
- minor changes in spec file

* Mon Mar 18 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-2
- minor changes in spec file

* Mon Mar 11 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-1
- new upstream release
- introducing subpackages


