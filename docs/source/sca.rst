Working with SCA
================

.. _sca:

:ref:`TRACO <intro>` provides modification of intensities of *SCA* files. Various programs produce different headers of the *SCA* files. Therefore, **it is necessary to specify how many initial lines belong to the header**.

Example 1
---------

The *original_file.sca* starts with following lines:

XXX TAdy bude nejaky ten kod .... XXX

.. code-block:: console

   python3 traco.py -o new_file.sca --sca original_file.sca --sca_ignore 6 --k1 0.09 --fc1 0.4 0.3 0.0 --k2 0.13 --fc2 ...
   
The *new_file.sca* contains corrected intensities that can be further processed with standard tools. **Please, archive the *original_file.sca* file!**


Example 2
---------

The *original_file.sca* starts with following lines:

XXX TAdy bude nejaky ten kod .... XXX

.. code-block:: console

   python3 traco.py -o new_file.sca --sca original_file.sca --sca_ignore 3 --k1 0.09 --fc1 0.4 0.3 0.0 --k2 0.13 --fc2 ...
   
The *new_file.sca* contains corrected intensities that can be further processed with standard tools. **Please, archive the *original_file.sca* file!**
