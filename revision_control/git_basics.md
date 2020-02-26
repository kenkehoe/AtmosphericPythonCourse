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

## At the local directroy level
