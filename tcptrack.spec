%define name tcptrack
%define version 1.3.0
%define release 1
%define prefix /usr

Summary: A packet sniffer which displays TCP information like the 'top' command
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Utilities/Network
Source: %{name}-%{version}.tar.gz
URL: http://www.rhythm.cx/~steve/devel/tcptrack
BuildRoot: %{_tmppath}/%{name}-buildroot

%description 
tcptrack is a sniffer which displays information about TCP connections it
sees on a network interface. It passively watches for connections on the
network interface, keeps track of their state and displays a list of
connections in a manner similar to the unix 'top' command. It displays
source and destination addresses and ports, connection state, idle time, and
bandwidth usage.

%prep
%setup -q

%build
./configure --prefix=%{prefix} --mandir=%{prefix}/share/man
make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{prefix}/bin/tcptrack
%{prefix}/share/man/man1/tcptrack.1.gz

%doc  AUTHORS COPYING ChangeLog README INSTALL NEWS

%changelog
* Wed Dec 20 2006 Steve Benson <steve@NO.rhythm.SPAM.cx.REMOVE
- Fixes for compiling on gcc 4.1+ (thanks to Dries Verachtert, Christian
  Weiss)
- 802.1q VLAN support (thanks to Adam Osuchowski)

* Sat Mar 12 2005 Steve Benson <steve@NO.rhythm.SPAM.cx.REMOVE>
- This release fixes a bug that causes a floating point exception when
  handling packets with source or destination ports of 0.

* Sun Oct 10 2004 Steve Benson <steve@NO.rhythm.SPAM.cx.REMOVE>
- Fixed a memory leak in the TCPConnection class.

* Mon Aug 16 2004 Steve Benson <steve@NO.rhythm.SPAM.cx.REMOVE>
- Added a total for the speed column at the bottom of the display. Thanks to
  Leo Costela for the patch.
- Fixed a few minor user interface bugs (mostly exposed by the above patch).

* Thu Jun  3 2004 Steve Benson <steve@NO.rhythm.SPAM.cx.REMOVE>
- Fixed assertion an assertion failure (in IPv4Packet.cc) bug.
- tcptrack can now run on interfaces with no IPv4 addresses (ie, stealth
  interfaces).
- Fixed a few crashes and assertion failures on Mac OSX and FreeBSD caused
  by missing pthread_*_init calls. Thanks to Chuck Schied for the patch.
- Added a timeout for connections in the CLOSING state. Connections may get
  stuck in that state due to dropped packets, timeouts by the peers, or
  there may be a bug in the TCPConnection state machine code that I haven't
  found yet.
- ChangeLog is now a regular ChangeLog, not a development log. The contents
  of this file were previously in the NEWS file. NEWS will now contain
  the same stuff that's on the web page.

* Mon May 10 2004 Steve Benson <steve@NO.rhythm.SPAM.cx.REMOVE>
- Fixed problem where tcptrack would silently not work on certain ppp
  connections (a.k.a. debian bug #245227)
- Added support for NULL and RAW pcap interface types. tcptrack should now
  work on all linux PPP, ethernet, tun/tap and local loopback interfaces.
- tcptrack now compiles properly with gcc 3.4. Thanks to Jim Gifford.
- Added EXAMPLES section to man page and a few extra notes to man page about
  guessing, pause/sort options.

* Sun Apr 18 2004 Steve Benson <steve@NO.rhythm.SPAM.cx.REMOVE>
- Fixed problems with crashes on FreeBSD and Solaris. Stack sizes of certain
  threads were too small (adjustable in defs.h).

* Wed Mar 31 2004 Steve Benson <steve@NO.rhythm.SPAM.cx.REMOVE>
- Idle time can be computed & updated more than once a second now and may be 
  more accurate under heavy load. See the man page for more info.
- Idle time now displays hours/minutes instead of always seconds.
- tcptrack can now see connections that were started before tcptrack was.
- Added -d option to disable connection detection (above).
- List of connections is now scrollable with arrow keys. 
- Added pause/unpause and enable/disable sort options
- Added status display for number of connections shown and total and pause /
  sort options
- tcptrack now exits cleaner
- internal data structures changed to make tcptrack more CPU efficient.
- lots of internal code changes to make code more organized and reusable.
- More error handling added.
- Added -p option to enable/disable promisc mode
- Sorting is now done by speed first, least idle time second. Before, idle 
  time was not factored in the sorting.
- Stack size of each thread reduced. configurable in defs.h. tcptrack now
  uses a lot less virtual address space.

* Thu Dec  4 2003 Steve Benson <steve@NO.rhythm.SPAM.cx.REMOVE>
- Fixed some Solaris build issues
- configure script updated 
- Fixed assert compile problem on some systems

* Thu Nov 27 2003 Steve Benson <steve@NO.rhythm.SPAM.cx.REMOVE>
- Fixed a memory leak
- fixed a problem that would cause tcptrack to segfault under heavy load
- tcptrack no longer grabs packet payloads off of the network, making it
  more efficient (especially in terms of memory under heavy load).
- FreeBSD (and probably other BSD) timing issues have been fixed.
- New timing options controllable in defs.h
- tcptrack only works on ethernet interfaces for now. It will now fail to
  start up on non-ethernet interfaces and print an error.
- tcptrack still won't compile on Solaris. I'm working on getting access to
  a Solaris machine to test on.

* Sun Nov 23 2003 Steve Benson <steve@NO.rhythm.SPAM.cx.REMOVE>
- First public release.

 
