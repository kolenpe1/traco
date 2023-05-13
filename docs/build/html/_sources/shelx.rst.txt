Working with hkl
================

.. _hkl:

*hkl* files suitable for refinement with *SHELX* contain structure factors. They cannot be mixed up with :ref:`HKL files from XDS <xds_files>`.

*Example:*

.. code-block:: console

   python3 traco.py -o new_file.hkl --hkl original_file.hkl --k1 0.09 --fc1 0.4 0.3 0.0 --k2 0.13 --fc2 ...
   
The *new_file.hkl* contains corrected structure factors only. **Please, archive the original_file.hkl!**
