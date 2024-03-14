# Software Configuration Management
## What is software configuration management and why should I care?
Well what's better than the [Wikipedia article on Software Configuration Managemnt](https://en.wikipedia.org/wiki/Software_configuration_management) for a starting place.

- _Software configuration management (SCM) practices include revision control and the establishment of baselines. If something goes wrong, SCM can determine what was changed and who changed it. If a configuration is working well, SCM can determine how to replicate it across many hosts._

The reasons for using a SCM system include
  - Historical change log to see when a change was made and by whom
  - Automatically distributing changes across multiple machines with ease
  - Enabling multiple developers to work on the same suite of code simultaneously without creating errors and/or collisions.
  - Creating multiple copies of the code across multiple machines for secure backup
  - Fostering collaboration or new projects from the code
  - Additoinal tools from the SCM software to help manage code checking before inserting into the current working version
  - Bug tracking at the location of the code. This can help track what needs to be worked on and by who
  
 ## Types of software configuration management software
 There have been (and currently are) many different types of software for SCM. A few older and current systems include
   - Revision Control System (RCS)
   - Concurrent Versions System (CVS)
   - Subversion (SVN)
   - Mercurial
   - Bazaar
   - Git (GIT)
   
These all perform the same basic function but with better tools and methods as new systems are developed. People have a tendency to be passionate about the one they like the most. (I suggest not getting into that argument.) This tutorial will focus on one, Git, because it has become very popular and is widely used in the atmospheric sciences.

# Git specific information
## At the local directory level
Git is software running on the computer that will track changes through the command line or a GUI interface. First, we need to have Git installed.
```
> which git
/usr/bin/git
```
Like most command line programs, there is a help menu. You may find this helpful or you may prefer to use web references.
```
git --help
> git --help
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index
   
...
```
To create a new Git repository, _cd_ into the top level directory and type:

```
> git init
Initialized empty Git repository in ~/testing/.git/
```

This will add a new hidden folder called _.git_ . The existance of this folder and the subsequent files in that folder make the directory a Git repository (or project). If we wanted to remove the Git tracking of this folder we could delete the folder and the Git tracking is removed along with all the history of that Git repository.

Now that we have a directory under SCM, we can use Git to also retrieve information about the repository.
```
> git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```
At this point we have an empty repository. We can create new files and folders that will exist in the directory but will not be part of the Git repository until we tell it to add those fles.

```
> touch new_file.py
> git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	new_file.py
```

This file exists in the directory but is not part of the Git repository. To add it to the repository we need to add it to the repository listing. After adding, we can check the status of the repository.
```
> git add new_file.py 
> git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   new_file.py
```

To make the changes part of the history of the Git repository we need to commit the changes. After it has been committed the file is tracked in the Git repository. Any time that file is changed the repository will know what changed, when, and by whom.
```
> git commit new_file.py -m 'Adding a new file to repository.'
[master (root-commit) cff5745] Adding a new file to repository.
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 new_file.py
> git status
On branch master
nothing to commit, working tree clean
```

Now when we make a change to the file, Git will detect the file has changed and can tell us which files have changed since last committed.
```
> echo "A line in the file" >> new_file.py 
> git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   new_file.py
```
To commit the file to Git with the change, we perform the same steps as initially adding the file. This file now has two versions, the initial commit when added to the Git repository and the current version with the changes. It is generally agreed upon to make frequent commits to the files as you develop vs. one large commit. But styles differ. There is no limit to the number of commits nor the size of the commit.
```
> git commit new_file.py -m 'Adding some changes to the file.'
[master f88c322] Adding some changes to the file.
 1 file changed, 1 insertion(+)
```

## Why will using Git help?
To understand why using Git will help with your software development (or really any text file development) we need some use cases:

