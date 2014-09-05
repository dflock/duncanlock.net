:title: Reliably Building VirtualBox Guest Additions on CentOS 6.x
:slug: reliably-building-virtualbox-guest-additions-on-centos-6x
:date: 2014-01-22 19:54:48
:tags: linux, centos, virtualbox

We use CentOS VM's at work to emulate our production environment - and it took me a while to figure out how to get the VirtualBox Guest Additions to build reliably on CentOS 6.4/5. This is what I've currently settled on as a reliable method.

First, make sure that you've got the kernel headers and tools installed that you need to build stuff:

.. code-block:: base

    sudo yum update -y
    sudo yum install gcc kernel-devel kernel-headers dkms make bzip2 perl

Make sure that you've only got the current set of kernel headers installed - the one for the kernel you're actually running. Having more than one set installed prevents this working properly. Running this should show you one version of each kernel package:

.. code-block:: bash

    rpm -qa | grep kernel | sort

It should look something like this:

.. code-block:: text

    dracut-kernel-004-336.el6_5.2.noarch
    kernel-2.6.32-431.3.1.el6.x86_64
    kernel-devel-2.6.32-431.3.1.el6.x86_64
    kernel-firmware-2.6.32-431.3.1.el6.noarch
    kernel-headers-2.6.32-431.3.1.el6.x86_64

if you have multiple versions of one of the kernel packages installed, it will look something like this:

.. code-block:: text

    dracut-kernel-004-336.el6_5.2.noarch
    kernel-2.6.32-132.1.2.el6.x86_64
    kernel-2.6.32-431.3.1.el6.x86_64
    kernel-devel-2.6.32-132.1.2.el6.x86_64
    kernel-devel-2.6.32-431.3.1.el6.x86_64
    kernel-firmware-2.6.32-431.3.1.el6.noarch
    kernel-headers-2.6.32-431.3.1.el6.x86_64

remove the older ones:

.. code-block:: bash

    sudo rpm -e kernel-2.6.32-132.1.2.el6.x86_64 kernel-devel-2.6.32-132.1.2.el6.x86_64

Now we're ready to install & build the guest additions, so mount the CD by selecting 'Install Guest Additions' from the VirtualBox menu. Don't autorun it - you'll need to run the following to install it properly.

Some of this needs to run as sudo, and we need to export variables that sudo can see, so we'll just do all of the following as root:

.. code-block:: bash

    sudo su -
    export MAKE='/usr/bin/gmake -i'
    export KERN_DIR=/usr/src/kernels/`uname -r`
    # Change the version number here to whatever is current
    # cd /media/VB<tab> will probably work
    cd /media/VBOXADDITIONS_4.3.6_91406/
    ./VBoxLinuxAdditions.run

This should build & install all the guest additions successfully. If it doesn't, let me know in the comments.