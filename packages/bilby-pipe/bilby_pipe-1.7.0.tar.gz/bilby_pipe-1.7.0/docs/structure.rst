=============
Code overview
=============

Most users will only interact with the `command-line executable <user-interface>`_.
In this document, we'll give a brief overview of how these are used internally
to help developers orient themselves with the project.

Python Modules
--------------

At the top-level, the :code:`bilby_pipe` python package provides several
sub-modules as visualised here:

.. graphviz::

   digraph {
         "bilby_pipe" -> ".main";
         "bilby_pipe" -> ".data_generation";
         "bilby_pipe" -> ".data_analysis";
         "bilby_pipe" -> ".create_injections";
         "bilby_pipe" -> ".utils";
	 "bilby_pipe" -> ".gracedb";
            }

each submodule (e.g., :code:`bilby_pipe.utils`) serves a different purpose.
On this page, we'll give a short description of the general code structure.
Specific details for different modules can then be found by following the
links in the API reference section.

Workflow
--------

The typical workflow for `bilby_pipe` is that a user calls the
:code:`bilby_pipe` command line tool giving it some "User input". Typically,
this is of the form of an `ini file <ini_file.txt>`_, and any extra command
line arguments. This user input is handled by the `bilby_pipe.main <main.txt>`_
module (which provides the command-line interface). It generates two types of
output, "DAG files" and a "summary webpage" (if requested). I.e., the top-level
workflow looks like this:

.. graphviz::

   digraph {
         rankdir="LR";
         "User input" -> "bilby_pipe.main";
         "bilby_pipe.main" -> "DAG files";
         "bilby_pipe.main" -> "summary webpage";
            }

Depending on the exact type of the job, the DAG may contain a number of jobs.
Typically, there are *generation* and *analysis* jobs. For a simple job, e.g.,
analysing a GraceDB candidate. There may be one generation job (to load the
JSON data from GraceDB, find relevant frame files and make PSDs) and one
analysis job (to run some sampler given some prior etc.). For cases with
multiple components (e.g., create an analysis n injections) things may be
more complicated. The logic for handling all of this is contained within the
`main <main.txt>`_ module.

In the most general case, there will be n parallel jobs with no inter-job
dependencies. Within each of these jobs, there is typically a structure in
the DAG as follows:

.. graphviz::

   digraph {
         rankdir="TD";
         "Data Generation" -> "Data Analysis 1";
         "Data Generation" -> "Data Analysis 2";
         "Data Generation" -> "...";
         "Data Generation" -> "Data Analysis M";
         "Data Analysis 1" -> "post-processing";
         "Data Analysis 2" -> "post-processing";
         "..." -> "post-processing";
         "Data Analysis N" -> "post-processing";
            }

Each Data Analysis job refers to a different way to analyse the same data. For
example, using different samplers, or different subsets of detectors. If there
are M Data Anlaysis jobs and N top-level jobs, there is MN jobs in total.

The "Data Generation" job uses the `bilby_pipe_generation
<data_generation.txt>`_ executable to create all the data which may be
analysed.

The "Data Analysis" jobs uses the `bilby_pipe_analysis
<data_analysis.txt>`_ executable to create all the data which may be
analysed.

For the case of running on GraceDB events, `bilby_pipe` has an additional step
to the typical workflow `bilby_pipe_gracedb <gracedb.txt>`_ executable. For
this case the user can calls :code:`bilby_pipe_gracedb` along with either the
GraceDB ID of the event or a json file containing information on the GraceDB
event. For examples on using `bilby_pipe_gracedb` please see the section
`Running on GraceDB events` under `Examples <examples.txt>`_. 

See the table of contents below for an overview of the API.


Code Format
-----------
To ensure a consistent style across the project, :code:`bilby_pipe` uses two
linting tools: `flake8 <https://pypi.org/project/flake8/>`_ and `black
<https://github.com/ambv/black>`_. Practically speaking, when you submit a
merge request, these commands are run by the CI

.. code-block:: console

   $ black --check bilby_pipe/
   $ flake8 .

which check a number of small stylistic and formatting issues. Often, you will
find the CI fails due to difference between your style and those accepted by
these commands. Usually these can be resolved by simply running

.. code-block:: console

   $ black bilby_pipe/

prior to committing (or run it, add the changes and add another commit). This
will reformat the code in the accepted style. To avoid having to do this, you
can use the `pre-commit hook
<https://github.com/ambv/black#version-control-integration>`_. To use this
feature, run the following commands from the :code:`bilby_pipe` directory:

.. code-block:: console

   $ pip install pre-commit
   $ pre-commit install

For a detailed discussion of why we use :code:`flake8` and :code:`black`, you
be wish to `read this article
<https://www.mattlayman.com/blog/2018/python-code-black/>`_.
