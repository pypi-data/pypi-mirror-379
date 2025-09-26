TOFF
=======
|logo|

.. list-table::
    :widths: 12 35

    * - **Documentation**
      - |docs|
    * - **Tutorials**
      - |binder|
    * - **CI/CD**
      - |tests| |codecov| |codacy|
    * - **Build**
      - |pypi-version|
    * - **Source Code**
      - |github|
    * - **Python Versions**
      - |pyversions|
    * - **Dependencies**
      - |rdkit| |OpenMM| |OpenFF| |ParmEd|
    * - **License**
      - |license|
    * - **Downloads**
      - |downloads|

Description
-----------

**TOFF** (Topologies from Open Force Fields) is a Python package initially developed to get topologies from the OpenFF initiative. Now it is possible to get GAFF and Espaloma topological parameters as well. It was strongly inspired in this `Aniket's script <https://github.com/aniketsh/OpenFF/blob/82a2b5803e36b72f3525e3b8631cf256fbd8e35a/openff_topology.py>`__.

Since version **0.1.0** it is also possible to get `GAFF <https://ambermd.org/antechamber/gaff.html>`__ and
`Espaloma <https://docs.espaloma.org/en/latest/>`__.

You can try it out prior to any installation on `Binder <https://mybinder.org/v2/gh/ale94mleon/TOFF/HEAD?labpath=%2Fdocs%2Fnotebooks%2F>`__.

Documentation
-------------

The installation instructions, documentation and tutorials can be found online on `ReadTheDocs <https://toff.readthedocs.io/en/latest/>`_.

Issues
------

If you have found a bug, please open an issue on the `GitHub Issues <https://github.com/ale94mleon/TOFF/issues>`_.

Discussion
----------

If you have questions on how to use **TOFF**, or if you want to give feedback or share ideas and new features, please head to the `GitHub Discussions <https://github.com/ale94mleon/TOFF/discussions>`_.

Citing **TOFF**
------------------

Please refer to the `citation page <https://TOFF.readthedocs.io/en/latest/source/citations.html>`__ on the documentation.

Funding
-------

This project received funding from `Marie Skłodowska-Curie Actions <https://cordis.europa.eu/project/id/860592>`__. It was developed in the 
`Computational Biophysics Group <https://biophys.uni-saarland.de/>`__ of `Saarland University <https://www.uni-saarland.de/en/home.html>`__.

..  |logo|  image:: https://github.com/ale94mleon/toff/blob/main/docs/source/_static/logo.png?raw=true
    :target: https://github.com/ale94mleon/toff/
    :alt: logo

..  |docs|  image:: https://readthedocs.org/projects/toff/badge/?version=latest
    :target: https://toff.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation

..  |binder| image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/ale94mleon/TOFF/HEAD?labpath=%2Fdocs%2Fnotebooks%2F
    :alt: binder

..  |tests| image:: https://github.com/ale94mleon/TOFF/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/ale94mleon/TOFF/actions/workflows/tests.yml
    :alt: tests

..  |codecov| image::  https://app.codacy.com/project/badge/Coverage/53c53c810b3c4767ab76f5d622ec6aef
    :target: hhttps://app.codacy.com/gh/ale94mleon/TOFF/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage
    :alt: codecov

..  |codacy| image:: https://app.codacy.com/project/badge/Grade/53c53c810b3c4767ab76f5d622ec6aef
    :target: https://app.codacy.com/gh/ale94mleon/TOFF/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade
    :alt: codacy

..  |pypi-version|  image:: https://img.shields.io/pypi/v/TOFF.svg
    :target: https://pypi.python.org/pypi/TOFF/
    :alt: pypi-version

..  |conda|  image:: https://anaconda.org/ale94mleon/TOFF/badges/version.svg
    :target: https://anaconda.org/ale94mleon/TOFF
    :alt: conda

