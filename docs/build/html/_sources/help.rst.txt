Help
====

.. _help:



.. code-block:: console
   
   python3 traco.py --help
   
   ####################################################
   # Correction for multi-lattice translocation defects
   ####################################################

   usage: TRACO [-h] [-c CELL [CELL ...]] [--mtz_I MTZ_I] [--I_label I_LABEL] [--SIGI_label SIGI_LABEL] [--mtz_F MTZ_F] [--F_label F_LABEL]
             [--SIGF_label SIGF_LABEL] [--hkl HKL] [--HKL HKL] [--sca SCA] [--sca_ignore SCA_IGNORE] [--k1 K1] [--fc1 FC1 [FC1 ...]]
             [--k2 K2] [--fc2 FC2 [FC2 ...]] [--k3 K3] [--fc3 FC3 [FC3 ...]] [--k4 K4] [--fc4 FC4 [FC4 ...]] [--k5 K5]
             [--fc5 FC5 [FC5 ...]] [--force] [-o OUTPUT_FILE]

   options:
     -h, --help            show this help message and exit
     -c CELL [CELL ...], --cell CELL [CELL ...]
                        unit cell parameters
     --mtz_I MTZ_I         input MTZ file with intensities
     --I_label I_LABEL     label for intensities
     --SIGI_label SIGI_LABEL
                        label for sigmas
     --mtz_F MTZ_F         input MTZ file with structure factors
     --F_label F_LABEL     label for structure factors
     --SIGF_label SIGF_LABEL
                           label for sigmas
     --hkl HKL             input file with SHELX-like structure factors
     --HKL HKL             XDS_ASCII.HKL input file from XDS
     --sca SCA             input SCA file with intensities
    --sca_ignore SCA_IGNORE
                           how many initial lines should be ignored (do not contain data)
     --k1 K1               fraction of the 1st translocation disorder
     --fc1 FC1 [FC1 ...]   fractional coordinates of the 1st translocation disorder
     --k2 K2               fraction of the 2nd translocation disorder
     --fc2 FC2 [FC2 ...]   fractional coordinates of the 2nd translocation disorder
     --k3 K3               fraction of the 3rd translocation disorder
     --fc3 FC3 [FC3 ...]   fractional coordinates of the 3rd translocation disorder
     --k4 K4               fraction of the 4th translocation disorder
     --fc4 FC4 [FC4 ...]   fractional coordinates of the 4th translocation disorder
     --k5 K5               fraction of the 5th translocation disorder
     --fc5 FC5 [FC5 ...]   fractional coordinates of the 5th translocation disorder
     --force, -f           forcing output file
     -o OUTPUT_FILE, --output_file OUTPUT_FILE
                           defines the output file

