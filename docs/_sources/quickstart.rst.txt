Quickstart
==========

This page provides a minimal guide to downloading and running **FEDSRT**.
For most users, the recommended way to get started is to **clone the GitHub repository**
and follow the end-to-end tutorial notebook.

Overview
--------

**FEDSRT** is a federated learning framework for spatial transcriptomics that enables
joint representation learning across multiple datasets or institutions **without sharing
raw expression matrices**.

The repository includes:

- the core FEDSRT implementation,
- configuration files with all model and training parameters,
- an end-to-end tutorial notebook using the DLPFC dataset, and
- scripts for visualization, clustering, and privacy analysis.

All components are designed to be reproducible and easy to modify.

---

Download the repository
-----------------------

Clone the full repository from GitHub:

.. code-block:: bash

   git clone https://github.com/<your-username>/fedsrt.git
   cd fedsrt

This will download **all code, documentation, and tutorial notebooks** required to run FEDSRT.

---

Set up the Python environment
-----------------------------

We recommend using a clean virtual environment or Conda environment.

Using ``venv``:

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate    # macOS / Linux
   # venv\Scripts\activate     # Windows

Install the required dependencies:

.. code-block:: bash

   pip install -r requirements.txt

The main dependencies include PyTorch, NumPy, Scanpy, AnnData, and standard scientific
Python packages.

---

Configuration and parameters
----------------------------

All hyperparameters and file paths used in FEDSRT are centralized in:

.. code-block:: text

   parameters.py

This file controls:

- federated learning settings (number of clients, communication rounds),
- model architecture and optimization hyperparameters,
- clustering and evaluation options, and
- dataset and output paths.

Users are encouraged to modify **only** ``parameters.py`` when experimenting with
different configurations.

---

Run the tutorial notebook
-------------------------

The fastest way to understand and use FEDSRT is to run the provided tutorial notebook.

Launch Jupyter:

.. code-block:: bash

   jupyter lab

Then open:

.. code-block:: text

   notebooks/tutorial_only_process.ipynb

This notebook walks through:

1. loading and preprocessing spatial transcriptomics data,
2. federated training of the FEDSRT model,
3. visualization of learned embeddings and spatial clusters, and
4. privacy analysis via gradient-based reconstruction attacks.

All figures shown in this documentation are generated from this notebook.

---

Outputs and results
-------------------

By default, FEDSRT saves results to the directory specified in ``parameters.py``,
including:

- low-dimensional embeddings for each client,
- clustering assignments,
- reconstructed gene expression (if enabled), and
- intermediate artifacts used for analysis and visualization.

These outputs can be directly reused for downstream analysis or external plotting.

---

Next steps
----------

- See the **Tutorial** section for a detailed, step-by-step walkthrough.
- Refer to the **Installation** page for advanced setup options.
- Check the source code for customization and extension of the FEDSRT framework.

If you use FEDSRT in your research, please remember to cite the corresponding paper.
