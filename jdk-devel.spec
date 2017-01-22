%global jdk_major %{?jdk_version_major}%{!?jdk_version_major:8}
%global jdk_minor %{?jdk_version_minor}%{!?jdk_version_minor:0}
%global jdk_patch %{?jdk_version_patch}%{!?jdk_version_patch:112}
%global jdk_version_api   1.%{jdk_major}.%{jdk_minor}
%global jdk_version_full  %{jdk_version_api}_%{jdk_patch}

%global jdk_home %{_prefix}/java/jdk%{jdk_version_full}
%global jre_home %{jdk_home}/jre
%global pki_dir %{_sysconfdir}/pki

Name:           jdk%{jdk_version_full}-devel
Version:        %{jdk_version_full}
Release:        %{ITERATION}%{?dist}
Summary:        Oracle JDK Development Dummy Package
Group:          Development/Tools
AutoReqProv:    no
Provides:       java-%{jdk_version_api}-devel
Provides:       java-devel
Provides:       java-sdk
Provides:       java-sdk-%{jdk_version_api}
Provides:       java%{jdk_version_major}-%{jdk_version_api}-devel
Provides:       java%{jdk_version_major}-devel
Provides:       java%{jdk_version_major}-sdk
Provides:       java%{jdk_version_major}-sdk-%{jdk_version_api}
Provides:       libjvm.so()(64bit)
License:        Apache License v2.0
URL:            http://www.oracle.com/technetwork/java/javase/downloads/index.html

Requires:       jdk%{jdk_version_full}
Requires:       ca-certificates

%description
Dummy package to ensure "provides" for Oracle's JDK are available to the OS to avoid installing OpenJDK unnecessarily

%files

# Symlink ca-certificates cacerts for Java over JDK
%triggerin -p /bin/bash -- jdk%{jdk_version_full}
[[ -f %{jre_home}/lib/security/cacerts ]] && mv -f %{jre_home}/lib/security/cacerts %{jre_home}/lib/security/cacerts.divert
ln -sf %{pki_dir}/java/cacerts %{jre_home}/lib/security/cacerts

%triggerun -- jdk%{jdk_version_full}
[[ -h %{jre_home}/lib/security/cacerts ]] && rm -f %{jre_home}/lib/security/cacerts
[[ -f %{jre_home}/lib/security/cacerts.divert ]] && mv -f %{jre_home}/lib/security/cacerts.divert %{jre_home}/lib/security/cacerts

%triggerpostun -- jdk%{jdk_version_full}
[[ -h %{jre_home}/lib/security/cacerts ]] && rm -f %{jre_home}/lib/security/cacerts
[[ -f %{jre_home}/lib/security/cacerts.divert ]] && mv -f %{jre_home}/lib/security/cacerts.divert %{jre_home}/lib/security/cacerts


%changelog
* Sun Jan 22 2017 Brett Delle Grazie <brett.dellegrazie@gmail.com> - 1.8.0_112-2
- Handle ca-certificates as well
* Sun Jan 22 2017 Brett Delle Grazie <brett.dellegrazie@gmail.com> - 1.8.0_112-1
- Initial version of the package
