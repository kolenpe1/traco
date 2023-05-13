Working with HKL
================

.. _xds_files:

:ref:`TRACO <intro>` provides modification of intensities of *XDS_ASCII.HKL* file from the `XDS <https://xds.mr.mpg.de/>`_. 


*Example:*

.. code-block:: console

   python3 traco.py -o new_file.HKL --HKL XDS_ASCII.HKL --k1 0.09 --fc1 0.4 0.3 0.0 --k2 0.13 --fc2 ...
   
The *new_file.HKL* contains corrected intensities that can be further processed with standard tools like `AIMLESS <https://www.ccp4.ac.uk/html/aimless.html>`_ or any other software. **Please, archive the *XDS_ASCII.HKL* file!**
