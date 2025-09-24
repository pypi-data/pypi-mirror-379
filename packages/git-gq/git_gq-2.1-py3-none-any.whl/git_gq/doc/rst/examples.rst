Example Workflows
-----------------

Local development
+++++++++++++++++

Assuming you have cloned another git repository and want to start development
here. With git-gq you don't need to create a local branch. Just run::

  git gq init

This sets up the git-gq directory and marks the current HEAD revision
as parent revision.

You can now begin to make changes. You create preliminary commits with::

  git gq new NAME

where NAME should be a one line string with no spaces in it. This is a
preliminary log message that you can later update and extend. Every time you
make more changes you can either:

- run ``git gq new`` to create a new commit
- run ``git gq refresh`` to update the topmost commit
- run the ``git add..`` and ``git commit`` as usual to create a new commit

You can see what patches are applied with::

  git gq applied

You can see what patches are unapplied with::

  git gq unapplied

When you want to finalize your commits and update commit messages, first move
all of them as patches to the patch queue::

  git gq pop -a

Then for each patch, to provide a proper log message, run::

  git gq push
  git gq refresh -e

You can also combine ('fold') an unapplied patch with::

  git gq fold PATCH

Inspect the applied patches with::

  git gq glog

When you are finished for all patches you can finalize these changes by setting
the parent version to the current HEAD version::

  git gq parent HEAD

You are now ready to publish your patches.

Updates from a remote repository
++++++++++++++++++++++++++++++++

When you have created local patches and want to update your repository with new
patches from a remote repository, the usual way would be to run
``git pull`` and then ``git merge`` or ``git rebase -i``.

With the patch queue, there is now another way to handle this. Before pulling
patches from the public repository, put all your local changes on the patch
queue::

  git gq pop -a

As a safety measure backup your patch queue with::

  git gq backup

Now pull patches from the remote repository::

  git pull

Reset the parent revision to the new repository HEAD::

  git gq parent HEAD

Finally re-apply all your patches::

  git gq push -a

If you get messages about conflicts ("rejects") you have to resolve them. See
further above at "Conflicts and conflict resolution".

This workflow allows to resolve conflicts step by step which is usually easier
than resolving all conflicts that arise from ``git pull`` all at once. Also the
reject files created for each conflict clearly show which change was intended
at the patch which is usually easier than the common 3-way merge.
