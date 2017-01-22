# jdk-devel RPM

Oracle JDK's devel dependencies

This RPM adds the necessary `provides` to RPM database to prevent openjdk versions from being erroneously installed when only Oracle's JDK is present.
The `provides` are specific to the version of Oracle's JDK so if multiple versions are present, multiple versions of this RPM would need to be installed.

## Making the RPM
The RPM only requires:
* make
* rpmbuild
* the version number of the Oracle JDK RPM to create a jdk-devel rpm for

Syntax:
```
make JDK_MAJOR=8 JDK_MINOR=0 JDK_PATCH=112
```

Where the Oracle JDK we're producing an RPM for is 1.8.0_112
The leading '1' is assumed at this time.
