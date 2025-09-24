.. git-gq documentation master file, created by
   sphinx-quickstart on Fri Jun  6 09:27:37 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to git-gq's documentation!
==================================

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Contents:

   overview
   prerequisites
   implementation
   conflicts
   backups
   examples
   commandline
   install

Patch queues for git
--------------------

This program implements patch queues for 
`git <https://git-scm.com/>`_.

It adds the subcommand 'gq' for git. You can use it like any
other built-in git subcommand like in::

  git gq COMMAND OPTIONS

With it's bash
`command completion <https://en.wikipedia.org/wiki/Command-line_completion>`_ 
support you can always just enter the first letters of your COMMAND and press
<TAB> to show all possible completions.

Patch queues are a very flexible tool for your *local* development, everything
you have not yet published or pushed to another git repository. You can put git
commits on the patch queue with ``git gq pop`` and re-apply them later with
``git gq push``. You can change, reorder or combine patches.

Patch queues can replace the usual 'git pull or git rebase' workflow. Instead
you put your local commits on the queue with ``git gq pop -a``, run ``git
pull`` and re-apply them with ``git gq push -a``.

If there are conflicts with your patches, you do not have resolve them all at
once in one big merge commit, instead you resolve conflicts step by step for
each patch, which is usually much easier.

:Author:
    Goetz Pfeiffer <goetzpf@googlemail.com>

:Version:
    |version|

.. seealso::
   `Goetz Pfeiffer's Project site <https://goetzpf.github.io/>`_
   for other open source projects.

Disclaimer
----------

.. warning::
   I have tested git-gq and use it myself. However, I cannot *guarantee* that
   it will *never* damage your repository. It's high degree of flexibility also
   means that you may use it in a way I didn't intend and didn't test. 

When you are new using this tool for the first time, you should make a backup
of your repository, for example like this::

  cp -a MYREPO MYREPO-BACKUP

A backup of the current state of the patch queue is done with::

  git gq backup

It is recommended that you *always* run this command *before* you reorder or
fold patches and before you run ``git pull`` while some of your patches are
still unapplied.

Documentation
-------------

- :doc:`overview`
- :doc:`prerequisites`
- :doc:`implementation`
- :doc:`conflicts`
- :doc:`backups`
- :doc:`examples`
- :doc:`commandline`
- :doc:`install`

Installation
------------

See :doc:`install`

Repository site
---------------

https://github.com/goetzpf/git-gq

Indices and tables
------------------

* :ref:`genindex`
* :ref:`search`


License and copyright
---------------------

Copyright (c) 2025 by Goetz Pfeiffer <goetzpf@googlemail.com>

This software of this project can be used under GPL v.3, see :doc:`license`.

