:title: Setting up a Raid1 Btrfs Home partition
:slug: setting-up-a-raid1-btrfs-home-partition
:date: 2014-04-19 03:39:21
:tags: linux, howto, btrfs

.. code-block:: bash

	$ sudo su -

	$ mkfs.btrfs -f /dev/sdb
	$ mkfs.btrfs -f /dev/sdc

	$ btrfs fi show

Should give you output something like this:

.. code-block:: txt

	Label: none  uuid: bfee4bb4-3886-406f-94df-cb2dcf42f044
		Total devices 1 FS bytes used 112.00KiB
		devid    1 size 5.00GiB used 548.00MiB path /dev/sdc

	Label: none  uuid: a0192bd3-a8f7-477b-9bae-fea9a48aa1ab
		Total devices 1 FS bytes used 2.24GiB
		devid    1 size 5.00GiB used 3.04GiB path /dev/sdb

	Btrfs v3.12


$ mkdir /mnt/butter

$ mount /dev/sdb /mnt/butter
$ btrfs device add -f /dev/sdc /mnt/butter

.. code-block:: bash

	$ btrfs fi show

	Label: none  uuid: a0192bd3-a8f7-477b-9bae-fea9a48aa1ab
		Total devices 2 FS bytes used 2.24GiB
		devid    1 size 5.00GiB used 3.04GiB path /dev/sdb
		devid    2 size 5.00GiB used 0.00 path /dev/sdc

	Btrfs v3.12

	$ btrfs fi df /mnt/butter

	Data, single: total=2.51GiB, used=2.23GiB
	System, DUP: total=8.00MiB, used=16.00KiB
	System, single: total=4.00MiB, used=0.00
	Metadata, DUP: total=256.00MiB, used=2.94MiB
	Metadata, single: total=8.00MiB, used=0.00


	$ btrfs balance start -v -dconvert=raid1 -mconvert=raid1 /mnt/butter

	$ btrfs fi df /mnt/butter

	Data, RAID1: total=3.96GiB, used=2.23GiB
	System, RAID1: total=32.00MiB, used=16.00KiB
	System, single: total=4.00MiB, used=0.00
	Metadata, RAID1: total=256.00MiB, used=2.55MiB


	$ btrfs fi show
	Label: none  uuid: a0192bd3-a8f7-477b-9bae-fea9a48aa1ab
		Total devices 2 FS bytes used 2.24GiB
		devid    1 size 5.00GiB used 4.25GiB path /dev/sdb
		devid    2 size 5.00GiB used 4.25GiB path /dev/sdc



	$ btrfs balance start -v -dconvert=raid1 -mconvert=raid1 /mnt/btrfs/

	Dumping filters: flags 0x7, state 0x0, force is off
	  DATA (flags 0x100): converting, target=16, soft is off
	  METADATA (flags 0x100): converting, target=16, soft is off
	  SYSTEM (flags 0x100): converting, target=16, soft is off
	... 10 hours later ...
	Done, had to relocate 1269 out of 1269 chunks


	$ btrfs fi show
	Label: home1  uuid: 43f4a92c-9475-400b-a6e4-88639f55dd71
		Total devices 2 FS bytes used 1.23TiB
		devid    1 size 1.82TiB used 1.24TiB path /dev/sdb1
		devid    2 size 1.82TiB used 1.24TiB path /dev/sdc1


	$ btrfs fi df /mnt/btrfs/

	Data, RAID1: total=1.23TiB, used=1.23TiB
	System, RAID1: total=32.00MiB, used=184.00KiB
	Metadata, RAID1: total=6.00GiB, used=2.71GiB



	watch -cn 300 btrfs balance status /mnt/btrfs/
