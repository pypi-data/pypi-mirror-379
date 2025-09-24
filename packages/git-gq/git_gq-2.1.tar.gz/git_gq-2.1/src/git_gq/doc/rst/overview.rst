Overview
--------

Patches vs. Commits
+++++++++++++++++++

git manages a repository with *commits*. A commit has the following properties:

- A state, this is the directory structure and the files and their contents and
  permissions.
- Metadata: log message, author and date
- A hash key that git uses internally to identify commits. Git hashes are
  calculated based on the contents of the files in the commit, the metadata of
  the commit (like timestamp and author), and the parent commit's hash.
- A predecessor commit unless it is the first commit in the repository
- A successor commit unless it is the head commit of a branch

For simplicity, we only consider a single branch for now. Then each commit has
exactly one or no predecessor and one or no successor.

All commits then form an ordered sequence like here::

  A --> B --> C --> D

A *patch* is the difference between two commits combined with the metadata of
the second patch.

So the commits A, B, C and D as shown above could also be represented as patches::

  (A-0) --> (B-A) --> (C-B) --> (D-C)

Here '(B-A)' means the difference of the files and directories of commits 'B'
and 'A'. '0' is the empty state before the very first commit where no files and
directories exist.

When you apply a patch to a commit you get the next commit::

  A + (B-A) = B

The patch queue
+++++++++++++++

The *patch queue* is a structure that contains patches outside of git. Patches
can be moved between the repository and the patch queue. Patches on the patch
queue are called *unapplied*, patches that are in the repository are called
*applied*.

In the following examples, the top of the repository and the patch queue is
always on the right side::

  Repository:  A --> B --> C --> D      Patch-Queue: <empty>
  applied: (A-0), (B-A), (C-B), (D-C)   unapplied: <none>

Now operation 'pop' moves a patch from the repository to the patch-queue::

  Repository:  A --> B --> C            Patch-Queue: (D-C)
  applied: (A-0), (B-A), (C-B)          unapplied: (D-C)

Another 'pop' moves the next patch from the repository to the patch-queue::

  Repository:  A --> B                  Patch-Queue: (D-C) --> (C-B)
  applied: (A-0), (B-A)                 unapplied: (D-C), (C-B)

Operation 'push' moves the top patch from the patch-queue back to the
repository::

  Repository:  A --> B --> C            Patch-Queue: (D-C)
  applied: (A-0), (B-A), (C-B)          unapplied: (D-C)

Advantages of the patch queue
+++++++++++++++++++++++++++++

The patch-queue is much more flexible than traditional commits:

- Patches can be reordered easily.
- Patches can be combined (``git gq fold``).
- Patches can be updated (``git gq refresh``).
- Patches can replace development branches. You can put your local changes on
  the patch queue, run ``git pull`` and put your patches back on the
  repository.
- Conflicts that may occur with ``git gq push`` are usually easier to resolve
  than git merge conflicts.

Disadvantages of the patch queue
++++++++++++++++++++++++++++++++

- Moving a patch to the patch queue and back changes it's git hash key. This
  means you must not apply this operation on patches that exist in other
  repositories. The definition of the *parent revision* ensures that you cannot
  do this by accident.
- Changing the order of patches may lead to *conflicts*.
- Applying new commits in the repository while some patches are unapplied may
  lead to conflicts when the patches are applied later on.
