Implementation
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

patch files '\*.patch'
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
   
  -    printf("number of arguments: %d\n", argc);
       printf("program name: %s\n", argv[0]);
  +    /* iterate over all command line arguments: */
       for(i=1; i<argc; i++)
         printf("arg no %2d: %s\n", i, argv[i]);
       return 0;
  -- 
  2.49.0

applied
:::::::

Directory 'applied' is created by ``git gq backup``. It contains the *applied*
patches from the time this command is issued. Note that files in this directory
are not changed by ``git gq push`` or ``git gq pop``, only by ``git gq backup``.
