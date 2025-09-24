#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
"""git-gq : a patch queue for git

Copyright (C) 2025  Goetz Pfeiffer <goetzpf@googlemail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# pylint: disable= invalid-name
# pylint: disable= too-many-lines

import argparse
#import string
import pathlib
import os.path
import sys
import subprocess
import shutil
import datetime
import pydoc
import re

if sys.version_info < (3, 9):
    import importlib_resources as resources
else:
    from importlib import resources


# pylint: disable=invalid-name

ojoin= os.path.join

MYNAME_GIT= "git gq"

TOPPATCHDIR=".gqpatches"

TEMP_BASEDIR="tmp"
TEMPDIR=os.path.join(TOPPATCHDIR, TEMP_BASEDIR)

FORBIDDED_QUEUENAMES=set((TEMP_BASEDIR, ))

DIFF_FILENAME=ojoin(TEMPDIR, "DIFF.patch")
HDIFF_FILENAME=ojoin(TEMPDIR, "HEAD.patch")
LOG_FILENAME=ojoin(TEMPDIR, "LOG")
DATE_FILENAME=ojoin(TEMPDIR, "DATE")
AUTHOR_FILENAME=ojoin(TEMPDIR, "AUTHOR")
CONFLICT_FILENAME=ojoin(TEMPDIR, "CONFLICT")
UNKNOWN1_FILENAME=ojoin(TEMPDIR, "UNKNOWN.1")
UNKNOWN2_FILENAME=ojoin(TEMPDIR, "UNKNOWN.2")

HOMEPAGE="https://goetzpf.github.io/git-gq"

# name of bash completion function, see also BASHCOMPLETION:
COMPLETION_FUNC="_git_gq"

VERSION= "2.1" #VERSION#

SUMMARY="A program to implement patch queues for git."

BASHCOMPLETION=r'_git_gq() { __gitcomp "$(git-gq commands)" "" "$cur"; }'

USAGE= "%(prog)s [OPTIONS] COMMAND"

DESC= '''
Documentation conventions
+++++++++++++++++++++++++

- Arguments for commands are in capital letters.
- Arguments in square brackets are optional.
- A '|' means that one of the shown arguments must be used.
- 'REGEXP' is a regular expression. For regular expression syntax see:
  https://docs.python.org/3/howto/regex.html#regex-howto

Help and documentation
++++++++++++++++++++++

  help
    Show this help.

  doc
    Show reStructuredText source of man page.

  man
    Show man page.

Bash completion commands
++++++++++++++++++++++++

  commands       
    List all known commands on the console

  bashcompletion

    Prints a text that, if you add it to your bash configuration in
    $HOME/.bashrc, adds bash completion. This means that you get a list of
    possible commands when you type <TAB>, e.g.::

      git gq a<TAB>

    shows the possible completions ``abort`` and ``applied``. If there is only one
    matching command, you command line is completed, e.g::

      git gq ab<TAB>

    becomes::

      git gq abort

    This can save you many keystrokes and makes using this tool easier.

    Example how to install completion::

      git gq bashcompletion >> $HOME/.bashrc

Queue management commands
+++++++++++++++++++++++++

  init [QNAME [REV]]
    Create/select a patch queue with name QNAME. QNAME is optional, the
    default patch queue name is 'default'. If REV is given this is the parent
    revision, if it is not given, 'HEAD' is taken as the parent. You must run
    this command once to initialize the patch queue in your repository.

  qname [QNAME]   
    If QNAME is not given, show current patch queue name. if QNAME is given,
    change to patch queue QNAME. If the patch queue QNAME is created for the
    first time, the parent revision is set to your 'HEAD' revision. If this is
    not intended, you may change this with ``git gq parent REVISION`` to
    another revision.

  backup         
    Backup patch queue directory with a separate git repository. You may
    provide a short log message with option ``-m``.

  restore REVISION   
    Restore patch directory to a REVISION that was created with ``git gq
    backup`` before. This *does not* change your git repository. Enter ``git gq
    revert`` to reset your repository to the last saved state.

  revert
    Revert git repository to the state from the last backup of the patch queue.
    All *applied* patches are restored to the state at the last ``git gq
    backup``. All *unapplied* patches remain in their present state. This will
    create a new branch in the repository at the PARENT revision. The new
    branch name will be the name of your current branch with a number appended
    like in 'master-1'. If you want instead have the new branch given the name
    of the current branch and the old patches given a new branch name, use
    option '--move-branchname'.

  qrepo COMMAND [-- OPTIONS]
    Run git command COMMAND with OPTIONS in patch-queue repository. Note that
    OPTIONS must be preceded by a *double* '-' character.

  change-order   
    Call an editor to edit the file 'series' that contains all currently
    unapplied patches. Note that ``git gq push`` always applies the patch from
    the *first* line in this file, so the top of the queue is the top of the
    file.

  applied    
    Show all applied patches up to parent+1.

  unapplied      
    Show all patches of the patch queue.

  parent [REVISION]   
    Set REVISION as patch queue parent revision. Do never go beyond this
    revision with pop. Use 'HEAD' to set your repository HEAD as parent
    revision. If REVISION is `NULL`, it means that *all* revisions in the
    repository can be managed with ``git gq pop``, you should only use this for
    unpublished repositories. If REVISION is not given, show the current parent
    revision.

  export DIRECTORY
    Create numbered patch files from all currently applied patches in
    DIRECTORY. The numbers are in the order of patches from bottom to top.
    DIRECTORY must exist.

  import PATCHFILE [PATCHFILE...]
    Import a number of patchfiles to the patch queue. The last patchfile in the
    list will be on the top of the queue. Note that the patch files must have
    been generated with ``git format-patch`` or ``git gq pop``. This
    cannot be used for patches generated with the ``patch`` program. These you
    have to apply with ``git apply PATCHFILE``.

Patch management commands
+++++++++++++++++++++++++

  new [NAME]     
    Create new patch (commit) with log-message NAME. NAME is meant as a
    preliminary commit message, it should be a single line without spaces. If
    NAME is omitted, you can enter a complete log message interactively.

  record [NAME]  
    Interactively select changes for a new patch (commit with log-message
    NAME). This command runs ``git add --patch`` to select the changes before
    ``git commit``.

  refresh        
    Update the top patch, all changes in files known to git are added to the
    top patch. If you want to add new files, add them with ``git add`` first.
    If you want complete control over the changes added, run ``git add``
    yourself and then run this command with option ``--no-add``.

  pop            
    Pop the top patch, the HEAD patch of your repository is moved to the patch
    queue.

  push           
    Apply the top patch from the patch queue, the patch is moved to your
    repository as the new HEAD patch.

  goto NAME|REGEXP
    Do push or pop until the patch specified by name or regular expression is
    the latest applied patch.

  fold NAME|REGEXP
    Fold patch 'NAME' to the top patch. Patch 'NAME' must not have been applied
    already. Note that the log message of the fold-patch is appended to the
    existing log message. You can change the log message with
    ``git gq refresh -e``.

  edit NAME|REGEXP
    Call an editor to edit the patch file of an unapplied patch. 

  delete NAME|REGEXP
    Delete unapplied patch with given by name or regular expression.

  show NAME|REGEXP
    Show changes of an applied or unapplied patch on the console.

  continue       
    Continue 'push' after you had a conflict and had it fixed manually. This
    also removes all reject (\\*.rej) files that are not tracked by git.

  abort          
    Abort (undo) 'push' after you had a conflict and could not fix it manually.
    This also removes all reject (\\*.rej) files that are not tracked by git.

Miscellaneous commands
++++++++++++++++++++++

  conflict [CMD]
    Show if the repository is in an unresolved conflict state.
    CMD is a sub-command, ``files`` shows files changed by the patch,
    ``show`` shows the patch.

  glog
    Graphical log, display all commits and branches as a tree on the console.

OPTIONS
+++++++
'''

DOC_HEADING=\
'''======================================================
git gq - patch queues for git
======================================================
'''

DOC_OVERVIEW=\
'''Overview
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
'''

DOC_IMPLEMENTATION=\
'''Implementation
--------------

Directory structure
+++++++++++++++++++

All files git-gq uses are in directory '.gqpatches'. You may want to add this
to your .gitignore file.

'.gqpatches/tmp' is the directory for temporary files git-gq creates.

The program can manage more than one patch queue. Each patch queue has a name
and all files of the queue are in a directory with the same name, e.g.
'.gqpatches/MYQUEUE'. The default name for the first patch queue is 'default'.

The file '.gqpatches/queue' contains the name of the currently selected patch
queue.

Files in the patch queue directory
++++++++++++++++++++++++++++++++++

In the patch queue directory, e.g. '.gqpatches/default', you find the following
files or directories:

series
::::::

The order of patches is kept in a file named 'series' that just contains all
the filenames of all unapplied patches. ``git gq push`` takes and applies the
patch from the first line in this file.

parent
::::::

The parent revision is stored in a file 'parent'. This is the most recent
commit that is not allowed to be modified. This file is created when you start
your work with ``git gq init``. It can be changed with ``git gq parent``.

A special revision is `NULL`. This is the very first revision in the repository
where no files are committed. git doesn't have a concept of a `NULL` revision,
this is emulated by git-gq by creating a revision with no files in it. When the
parent is set to `NULL` this means that you can put the very first revision on
the patch queue and by this have the ability to modify the very first revision.
Of course, you should never do this with a published repository, since ``git gq
pop`` and ``git gq push`` always modify revision hash keys.

patch files '\\*.patch'
::::::::::::::::::::::

A *patch file* is basically a file with recipes for changes in files. Each
recipe is called a *hunk*. A *hunk* contains line numbers, context lines, lines
to remove and lines to add.

git-gq uses standard git commands to move patches between the
repository and the patch queue. In the patch queue, each patch is a file
created from the difference of a commit and it's predecessor in the repository
with ``git format-patch``. Among the changes between two commits this file also
contains all the metadata of the second commit. The name of the patch file is
computed from the first line of the log message where spaces are replaced with
dashes and end with the extension '.patch'.

A patch file is re-applied to the repository with ``git am``. 

Here is an example of a patch file::

  From 273c3709f7da0fe0e11369ea0d9a26053f78e3ee Mon Sep 17 00:00:00 2001
  From: Goetz Pfeiffer <goetzpf@googlemail.com>
  Date: Tue, 3 Jun 2025 18:45:57 +0200
  Subject: [PATCH] sample-comment
  
  ---
   sample.c | 2 +-
   1 file changed, 1 insertion(+), 1 deletion(-)
  
  diff --git a/sample.c b/sample.c
  index e5cf2b0..350c29b 100644
  --- a/sample.c
  +++ b/sample.c
  @@ -4,8 +4,8 @@ int main(int argc, char *argv[])
     {
       int i;
   
  -    printf("number of arguments: %d\\n", argc);
       printf("program name: %s\\n", argv[0]);
  +    /* iterate over all command line arguments: */
       for(i=1; i<argc; i++)
         printf("arg no %2d: %s\\n", i, argv[i]);
       return 0;
  -- 
  2.49.0

applied
:::::::

Directory 'applied' is created by ``git gq backup``. It contains the *applied*
patches from the time this command is issued. Note that files in this directory
are not changed by ``git gq push`` or ``git gq pop``, only by ``git gq backup``.
'''

# Note how this example was created:
# mkdir sample && cd sample
# cp -a $HOME/devel/c/template.c sample.c
# git init
# git add sample.c
# git commit -m Initial
# git gq init
# sed -i -e '/number of arg/d' sample.c
# sed -i -e '/program name:/a\    \/* iterate over all command line arguments: *\/' sample.c
# git gq new sample-comment
# git gq pop
# sed -i -e 's/number of/My number of/' sample.c
# git gq new extra-change
# git gq push

DOC_CONFLICTS=\
'''Conflicts and conflict resolution
---------------------------------

Conflicts may happen when:

- you change the order of unapplied patches with ``git gq change-order``
  and then run ``git gq push``
- you unapply patches, make changes in the repository, e.g. ``git pull`` and
  then apply the patches again
- you combine unapplied patches with ``git gq fold`` that are not in
  consecutive order

In the patch file example above, you see after ``@@ -4,8 +4,8 @@`` a single
*hunk*. The numbers are line numbers in the source file, here 'sample.c'.

All following lines that are indented with a single space are *context* lines.
Lines that start with a '-' character are to be removed, lines that start with
a '+' character are to be added.

A conflict occurs when the context lines or the lines to be removed couldn't be
found. In this case, a reject file is created.

Here are the messages you see in case of a conflict after you ran
``git gq push``::

  Applying: sample-comment
  Checking patch sample.c...
  error: while searching for:
    {
      int i;
  
      printf("number of arguments: %d\\n", argc);
      printf("program name: %s\\n", argv[0]);
      for(i=1; i<argc; i++)
        printf("arg no %2d: %s\\n", i, argv[i]);
      return 0;
  
  error: patch failed: sample.c:4
  Applying patch sample.c with 1 reject...
  Rejected hunk #1.
  Patch failed at 0001 sample-comment
  hint: Use 'git am --show-current-patch=diff' to see the failed patch
  hint: When you have resolved this problem, run "git am --continue".
  hint: If you prefer to skip this patch, run "git am --skip" instead.
  hint: To restore the original branch and stop patching, run "git am --abort".
  hint: Disable this message with "git config set advice.mergeConflict false"
  
  git gq help on conflicts
  ------------------------
  
  Resolve this conflict by looking at the *.rej files.
  For files that were not found there is no reject file, look at the original
  patch with:
    less .gqpatches/tmp/DIFF.patch
  
  To see the state of your repository enter:
    git status
  
  Unknown files for git that should be part of the patch must be added with:
    git add FILE
  
  If you managed to resolve all the conflicts run:
    git gq continue
  
  To abort the whole operation without resolving conflicts run:
    git gq abort

And here is the content of the reject file, 'sample.c.rej' in this case::

  diff a/sample.c b/sample.c	(rejected hunks)
  @@ -4,8 +4,8 @@ int main(int argc, char *argv[])
     {
       int i;
   
  -    printf("number of arguments: %d\\n", argc);
       printf("program name: %s\\n", argv[0]);
  +    /* iterate over all command line arguments: */
       for(i=1; i<argc; i++)
         printf("arg no %2d: %s\\n", i, argv[i]);
       return 0;

In our example here, while the patch was moved to the patch queue, this line::

  printf("number of arguments: %d\\n", argc);

had been changed to::

  printf("My number of arguments: %d\\n", argc);

So the line to remove by the patch wasn't found and we had a conflict. If we
open both, the original file 'sample.c' and the reject file 'sample.c.rej' in
any text editor, we can easily see what the patch intended to do and apply the
changes manually.

This is called *resolving a conflict*. You have to go through all reject files,
there may be more than one, and resolve all conflicts.

 .. important::
    If a file that the patch modifies couldn't be found, **there is no reject
    file**. Look carefully at the git message and look at the original patch as
    described in the git-gq help message that is printed when the conflict is
    detected.

After you are finished, run::

  git gq continue

This finishes the operation and tells git that the conflict was resolved. You
*must not* run ``git am continue`` yourself, ``git gq continue`` already
does this for you.

If you cannot resolve conflicts because the reject files are too long or
complicated, you can abort the last command with::

  git gq abort

In this case you may have to compare two versions of files and apply changes
directly.
'''

DOC_EXAMPLES=\
'''Example Workflows
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
'''

DOC_REJECT_MESSAGE=\
f'''git gq help on conflicts
------------------------

Resolve this conflict by looking at the *.rej files.
For files that were not found there is no reject file, look at the original
patch with:
  less {DIFF_FILENAME}

To see the state of your repository enter:
  git status

Unknown files for git that should be part of the patch must be added with:
  git add FILE

If you managed to resolve all the conflicts run:
  git gq continue

To abort the whole operation without resolving conflicts run:
  git gq abort'''

DOC_SEE_ALSO=\
f'''See also
--------

git-gq online documentation at

{HOMEPAGE}
'''

# ---------------------------------------------------------
# globals
# ---------------------------------------------------------

gbl_verbose= None
gbl_dry_run= None
gbl_parser= None

gbl_tag_warning= True

# ---------------------------------------------------------
# exceptions
# ---------------------------------------------------------

class GitGqException(Exception):
    """Exception raised for errors in git-gq.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# ---------------------------------------------------------
