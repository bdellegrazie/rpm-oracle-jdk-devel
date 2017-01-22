JDK_MAJOR:=8
JDK_MINOR:=0
JDK_PATCH:=112
ITERATION:=1
ARCH:=native
BUILD_DIR:=build

.PHONY: rpm rpm-clean clean packages

all: packages

rpm-clean:
	rm -f *.rpm

clean: rpm-clean

dist-clean: clean

rpm: rpm-clean
	mkdir -p $(BUILD_DIR)/BUILD
	mkdir -p $(BUILD_DIR)/BUILDROOT
	mkdir -p $(BUILD_DIR)/RPMS
	rpmbuild -bb -D'jdk_version_major $(JDK_MAJOR)'\
 -D'jdk_version_minor $(JDK_MINOR)'\
 -D'jdk_version_patch $(JDK_PATCH)'\
 -D'ITERATION $(ITERATION)'\
 -D'_builddir $(PWD)/$(BUILD_DIR)/BUILD'\
 -D'_rpmdir   $(PWD)/$(BUILD_DIR)/RPMS'\
 -D'_sourcedir $(PWD)'\
 -D'_buildrootdir $(PWD)/$(BUILD_DIR)/BUILDROOT'\
 jdk-devel.spec
	mv $(BUILD_DIR)/RPMS/$$(uname -m)/*.rpm .

packages: rpm

clean: rpm-clean

dist-clean: clean

