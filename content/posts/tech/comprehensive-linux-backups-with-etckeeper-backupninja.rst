:title: Comprehensive Linux Backups with etckeeper & backupninja
:slug: comprehensive-linux-backups-with-etckeeper-backupninja
:date: 2013-08-27 12:36:36
:tags: linux, sysadmin
:meta_description: Having an easy to setup, comprehensive, automated backup strategy is very relaxing - here's how to create one. Do it now!

I'm going to build on `Jamie Zawinski's excellent advice about backups <http://www.jwz.org/doc/backups.html>`_, which you should read first. This is basically that, but with some extra bits.

The plan is to use `Backupninja <https://labs.riseup.net/code/projects/backupninja>`_ to backup everything. Backupninja provides a centralized way to configure and schedule many different backup utilities, by dropping a few simple configuration files into ``/etc/backup.d/``.

I have a two hard disk setup for my desktop linux box - my ``/home`` folders live on one disk and ``/`` lives on another one. I don't want to backup everything from the system disk - I can re-install it in 10 mins, quicker than restoring a backup. I just want to backup a few system wide configuration items from ``/`` - and my MySQL databases, which are kept on there.

To do this, I'm going to tell ``backupninja`` to backup the system config, MySQL and anything else I want backed up up to my ``/home`` folder, then backup the whole ``/home`` folder.

I'm also going to do extra backups to Amazon S3, so we'll have some extra cloud backups of critical stuff.

I'm going to use ``etckeeper`` to store the system wide config from ``/etc`` in a ``git`` repository - this way I get a history of changes and the ability to roll back config changes. I'm then just going to backup that git repository.

Backing up System Configuration using etckeeper
------------------------------------------------

Basically, ``etckeeper`` runs itself - you just have to install it and switch it on. You can commit manual changes to ``/etc`` manually if you want to, but by default it hooks into ``apt`` to commit changes when you install things and has a ``cron`` job to backup outstanding changes daily:

.. epigraph::

   *etckeeper* allows the contents of ``/etc`` be easily stored in Version Control System (VCS) repository. It hooks into *apt* to automatically commit changes to ``/etc`` when packages are installed or upgraded. Placing ``/etc`` under version control is considered an industry best practice, and the goal of *etckeeper* is to make this process as painless as possible.

   -- https://help.ubuntu.com/12.10/serverguide/etckeeper.html

To install ``etckeeper``, run this in a console:

.. code-block:: bash

    sudo apt-get install git etckeeper

The ``etckeeper`` from the Ubuntu repositories is setup to use ``bzr`` by default, because they're idiots, so lets change it to use ``git``. Edit the ``/etc/etckeeper.conf`` file like so:

.. code-block:: ini

    # The VCS to use.
    #VCS="hg"
    VCS="git"
    #VCS="bzr"
    #VCS="darcs"

If you have ``bzr`` installed for some reason, then the ``etckeeper`` ``bzr`` repository will be automatically initialized. To undo this, run this:

.. code-block:: bash

    sudo etckeeper uninit

Then to re-initialize with a git repository:

.. code-block:: bash

    sudo etckeeper init

If you don't have ``bzr`` installed it will fail to initialize the ``bzr`` repo, so you can just run that.

The only weird thing about running ``etckeeper`` is that it keeps its git repo inside ``/etc`` (which is fine) - but it means that it runs as ``root`` which takes a bit of getting used to if you're going to use it manually. You will also need to setup at least a minimal git config for the root user:

.. code-block:: bash

    sudo -s
    git config --global user.name "Duncan Lock"
    git config --global user.email duncan.lock@gmail.com

Once you've done that you can check everything in:

.. code-block:: bash

    cd /etc
    sudo git status
    sudo etckeeper commit "Initial Commit"


Setting up backupninja
--------------------------

Install backupninja like this:

.. code-block:: bash

    sudo apt-get install backupninja

This will create a config folder: ``/etc/backup.d`` where we'll be storing our backup jobs - and a config file ``/etc/backupninja.conf`` which we'll configure like this - everything else can stay at its defaults:

.. code-block:: ini

    reportdirectory = /home/duncan/Dropbox/backups
    when = everyday at 02:00

I'm sending the backup report log to dropbox and kicking everything off at 2am.

Now we'll setup each of the backup jobs we want to run, by adding a simple text config file to the ``/etc/backups.d`` folder. These are executed in alphanumeric order, so I suggest you create them like this:

.. image:: /static/images/posts/comprehensive-linux-backups-with-etckeeper-backupninja/backupninja-etc-backupsd-files.png

The only caveat with these is that Backupninja config files need to be owned by root and not world or group readable, so: ``-rw\-\-\-\-\-\-\-``

10-little-things.sh
=====================

This does some housekeeping and copies some little things into the /home folder for later backing up.