# date utilities
# ---------------------------------------------------------

def portable_isodate():
    """an ISO date without colons."""
    return \
        datetime.datetime.now().isoformat(timespec="seconds").replace(":","")

# ---------------------------------------------------------
# porttability
# ---------------------------------------------------------

def is_wsl():
    """find out if we run in WSL under windows."""
    try:
        with open("/proc/version", "r", encoding="utf-8") as f:
            return "microsoft" in f.read().lower()
    except FileNotFoundError:
        return False

def parent_shell():
    """return parent shell, needed for WSL in windows."""
    # pylint: disable=broad-except
    try:
        ppid = os.getppid()
        out = subprocess.check_output(
            ["ps", "-p", str(ppid), "-o", "comm="], text=True
        )
        return out.strip()
    except Exception:
        return None

def is_bash_shell():
    """return if bash shell is used."""
    shell = os.environ.get("SHELL")
    if shell is not None:
        return shell.endswith("bash")
    if is_wsl():
        return parent_shell() == "bash"
    return False

def check_bashcompletion():
    """Print a message when bash is used and bash completion is not installed.
    """
    if not is_bash_shell():
        return
    try:
        subprocess.check_output(
            ["bash", "-i", "-c", f"declare -F {COMPLETION_FUNC}"],
            stderr=subprocess.DEVNULL,
            text=True
        )
        return # _git_gq function was found
    except subprocess.CalledProcessError:
        pass   # _git_gq function was not found
    errprint("Note: You can install bash completion on your system with:\n"
             "  git gq bashcompletion >> $HOME/.bashrc\n"
             "See also:\n"
             f"  {HOMEPAGE}\n"
             "or enter:\n"
             "  'git gq man' and look for 'bashcompletion'.")

# ---------------------------------------------------------
# console input
# ---------------------------------------------------------

def ask_continue():
    """ask the user to enter 'y' to continue,"""
    reply= input("Enter 'y' or 'Y' to continue, everything else aborts.")
    print()
    sys.stdout.flush()
    return reply in ("y", "Y")

# ---------------------------------------------------------
# shell utilities
# ---------------------------------------------------------

def errprint(*args, **kwargs):
    """print to stderr."""
    kwargs["file"]= sys.stderr
    print(*args, **kwargs)

def sh_prg_exists(program):
    """test if a program exists."""
    return shutil.which(program) is not None

def sh_set_from_file(filename):
    """create a set from a file."""
    with open(filename, "r", encoding="utf-8") as f:
        line_set = {line.rstrip("\n") for line in f}
    return line_set

def sh_cat_file(filename):
    """prints a text file to the console."""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")

def sh_file_pager(filename):
    """show a file with a pager, much like 'less'.

    Note that will read the complete file first.
    """
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    # Display with pager (uses less/more if available)
    pydoc.pager(text)

def sh_file_add_extension(file, ext):
    """add an extension to a filename."""
    return f"{file}.{ext}"

def sh_file_bak(file):
    """add .bak to filename."""
    return sh_file_add_extension(file, "bak")

def sh_file_new(file):
    """add .new to filename."""
    return sh_file_add_extension(file, "new")

def sh_file_rename(old, new):
    """rename, remove new if it already exists."""
    if os.path.isfile(new):
        os.remove(new)
    os.rename(old, new)

def sh_chdir(dir_):
    """returns the old CWD."""
    this_dir= os.getcwd()
    os.chdir(dir_)
    return this_dir

def sh_mkdir_p(dir_):
    """mkdir -p"""
    pathlib.Path(dir_).mkdir(parents= True, exist_ok= True)

def sh_file_exists(file):
    """check if a file exists.

    May raise GitGqException
    """
    if not os.path.isfile(file):
        raise GitGqException(f"Error, file '{file}' doesn't exist")

def sh_dir_exists(dir_):
    """check if a directory exists.

    May raise GitGqException
    """
    if not os.path.isdir(dir_):
        raise GitGqException(f"Error, directory '{dir_}' doesn't exist")

def sh_directories(dir_):
    """return all directories in dir_."""
    return [d for d in os.listdir(dir_) if os.path.isdir(ojoin(dir_,d))]

def sh_rm_f(*arg):
    """force-remove a file."""
    for file in arg:
        if not os.path.exists(file):
            continue
        os.remove(file)

def sh_rm_rf(*arg):
    """force-remove directories, dangerous !!!"""
    for dir_ in arg:
        if not os.path.isdir(dir_):
            continue
        shutil.rmtree(dir_)

def sh_file_to_file(in_file, out_file, do_append):
    """append one file to another.

    do_append: True or False
    """
    if do_append:
        mode= "at"
    else:
        mode= "wt"
    with open(out_file, mode, encoding= "utf-8") as fh_w:
        with open(in_file, "rt", encoding= "utf-8") as fh_r:
            shutil.copyfileobj(fh_r, fh_w)

def sh_text_to_file(lines, out_file, do_append, add_final_newline= False):
    """create a text file."""
    if do_append:
        mode= "at"
    else:
        mode= "wt"
    if isinstance(lines, str):
        text= lines
    else:
        text="\n".join(lines)
    with open(out_file, mode, encoding="utf-8") as fh_w:
        fh_w.write(text)
        if add_final_newline:
            fh_w.write("\n")

def sh_file_to_list(file):
    """read a file, return a list of lines."""
    with open(file, "rt", encoding="utf-8") as fh:
        return [l.rstrip() for l in fh.readlines()]

def sh_file_to_list_filter(file, func):
    """read a file, return a list of lines."""
    out= []
    with open(file, "rt", encoding="utf-8") as fh:
        # note: each read line has an '\n' at the end:
        for line in fh:
            line= line.rstrip()
            if func(line):
                out.append(line)
    return out

def sh_file_grep(regexp, file):
    """return matching lines as a list."""
    rx= re.compile(regexp)
    lines=[]
    with open(file, "rt", encoding="utf-8") as fh:
        # note: each read line has an '\n' at the end:
        for line in fh:
            line= line.rstrip()
            if rx.search(line):
                lines.append(line)
    return lines

def sh_prepend_line(str_, file):
    """prepend a line to a file.

    Note: str_ must end with '\n'.
    """
    if not os.path.exists(file):
        with open(file, "wt", encoding="utf-8") as fh:
            fh.write(str_)
    else:
        tempfile= sh_file_bak(file)
        sh_file_rename(file, tempfile)
        sh_text_to_file(str_, file, do_append= False)
        sh_file_to_file(tempfile, file, do_append= True)
        os.remove(tempfile)

def sh_file_filter(str_, file, file_out, cleanup= True):
    """remove all lines that are equal to str_.

    file_out==file is allowed !

    Note: str_ must end with '\n'.
    """
    if not os.path.exists(file):
        raise AssertionError(f"Error, file {file} doesn't exist.")
    if file_out==file:
        file_in= sh_file_bak(file)
        sh_file_rename(file, file_in)
    else:
        file_in= file
    with open(file_in, "rt", encoding="utf-8") as fh_r:
        with open(file_out, "wt", encoding="utf-8") as fh_w:
            # note: each read line has an '\n' at the end:
            for line in fh_r:
                if line==str_:
                    continue
                fh_w.write(line)
    if cleanup:
        # remove *.bak file:
        if file_out==file:
            os.remove(file_in)

