.. _pa-dlna:

pa-dlna command
===============

Synopsis
--------

:program:`pa-dlna` [*options*]

UPnP discovery is run on all the networks (except the loopbak interface ``lo``)
when the ``--ip-addresses`` and ``--nics`` command line arguments are not used
or empty. Otherwise both arguments may be used indifferently or even jointly.

Options
-------

.. option::  -h, --help

   Show this help message and exit.

.. option::  --version, -v

   Show program's version number and exit.

.. option:: --ip-addresses IP_ADDRESSES, -a IP_ADDRESSES

   IP_ADDRESSES is a comma separated list of the local IPv4 addresses of the
   networks where UPnP devices may be discovered (default: ``''``).

.. option:: --nics NICS, -n NICS

   NICS is a comma separated list of the names of network interface controllers
   where UPnP devices may be discovered, such as ``wlan0,enp5s0`` for
   example (default: ``''``).

.. option::  --msearch-interval MSEARCH_INTERVAL, -m MSEARCH_INTERVAL

   Set the time interval in seconds between the sending of the MSEARCH datagrams
   used for UPnP device discovery (default: 60).

.. option::  --msearch-port MSEARCH_PORT, -p MSEARCH_PORT

   Set the local UDP port for receiving MSEARCH response messages from UPnP
   devices, a value of ``0`` means letting the operating system choose an
   ephemeral port (default: 0).

.. option::  --ttl TTL

   Set the IP packets time to live to TTL (default: 2).

.. option::  --port PORT

   Set the TCP port on which the HTTP server handles DLNA requests (default:
   8080).

.. option::  --dump-default, -d

   Write to stdout (and exit) the default built-in configuration.

.. option::  --dump-internal, -i

   Write to stdout (and exit) the configuration used internally by the program
   on startup after the pa-dlna.conf user configuration file has been parsed.

.. option::  --clients-uuids PATH

   PATH is the name of the file where are stored the associations between client
   applications and their DLNA device uuid. This is used to work around
   `Wireplumber issue 511`_ on Pipewire.

   Client applications names that play an audio stream are written by pa-dlna to
   PATH with the uuid of the DLNA device. In a next pa-dlna session and upon
   discovering a DLNA device, the list of the playback streams currently being
   currently run by the sound server  is inspected by pa-dlna and if one of the
   client applications names matches an entry in PATH that maps to this DLNA
   device, then the playback stream is moved to the DLNA device by pa-dlna.

   These associations can be removed from PATH or commented out by the user upon
   becoming irrelevant.

.. option::  --loglevel {debug,info,warning,error}, -l {debug,info,warning,error}

   Set the log level of the stderr logging console (default: info).

.. option:: --systemd

   Run as a systemd service unit.

.. option::  --logfile PATH, -f PATH

   Add a file logging handler set at ``debug`` log level whose path name is PATH.

.. option::  --nolog-upnp, -u

   Ignore UPnP log entries at ``debug`` log level.

.. option::  --log-aio, -y

   Do not ignore asyncio log entries at ``debug`` log level; the default is to
   ignore those verbose logs.

.. option::  --test-devices MIME-TYPES, -t MIME-TYPES

   MIME-TYPES is a comma separated list of distinct audio mime types. A
   DLNATestDevice is instantiated for each one of these mime types and
   registered as a virtual DLNA device. Mostly for testing.

.. _Wireplumber issue 511:
        https://gitlab.freedesktop.org/pipewire/wireplumber/-/issues/511
