.. traco documentation master file, created by
   sphinx-quickstart on Sat Apr 15 15:53:25 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation of TRACO
======================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   mtz.rst
   xds.rst
   shelx.rst
   sca.rst
   help.rst

Introduction
------------

.. _intro:

TRACO is a script that helps to deal with multi-lattice translocation
defects. If translocation defects are present, they may affect the quality
of electron density dramatically.

TRACO works with :ref:`MTZ files <mtz>` with intensities or structure factors,
:ref:`HKL files <HKL>` from XDS, :ref:`hkl files <hkl>` for SHELX, and also
with :ref:`SCA files <sca>`.



Example
-------

The very first structure tested with TRACO is (Kristyna et al.).




Help
----

.. code-block:: console

   python3 traco.py --help

More information on :ref:`Help is here <help>`.

