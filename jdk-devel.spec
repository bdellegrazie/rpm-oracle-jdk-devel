%global jdk_major %{?jdk_version_major}%{!?jdk_version_major:8}
%global jdk_minor %{?jdk_version_minor}%{!?jdk_version_minor:0}
%global jdk_patch %{?jdk_version_patch}%{!?jdk_version_patch:112}
%global jdk_version_api   1.%{jdk_major}.%{jdk_minor}
%global jdk_version_full  %{jdk_version_api}_%{jdk_patch}

Name:		jdk%{jdk_version_full}-devel
Version:	%{jdk_version_full}
Release:	%{ITERATION}%{?dist}
Summary:	Oracle JDK Development Dummy Package
Group:		Development/Tools
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
License:	Apache License v2.0
URL:		http://www.oracle.com/technetwork/java/javase/downloads/index.html

Requires:	jdk%{jdk_version_full}

%description
Dummy package to ensure "provides" for Oracle's JDK are available to the OS to avoid installing OpenJDK unnecessarily

%files

%changelog
* Sun Jan 22 2017 Brett Delle Grazie <brett.dellegrazie@gmail.com> - 1.8.0_112-1
- Initial version of the package
