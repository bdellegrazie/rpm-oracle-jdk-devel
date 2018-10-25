%global jdk_major %{?jdk_version_major}%{!?jdk_version_major:8}
%global jdk_minor %{?jdk_version_minor}%{!?jdk_version_minor:0}
%global jdk_patch %{?jdk_version_patch}%{!?jdk_version_patch:181}
%global iteration %{?ITERATION}%{!?ITERATION:1}

%ifarch x86_64 amd64
%global jdk_rpm_arch amd64
%else
%global jdk_rpm_arch i586
%endif

%global jdk_version_api   1.%{jdk_major}.%{jdk_minor}
%global jdk_version_api_major   1.%{jdk_major}
%global jdk_version_full  %{jdk_version_api}_%{jdk_patch}
%global jdk_rpm_version 2000:%{jdk_version_full}-fcs

%global jdk_home %{_prefix}/java/jdk%{jdk_version_full}-%{jdk_rpm_arch}
%global jre_home %{jdk_home}/jre
%global pki_dir %{_sysconfdir}/pki

Name:           jdk%{jdk_version_api_major}-devel
Version:        %{jdk_version_full}
Release:        %{iteration}%{?dist}
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
Provides:       libjawt.so()(64bit)
Provides:       libjawt.so(SUNWprivate_1.1)(64bit)
Provides:       libjvm.so()(64bit)
Provides:       libjvm.so(SUNWprivate_1.1)(64bit)

License:        Apache License v2.0
URL:            http://www.oracle.com/technetwork/java/javase/downloads/index.html

Requires:       ca-certificates
Requires:       jdk1.8 = %{jdk_rpm_version}

%description
Dummy package to ensure "provides" for Oracle's JDK are available to the OS to avoid installing OpenJDK unnecessarily

%files

# Symlink CA certs
%triggerin -p /bin/bash -- jdk%{jdk_version_api_major}=2000:%{jdk_version_full}-fcs
[[ -f "%{jre_home}/lib/security/cacerts" ]] && mv -f "%{jre_home}/lib/security/cacerts" "%{jre_home}/lib/security/cacerts.divert"
ln -sf "%{pki_dir}/java/cacerts" "%{jre_home}/lib/security/cacerts"

%triggerun -- jdk%{jdk_version_api_major}=%{jdk_version_full}
[[ -h "%{jre_home}/lib/security/cacerts" ]] && rm -f "%{jre_home}/lib/security/cacerts"
[[ -f "%{jre_home}/lib/security/cacerts.divert" ]] && mv -f "%{jre_home}/lib/security/cacerts.divert" "%{jre_home}/lib/security/cacerts"

%triggerpostun -- jdk%{jdk_version_api_major}=%{jdk_version_full}
[[ -h "%{jre_home}/lib/security/cacerts" ]] && rm -f "%{jre_home}/lib/security/cacerts"
[[ -f "%{jre_home}/lib/security/cacerts.divert" ]] && mv -f "%{jre_home}/lib/security/cacerts.divert" "%{jre_home}/lib/security/cacerts"

%changelog
* Wed Oct 24 2018 Brett Delle Grazie <brett.dellegrazie@gmail.com> - 1.8.0_181-1
- Updated to 1.8.0_181
- Removed Policy JAR management (no longer required) so the corresponding JCE RPM is not required either

* Fri Jan 19 2018 Brett Delle Grazie <brett.dellegrazie@gmail.com> - 1.8.0_162-1
- Updated to 1.8.0_162
- RPM rename due to Oracle JDK rename in 1.8.0_144
* Wed Oct 20 2017 Brett Delle Grazie <patrickfmarques@gmail.com> - 1.8.0_152
- Updated to 1.8.0_152
* Wed Jun 14 2017 Brett Delle Grazie <brett.dellegrazie@gmail.com> - 1.8.0_131-1
- Renamed to jdk-<version>-helper
- Updated to 1.8.0_131
- Support Java Cryptography Extensions as well
* Sun Jan 22 2017 Brett Delle Grazie <brett.dellegrazie@gmail.com> - 1.8.0_112-2
- Handle ca-certificates as well
* Sun Jan 22 2017 Brett Delle Grazie <brett.dellegrazie@gmail.com> - 1.8.0_112-1
- Initial version of the package
