Contributing
============

This project is still in development, however, contributions are welcome and 
appreciated. Credit will always be given for work done.

Types of contributions
----------------------

Reporting bugs
^^^^^^^^^^^^^^

Report bugs at https://github.com/IainMcl/BoatComp/issues.

If reporting a bug, please include:

* Your Operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix bugs
^^^^^^^^

Any issues found in GitHub issues for anything tagged with "bug", these are open
to anyone who wants to implement, or help implement it.

Implement features
^^^^^^^^^^^^^^^^^^

While in development the main features are those found in the **Aims** of the 
homepage. If there are new features that you think would be useful add a new 
issue with the tag "feature". This will allow others to know what development is 
being carried out to reduce the chance of work duplication.

Any issue tagged as "feature" is open to whoever wants to implement it. If doing
this, have a quick check that it is not already assigned.

Write documentation
^^^^^^^^^^^^^^^^^^^

Documentation contributions are welcome. These current documentation is produced
using `Sphinx <https://www.sphinx-doc.org/en/master/>`_. This includes in-code 
docstrings. If contributing to docstrings, please use the Sphinx docstring 
style guide to ensure consistency project wide. A brief overview for this style
can be found `here <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html>`_.

**Note**: If using the `Python Docstring Generator <https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring>`_
extension for VS Code, the default docstring style is **not** set to Sphinx. To 
change this, set :code:`"autoDocstring.docstringFormat": "sphinx"` setting, 
under File > Preferences > Settings.

Submit feedback
^^^^^^^^^^^^^^^

The best way to send feedback is to file an issue at https://github.com/IainMcl/BoatComp/issues.

If you Are proposing a new feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this as a volunteer-driven project and that contributions are
  welcome.

Getting started
---------------

If you are looking to contribute, here are some setup steps for local 
development.

#. Fork the *boatcomp* repo on GitHub.
#. Clone your fork locally: 

   .. code-block:: bash
   
     $ git clone git@github.com:<your-user-name>/BoatComp.git

#. Set up your virtual environment:

   .. code-block:: bash
   
     $ cd BoatComp
     $ python -m venv ENV # Ensure your environment name (here ENV) is not included in version control.
     $ python setup.py develop

#. Create a branch for local development:
   
   .. code-block:: bash

     $ git checkout -b <your-branch-name>

   Use this branch for development as your :code:`main` branch.

#. Type checking. We are trying to encourage the use of the typing functionality 
   added to python in version 3.9. For this to be checked, run :code:`mypy` 
   checks for all changes.

   .. code-block:: bash

     $ mypy <file-name.py>

   This will identify any untyped, or incorrectly used variables. This is 
   particularly important with function definitions to encourage correct usage.
    

#. When you are done making changes, check that your changes pass tests with 
   :code:`pytest` including different versions of Python using :code:`tox`.

   .. code-block:: bash

     $ pytest
     $ tox

#. Commit and push your changes to GitHub:
   
   .. code-block:: bash

     $ git add .
     $ git commit -m "Short description" -m "Long description"
     $ git push origin <your-branch-name>

#. Submit a pull request through the GitHub website.


Pull request guidelines
-----------------------

Before you submit a pull request, check that it meets these guideline:

#. The pull request should include tests.
#. If the pull request adds functionality, the docs should be updates. Put your
   new functionality into a docstring.
#. Check any other requirements to pass builds.

