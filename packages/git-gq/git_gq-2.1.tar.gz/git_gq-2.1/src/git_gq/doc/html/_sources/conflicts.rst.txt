Conflicts and conflict resolution
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
  
      printf("number of arguments: %d\n", argc);
      printf("program name: %s\n", argv[0]);
      for(i=1; i<argc; i++)
        printf("arg no %2d: %s\n", i, argv[i]);
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
   
  -    printf("number of arguments: %d\n", argc);
       printf("program name: %s\n", argv[0]);
  +    /* iterate over all command line arguments: */
       for(i=1; i<argc; i++)
         printf("arg no %2d: %s\n", i, argv[i]);
       return 0;

In our example here, while the patch was moved to the patch queue, this line::

  printf("number of arguments: %d\n", argc);

had been changed to::

  printf("My number of arguments: %d\n", argc);

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
