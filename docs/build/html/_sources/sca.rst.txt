Working with SCA
================

.. _sca:

:ref:`TRACO <intro>` provides modification of intensities of *SCA* files. Various programs produce different headers of the *SCA* files. Therefore, **it is necessary to specify how many initial lines belong to the header**.

The *original_file.sca* starts with following lines:

.. code-block:: console

       1
    -987
       83.500    96.740    57.970    90.000    90.000    90.000 c 2 2 21
      0   0   2   155.1     3.7
      0   0   3    -0.0     0.1
      0   0   4  2852.9    56.1
      0   0   5    -0.1     0.2
      0   0   6   531.2    11.3
      0   0   7     0.5     0.3
      0   0   8   384.1     8.5

The first three lines is header information. They must be ommited (ignored) this way:

.. code-block:: console

   python3 traco.py -o new_file.sca --sca original_file.sca --sca_ignore 3 --k1 0.09 --fc1 0.4 0.3 0.0 --k2 0.13 --fc2 ...
   
The *new_file.sca* contains corrected intensities that can be further processed with standard tools. **Please, archive the *original_file.sca* file!**
