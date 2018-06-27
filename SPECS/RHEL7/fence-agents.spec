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

Name: fence-agents
Summary: Fence Agents for Red Hat Cluster
Version: 4.2.1
Release: 1%{?alphatag:.%{alphatag}}%{?dist}
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
URL: https://github.com/ClusterLabs/fence-agents
Source0: fence-agents/%{name}-%{version}.tar.xz

%if 0%{?rhel}
%global supportedagents amt_ws apc apc_snmp aws azure_arm bladecenter brocade cisco_mds cisco_ucs compute drac5 eaton_snmp emerson eps hpblade ibmblade ifmib ilo ilo_moonshot ilo_mp ilo_ssh intelmodular ipdu ipmilan mpath kdump rhevm rsa rsb sbd scsi vmware_rest vmware_soap wti docker vbox evacuate
%global allfenceagents fence-agents-amt-ws fence-agents-apc fence-agents-apc-snmp fence-agents-bladecenter fence-agents-brocade fence-agents-cisco-mds fence-agents-cisco-ucs fence-agents-compute fence-agents-drac5 fence-agents-eaton-snmp fence-agents-emerson fence-agents-eps fence-agents-heuristics-ping fence-agents-hpblade fence-agents-ibmblade fence-agents-ifmib fence-agents-ilo2 fence-agents-ilo-moonshot fence-agents-ilo-mp fence-agents-ilo-ssh fence-agents-intelmodular fence-agents-ipdu fence-agents-ipmilan fence-agents-mpath fence-agents-kdump fence-agents-rhevm fence-agents-rsa fence-agents-rsb fence-agents-sbd fence-agents-scsi fence-agents-vmware-rest fence-agents-vmware-soap fence-agents-wti
%ifarch ppc64le
%global testagents virsh lpar heuristics_ping
%endif
%ifarch s390x
%global testagents virsh zvm heuristics_ping
%endif
%ifnarch ppc64le s390x
%global testagents virsh heuristics_ping
%endif
%endif

## Setup/build bits

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# Build dependencies
BuildRequires: glibc-devel
BuildRequires: gnutls-utils
BuildRequires: libxslt
BuildRequires: python pexpect python-pycurl python-suds python-requests openwsman-python
BuildRequires: net-snmp-utils
BuildRequires: autoconf automake libtool
BuildRequires: iputils

%prep
%setup -q -n %{name}-%{version}

%build
./autogen.sh
%{configure} --with-agents='%{supportedagents} %{testagents}'
CFLAGS="$(echo '%{optflags}')" make %{_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

## tree fix up
# fix libfence permissions
chmod 0755 %{buildroot}%{_datadir}/fence/*.py
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
%{_datadir}/fence/fencing.py
%{_datadir}/fence/fencing_snmp.py
%exclude %{_datadir}/cluster/fence_scsi_check*

%package all
License: GPLv2+, LGPLv2+ and ASL 2.0
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

%if 0%{?fedora}
%package alom
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for SUN ALOM
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description alom
Red Hat Fence Agents
%files alom
%defattr(-,root,root,-)
%{_sbindir}/fence_alom
%{_mandir}/man8/fence_alom.8*
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
%{_sbindir}/fence_tripplite_snmp
%{_mandir}/man8/fence_apc_snmp.8*
%{_mandir}/man8/fence_tripplite_snmp.8*

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

%package azure-arm
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Azure Resource Manager
Requires: fence-agents-common >= %{version}-%{release}
Requires: python-azure-sdk
Obsoletes: fence-agents
%description azure-arm
The fence-agents-azure-arm package contains a fence agent for Azure instances. 
%files azure-arm
%defattr(-,root,root,-)
%{_sbindir}/fence_azure_arm
%{_mandir}/man8/fence_azure_arm.8*
%{_datadir}/fence/azure_fence.py

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

%package docker
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Docker
Requires: pycurl
Requires: fence-agents-common = %{version}-%{release}
Obsoletes: fence-agents
%description docker
The fence-agents-docker package contains a fence agent for Docker images that are accessed over HTTP.
%files docker
%defattr(-,root,root,-)
%{_sbindir}/fence_docker
%{_mandir}/man8/fence_docker.8*

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

%if 0%{?fedora}
%package ldom
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Sun LDom virtual machines
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description ldom
The fence-agents-ldom package contains a fence agent for Sun LDom devices that are accessed via telnet or SSH.
%files ldom
%defattr(-,root,root,-)
%{_sbindir}/fence_ldom
%{_mandir}/man8/fence_ldom.8*
%endif

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
%{_datadir}/cluster/fence_scsi_check
%{_datadir}/cluster/fence_scsi_check_hardreboot
%{_mandir}/man8/fence_scsi.8*

%package vbox
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for VirtualBox
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description vbox
The fence-agents-vbox package contains a fence agent for VirtualBox
%files vbox
%defattr(-,root,root,-)
%{_sbindir}/fence_vbox
%{_mandir}/man8/fence_vbox.8*

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
%endif

%changelog
* Thu Apr 12 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-86.2
- fence_azure_arm: fix subscriptionId from metadata
  Resolves: rhbz#1566632

* Wed Apr 11 2018 Oyvind Albrigtsen <oalbrigt@redhat.com> - 4.0.11-86.1
- fence_azure_arm: add network-fencing
  Resolves: rhbz#1565670
- fence_compute/fence_evacuate: fix parameters
  Resolves: rhbz#1565701

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


