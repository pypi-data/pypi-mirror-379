============
The ini file
============

The primary user-inputs to :code:`bilby_pipe` is an ini file and optionally
additional command-line arguments. To handle both command line arguments and
ini-files, we use the `ConfigArgParse
<https://pypi.org/project/ConfigArgParse/>`_ python module.

An ini file can contain multiple types of input. In this example, we
demonstrate passing in a float for the :code:`trigger-time` attribute, an integer
for the :code:`duration`, a list for the :code:`detectors`, a boolean for the
:code:`coherence-test`, and a dictionary of :code:`sampler-kwargs`:

.. code-block:: text

    # config.ini
    trigger-time = 1126259462.4
    duration = 4
    detectors = [H1, L1]
    sampler-kwargs = {nlive: 500, n_check_point: 1000}

For dictionaries, the input can be quite loose, for example here we use mixed
colons, equals signs and quotations.

.. code-block:: text

    sampler-kwargs = {nlive: 500, method='rwalk', 'n_check_point' = 1000}

Additional command-line arguments can be given, or those in the ini file
overwritten, for example

.. code-block:: console

   $ bilby_pipe config.ini --duration 8

will overwrite the :code:`duration` argument provided in the ini file.

We can generate an ini file with current documentation and all of the default
options by running

.. code-block:: text

   $ bilby_pipe_write_default_ini default.ini

.. literalinclude:: default.ini

The ini file for GraceDB events can be generated using the command line
program :code:`bilby_pipe_gracedb` with the arguments :code:`--gracedb` for
example, to generate an ini file for the GraceDB event G298936 we use the 
following command,

.. code-block:: text

   $ bilby_pipe_gracedb --gracedb G298936 --output ini

This will produce an ini file, bilby_config.ini, which automatically sets an 
appropriate configuration and is ready for submission.

.. literalinclude:: bilby_config.ini
