# Software configuration management
## What is software configuration management and why should I care?
Well what's better than the [Wikipedia article on Software Configuration Managemnt](https://en.wikipedia.org/wiki/Software_configuration_management) for a starting place.

- _Software configuration management (SCM) practices include revision control and the establishment of baselines. If something goes wrong, SCM can determine what was changed and who changed it. If a configuration is working well, SCM can determine how to replicate it across many hosts._

The reasons for using a SCM system include
  - Historical change log to see when a change was made and by whom
  - Automatically distributing changes across multiple machines with ease
  - Enabling multiple developers to work on same suite of code simultaneously without creating errors, collisions.
  - Creating multiple copies of the code across multiple machines for secure backup
  - Fostering collaboriation or new projects from the code
  - Additinal tools from the SCM software to help manage code checking before inserting into the current working version
  - Bug tracking at the location of the code. This can help track what needs to be worked on and by who
  
 ## Types of software configuration management software
 There have been (and curentl are) many different types of software for SCM. A few older and curent systems include
   - Revision Control System (RCS)
   - Concurrent Versions System (CVS)
   - Subversion (SVN)
   - Mercurial
   - Bazaar
   - Git (GIT)
   
These all perform the same basic function but with better tools and methods as new systems are developed. People have a tendency to be pationate about the one they like the most. (I suggest not getting into that argument.) This tutorial will focus on one, Git, because it has become very popular and is widly used in the atmospheric sciences.

# Git specific information
## At the local directroy level
Git is software running on the computer that will track changes through command line or GUI interface. First we need to have Git installed.
```
> which git
/usr/bin/git
```
As like most command line programs there is a help menu. You may find this helpful or you may prefer to use web references.
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
To create a new Git repository _cd_ into the top level directory and type

```
> git init
Initialized empty Git repository in ~/testing/.git/
```

This will add a new hidden folder called _.git_ . The existance of this folder and the subsequent files in that folder make the directory a Git repository (or project). If we wanted to remove the Git tracking of this folder we could delete the folder and the Git tracking is removed along with all the history of that Git repository.

Now that we have a directory under SCM we can use Git to also retrieve informatoin about the repository.
```
> git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```
At this point we have an empty repository. We can create new files and folders that will exist in the directory but will not be part of the Git repository until we tell it add those fles.

```
> touch new_file.py
> git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	new_file.py
```

This file exist in the directory but is not part of the Git repository. To add it to the repository we need to add it to the repository listing. After adding we can check the status of the repository.
```
> git add new_file.py 
> git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   new_file.py
```

To make the changes part of the history of the Git repository we need to commit the changes. After it has been committed the file is tracked in the Git repository. Any time that file is changed the repository will know what changed, when and by whom.
```
> git commit new_file.py -m 'Adding a new file to repository.'
[master (root-commit) cff5745] Adding a new file to repository.
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 new_file.py
> git status
On branch master
nothing to commit, working tree clean
```

Now when we make a change to the file Git will detect the file has changed and can tell us which files have changed since last commited.
```
> echo "A line in the file" >> new_file.py 
> git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   new_file.py
```
To commit the file to Git with the change we perform the same steps as initially adding the file. This file now has two verisions, the inital commit when added to the Git repository and the current version with the changes. It is generlly agreed upon to make frequent commits to the fiels as you develope vs. one large commit. But style differ. There is no limit to the number of commits nor the size of the commit.
```
> git commit new_file.py -m 'Adding some changes to the file.'
[master f88c322] Adding some changes to the file.
 1 file changed, 1 insertion(+)
```

## Why will using Git help?
To understand why using Git will help with your software development (or really any text file development) we need some use cases

### Reverting changes to the version in the Git repository
We can make some quick changes to a file to do some testing for debugging some code. For example we can make a bunch of changes and run the code looking for print statements or changes. But during the process we discover the error is not in the file _new_file.py_ so we need that file to go back to the orginal state that we know works. We can select undo with our text editor until we get the start of the editing but that may not always work. Or we can can try to get things back to where we remember them, but let's be honest how good is your memory? The better thing is to let software do it for you.
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
Git knows the file was changed, what characters and where in the file. Here we can see a line was removed (the - character means missing) and three new lines were added (the + character means added). To revert the file back to the orginal version we use the checkout command.
```
> git checkout new_file.py 
> cat new_file.py
A line in the file
```
We can now see the file is back to the orginal state.