def sh_file_linenumbers(file):
    """count line numbers in a file."""
    cnt=0
    with open(file, "rt", encoding="utf-8") as fh:
        for _ in fh:
            cnt+=1
    return cnt

def sh_file_head(head_no, invert, file, file_out):
    """works like 'head -n head_no'.

    With invert, select all lines 'head -n head_no' would no select.

    If file_out is not None, put results in file_out.
    """
    # pylint: disable=too-many-branches
    if not os.path.exists(file):
        raise AssertionError(f"Error, file {file} doesn't exist.")
    if file_out==file:
        file_in= sh_file_bak(file)
        sh_file_rename(file, file_in)
    else:
        file_in= file
    # first line is line 1 per definition
    line_no=0
    lines=[]
    fh_w= None
    # pylint: disable=consider-using-with
    if file_out:
        fh_w= open(file_out, "wt", encoding="utf-8")
    with open(file_in, "rt", encoding="utf-8") as fh:
        if not file_out:
            # note: each read line has an '\n' at the end:
            for line in fh:
                line= line.rstrip()
                line_no+= 1
                if not invert:
                    if line_no > head_no:
                        break
                else:
                    if line_no <= head_no:
                        continue
                lines.append(line)
        else:
            # note: each read line has an '\n' at the end:
            for line in fh:
                line_no+= 1
                if not invert:
                    if line_no > head_no:
                        break
                else:
                    if line_no <= head_no:
                        continue
                fh_w.write(line)
    if file_out:
        fh_w.close()
        if file_out==file:
            os.remove(file_in)
        return None
    return lines

# ---------------------------------------------------------
# constants
# ---------------------------------------------------------

RX_TOPPPATCHDIR_FILES=re.compile(f'^ {TOPPATCHDIR}[{os.sep}-]')
RX_TOPPPATCHDIR=re.compile(f'^{TOPPATCHDIR}[{os.sep}-]')

RX_STAT= re.compile(r'^(..) (.*)')
RX_REJ= re.compile(r'\.rej$')

RX_TOPPPATCHDIR=re.compile(f'^{TOPPATCHDIR}{os.sep}')

RX_NUMBER=re.compile(r'^[0-9]+-')

RX_HASH=re.compile(r'^[A-Fa-f0-9]{6,}$')
RX_GITSTAT_MV=re.compile(r'^R[M ] .*-> (.*)')

RX_RST_PLUS=re.compile(r'\++$')

QUEUENAME="default"
PATCHDIR=ojoin(TOPPATCHDIR, QUEUENAME)
APPLIEDDIR=ojoin(PATCHDIR, "applied")
SERIESFILE=ojoin(PATCHDIR, "series")
PARENTFILE=ojoin(PATCHDIR, "parent")
QUEUEFILE=ojoin(TOPPATCHDIR, "queue")


ALL_COMMANDS={\
    "abort", "applied", "backup", "bashcompletion", "change-order", "commands",
    "conflict", "continue", "delete", "doc", "edit", "export", "fold", "glog",
    "goto", "help", "import", "init", "man", "new", "parent", "pop", "push",
    "qname", "qrepo", "record", "refresh", "restore", "revert",
    "show", "unapplied"} # type: ignore

# ---------------------------------------------------------
# documentation functions
# ---------------------------------------------------------

def short_help_text(style):
    """short help text generated by argparse."""
    if gbl_parser is None:
        raise AssertionError("gbl_parser not initialized")
    if style not in ("rst", "txt"):
        raise AssertionError(f"unknown style: {style}")
    lines= gbl_parser.format_help().splitlines()
    new= []
    for line in lines:
        if line=="options:":
            # filter 'options:' always
            continue
        if style=="txt":
            if RX_RST_PLUS.search(line):
                continue
        new.append(line)
    return "\n".join(new)


def print_doc(part, lst):
    """Print documentation.

    If lst is a list, append text parts to that list.
    """
    def lprint(txt, lst):
        """internal print."""
        if lst is not None:
            lst.append(txt)
        else:
            print(txt)
    if part is not None:
        if part not in ("overview", "implementation", "conflicts",
                        "examples", "commandline"):
            raise ValueError(f"unknown documentation part for 'doc' "
                             f"command: {part}")
    if not part:
        lprint(DOC_HEADING, lst)
    if (not part) or (part=="overview"):
        lprint(DOC_OVERVIEW, lst)
    if (not part) or (part=="implementation"):
        lprint(DOC_IMPLEMENTATION, lst)
    if (not part) or (part=="conflicts"):
        lprint(DOC_CONFLICTS, lst)
    if (not part) or (part=="examples"):
        lprint(DOC_EXAMPLES, lst)
    if (not part) or (part=="commandline"):
        lprint("Command line interface\n----------------------", lst)
        lprint(short_help_text(style="rst"), lst)
        lprint("", lst)
    if (not part) or (part=="see also"):
        lprint(DOC_SEE_ALSO, lst)

def print_short_help():
    """print short help."""
    print(short_help_text(style="txt"))

def print_reject_message():
    """print reject message."""
    print(DOC_REJECT_MESSAGE, file=sys.stderr)

# ---------------------------------------------------------
# system calls
# ---------------------------------------------------------

# standard set of environment variables here:
_new_env = dict(os.environ)

# Only on Unix-Like systems:
# Ensure that language settings for called commands are english, keep current
# character encoding:
if os.name=="posix" and "LANG" in _new_env:
    _l= _new_env["LANG"].split(".")
    if len(_l)==2:
        _l[0]= "en_US"
        _new_env["LANG"]= ".".join(_l)

def copy_env():
    """create a new environment that the user may change."""
    return dict(_new_env)

# None
# PIPE
# filehandle

def system_rc_io(cmd,
                 stdin_par,
                 stdout_par, stderr_par,
                 env, verbose, dry_run):
    """execute a command.

    cmd: either a string or a list of strings

    stdin_par:
      - None         : no standard input
      - <str>        : take input from string
    stdout_par:
      - None         : do not capture 
      - "PIPE"       : capture
      - <filehandle> : write to file

    sterr_par:
      - None         : do not capture 
      - "PIPE"       : capture
      - <filehandle> : write to file

    execute a command and return the programs output
    may raise:
    IOError(errcode,stderr)
    OSError(errno,strerr)
    ValueError

    returns:
      (stdout-output, stderr-output, returncode)
    """
    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-positional-arguments
    def to_str(data):
        """decode byte stream to unicode string."""
        if data is None:
            return None
        return data.decode()
    if dry_run or verbose:
        print(">", cmd)
        if dry_run:
            return (None, None, 0)
    if stdout_par is not None:
        if isinstance(stdout_par, str):
            if stdout_par=="PIPE":
                stdout_par=subprocess.PIPE
            else:
                raise ValueError(f"stdout_par has wrong value: {stdout_par!r}")
        # otherwise assume file-like object
    if stderr_par is not None:
        if isinstance(stderr_par, str):
            if stderr_par=="PIPE":
                stderr_par=subprocess.PIPE
            else:
                raise ValueError(f"stderr_par has wrong value: {stderr_par!r}")
        # otherwise assume file-like object
    if env is None:
        env= _new_env

    stdin_p_par= None
    stdin_bytes= None
    if stdin_par is not None:
        stdin_p_par= subprocess.PIPE
        stdin_bytes= stdin_par.encode("utf-8")
    # pylint: disable=consider-using-with
    p= subprocess.Popen(cmd, shell= isinstance(cmd, str),
                        stdin=stdin_p_par,
                        stdout=stdout_par, stderr=stderr_par,
                        close_fds=True,
                        env= env
                       )
    (child_stdout, child_stderr) = p.communicate(input= stdin_bytes)
    # pylint: disable=E1101
    #         "Instance 'Popen'has no 'returncode' member
    return (to_str(child_stdout), to_str(child_stderr), p.returncode)

def system_rc(cmd, catch_stdout, catch_stderr, env, verbose, dry_run):
    """execute a command.

    execute a command and return the programs output
    may raise:
    IOError(errcode,stderr)
    OSError(errno,strerr)
    ValueError

    returns:
      (stdout-output, stderr-output, returncode)
    """
    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-positional-arguments
    stdout_par= None
    if catch_stdout:
        stdout_par= "PIPE"
    stderr_par= None
    if catch_stderr:
        stderr_par= "PIPE"
    return system_rc_io(cmd, None, stdout_par, stderr_par, env,
                        verbose, dry_run)

def system_io(cmd,
              stdin_par,
              stdout_par, stderr_par,
              env, verbose, dry_run):
    """execute a command.

    cmd: either a string or a list of strings

    stdin_par:
      - None         : no standard input
      - <str>        : take input from string
    stdout_par:
      - None         : do not capture 
      - "PIPE"       : capture
      - <filehandle> : write to file

    sterr_par:
      - None         : do not capture 
      - "PIPE"       : capture
      - <filehandle> : write to file

    execute a command and return the programs output
    may raise:
    IOError(errcode,stderr)
    OSError(errno,strerr)
    ValueError

    returns:
      (stdout-output, stderr-output)
    """
    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-positional-arguments
    (child_stdout, child_stderr, rc)= system_rc_io(cmd,
                                                   stdin_par,
                                                   stdout_par, stderr_par,
                                                   env,
                                                   verbose, dry_run)
    if rc!=0:
        # pylint: disable=no-else-raise
        if stderr_par=="PIPE":
            raise IOError(rc,
                          f"cmd '{cmd}', errmsg '{child_stderr}'")
        else:
            raise IOError(rc,
                          f"cmd '{cmd}', rc '{rc}'")
    return (child_stdout, child_stderr)

def system(cmd, catch_stdout, catch_stderr, env, verbose, dry_run):
    """execute a command.

    execute a command and return the programs output
    may raise:
    IOError(errcode,stderr) when the command failed
    OSError(errno,strerr)
    ValueError

    returns:
      (stdout-output, stderr-ouzput)
    """
    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-positional-arguments
    (child_stdout, child_stderr, rc)= system_rc(cmd,
                                                catch_stdout, catch_stderr,
                                                env,
                                                verbose, dry_run)
    if rc!=0:
        # pylint: disable=no-else-raise
        if catch_stderr:
            raise IOError(rc,
                          f"cmd '{cmd}', errmsg '{child_stderr}'")
        else:
            raise IOError(rc,
                          f"cmd '{cmd}', rc '{rc}'")
    return (child_stdout, child_stderr)

def system_simple(cmd):
    """very simple system call."""
    (_, _)= system(cmd,
                   catch_stdout= False, catch_stderr= False,
                   env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)

# ---------------------------------------------------------
# utilities
# ---------------------------------------------------------

def unique_patch_name(patchname):
    """generate unique filename for a patch.

    May raise:
    AssertionError
    """
    if not os.path.exists(ojoin(PATCHDIR, patchname)):
        return patchname
    cnt=0
    while True:
        cnt+= 1
        if cnt > 1000:
            raise AssertionError("unique_patch_name: loop limit")
        temp_patchname= f"{cnt : 04d}-{patchname}"
        if not os.path.exists(ojoin(PATCHDIR, temp_patchname)):
            return temp_patchname

def editor_dialog():
    """return the name of the editor to use.

    May raise GitGqException
    """
    editor= os.environ.get("EDITOR")
    if not editor:
        editor= os.environ.get("VISUAL")
    if not editor:
        print("Caution: No default editor is specified in environment ")
        print("variables 'EDITOR' and 'VISUAL'.")
        print("Use 'vi' instead ?")
        print("Note that you can always abort editing in 'vi' with")
        print("  <ESC> :qa!")
        if ask_continue():
            editor= "vi"
        else:
            raise GitGqException("no editor selected")
    return editor

