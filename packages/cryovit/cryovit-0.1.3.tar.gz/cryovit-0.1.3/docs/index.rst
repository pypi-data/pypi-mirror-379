.. CryoViT documentation master file, created by
   sphinx-quickstart on Tue Sep 16 17:33:10 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CryoViT Documentation
=================================================

Welcome to the CryoViT documentation!

CryoViT is a deep learning library for automated segmentation of Cryo-ET data.
It provides both a command line interface (CLI)
and a `napari`_ plugin for easy use,
as well as tools for training and evaluating custom models.

.. _napari: https://napari.org/


More details can be found in the `preprint`_, and
you can check out the `source code`_ for implementation details.

.. _preprint: https://www.biorxiv.org/content/10.1101/2024.06.26.600701v1
.. _source code: https://github.com/VivianDLi/CryoVIT

.. hint::
   - If you already have a dataset, and just want to get it segmented using one of the provided pre-trained models, check out the :ref:`quick start guide <quick start guide>`.

   - If you are new to CryoViT and want to train your own segmentation model, check out the :ref:`user guide <user guide>`.

   - For more information on running experiments like those shown in the CryoViT paper, check out the `GitHub repository`_ for example configuration files and instructions.

   - If you run into any issues, check out :ref:`the help section <debugging issues>` to see if your issue has already been addressed.

.. _GitHub repository: https://github.com/VivianDLi/CryoVIT

=================================================
Getting Started
=================================================

These sections cover the basics of getting started with CryoViT,
including installation instructions for use and development,
setting up dependencies like :ref:`napari <setting up napari>`,
and a quick start guide to training and using your first model.

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   usage/installation
   napari/installation
   usage/quickstart

=================================================
User Guide
=================================================

These sections go over the basic workflow of using CryoViT,
from preparing your dataset for training or inference,
to running commands using either the CLI or napari plugin.

.. toctree::
   :name: userguide
   :maxdepth: 2
   :caption: User Guide

   usage/dataset
   usage/commands
   napari/plugin

..  toctree::
   :caption: Help
   :hidden:

   development/debugging

=================================================
Reference
=================================================

These sections contain the API reference for CryoViT,
for those seeking to expand or customize the library, or simply to dive deeper.

.. autosummary::
   :toctree: _modules
   :caption: API
   :recursive:

   cryovit.run
   cryovit.models
   cryovit.datasets
   cryovit.datamodules

   cryovit.types
   cryovit.config
   cryovit.utils
