#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

KDIR = kerneltools.getKernelVersion()

def build():
    shelltools.system("patch -p1 < ndiswrapper-1.59.patch")
    autotools.make("-C /lib/modules/%s/build M=`pwd`" % KDIR)

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/etc/ndiswrapper")

    pisitools.dodoc("README", "AUTHORS", "ChangeLog")
