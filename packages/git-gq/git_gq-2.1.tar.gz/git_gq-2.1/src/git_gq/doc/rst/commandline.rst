Command line interface
----------------------
usage: git_gq.py [OPTIONS] COMMAND

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
    also removes all reject (\*.rej) files that are not tracked by git.

  abort          
    Abort (undo) 'push' after you had a conflict and could not fix it manually.
    This also removes all reject (\*.rej) files that are not tracked by git.

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

  --version             show program's version number and exit
  --summary             print a summary of the function of the program
  -h, --help            Show help.
  --verbose             show what commands are called
  --dry-run             show what commands would be called
  -D, --debug           Show debug information.
  -a, --all             push/pop: apply on ALL patches.
  -N, --no-add          new/refresh/fold: DO NOT add all modified changes to
                        patch, continue: DO NOT add all modified and unknown
                        changes to patch.
  -e, --edit            refresh/fold: start editor to edit log message
  -m, --message MESSAGE
                        backup/refresh: use MESSAGE as log message.
  -F, --file FILE       refresh: take log message from FILE.
  -l, --lines LINECOUNT
                        applied, unapplied: Limit the number of lines printed
                        by the command. Print only the first LINECOUNT lines.
  -R, --force           `git gq pop`, `git gq push`: Execute command even if
                        there are uncommited changes. Note that `git gq pop`
                        will discard uncommited changes. `git gq restore`:
                        discard uncommitted changes and unknown files in patch
                        queue.
  --move-branchname     For ``git gq revert``, move the current branch name to
                        the new created branch.
  --exception           do not catch exceptions (for debugging).