def prepend_seriesfile(patchfile):
    """prepend a filename to the series file."""
    sh_prepend_line(f"{patchfile}\n", SERIESFILE)

def git_goto_repo_dir():
    """change to top of git working copy.

    May raise GitGqException
    """
    prev_dir=None
    this_dir= os.getcwd()
    while prev_dir != this_dir:
        if os.path.isdir(".git"):
            return this_dir
        prev_dir= this_dir
        os.chdir("..")
        this_dir= os.getcwd()
    raise GitGqException("Error, '.git' not found")

# ---------------------------------------------------------
# functions that call git
# ---------------------------------------------------------

def git_init(dir_, initial_branch="master"):
    """git init and git add."""

    cmd_list= ["git", "init", "-b", initial_branch]
    if dir_:
        cmd_list.append(dir_)
    system_simple(cmd_list)

def git_checkout(revision_spec, dir_= None,
                 detached_head_warn= True):
    """run git checkout

    dir_: change to this directory first
    detached_head_warn: If True, suppress warning about detached head.
    """
    old_dir= None
    if dir_ is not None:
        old_dir= sh_chdir(dir_)
    try:
        cmd= ["git"]
        if not detached_head_warn:
            cmd.extend(["-c", "advice.detachedHead=false"])
        cmd.extend(["checkout", revision_spec])
        system_simple(cmd)
    finally:
        if old_dir is not None:
            sh_chdir(old_dir)

def git_clean(dir_= None):
    """run git clean -d -f

    CAUTION: removes all files/directories unoknown to git.

    dir_: change to this directory first
    """
    old_dir= None
    if dir_ is not None:
        old_dir= sh_chdir(dir_)
    try:
        system_simple(("git", "clean", "-d", "-f"))
    finally:
        if old_dir is not None:
            sh_chdir(old_dir)

def git_rev_parse(revision_spec, catch_stderr, dir_= None):
    """runs git rev-parse on revision_spec.

    catch_err: If true, catch stderr output.
    dir_: change to this directory first

    returns:
    revision 

    May raise IOError
    """
    old_dir= None
    if dir_ is not None:
        old_dir= sh_chdir(dir_)
    try:
        (out, _)= system(("git", "rev-parse", "--short", revision_spec),
                         catch_stdout= True, catch_stderr= catch_stderr,
                         env= None,
                         verbose= gbl_verbose, dry_run= gbl_dry_run)
        # Note: if an error occurs and catch_stderr==True, the output on stderr
        # is part of the IOError exception text.
    finally:
        if old_dir is not None:
            sh_chdir(old_dir)
    return out.strip()

