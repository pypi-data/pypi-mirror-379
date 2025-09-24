How to install git-gq
=====================

Install from pypi with pip (recommended)
----------------------------------------

In order to install git-gq with `pip <https://en.wikipedia.org/wiki/Pip_(package_manager)>`_,
you use the command [1]_::

  pip install git-gq

.. [1] Your version of pip may have a different name, e.g. "pip-3" or "pip-3.2"

You find documentation for the usage of pip at `Installing Python Modules
<https://docs.python.org/3/installing/index.html#installing-index>`_.

Install from distribution tar file
----------------------------------

This file can be downloaded at 
`github <https://github.com/goetzpf/git-gq/releases>`_.

Unpack the file with::

  tar -xzf git-gq-VERSION.tar.gz

Enter the created directory::

  cd git-gq-VERSION

You can install git-gq system-wide if you have "sudo" rights, or in a local
directory.

In both cases you do this with the script `install.sh`.

System wide installation
++++++++++++++++++++++++

Run::

  sudo ./install.sh

Local installation in DIRECTORY
+++++++++++++++++++++++++++++++

Run::

  ./install.sh DIRECTORY

You should set your PATH variable to the install location. Add this line to
your `$HOME/.bashrc` file (replace 'DIRECTORY' with the actual directory
name)::

  PATH=DIRECTORY/bin:$PATH

To have bash completion, add this line to your `$HOME/.bashrc` file (replace
'DIRECTORY' with the actual directory name)::

  source DIRECTORY/profile.d/git-gq.sh

How to uninstall
++++++++++++++++

In any case, git-gq can be uninstalled with::

  git-gq-uninstall.sh

The script is installed at the same location as the program `git-gq`.

Install from source
-------------------

Check out the repository::

  git clone https://github.com/goetzpf/git-gq.git

Build distribution directory::

  administration_tools/doc-rebuild.sh
  administration_tools/mk-tar-dist.sh --keep

Now go to directory "dist::

  cd dist

go to the distribution directory::

  cd git-gq-*[0-9]

And continue at `Install from distribution tar file`_.