..  |github|    image:: https://badgen.net/badge/icon/github?icon=github&label
    :target: https://github.com/ale94mleon/TOFF
    :alt: GitHub-TOFF

..  |pyversions|    image:: https://img.shields.io/pypi/pyversions/toff.svg
    :target: https://pypi.python.org/pypi/toff/

..  |rdkit| image:: https://img.shields.io/static/v1?label=Powered%20by&message=RDKit&color=3838ff&style=flat&logo=data:image/x-icon;base64,AAABAAEAEBAQAAAAAABoAwAAFgAAACgAAAAQAAAAIAAAAAEAGAAAAAAAAAMAABILAAASCwAAAAAAAAAAAADc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nz/FBT/FBT/FBT/FBT/FBT/FBTc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nz/FBT/PBT/PBT/PBT/PBT/PBT/PBT/FBTc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nz/FBT/PBT/ZGT/ZGT/ZGT/ZGT/ZGT/ZGT/PBT/FBTc3Nzc3Nzc3Nzc3Nzc3Nz/FBT/PBT/ZGT/ZGT/ZGT/ZGT/ZGT/ZGT/ZGT/ZGT/PBT/FBTc3Nzc3Nzc3Nz/FBT/PBT/ZGT/ZGT/ZGT/jIz/jIz/jIz/jIz/ZGT/ZGT/ZGT/PBT/FBTc3Nzc3Nz/FBT/PBT/ZGT/ZGT/jIz/jIz/jIz/jIz/jIz/jIz/ZGT/ZGT/PBT/FBTc3Nzc3Nz/FBT/PBT/ZGT/ZGT/jIz/jIz/tLT/tLT/jIz/jIz/ZGT/ZGT/PBT/FBTc3Nzc3Nz/FBT/PBT/ZGT/ZGT/jIz/jIz/tLT/tLT/jIz/jIz/ZGT/ZGT/PBT/FBTc3Nzc3Nz/FBT/PBT/ZGT/ZGT/jIz/jIz/jIz/jIz/jIz/jIz/ZGT/ZGT/PBT/FBTc3Nzc3Nz/FBT/PBT/ZGT/ZGT/ZGT/jIz/jIz/jIz/jIz/ZGT/ZGT/ZGT/PBT/FBTc3Nzc3Nzc3Nz/FBT/PBT/ZGT/ZGT/ZGT/ZGT/ZGT/ZGT/ZGT/ZGT/PBT/FBTc3Nzc3Nzc3Nzc3Nzc3Nz/FBT/PBT/ZGT/ZGT/ZGT/ZGT/ZGT/ZGT/PBT/FBTc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nz/FBT/PBT/PBT/PBT/PBT/PBT/PBT/FBTc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nz/FBT/FBT/FBT/FBT/FBT/FBTc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nz/////+B////AP///gB///wAP//4AB//+AAf//gAH//4AB//+AAf//gAH//8AD///gB///8A////gf////////
    :target: https://www.rdkit.org/docs/index.html
    :alt: rdkit

..  |OpenMM| image:: https://img.shields.io/static/v1?label=Powered%20by&message=OpenMM&color=6858ff&style=flat
    :target: http://docs.openmm.org/latest/userguide/
    :alt: OpenMM

..  |OpenFF| image:: https://img.shields.io/static/v1?label=Powered%20by&message=OpenFF&color=9438ff&style=flat
    :target: https://docs.openforcefield.org/projects/toolkit/en/latest/
    :alt: OpenFF

..  |ParmEd| image:: https://img.shields.io/static/v1?label=Powered%20by&message=ParmEd&color=2038ff&style=flat
    :target: https://parmed.github.io/ParmEd/html/'
    :alt: ParmEd

..  |license| image:: https://badgen.net/pypi/license/toff/
    :target: https://pypi.python.org/pypi/toff/
    :alt: license

..  |downloads| image:: https://static.pepy.tech/personalized-badge/toff?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads
    :target: https://pepy.tech/project/toff
    :alt: download