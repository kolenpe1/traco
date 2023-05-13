Working with MTZ files
======================

.. _mtz:

Traco allows modification of :ref:`intensities <intensities>` or :ref:`structure factors <structure_factors>`.

Work with MTZ files requires specification of labels used. Traco does not fill the original values with new calculated values. Instead, it adds two new columns (including sigmas) with new appendix (*e.g.* FP_NEW).


.. _intensities:

Intensities
-----------

*Example:*

.. code-block:: console

   python3 traco.py -o new_file.mtz --mtz_I file_with_intensities.mtz --I_label I_cryst --SIGI_label SIGI_cryst --k1 0.09 --fc1 0.4 0.3 0.0 --k2 0.13 --fc2 ...


The *new_file.mtz* file will contain all original information, but also new columns *I_label_new* and *SIGI_label_new*. These are to be used in *CTRUNCATE* or in the refinement.


.. _structure_factors:

Structure factors
-----------------

*Example:*

.. code-block:: console

   python3 traco.py -o new_file.mtz --mtz_F file_with_intensities.mtz --F_label F_cryst --SIGF_label SIGF_cryst --k1 0.09 --fc1 0.4 0.3 0.0 --k2 0.13 --fc2 ...


As previously, the *new_file.mtz* file will contain all original information, but also new columns *F_label_new* and *SIGF_label_new*. These are to be used in the refinement.

