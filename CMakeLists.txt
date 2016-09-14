PROJECT (dnf-plugins-extras NONE)
CMAKE_MINIMUM_REQUIRED (VERSION 2.4)

if (NOT PYTHON_DESIRED)
    set (PYTHON_DESIRED "2")
endif()

if (${PYTHON_DESIRED} STREQUAL "2")
	FIND_PACKAGE (PythonInterp REQUIRED)
else()
	SET(Python_ADDITIONAL_VERSIONS 3.3)
	FIND_PACKAGE(PythonLibs 3.0)
	FIND_PACKAGE(PythonInterp 3.0 REQUIRED)
endif()

EXECUTE_PROCESS(COMMAND ${PYTHON_EXECUTABLE} -c "from sys import stdout; from distutils import sysconfig; stdout.write(sysconfig.get_python_lib())" OUTPUT_VARIABLE PYTHON_INSTALL_DIR)
EXECUTE_PROCESS(COMMAND ${PYTHON_EXECUTABLE} -c "import sys; sys.stdout.write('%s.%s' % (sys.version_info.major, sys.version_info.minor))" OUTPUT_VARIABLE PYTHON_MAJOR_DOT_MINOR_VERSION)
MESSAGE(STATUS "Python install dir is ${PYTHON_INSTALL_DIR}")

SET (SYSCONFDIR /etc)
SET (SYSTEMD_DIR /usr/lib/systemd/system)

ADD_SUBDIRECTORY (doc)
ADD_SUBDIRECTORY (etc)
ADD_SUBDIRECTORY (plugins)
ADD_SUBDIRECTORY (po)

if(WITH_SYSTEMD)

    EXECUTE_PROCESS(COMMAND pkg-config systemd --variable systemdsystemunitdir OUTPUT_VARIABLE SYSTEMD_CONFIGURATIONS_FILES_DIR)

    configure_file(${CMAKE_SOURCE_DIR}/dnf-system-upgrade.service ${CMAKE_SOURCE_DIR}/dnf-system-upgrade.service @ONLY)
    message( STATUS "Configured systemd unit file dnf-system-upgrade" )

    if(EXISTS ${SYSTEMD_CONFIGURATIONS_FILES_DIR})
        install(FILES ${CMAKE_SOURCE_DIR}/dnf-system-upgrade.service DESTINATION ${SYSTEMD_CONFIGURATIONS_FILES_DIR} )
        message(STATUS "Unit file will be installed to ${SYSTEMD_CONFIGURATIONS_FILES_DIR} after make install" )
    else(EXISTS ${SYSTEMD_CONFIGURATIONS_FILES_DIR})
        message(STATUS "Unit file will not be installed to ${SYSTEMD_CONFIGURATIONS_FILES_DIR} after make install" )
    endif(EXISTS ${SYSTEMD_CONFIGURATIONS_FILES_DIR})

endif(WITH_SYSTEMD)