### Reverting changes to the version in the Git repository
We can make some quick changes to a file to do some testing for debugging some code. For example, we can make a bunch of changes and run the code looking for print statements or changes. But during the process we discover the error is not in the file _new_file.py_ so we need that file to go back to the original state that we know works. We can select undo with our text editor until we get the start of the editing but that may not always work. Or we can try to get things back to where we remember them, but let's be honest how good is your memory? The better thing is to let software do it for you.
```
> echo "Making some changes to new_file.py" > new_file.py
> echo "And more changes" >> new_file.py
> echo "And more changes..." >> new_file.py

> git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   new_file.py
```

Git will tell us where the changes are in the file using the _diff_ command

```
> git diff new_file.py 
diff --git a/new_file.py b/new_file.py
index 16100d2..0b57a44 100644
--- a/new_file.py
+++ b/new_file.py
@@ -1 +1,3 @@
-A line in the file
+Making some changes to new_file.py
+And more changes
+And more changes...
```
Git knows the file was changed, what characters, and where in the file the changes occurred. Here we can see a line was removed (the - character means missing) and three new lines were added (the + character means added). To revert the file back to the original version we use the checkout command.
```
> git checkout new_file.py 
> cat new_file.py
A line in the file
```
We can now see the file is back to the original state.

### Seeing the metadata about the file changes to see who and when a file changes
What if we see something is no longer working and don't understand why things stopped working at Wed Feb 26 15:00:0 2020
```
> git log
commit f88c322506cf19b03665bb90c9e8e333e934f05d (HEAD -> master)
Author: Kenneth Kehoe <kkehoe@ou.edu>
Date:   Wed Feb 26 14:42:01 2020 -0700

    Adding some changes to the file.

commit cff57450877744b5bc195ef68cbda9138c1d58c0
Author: Kenneth Kehoe <kkehoe@ou.edu>
Date:   Wed Feb 26 14:29:28 2020 -0700

    Adding a new file to repository.
```
According to the log the file was updated by Kenneth Kehoe at Wed Feb 26 14:42:01 2020 -0700. So the next time the file was run from a scheduler at 15:00:00, it failed because of the change. For a single file this is a funny example but when there are 10's or 100's of files this can be a life saver.

### What if we need to make a quick change to a file to fix a problem when we are in the middle of a big overhaul of the code!
It happens. We decided we needed to make a lot of changes to the code and then something breaks and we need to get one line of code fixed fast. But we have all these changes to the code. Do we throw them all away with a checkout command and make the small change to get that fixed now because the gov. agency is freeking out! No, we can store our current changes and get back to the original quickly.
```
> echo 'Some changes to new_file.py' >> new_file.py
> echo "Stuff in a second file" > second_file.py
> echo "Stuff in a thrid file" > third_file.py
> git add second_file.py add third_file.py new_file.py
> git status
> git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   new_file.py
	new file:   second_file.py
	new file:   third_file.py
```
Now if we needed to revert the changes to new_file.py, we will lose all our changes and have to put them back in later, in addition to the fast fix we need to do right away. Instead we can use _stash_ to hid our current changes.
```
> git stash
Saved working directory and index state WIP on master: f88c322 Adding some changes to the file.
> git status
On branch master
nothing to commit, working tree clean

> echo 'Our fast update to new_file.py' >> new_file.py
> cat new_file.py 
A line in the file
Our fast update to new_file.py

> git commit new_file.py -m 'Fast fix for issue.'
```

Then we can pull back our other changes with the _stash_ command again.
```
> git stash pop
> get status
```
You will see we have caused a conflict between the two versions of new_file.py. We will need to manually edit that file to fix the conflict, but Git will give us some hint on where the issue resides. So you can edit the file making it correct with the fast fix in the new code and then add it back into the workflow.
```
> vim new_file.py
> git add new_file.py
> cat new_file.py 
A line in the file
Our fast update to new_file.py
Some changes to new_file.py
> git add new_file.py
> git commit -m 'A big update that fixes the too many cats problem'
```
This is just an example; it's actually not the best way to solve this problem. That is with branching, but we will discuss that next as it is a bit more complicated.