def git_current_branch():
    """return name of current branch"""
    (out,_)=system(["git","rev-parse","--abbrev-ref","HEAD"],
                    catch_stdout= True, catch_stderr= False,
                    env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    return out.strip()

def git_local_branches():
    """return a set of all local branches."""
    (out,_)=system(["git","branch",'--format="%(refname:short)'],
                   catch_stdout= True, catch_stderr= False,
                   env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    return set(out.splitlines())

def git_create_branchname(oldname):
    """create a name for a new branch by appending '-number'.

    This command ensures that the new branch name doesn't already exist.
    """
    local_branches= git_local_branches()
    num=1
    while True:
        newname= f"{oldname}-{num}"
        if newname not in local_branches:
            break
        num+=1
    return newname

def git_switch_branch(branchname):
    """create a new branch.
    """
    system_simple(("git", "checkout", "-b", branchname))

def git_move_branch(branchname, revision):
    """move bramch to revision
    """
    system_simple(("git", "checkout", "-B", branchname, revision))

def git_show(revspec):
    """git show."""
    system_simple(("git", "show", revspec))

def git_head_tags():
    """return tags of the HEAD revision."""
    (out, _)= system(("git", "tag", "--contains", "HEAD"),
                     catch_stdout= True, catch_stderr= False,
                     env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    return out.splitlines()

def git_glog():
    """git graphlog."""
    system_simple(("git", "log", "--graph", "--all", "--decorate"))

def git_add(filelist, dir_=None):
    """add a list of files to git.+

    If dir_ is not None, do chdir to that directory first
    """
    if not filelist:
        return
    old_dir= None
    if dir_ is not None:
        old_dir= sh_chdir(dir_)
    cmd_lst= ["git", "add"]
    cmd_lst.extend(filelist)
    try:
        system_simple(cmd_lst)
    finally:
        if old_dir is not None:
            sh_chdir(old_dir)

def git_commit(message, dir_=None):
    """simple git commit.

    If dir_ is not None, do chdir to that directory first
    """
    old_dir= None
    if dir_ is not None:
        old_dir= sh_chdir(dir_)
    cmd_lst= ["git", "commit", "-m", message]
    try:
        system_simple(cmd_lst)
    finally:
        if old_dir is not None:
            sh_chdir(old_dir)

def git_rm_all():
    """remove all tracked files."""

    cmd_lst= ["git", "rm", "-r", "*"]
    system_simple(cmd_lst)

def git_select_changes():
    """Interactively select files to add to stash."""
    system_simple(("git", "add", "--patch"))

def git_check_exists(revision):
    """checks if a revision exists.

    returns:
    - True: revision exists
    - False: revision doesn't exist
    """
    (_, _, rc)= system_rc(("git", "cat-file", "-e", revision),
                          catch_stdout= True, catch_stderr= True,
                          env= None,
                          verbose= gbl_verbose, dry_run= gbl_dry_run)
    return rc==0

def git_unknown_files(file):
    """finds files unknown to git, creates <file>."""

    (out, _)= system(("git", "status", "--porcelain"),
                     catch_stdout= True, catch_stderr= False,
                     env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    with open(file, "wt", encoding="utf-8") as fh_w:
        for line in out.splitlines():
            m= RX_STAT.search(line)
            if m is None:
                errprint(f"WARNING: Cannot parse {line!r}")
                continue
            (stat, file)= (m.group(1), m.group(2))
            if stat != "??":
                continue
            if RX_TOPPPATCHDIR.search(file):
                continue
            fh_w.write(f"{file}\n")

def git_untracked(dir_= None):
    """returns list untracked files.

    dir_: change to this directory first
    """
    old_dir= None
    if dir_ is not None:
        old_dir= sh_chdir(dir_)
    try:
        (out, _)= system(("git", "ls-files", "--others", "--exclude-standard"),
                         catch_stdout= True, catch_stderr= False,
                         env= None,
                         verbose= gbl_verbose, dry_run= gbl_dry_run)
    finally:
        if old_dir is not None:
            sh_chdir(old_dir)
    return out.splitlines()

def git_uncommitted(dir_= None):
    """returns list uncommited changes.

    dir_: change to this directory first
    """
    old_dir= None
    if dir_ is not None:
        old_dir= sh_chdir(dir_)
    try:
        (out, _)= system(("git", "status", "--porcelain=v1"),
                         catch_stdout= True, catch_stderr= False,
                         env= None,
                         verbose= gbl_verbose, dry_run= gbl_dry_run)
    finally:
        if old_dir is not None:
            sh_chdir(old_dir)
    filelist=[]
    for l in out.splitlines():
        if l.startswith("??"):
            # unknown file
            continue
        file= l[2:]
        filelist.append(file)
    return sorted(filelist)

def git_head_track_error():
    """check if git is tracking .gqpatches."""

    (out, _)= system(("git", "show", "HEAD", "--stat"),
                     catch_stdout= True, catch_stderr= False,
                     env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    for line in out.splitlines():
        if RX_TOPPPATCHDIR_FILES.search(line):
            errtext=[f"FATAL Error, somehow git is tracking {TOPPATCHDIR}.",
                     f"'git gq pop' would remove {TOPPATCHDIR}.",
                      "Do the following to fix this:",
                     f"  git reset HEAD~1 {TOPPATCHDIR}*",
                      "  git commit -C HEAD --amend"]
            raise GitGqException("\n".join(errtext))


def git_head_revision():
    """returns hash of head revision."""
    (out, _)= system(("git", "rev-parse", "--short", "HEAD"),
                     catch_stdout= True, catch_stderr= False,
                     env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    return out.strip()

def git_revision_1():
    """returns hash of first revision."""
    (out, _)= system(("git", "rev-list", "--max-parents=0",
                     "--format=%h", "HEAD"),
                     catch_stdout= True, catch_stderr= False,
                     env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    return out.splitlines()[-1]

def git_head_log():
    """Get the pure full log message of the HEAD patch."""

    (out, _)= system(("git", "log", "-1", "--pretty=%B"),
                     catch_stdout= True, catch_stderr= False,
                     env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    return out.strip()

def git_head_subject():
    """Get the subject of the HEAD patch."""

    (out, _)= system(("git", "log", "-1", "--pretty=%s"),
                    catch_stdout= True, catch_stderr= False,
                    env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    return out.strip()

def git_head_date():
    """Get the date of the HEAD patch."""

    (out, _)= system(("git", "log", "-1", "--pretty=%aI"),
                     catch_stdout= True, catch_stderr= False,
                     env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    return out.strip()

def git_head_author():
    """Get the author of the HEAD patch."""

    (out, _)= system(("git", "log", "-1", "--pretty='%aN <%aE>'"),
                     catch_stdout= True, catch_stderr= False,
                     env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    return out.strip()

def _git_oneline_log(revision_spec, lines,
                     print_to_console,
                     use_long_hash):
    """prints one-line log, possible with color, to the console."""

    cmd_lst=["git", "log"]
    if print_to_console:
        cmd_lst.append("--color=auto")
    if not use_long_hash:
        cmd_lst.append("--oneline")
    else:
        cmd_lst.append("--pretty=oneline")
    if lines:
        cmd_lst.append(f"-{lines}")
    if (revision_spec != "NULL") and revision_spec:
        cmd_lst.append(revision_spec)
    if not print_to_console:
        (out, _)= system(cmd_lst,
                         catch_stdout= True, catch_stderr= False,
                         env= None,
                         verbose= gbl_verbose, dry_run= gbl_dry_run)
        return out.splitlines()
    my_env= copy_env()
    if sh_prg_exists("cat"):
        my_env["GIT_PAGER"]="cat"
    (_, _)= system(cmd_lst,
                   catch_stdout= False, catch_stderr= False,
                   env= my_env,
                   verbose= gbl_verbose, dry_run= gbl_dry_run)
    return None

def applied_log(parent, lines, print_to_console, use_long_hash):
    """show all logs for revisions *after* parent."""
    if parent!="NULL":
        revspec= f"{parent}.."
    else:
        revspec= parent
    return _git_oneline_log(revspec, lines, print_to_console, use_long_hash)

def repo_log(revspec, lines, print_to_console, use_long_hash):
    """show all logs for revisions from (including) revspec."""
    return _git_oneline_log(revspec, lines, print_to_console, use_long_hash)

def _git_format_patch(revision_spec, lines, output_dir):
    """run git format-patch"""
    cmd_lst=["git", "format-patch", "-o", output_dir]

    if lines:
        cmd_lst.append(f"-{lines}")
    if revision_spec=="NULL":
        cmd_lst.append("--root")
    else:
        cmd_lst.append(revision_spec)
    (out, _)= system(cmd_lst,
                     catch_stdout= True, catch_stderr= False,
                     env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    return out.splitlines()

def git_format_applied(parent, lines, output_dir):
    """run git format-patch"""
    if parent!="NULL":
        revspec= f"{parent}.."
    else:
        revspec= parent
    return _git_format_patch(revspec, lines, output_dir)

def git_format_patches(first_rev, lines, output_dir):
    """run git format-patch"""
    if first_rev=="NULL":
        raise AssertionError
    return _git_format_patch(first_rev, lines, output_dir)

def git_print_oneline_log_single(revision_spec):
    """prints one-line log, possible with color, to the console."""

    my_env= copy_env()
    if sh_prg_exists("cat"):
        my_env["GIT_PAGER"]="cat"
    system_simple(("git", "log", "--color=auto", "--oneline", "-1",
                   revision_spec))

def git_apply(filename):
    """git apply."""
    system_simple(("git", "apply", filename))

def git_am_simple(patch_file_glob):
    """apply patchfiles from a file-glob.

    May raise IOError
    """
    system_simple(f"git am {patch_file_glob}")

def git_am(patchfile):
    """apply a patch file.

    May raise IOError
    """
    system_simple(("git", "am", "--reject", patchfile))

def git_am_continue():
    """continue to apply a patch file.

    May raise IOError
    """
    system_simple(("git", "am", "--continue"))

def git_am_abort():
    """abort to apply a patch file.

    May raise IOError
    """
    system_simple(("git", "am", "--abort"))

def git_revert():
    """revert all changes."""
    system_simple(("git", "checkout", "--", "."))

def git_conflict_diff(file):
    """return conflict diff.

    file: if not None, append to this file
    may raise IOError
    """

    cmd_lst= ("git", "am", "--show-current-patch=diff")
    stdout_par= "PIPE"
    # pylint: disable=consider-using-with
    if file is not None:
        stdout_par= open(file, "wt", encoding= "utf-8")
    try:
        (out, _)= system_io(cmd_lst,
                            None, stdout_par, None,
                            env= None,
                            verbose= gbl_verbose, dry_run= gbl_dry_run)
    finally:
        if file is not None:
            stdout_par.close()
    if file is not None:
        return []
    return out.splitlines()

def git_reset_hard(revspec, dir_= None):
    """run git reset --hard."""

    old_dir= None
    if dir_ is not None:
        old_dir= sh_chdir(dir_)
    try:
        system_simple(("git", "reset", "--hard", revspec))
    finally:
        if old_dir is not None:
            sh_chdir(old_dir)

def git_amend_null():
    """create NULL revision with git commit --amend."""

    cmd_list=["git", "commit", "--amend", "-m", "NULL",
              "--reset-author", "--allow-empty"]
    system_simple(cmd_list)

def git_amend(log_message, log_message_file, log_message_template,
              date, author):
    """simple amend of HEAD revision."""
    cmd_list=["git", "commit", "--amend"]
    if log_message:
        cmd_list.extend(["-m", log_message])
    elif log_message_template:
        cmd_list.extend(["-t", log_message_file])
    elif log_message_file:
        cmd_list.extend(["-F", log_message_file])
    if date:
        cmd_list.extend(["--date", date])
    if author:
        cmd_list.extend(["--author", author])
    system_simple(cmd_list)

# ---------------------------------------------------------
# function that call git several times
# ---------------------------------------------------------

def git_create_null():
    """create a new NULL revision."""
    # go to the very first revision:
    rev1= git_revision_1()
    git_checkout(rev1)
    # Create a "zero revision" patch by deleting all files and amend the first
    # patch accordingly:
    git_rm_all()
    git_amend_null()

# ---------------------------------------------------------
# other functions
# ---------------------------------------------------------

def at_null_revision():
    """returns if we are at the null revision."""
    return git_head_subject() == "NULL"

def git_add_changes(add_unknown_files):
    """add only changed files to stash.

    Does not add:
    - unknown files (depending on add_unknown_files)
    - all files starting with $TOPPATCHDIR
    - all files ending with '.rej'
    - renames: the old files that are removed, these are already in git stash
    sample output from git --porcelain:
     M bin/git-gq
     M test/Makefile
     M test/TESTS
    RM test/git_gq_dump.ok -> test/git_gq_show.ok
    RM test/git_gq_dump.sh -> test/git_gq_show.sh
    ?? .gqpatches-2025-06-07T172509.tgz
    ?? .gqpatches/
    """
    cmd_list= ["git", "status", "--porcelain"]
    if not add_unknown_files:
        # do not show unknown files:
        cmd_list.append("-uno")

    (out, _)= system(cmd_list,
                     catch_stdout= True, catch_stderr= True,
                     env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    filelist= []
    for line in out.splitlines():
        m= RX_STAT.search(line)
        if m is None:
            errprint(f"WARNING: Cannot parse {line!r}, maybe not all "
                     f"unknown files were added")
            continue
        (stat, file)= (m.group(1), m.group(2))
        if stat=="??":
            # a file unknown to git
            # do not add .gqpatches directory:
            if RX_TOPPPATCHDIR.search(file):
                continue
            # do not add 'reject' files:
            if RX_REJ.search(file):
                continue
        if stat=="D ":
            # deleted file
            continue
        m= RX_GITSTAT_MV.search(line)
        if m:
            # renamed file
            # a line in the form 'R  README.txt -> README.rst'
            file= m.group(1)
        # do not add .gqpatches directory:
        filelist.append(file)
    if filelist:
        git_add(filelist)

def git_head_patch_status():
    """returns a status for each changed file for head patch.

    Example:
    D	README.rst
    M	bin/git-gq
    M	test/Makefile
    M	test/TESTS
    A	test/git_gq_pop_push_null.ok
    A	test/git_gq_pop_push_null.sh
    M	test/util.sh

    Flags:
    - A : added
    - C : copied
    - D : deleted
    - M : modified
    - R : renamed
    - T : changed
    - U : unmerged
    - X : unknown
    - B : broken

    Note: a rename looks like this:
    'R100 README.txt\tREADME2.txt'
    """
    (out, _)= system(("git", "diff", "--name-status", "HEAD~1", "HEAD"),
                     catch_stdout= True, catch_stderr= False,
                     env= None,
                     verbose= gbl_verbose, dry_run= gbl_dry_run)
    result= []
    for line in out.splitlines():
        (flag, file)= line.split(maxsplit=1)
        result.append((flag, file))
    return result

def git_head_patch_filelist():
    """just all files the head patch adds, modifies or renames."""
    exclude_list= set(("D", "X", "B"))
    lst= git_head_patch_status()
    files= []
    for e in lst:
        if e[0] in exclude_list:
            continue
        if e[0].startswith("R"):
            # rename
            files.append(e[1].split("\t", maxsplit=1)[1])
        else:
            files.append(e[1])
    return files

def _new_unknown_files(oldlist_file, newlist_file):
    """return list of new unknown files for git."""
    old_files= sh_set_from_file(oldlist_file)
    new_files= sh_set_from_file(newlist_file)
    lst= []
    if old_files == new_files:
        return lst
    for file in sorted(new_files.difference(old_files)):
        # do not add .gqpatches directory:
        if RX_TOPPPATCHDIR.search(file):
            continue
        # do not add 'reject' files:
        if RX_REJ.search(file):
            continue
        lst.append(file)
    return lst

def rm_new_unknown_files(file1, file2):
    """remove new unknown files."""

    for f in _new_unknown_files(file1, file2):
        os.remove(f)

def add_new_unknown_files(file1, file2):
    """add new files to git."""

    git_add(_new_unknown_files(file1, file2))

def log_template(logmessage, logmessage_file, outputfile, add_preamble):
    """create a template file for a log message."""

    sh_rm_f(outputfile)
    if add_preamble:
        sh_text_to_file("*** Please review and change this log message\n",
                        outputfile, do_append= True)
    if logmessage:
        sh_text_to_file(logmessage, outputfile, do_append= True)
    if logmessage_file:
        sh_file_to_file(logmessage_file, outputfile, do_append= True)

def make_head_logfile(outfile, add_preamble):
    """create or append file with HEAD log message."""

    if add_preamble:
        sh_text_to_file("*** Please review and change this log message\n",
                        outfile, do_append= False)
    else:
        sh_text_to_file(git_head_log(), outfile, do_append= False)

def check_uncomitted(commandname, force):
    """check for uncomitted changes.

    commandname: either 'push' or 'pop'

    May raise:
    AssertionError
    GitGqException
    """
    if force:
        return
    if not git_uncommitted():
        return
    errtext=["Error, there are uncomitted changes.",
             "You may:",
             "- Run this command with --force"]
    if commandname == "push":
        errtext.append("  CAUTION: You may get conflicts with this option.")
    elif commandname == "pop":
        errtext.append("  CAUTION: all your uncomitted changes will "
                       "be lost with this option.")
    else:
        raise AssertionError(f"unknown commandname: {commandname}")
    errtext.append("- Create a new patch with 'git gq new PATCHNAME' "
                   "and run this command again.")
    errtext.append("")
    raise GitGqException("\n".join(errtext))

def mark_conflict(patchname):
    """mark that a conflict exists."""

    sh_text_to_file(patchname, CONFLICT_FILENAME, do_append= False)
    git_conflict_diff(DIFF_FILENAME)

def conflict_patch():
    """return name of conflicting patch."""

    return sh_file_to_list(CONFLICT_FILENAME)[0]

def clear_conflict():
    """clean conflict."""

    sh_rm_f(CONFLICT_FILENAME, DIFF_FILENAME)

def conflict_exists():
    """check if a conflict exists."""

    return os.path.exists(CONFLICT_FILENAME)

def conflict_message(print_err):
    """message for a conflict."""
    if print_err:
        return "Error, an unresolved conflict exists.\n\n" + DOC_REJECT_MESSAGE
    return "\n"+DOC_REJECT_MESSAGE

def check_conflict(print_err):
    """raise GitGqException if conflict exists."""
    if conflict_exists():
        raise GitGqException(conflict_message(print_err))

def git_mk_changes_files(only_diff_patch):
    """create changes files that help editing a log message.

    create files:
    TOPPATCHDIR/HEAD.patch : all changes of the HEAD patch
    TOPPATCHDIR/DIFF.patch : all changes in the working copy not yet
    """
    with open(DIFF_FILENAME, "wt", encoding= "utf8") as fh:
        (_, _)= system_io(("git", "diff", "--cached"),
                          None, fh, None,
                          env= None,
                          verbose= gbl_verbose, dry_run= gbl_dry_run)
    if os.path.getsize(DIFF_FILENAME)==0:
        os.remove(DIFF_FILENAME)
    if not only_diff_patch:
        with open(HDIFF_FILENAME, "wt", encoding="utf-8") as fh:
            (_, _)= system_io(("git", "show", "HEAD"),
                              None, fh, None,
                              env= None,
                              verbose= gbl_verbose, dry_run= gbl_dry_run)
        if os.path.getsize(HDIFF_FILENAME)==0:
            os.remove(HDIFF_FILENAME)

def git_rm_changes_files():
    """remove changes files."""
    sh_rm_f(DIFF_FILENAME, HDIFF_FILENAME)

def get_parent(exist_test, use_exception):
    """get parent revision.

    Note: for parent=="NULL", the returned hash is "NULL"

    May raise:
    AssertionError
    GitGqException
    """
    if not os.path.exists(PARENTFILE):
        raise AssertionError(f"Error, {PARENTFILE} does not exist.")
    lines= sh_file_to_list(PARENTFILE)
    if len(lines)!=1:
        raise AssertionError(f"unexpected lineno: {len(lines)}")
    parent= lines[0]
    if parent=="NULL":
        return ("NULL", "NULL")
    hash_= parent.split(maxsplit=1)[0]
    if exist_test:
        if not git_check_exists(hash_):
            if not use_exception:
                return (None, parent)
            raise GitGqException(f"Error, parent revision {hash_} "
                                 f"doesn't exist in repository")
    return (hash_, parent)

def find_single_unapplied_patch(regexp):
    """finds a unique unapplied patch.
    
    if regexp is None, take the TOP patch.

    returns: 
      matching line if found
    in case of an error, the function prints an error message to stderr.

    May raise:
    GitGqException
    """
    sh_file_exists(SERIESFILE)
    if os.path.getsize(SERIESFILE)==0:
        raise GitGqException("Error, there are no unapplied patches.")
    if not regexp:
        return sh_file_head(1, False, SERIESFILE, None)[0].strip()
    matchlines= sh_file_grep(regexp, SERIESFILE)
    if not matchlines:
        raise GitGqException(f"Error, no patches match '{regexp}'.")
    if len(matchlines)!=1:
        raise GitGqException(f"Error, multiple patches match '{regexp}'.")
    return matchlines[0].strip()

def find_first_unapplied_patch(regexp):
    """finds unapplied patch.

    regexp: regular expression or empty string

    returns:
    the patch if found

    May raise:
    GitGqException
    """
    sh_file_exists(SERIESFILE)
    if os.path.getsize(SERIESFILE)==0:
        raise GitGqException("Error, there are no unapplied patches.")
    if not regexp:
        return sh_file_head(1, False, SERIESFILE, None)[0]
    match_lines= sh_file_grep(regexp, SERIESFILE)
    if not match_lines:
        raise GitGqException("Error, no matching unapplied patches found.")
    return match_lines[0]

def find_first_applied_patch(regexp):
    """Find applied patch, return hash key.

    regexp: regular expression or empty string

    returns:
    hash if found

    May raise:
    GitGqException
    """
    (parent_hash, _)= get_parent(exist_test= True, use_exception= True)
    use_long_hash= RX_HASH.search(regexp) is not None
    logs= applied_log(parent_hash, None,
                      print_to_console= False,
                      use_long_hash= use_long_hash)
    if not use_long_hash:
        rx_regexp= re.compile(regexp)
    else:
        rx_regexp= re.compile('^'+regexp)
    found= ""
    for log in logs:
        if rx_regexp.search(log):
            found= log
            break
    if not found:
        raise GitGqException(f"Error, patch '{regexp}' not found.")
    hash_= found.split(maxsplit=1)[0]
    return git_rev_parse(hash_, catch_stderr= False)

def find_head_patch(regexp):
    """looks if the HEAD patch matches pattern.

    returns:
      hash key if found
      None if not found

    """
    (out, _)= system(("git", "log", "--oneline", "-1"),
                     catch_stdout= True, catch_stderr= False,
                     env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    rx_regexp= re.compile(regexp)
    line= out.strip()
    if not rx_regexp.search(line):
        return None
    return line.split(maxsplit=1)[0]

def dump_patch_file(file):
    """print to console."""
    if sys.stdout.isatty() and sh_prg_exists("colordiff") \
        and sh_prg_exists("less"):
        # We're running in a real terminal
        system_simple(f"colordiff < {file} | less -R")
    else:
        # You're being piped or redirected
        sh_file_pager(file)

def save_applied_patches():
    """save all applied patches."""

    (parent_hash, _)= get_parent(exist_test= True, use_exception= True)
    head_rev= git_head_revision()
    sh_rm_rf(APPLIEDDIR)
    if head_rev != parent_hash:
        os.mkdir(APPLIEDDIR)
        # Note: printing the files here is only for compatibility with the old
        # git-gq bash implementation and should be removed in the future:
        files= git_format_applied(parent_hash, None, APPLIEDDIR)
        print("\n".join(files))

def select_queue(queue):
    """modifies global variables for a new queue.

    modified:
    QUEUENAME, PATCHDIR, SERIESFILE, PARENTFILE
    """
    # pylint: disable= global-statement
    global QUEUENAME
    global PATCHDIR
    global APPLIEDDIR
    global SERIESFILE
    global PARENTFILE
    QUEUENAME= queue
    PATCHDIR= ojoin(TOPPATCHDIR, QUEUENAME)
    APPLIEDDIR= ojoin(PATCHDIR, "applied")
    SERIESFILE= ojoin(PATCHDIR, "series")
    PARENTFILE= ojoin(PATCHDIR, "parent")

def qpop_check(force):
    """check if qpop is allowed.

    returns: 
    - True : allowed
    - False: not allowed

    May raise:
    GitGqException
    """

    git_head_track_error()
    # may raise GitGqException:
    check_uncomitted("pop", force)
    tags= None
    # pylint: disable= global-statement
    global gbl_tag_warning
    if gbl_tag_warning:
        tags= git_head_tags()
    if tags:
        print(f"Warning: The HEAD revision has the tag(s) {tags!r}")
        print("'git gq pop' cannot remove this tag, so the tagged revision ")
        print("will remain in the repository, just the 'HEAD' will be moved.")
        print("You may abort here and remove the tag with:")
        print("  git tag -d TAGNAME")
        print("or continue nevertheless.")
        if not ask_continue():
            raise GitGqException("user abort")
        # Warn only a single time (relevant for 'git gq pop -a')
        gbl_tag_warning= False
    # may raise GitGqException:
    (parent_hash, parent)= get_parent(exist_test= True, use_exception= True)
    if parent=="NULL":
        # with PARENT==NULL, qpop is always allowed
        if at_null_revision():
            # NULL revision reached
            return False
        return True
    head_rev= git_head_revision()
    if parent_hash == head_rev:
        return False
    return True

def qpop_one():
    """a single qpop operation."""
    orig_patchname= \
        RX_TOPPPATCHDIR.sub("", git_format_patches("HEAD", 1, TOPPATCHDIR)[0])
    patchname= RX_NUMBER.sub("", orig_patchname)
    patchname= unique_patch_name(patchname)
    sh_file_rename(ojoin(TOPPATCHDIR, orig_patchname), ojoin(PATCHDIR, patchname))
    prepend_seriesfile(patchname)
    headrev= git_head_revision()
    rev1= git_revision_1()
    if headrev == rev1:
        # special treatment for first revision, create a "zero revision" patch
        # by deleting all files and amend the first patch accordingly:
        git_rm_all()
        git_amend_null()
    else:
        git_reset_hard('HEAD~1')

def qpush_specified(patch, force):
    """push a patch.

    if patch is <None>, push the TOP patch from the patch queue.

    May raise GitGqException
    """
    check_uncomitted("push", force)
    patchname= find_single_unapplied_patch(patch)
    sh_file_exists(SERIESFILE)
    if os.path.getsize(SERIESFILE)==0:
        raise GitGqException("Error, there are no unapplied patches.")
    sh_text_to_file(patchname, ojoin(PATCHDIR, "PUSH"),
                    do_append= False, add_final_newline= True)
    # remove PATCHNAME from SERIESFILE:
    seriesfile_new= sh_file_new(SERIESFILE)
    if patch is None:
        # remove first patch
        sh_file_head(1, True, SERIESFILE, seriesfile_new)
    else:
        # remove line with the patchname:
        sh_file_filter(f"{patchname}\n", SERIESFILE, seriesfile_new)
    git_unknown_files(UNKNOWN1_FILENAME)
    try:
        git_am(ojoin(PATCHDIR, patchname))
    except IOError:
        mark_conflict(patchname)
        git_unknown_files(UNKNOWN2_FILENAME)
        raise GitGqException(conflict_message(False)) from None
    clear_conflict()
    sh_rm_f(ojoin(PATCHDIR, patchname), ojoin(PATCHDIR, "PUSH"),
            SERIESFILE)
    sh_file_rename(seriesfile_new, SERIESFILE)

def qedit(patch):
    """starts an editor."""
    editor= editor_dialog()
    patchname= find_single_unapplied_patch(patch)
    system_simple((editor, ojoin(PATCHDIR, patchname)))

def qdelete(patch):
    """deletes a patch."""
    patchname= find_single_unapplied_patch(patch)
    os.remove(ojoin(PATCHDIR, patchname))
    # remove line with the patchname:
    sh_file_filter(f"{patchname}\n", SERIESFILE, SERIESFILE, cleanup= False)

def create_parentfile(revspec):
    """create a parent file."""
    if revspec=="NULL":
        log= revspec
    else:
        rev= git_rev_parse(revspec, catch_stderr= False)
        if rev == revspec:
            print(f"queue parent revision set to {revspec}")
        else:
            print(f"queue parent revision set to {revspec} ({rev})")
        log= repo_log(rev, 1, print_to_console= False,
                      use_long_hash= False)
    sh_text_to_file(log, PARENTFILE, do_append= False,
                    add_final_newline= True)

# ---------------------------------------------------------
# main coommand functions
# ---------------------------------------------------------

def git_gq_man():
    """display man page."""

    # Try to find man page in a portable way. The recommendation to use
    # importlib.resources was taken from:
    # https://setuptools.pypa.io/en/latest/userguide/datafiles.html#subdir-data-files
    manpage= None
    if sh_prg_exists("man"):
        try:
            for d in resources.files("git_gq.man.man1").iterdir():
                if d.name=="git-gq.1":
                    manpage= d
                    break
        except ModuleNotFoundError:
            pass
        # Fallback: search relative to THIS binary:
        if manpage is None:
            b= os.path.dirname(__file__)
            m= os.path.join(b, "../src/git_gq/man/man1/git-gq.1")
            if os.path.exists(m):
                manpage= os.path.abspath(m)
        if manpage is not None:
            system_simple(["man", "-l", manpage])
            return

    errprint("'man' program or manpage not found, displaying reStructuredText instead.")
    lst= []
    print_doc(None, lst)
    pydoc.pager("\n".join(lst))

def git_gq_restore(revision, force):
    """restore from revision."""
    check_conflict(True)
    if not os.path.isdir(ojoin(TOPPATCHDIR, ".git")):
        raise GitGqException("Error, 'git gq backup' was never run.")

    if not force:
        untracked= git_untracked(TOPPATCHDIR)
        if untracked:
            raise GitGqException(f"Error, there are files not tracked in "
                                 f"in {TOPPATCHDIR}: {' '.join(untracked)}")
    uncommitted= git_uncommitted(TOPPATCHDIR)
    if uncommitted:
        if not force:
            raise GitGqException(f"Error, there are uncommitted changes "
                                 f"in {TOPPATCHDIR}: {' '.join(uncommitted)}")
        git_reset_hard("HEAD", TOPPATCHDIR)

    try:
        revspec= git_rev_parse(revision, catch_stderr= False,
                               dir_= TOPPATCHDIR)
        head_rev= git_head_revision()
        if revspec != head_rev:

            git_checkout(revspec, TOPPATCHDIR)
            errprint(f"Note: The 'detached HEAD' warning concerns to the "
                     f"repository in '{TOPPATCHDIR}'.")
        git_clean(TOPPATCHDIR)
    except IOError as e:
        raise GitGqException(str(e)) from None
    queuename= sh_file_to_list(QUEUEFILE)[0].strip()
    select_queue(queuename)
    parent_exists= True
    (parent_hash, parent)= get_parent(exist_test= True, use_exception= False)
    if parent=="NULL":
        print("Note: The restored PARENT revision is NULL.")
        print(f"Originally applied patches are in {APPLIEDDIR}.")
        # do not try to restore applied patches:
        parent_exists= False
    if parent_hash is None:
        # parent hash couldn't be found in repository
        parent_exists= False
        print("Warning: The restored PARENT revision:")
        print(f"{parent}")
        print("does not exist in your repository.")
        print("You have to set a valid parent with 'git gq parent'.")
    if parent_exists and (os.path.isdir(APPLIEDDIR)):
        print("You can now re-create the patch queue with 'git gq revert'.")

def git_gq_revert(move_branchname):
    """revert repo to state in patch queue."""
    check_conflict(True)
    if not os.path.isdir(ojoin(TOPPATCHDIR, ".git")):
        raise GitGqException("Error, 'git gq backup' was never run.")
    if git_uncommitted(TOPPATCHDIR):
        raise GitGqException(f"Error, there are uncommitted changes "
                             f"in {TOPPATCHDIR}")
    print("Reverting changes in repository cannot be undone easily.")
    print("Continue ?")
    if not ask_continue():
        print("command aborted")
        return
    (parent_hash, parent)= get_parent(exist_test= True, use_exception= False)
    if parent=="NULL":
        print("Note: The current PARENT revision is NULL.")
        if not at_null_revision():
            # Create a single empty 'NULL' revision at the start:
            git_create_null()
    elif parent_hash is None:
        # parent hash couldn't be found in repository
        print("Error: this parent:")
        print(f"{parent}")
        print("does not exist in your repository.")
        print("You have to set a valid parent with 'git gq parent' first.")
        return
    else:
        if git_head_revision() != parent_hash:
            # only needed if head revision != parent:
            # name of current branch:
            curr_branch= git_current_branch()
            if not move_branchname:
                # create a new name for the old, deprecated commits:
                deprecated_branch= git_create_branchname(curr_branch)
                # create branch for deprecated commits:
                git_switch_branch(deprecated_branch)
                # go to older revision, suppress detached head warning:
                git_checkout(parent_hash, detached_head_warn= False)
                # now move the original branch here:
                git_move_branch(curr_branch, "HEAD")
            else:
                # create a new name for the new, revert-commits:
                new_branch= git_create_branchname(curr_branch)
                # go to older revision, suppress detached head warning:
                git_checkout(parent_hash, detached_head_warn= False)
                # create this new branch
                git_switch_branch(new_branch)

    git_am_simple(f"{APPLIEDDIR}/*.patch")

def git_gq_backup(message):
    """create a backup."""
    save_applied_patches()
    if not os.path.isdir(ojoin(TOPPATCHDIR, ".git")):
        git_init(TOPPATCHDIR)
    git_add(os.listdir(TOPPATCHDIR), TOPPATCHDIR)
    if message is None:
        message=f"backup {portable_isodate()}"
    git_commit(message, TOPPATCHDIR)

def git_gq_qrepo(command_args):
    """run git command in .gqpatches.

    Examples:
    git-gq qrepo log
    git-gq qrepo log -- --stat
    """
    if not os.path.isdir(ojoin(TOPPATCHDIR, ".git")):
        raise GitGqException(f"Error, no git repo in {TOPPATCHDIR}")
    old_dir= sh_chdir(TOPPATCHDIR)
    cmd_list= ["git"]
    cmd_list.extend(command_args)
    try:
        system_rc(cmd_list, catch_stdout= False, catch_stderr= False,
                  env= None, verbose= gbl_verbose, dry_run= gbl_dry_run)
    finally:
        if old_dir is not None:
            sh_chdir(old_dir)

def git_gq_init(name, rev):
    """run git gq init."""
    if name:
        # pylint: disable= global-statement
        global QUEUENAME
        QUEUENAME= name
    try:
        os.mkdir(TOPPATCHDIR)
    except FileExistsError:
        raise GitGqException(f"Error, patch queue directory "
                             f"{TOPPATCHDIR!r} already exists") from None
    os.mkdir(TEMPDIR)
    if os.path.isdir(ojoin(TOPPATCHDIR, QUEUENAME)):
        raise GitGqException(f"Error, patch queue '{QUEUENAME}' "
                             f"already exists")
    sh_text_to_file(QUEUENAME, QUEUEFILE, do_append= False,
                    add_final_newline=True)
    select_queue(QUEUENAME)
    os.mkdir(ojoin(TOPPATCHDIR, QUEUENAME))
    if not rev:
        rev= "HEAD"
    create_parentfile(rev)

def git_gq_qname(qname):
    """qname command."""
    if qname is None:
        # pylint: disable= global-statement
        global QUEUENAME
        QUEUENAME= sh_file_to_list(QUEUEFILE)[0].strip()
        print("Existing queues:")
        dirs_= [d for d in sh_directories(TOPPATCHDIR) if d != TEMP_BASEDIR]
        for d in dirs_:
            print(f"\t{d}")
        print()
        print("Currently selected:")
        print(f"\t{QUEUENAME}")
        return
    check_conflict(True)
    if qname in FORBIDDED_QUEUENAMES:
        raise GitGqException(f"Error, '{qname}' is a special name "
                             f"and cannot be used as name for a queue.")
    QUEUENAME= qname
    sh_text_to_file(QUEUENAME, QUEUEFILE, do_append= False,
                    add_final_newline=True)
    select_queue(QUEUENAME)
    qdir= ojoin(TOPPATCHDIR, QUEUENAME)
    if not os.path.isdir(qdir):
        os.mkdir(qdir)
        create_parentfile("HEAD")

def git_gq_change_order():
    """edit series file."""
    check_conflict(True)
    sh_file_exists(SERIESFILE)
    if os.path.getsize(SERIESFILE)==0:
        raise GitGqException("Error, there are no unapplied patches.")
    editor= editor_dialog()
    system_simple((editor, SERIESFILE))

def git_gq_export(directory):
    """export command."""
    sh_dir_exists(directory)
    (parent_hash, _)= get_parent(exist_test= True, use_exception= True)
    out= git_format_applied(parent_hash, None, directory)
    print("\n".join(out))

def git_gq_import(patchfiles):
    """import command."""
    for f in patchfiles:
        sh_file_exists(f)
    for f in patchfiles:
        new_= unique_patch_name(os.path.basename(f))
        system_simple(("cp", "-a", f, ojoin(PATCHDIR, new_)))
        prepend_seriesfile(new_)

def git_gq_parent(revspec):
    """parent command."""
    if not revspec:
        (_, parent)= get_parent(exist_test= True, use_exception= True)
        print(parent)
        return
    check_conflict(True)
    create_parentfile(revspec)

def git_gq_new(name, no_add):
    """new command."""
    check_conflict(True)
    if not no_add:
        git_add_changes(add_unknown_files= False)
    cmd_list= ["git", "commit"]
    if not name:
        # if this case an editor will (probably) be started
        git_mk_changes_files(only_diff_patch= True)
    else:
        cmd_list.extend(["-m", name])
    system_simple(cmd_list)
    if not name:
        git_rm_changes_files()

def git_gq_record(name):
    """record command."""
    check_conflict(True)
    git_select_changes()
    cmd_lst= ["git", "commit"]
    if name:
        cmd_lst.extend(["-m", name])
    system_simple(cmd_lst)

def git_gq_refresh(message, file, edit, no_add):
    """refresh command."""
    check_conflict(True)
    if (not message) and (not file):
        make_head_logfile(LOG_FILENAME, edit)
    else:
        log_template(message, file, LOG_FILENAME, edit)
    if not no_add:
        git_add_changes(add_unknown_files= False)
    if edit:
        # create two files so the user can review changes while editing the
        # log message:
        git_mk_changes_files(only_diff_patch= False)
    git_amend(None, LOG_FILENAME, edit, None, None)
    if edit:
        # remove the changes files:
        git_rm_changes_files()
    sh_rm_f(LOG_FILENAME)

def git_gq_edit(name_regexp):
    """edit command."""
    qedit(name_regexp)

def git_gq_delete(name_regexp):
    """delete command."""
    qdelete(name_regexp)

def git_gq_pop(all_, force):
    """pop command."""
    check_conflict(True)
    while True:
        if not qpop_check(force):
            if all_:
                return
            raise GitGqException("Error, 'pop' beyond parent revision "
                                 "not allowed.")
        qpop_one()
        if not all_:
            break

def git_gq_push(all_, force):
    """push command."""
    check_conflict(True)
    null_revision= at_null_revision()
    while True:
        qpush_specified(None, force)
        if null_revision:
            # must convert 'push' into a 'fold'
            sh_text_to_file(git_head_log(), LOG_FILENAME, do_append= False)
            sh_text_to_file(git_head_date(), DATE_FILENAME, do_append= False)
            sh_text_to_file(git_head_author(), AUTHOR_FILENAME,
                            do_append= False)
            qpop_one()
            patchname= find_first_unapplied_patch(None)
            git_apply(ojoin(PATCHDIR, patchname))
            # add changes because we are at the NULL revision:
            date= sh_file_to_list(DATE_FILENAME)[0].strip()
            author= sh_file_to_list(AUTHOR_FILENAME)[0].strip()
            git_add_changes(add_unknown_files= True)
            git_amend(None, LOG_FILENAME, False, date, author)
            qdelete(patchname)
            null_revision= False
        if not all_:
            break
        sh_file_exists(SERIESFILE)
        # with "--all", reaching the end is no error:
        if os.path.getsize(SERIESFILE)==0:
            break
        null_revision= False

def git_gq_goto(name_regexp, force):
    """goto command."""
    check_conflict(True)
    patchname= None
    try:
        patchname= find_first_unapplied_patch(name_regexp)
    except GitGqException:
        pass
    if patchname is not None:
        while True:
            qpush_specified(None, force)
            try:
                find_first_unapplied_patch(patchname)
            except GitGqException:
                break
        return
    patchname= find_first_applied_patch(name_regexp)
    while True:
        if find_head_patch(patchname) is not None:
            break
        qpop_one()

def git_gq_fold(name_regexp, edit, force, no_add):
    """fold command."""
    check_conflict(True)
    if os.path.isfile(ojoin(PATCHDIR, name_regexp)):
        patchname= name_regexp
    else:
        patchname= find_single_unapplied_patch(name_regexp)
    if at_null_revision():
        raise GitGqException("Error, cannot fold to 'NULL' revision, "
                             "use 'git gq push' instead.")
    make_head_logfile(LOG_FILENAME, edit)
    sh_text_to_file("\n\n***\n\n", LOG_FILENAME, do_append= True)
    qpush_specified(patchname, force)
    filelist= git_head_patch_filelist()
    sh_text_to_file(git_head_log(), LOG_FILENAME, do_append= True,
                    add_final_newline= True)
    qpop_one()
    git_apply(ojoin(PATCHDIR, patchname))
    if not no_add:
        if at_null_revision():
            git_add_changes(add_unknown_files= True)
        else:
            git_add_changes(add_unknown_files= False)
            git_add(filelist)
    if edit:
        git_mk_changes_files(only_diff_patch= False)
    # if edit is True, git_amend will start an editor to edit the combination
    # of both log messages:
    git_amend(None, LOG_FILENAME, edit, None, None)
    if edit:
        # remove the changes files:
        git_rm_changes_files()
    # remove left-overs
    sh_rm_f(LOG_FILENAME)
    qdelete(patchname)
    print("Note: Log messages were combined into one, you should review/edit "
          "the log message with:")
    print("      git gq refresh -e")
    print("Note: If new files were added by the folded patch, run:")
    print("      git add NEW-FILES")
    print("      git gq refresh -e")

def git_gq_show(name_regexp):
    """fold command."""
    patchname= name_regexp
    try:
        # First try if $name_arg is a revision specification:
        patchname= git_rev_parse(name_regexp, catch_stderr= True)
        git_show(patchname)
        return
    except GitGqException:
        pass
    except IOError:
        pass
    try:
        patchname= find_first_applied_patch(name_regexp)
        git_show(patchname)
        return
    except GitGqException:
        pass
    if os.path.isfile(ojoin(PATCHDIR, patchname)):
        dump_patch_file(ojoin(PATCHDIR, patchname))
        return
    try:
        patchname= find_first_unapplied_patch(name_regexp)
        dump_patch_file(ojoin(PATCHDIR, patchname))
        return
    except GitGqException:
        raise GitGqException(f"Error, patch '{name_regexp}' not found.") \
              from None

def git_gq_applied(lines):
    """applied command."""
    # Note: for parent==NULL, parent_hash is "NULL"
    (parent_hash, _)= get_parent(exist_test= True, use_exception= True)
    applied_log(parent_hash, lines, print_to_console= True,
                use_long_hash= False)

def git_gq_unapplied(lines):
    """unapplied command."""
    try:
        sh_file_exists(SERIESFILE)
    except GitGqException:
        # print("no unapplied patches")
        return
    if os.path.getsize(SERIESFILE)==0:
        # print("no unapplied patches")
        return
    if not lines:
        system_simple(("cat", SERIESFILE))
    else:
        print("\n".join(sh_file_head(lines, False, SERIESFILE, None)))

def git_gq_continue(no_add):
    """continue command."""
    if not conflict_exists():
        raise GitGqException("Error, there currently is no conflict "
                             "to resolve.")
    if not no_add:
        git_add_changes(add_unknown_files= False)
        add_new_unknown_files(UNKNOWN1_FILENAME, UNKNOWN2_FILENAME)
    try:
        git_am_continue()
    except IOError:
        print_reject_message()
        return
    clear_conflict()
    #git_rm_reject_files()
    seriesfile_new= sh_file_new(SERIESFILE)
    if os.path.isfile(seriesfile_new):
        system_simple(("cp", "-a", seriesfile_new, SERIESFILE))
    patchname= sh_file_to_list(ojoin(PATCHDIR, "PUSH"))[0].strip()
    sh_rm_f(seriesfile_new, ojoin(PATCHDIR, patchname),
            ojoin(PATCHDIR, "PUSH"))

def git_gq_abort():
    """abort command."""
    if not conflict_exists():
        raise GitGqException("Error, there currently is no conflict "
                             "to resolve.")
    git_am_abort()
    clear_conflict()
    #git_rm_reject_files()
    # remove left over added files:
    rm_new_unknown_files(UNKNOWN1_FILENAME, UNKNOWN2_FILENAME)
    git_revert()
    sh_rm_f(UNKNOWN1_FILENAME, UNKNOWN2_FILENAME,
            sh_file_new(SERIESFILE), ojoin(PATCHDIR, "PUSH"))

def git_gq_conflict(cmd):
    """conflict command."""
    if not conflict_exists():
        raise GitGqException("Error, there currently is no conflict state.")
    if not cmd:
        print("The repository is currently in a conflict state.")
        print()
        print("Conflicting patch:")
        conflict_patch()
        print()
        print_reject_message()
    elif cmd=="files":
        lines= sh_file_to_list_filter(DIFF_FILENAME,
                                      lambda x: x.startswith("diff "))
        for l in lines:
            print(l.split()[3][2:])
    elif cmd=="show":
        sh_file_pager(DIFF_FILENAME)
    else:
        raise GitGqException(f"Error, unknown sub-command '{cmd}'")

# ---------------------------------------------------------
# process
# ---------------------------------------------------------

def unpack_list(lst, elms):
    """unpack 'elm' elements from list."""
    new= []
    l_lst= len(lst)
    for i in range(elms):
        # 0 .. (elms-1)
        if i<l_lst:
            new.append(lst[i])
        else:
            new.append(None)
    return new

def unpack_one(lst):
    """unpack one element from list."""
    if not lst:
        return None
    return lst[0]

def check_command_args(command, command_args, min_, max_):
    """Check number of args."""
    if min_ is not None:
        if min_>0:
            if (not command_args) or (len(command_args)<min_):
                raise GitGqException(f"Error, at least {min_} arguments "
                                     f"required for command '{command}'")
    if max_ is not None:
        if (command_args) and (len(command_args)>max_):
            raise GitGqException(f"Error, too many arguments for "
                                 f"command '{command}'")


def process(args, rest):
    """do all the work.
    """
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-statements
    # pylint: disable=too-many-return-statements
    #print("args:",args)
    #print("rest:",rest)
    try:
        if args.verbose:
            # pylint: disable= global-statement
            global gbl_verbose
            gbl_verbose= args.verbose
        if args.dry_run:
            # pylint: disable= global-statement
            global gbl_dry_run
            gbl_dry_run= args.dry_run

        if args.summary:
            print_summary()
            sys.exit(0)
        if args.help: # --help
            pydoc.pager(short_help_text("txt"))
            check_bashcompletion()
            return
        if not rest:
            git_gq_man()
            return

        command= rest[0]
        command_args= rest[1:]

        if command in ("help", "man"):
            git_gq_man()
            check_bashcompletion()
            return

        if command=="commands":
            check_command_args(command, command_args, None, 0)
            print("\n".join(sorted(ALL_COMMANDS)))
            return

        if command=="bashcompletion":
            check_command_args(command, command_args, None, 0)
            print(BASHCOMPLETION)
            return

        if command=="doc":
            check_command_args(command, command_args, None, 1)
            lst= []
            print_doc(unpack_one(command_args), lst)
            pydoc.pager("\n".join(lst))
            check_bashcompletion()
            return

        git_goto_repo_dir()

        if command=="glog":
            check_command_args(command, command_args, None, 0)
            git_glog()
            return

        if command=="restore":
            check_command_args(command, command_args, 1, 1)
            git_gq_restore(command_args[0], args.force)
            return

        if command=="revert":
            check_command_args(command, command_args, None, 0)
            git_gq_revert(args.move_branchname)
            return

        if command=="init":
            check_command_args(command, command_args, None, 2)
            #pylint: disable = no-value-for-parameter
            git_gq_init(*unpack_list(command_args, 2))
            return

        if not os.path.isdir(TOPPATCHDIR):
            raise GitGqException("please run 'git gq init' first.")

        if command=="qname":
            check_command_args(command, command_args, None, 1)
            git_gq_qname(unpack_one(command_args))
            return

        # pylint: disable= global-statement
        global QUEUENAME
        QUEUENAME= sh_file_to_list(QUEUEFILE)[0].strip()
        select_queue(QUEUENAME)
        # ensure PATCHDIR exists:
        sh_dir_exists(PATCHDIR)

        if command=="backup":
            check_command_args(command, command_args, None, 0)
            git_gq_backup(args.message)
            return

        if command=="qrepo":
            git_gq_qrepo(command_args)
            return

        if command=="change-order":
            check_command_args(command, command_args, None, 0)
            git_gq_change_order()
            return

        if command=="export":
            check_command_args(command, command_args, 1, 1)
            git_gq_export(command_args[0])
            return

        if command=="import":
            check_command_args(command, command_args, 1, None)
            git_gq_import(command_args)
            return

        if command=="parent":
            check_command_args(command, command_args, None, 1)
            git_gq_parent(unpack_one(command_args))
            return

        if command=="new":
            check_command_args(command, command_args, None, 1)
            git_gq_new(unpack_one(command_args), args.no_add)
            return

        if command=="record":
            check_command_args(command, command_args, None, 1)
            git_gq_record(unpack_one(command_args))
            return

        if command=="refresh":
            check_command_args(command, command_args, 0, 0)
            git_gq_refresh(args.message, args.file, args.edit, args.no_add)
            return

        if command=="edit":
            check_command_args(command, command_args, 1, 1)
            git_gq_edit(command_args[0])
            return

        if command=="delete":
            check_command_args(command, command_args, 1, 1)
            git_gq_delete(command_args[0])
            return

        if command=="pop":
            check_command_args(command, command_args, 0, 0)
            git_gq_pop(args.all, args.force)
            return

        if command=="push":
            check_command_args(command, command_args, 0, 0)
            git_gq_push(args.all, args.force)
            return

        if command=="goto":
            check_command_args(command, command_args, 1, 1)
            git_gq_goto(unpack_one(command_args), args.force)
            return

        if command=="fold":
            check_command_args(command, command_args, 1, 1)
            git_gq_fold(unpack_one(command_args),
                        args.edit, args.force, args.no_add)
            return

        if command=="show":
            check_command_args(command, command_args, 1, 1)
            git_gq_show(unpack_one(command_args))
            return

        if command=="applied":
            check_command_args(command, command_args, None, 0)
            git_gq_applied(args.lines)
            return

        if command=="unapplied":
            check_command_args(command, command_args, None, 0)
            git_gq_unapplied(args.lines)
            return

        if command=="continue":
            check_command_args(command, command_args, None, 0)
            git_gq_continue(args.no_add)
            return

        if command=="abort":
            check_command_args(command, command_args, None, 0)
            git_gq_abort()
            return

        if command=="conflict":
            check_command_args(command, command_args, 0, 1)
            git_gq_conflict(unpack_one(command_args))
            return

        raise GitGqException(f"Error, unknown command '{command}'")
    except (GitGqException, ValueError) as e:
        if args.exception:
            raise
        sys.exit(str(e))



def script_shortname():
    """return the name of this script without a path component."""
    return os.path.basename(sys.argv[0])

def print_summary():
    """print a short summary of the scripts function."""
    print(f"{script_shortname():<20}: {SUMMARY}\n")


def main():
    """The main function.

    parse the command-line options and perform the command
    """
    parser = argparse.ArgumentParser(\
                 usage= USAGE,
                 description= DESC,
                 add_help= False,
                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                    )
    parser.add_argument('--version', action='version',
                        version=f"{VERSION}")

    parser.add_argument("--summary",
                        action="store_true",
                        help="print a summary of the function of the program",
                       )
    parser.add_argument("-h", "--help",
                        action="store_true",
                        help="Show help."""
                       )
    parser.add_argument("--verbose",
                        action="store_true",
                        help="show what commands are called"
                       )
    parser.add_argument("--dry-run",
                        action="store_true",
                        help="show what commands would be called"
                       )
    parser.add_argument("-D", "--debug",
                        action="store_true",
                        help="Show debug information."
                       )
    parser.add_argument("-a", "--all",
                        action="store_true",
                        help="push/pop: apply on ALL patches.",
                       )
    parser.add_argument("-N", "--no-add",
                        action="store_true",
                        help="new/refresh/fold: DO NOT add all modified "
                             "changes to patch, continue: DO NOT add all "
                             "modified and unknown changes to patch."
                       )
    parser.add_argument("-e", "--edit",
                        action="store_true",
                        help="refresh/fold: start editor to edit log message"
                       )
    parser.add_argument("-m", "--message",
                        help="backup/refresh: use MESSAGE as log message.",
                        metavar="MESSAGE"
                       )
    parser.add_argument("-F", "--file",
                        help="refresh: take log message from FILE.",
                        metavar="FILE"
                       )
    parser.add_argument("-l", "--lines",
                        help="applied, unapplied: Limit the number of "
                             "lines printed by the command. Print only "
                             "the first LINECOUNT lines.",
                        type= int,
                        metavar="LINECOUNT"
                       )
    parser.add_argument("-R", "--force",
                        action="store_true",
                        help="`git gq pop`, `git gq push`: Execute command "
                             "even if there are uncommited changes. Note "
                             "that `git gq pop` will discard uncommited "
                             "changes. `git gq restore`: discard "
                             "uncommitted changes and unknown files in "
                             "patch queue."
                       )
    parser.add_argument("--move-branchname",
                        action="store_true",
                        help="For ``git gq revert``, move the current branch "
                             "name to the new created branch.",
                       )
    parser.add_argument("--exception",
                        action="store_true",
                        help="do not catch exceptions (for debugging)."
                       )


    (args, remains) = parser.parse_known_args()
    rest= []
    check= True
    for r in remains:
        if (not check) or (not r.startswith("-")) or (r=="-"):
            rest.append(r)
            continue
        if r=="--": # do not check further
            check= False
            continue
        sys.exit(f"unknown option: {r!r}")

    if args.summary:
        print_summary()
        sys.exit(0)

    # pylint: disable= global-statement
    global gbl_parser
    gbl_parser= parser
    # pylint: enable= global-statement

    process(args, rest)
    sys.exit(0)

if __name__ == "__main__":
    main()
