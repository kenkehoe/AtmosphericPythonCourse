# Conda
[Conda](https://docs.conda.io/en/latest/) is an open-source package manager and enviornment management tool. Conda as a package manager helps you find and install packages, and allows for creation of independent "virtual" enviornments. It is not Python specific, but works very well with Python.

First install the Conda software: [Link](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) This should install somewhere in your home directory structure, for example /Users/<username>/miniconda3/condabin/conda on a Mac.

Second we need to create a new environment to house the additional libraries we will use. By creating a new enviornment we can separate our development work from other work by choosing what version of Python and the libraries we want to use for each project. Some project could require different versions. Because we would prefer to not type out all the library names (and version numbers if desired) we can simply enter them from the environment.yml file.

Now we use Conda to create an environment file from the environment.yml file listing the desired libraries

`conda env create -f environment.yml`

Notice how there are lot of other librareis downloaded and installed that we did not list in our environment file. That is because Conda konws what other librareis are needed to make the libraries we list in enviornment.yml work. It will install those too so we don't need to list them.
After Conda creates the enviornment we can see what environments are available to use to use

`conda env list`

We can now start using the envornment we created

`conda activate AtmPyCourse`

Notece how the command line prompt starts with (AtmPyCourse) indicating what environment we are in.
We can leave or switch to another environment.

`conda deactivate`
