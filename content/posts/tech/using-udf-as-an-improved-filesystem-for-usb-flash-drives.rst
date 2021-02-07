:title: Using UDF as an improved filesystem for USB Flash Drives
:slug: using-udf-as-an-improved-filesystem-for-usb-flash-drives
:date: 2013-05-13 19:48:22
:tags: linux, windows, fat32, udf, filesystems, howto
:meta_description: Most USB Flash drives are formatted using the FAT32 filesystem - which only supports files up to 4GB each, no matter how much free space you've got.

Ever tried to copy something onto a USB flash drive, only to discover that the file was to big to copy?

This is because most USB Flash drives are formatted using the FAT32 [#fat32]_ filesystem - which only supports individual files up to 4GB in size, no matter how much free space you've got. It also only supports drives up to 2TB, can't store symbolic links, can't store files with these characters in the name: ``"*/:<>?\|`` -- and is generally pretty crappy.

The solution is to use a better filesystem
-------------------------------------------

There are `many filesystems <http://en.wikipedia.org/wiki/Comparison_of_file_systems>`_ to choose from - but there are a few criteria that a good USB flash drive filesystem needs to meet which cuts down the choices quite a bit:

- Compatible with every computer - just plug it in and it should work
- Has no permissions, or optional permissions, so you don't need to be logged in as the same user everywhere you want to access the files
- Can handle large files and volumes, special characters and is reliable - is a proper modern filesystem
- Ideally, is an open standard, isn't patent encumbered - or at the very least has a solid open implementation.

A better filesystem: The Candidates
-------------------------------------

+------------+------------+-------------+--------+-----------+
| Filesystem | Compatible | Permissions | Modern | Open(ish) |
+============+============+=============+========+===========+
| ext2,3,4   | linux      | ✗           | ✓      | ✓         |
+------------+------------+-------------+--------+-----------+
| hfs+       | linux, mac | ✗           | ✓      | (✓)       |
+------------+------------+-------------+--------+-----------+
| exFAT      | win, mac   | ✗           | ✓      | ✗         |
+------------+------------+-------------+--------+-----------+
| ntfs       | ✓          | ✗           | ✓      | (✓)       |
+------------+------------+-------------+--------+-----------+
| fat32      | ✓          | ✓           | ✗      | (✓)       |
+------------+------------+-------------+--------+-----------+
| udf        | ✓          | ✓           | ✓      | ✓         |
+------------+------------+-------------+--------+-----------+

Using a list table:

.. list-table::
	:header-rows: 1

	* - Filesystem
		- Compatible
		- Permissions
		- Modern
		- Open(ish)

	* - ext2,3,4
		- linux
		- ✗
		- ✓
		- ✓

So, the winner is... UDF [#udf]_. This filesystem is mostly used for DVD's - but supports full random access read/write storage, like any general purpose filesystem. Pretty much all OS's can read DVD's out of the box, and it supports large files and volumes. Every OS since Windows 95 can read UDF natively, and almost all of them can write to it too.

The fly in the ointment, as usual, is older versions of Windows. Windows 95 - 2003 **can't write to UDF volumes natively** - you need extra 3rd party software. Windows Vista, 7 & 8 **can** both read and write to UDF volumes, though. See `here for a full list of OS compatibility <http://en.wikipedia.org/wiki/Universal_Disk_Format#Compatibility>`_. Microsoft are now calling UDF the 'Live File System' [#live_file_system]_ and are still assuming it's just for DVD's.

Formatting your USB Flash Drive with UDF
-----------------------------------------

.. caution::
	If you need to be able to write to your USB flash drive on older version of Windows, pre-Vista - **then don't do this**!

	Also, this will wipe & reformat your USB flash drive, so backup anything you want to keep on another drive first.

To format your USB Flash drive using UDF, you need to do the following:

You'll probably need to install ``udftools`` first:

.. code-block:: console

	$ sudo apt-get install udftools

then wipe the existing partition table, to prevent the drive being detected as FAT. Assuming you USB drive is /dev/sdi:

.. code-block:: console

	$ sudo dd if=/dev/zero of=/dev/sdi bs=1M count=1

Then format it as UDF:

.. code-block:: console

	$ sudo mkudffs -b 512 --media-type=hd --utf8 --lvid=DriveLabel --vid=DriveLabel --fsid=DriveLabel  /dev/sdi

Change ``DriveLabel`` to whatever you want to drive to be called. Linux doesn't seem to take any notice of this, but apparently windows displays ``lvid`` as the drive label.

If you need out of the box compatibility back to Windows 95, you can add this:

.. code-block:: console

    --udfrev=0x0102

otherwise you'll get Windows XP and up [#udf_rev]_.

The ``-b 512`` parameter forces a file system block size equal to the USB stick's physical block size - as required by the UDF specification. It'll *probably* work without this, but it's a good idea to set this to ensure maximum compatibility & reliability. Change the ``512`` if you're lucky enough to have a USB flash drive with a larger block size. To find out what the physical block size is, run this:

.. code-block:: console

    $ sudo hdparm -I /dev/sdi | grep -i physical
    ...
    Logical/Physical Sector size:           512 bytes

This worked well for me on Xubuntu Linux: the performance is good, I was able to copy some virtual machines from one computer to another - a total of 11.5 GB of files, with individual files up to 6.5 GB each - without any problems.

There are some Mac instructions `here <http://tanguy.ortolo.eu/blog/article93/usb-udf#c1359985488-1>`_ which I haven't tried -- and I have *no idea* how you do this on Windows; let me know in the comments if you do.

------------

Footnotes & References:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I owe most of this to `Tanguy Ortolo's excellent blog post which you can find here <http://tanguy.ortolo.eu/blog/article93/usb-udf>`_ & this `Arch linux forum post <https://bbs.archlinux.org/viewtopic.php?pid=1030147>`_.

.. [#fat32] **FAT32** - File Allocation Table (FAT) is the name of a computer file system architecture and a family of proprietary file systems utilizing it: http://en.wikipedia.org/wiki/FAT32#FAT32
.. [#udf] **Universal Disk Format (UDF)** - is a profile of the specification known as ISO/IEC 13346 and ECMA-167 and is an open vendor-neutral file system for computer data storage for a broad range of media: http://en.wikipedia.org/wiki/Universal_Disk_Format
.. [#live_file_system] **Which CD or DVD format should I use?**: http://windows.microsoft.com/en-us/windows-vista/which-cd-or-dvd-format-should-i-use
.. [#udf_rev] **UDF has Multiple revisions**: http://en.wikipedia.org/wiki/Universal_Disk_Format#Revisions