.. code-block:: bash

    # Backup installed packages list
    dpkg --get-selections > /home/duncan/backups/dpkg-selections.txt

    # Take simple copies of major config files for convenience
    cp /etc/hosts /home/duncan/backups/
    cp /etc/fstab /home/duncan/backups/

    # Copy a few things over to dropbox, for extra safety
    cp /home/duncan/backups/hosts /home/duncan/Dropbox/backups/
    cp /home/duncan/backups/fstab /home/duncan/Dropbox/backups/

    # Change these so that I can use them
    chown -R duncan /home/duncan/backups/
    chown -R duncan /home/duncan/Dropbox/backups/

    # Backup etckeeper, plus any other git repo's I've backed up to /home/duncan/backups/git-backups
    cd /etc/
    git bundle create /home/duncan/backups/git-backups/etc.git-bundle --all
    rsync -vaxAX --delete --ignore-errors /home/duncan/backups/git-backups /home/duncan/Dropbox/backups/git-backups

50-daily-all-db.mysql
======================

This backs up all my MySQL databases into my home folder using ``mysqldump``:

.. code-block:: ini

    ### backupninja mysql config file ###

    databases   = all
    backupdir   = /home/duncan/backups/mysql
    hotcopy     = no
    sqldump     = yes
    compress    = yes
    dbusername  = ******
    dbpassword  = ******

60-daily-home-rsync.sh
========================

This is the big one that backups the /home folders to an external USB disk:

.. code-block:: bash

    # The actual backupninja .rsync support is overly complex - I should probably use it,
    # but all I wanted was this:

    rsync -vaxAX --delete --ignore-errors /home/ /media/duncan/backups/

70-photos-to-s3.sh
====================

This one backups up the photo's to Amazon S3. It requires ``s3cmd`` to be installed and configured:

.. code-block:: bash

    # Backup photo's to Amazon S3
    s3cmd -vH --progress --guess-mime-type sync /home/duncan/Photos/ s3://dflock-backups/dunc-desktop/photos/

To install s3cmd, do this:

.. code-block:: bash

    sudo apt-get install s3cmd
    s3cmd --configure

See here for more:

.. epigraph::

   You will be asked for the two keys - copy and paste them from your confirmation email or from your Amazon account page.

   -- http://s3tools.org/s3cmd

71-ebooks-to-s3.sh
====================

I also do the same with my eBooks collection:

.. code-block:: bash

    # Backup ebooks's to Amazon S3
    s3cmd -vH --progress --guess-mime-type sync /home/duncan/Books/ s3://dflock-backups/dunc-desktop/books/

99-cleanup-afterwards.sh
=========================

This one just does a tiny bit of housekeeping at the end:

.. code-block:: bash

    # Change permissions on backups so that I can use them
    chown -R duncan /home/duncan/backups/
    chown -R duncan /home/duncan/Dropbox/backups/


Testing with ninjahelper
-------------------------

Backupninja comes with a great little tool called ``ninjahelper`` to test your backup configurations:

.. figure:: /static/images/posts/comprehensive-linux-backups-with-etckeeper-backupninja/backupninja-ninjahelper-screenshot.png

    When it starts it gives you a list of each of your jobs. Choose the one you want to test, then you'll see this:

.. figure:: /static/images/posts/comprehensive-linux-backups-with-etckeeper-backupninja/backupninja-ninjahelper-screenshot-job.png

    Do a test run, then a real run of each job. This will also test permissions etc... and tell you if anything needs changing.

Use this to do a test run of each of your jobs in turn until it works, then actually run each one and check the output. Once they all work here, you're good to go.


Physical Offsite Backups
-------------------------

I also want *physical* offsite backups of everything - in case anything happens to my building - like a fire, flood or burglary, for example.

Once you've setup the above, this is simplicity itself - just remove the external USB backup disk, stick a post-it note with the date on it, and take it to work, or give it to a friend who lives separately from you.

Then just get a new blank disk and put it where the old one was, format, label and mount it the same way. Backups will then happen to that disk.

Then, like `jwz <http://www.jwz.org/doc/backups.html>`_ says - every month, bring that other drive back, plug it in an run the backup to it, then take it away again.

Testing
-----------

I'm deliberately not doing anything too fancy here - to compression, no encryption, etc... - just a simple copy of stuff. This means testing is pretty easy. Open some files from the back and check that they're ok.

Copy some file off the backup disk to check that works.

Do this periodically. Backups that don't restore are worse than no backups.

Then... relax
--------------

Once this is all setup, you can take a deep breath and relax - safe in the knowledge that you're covered if anything bad happens to you digital life. This only took me a couple of hours to setup from scratch - but will take you much less because you can copy & paste my hard work. What are you waiting for - give yourself the gift of some peace of mind.
