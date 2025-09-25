
Install ANUGA for Developers
----------------------------

If you want to use the very latest version of ANUGA (or to develop ANUGA code) then you need
to download the `anuga_core` repository from `github` and then `pip` install 
ANUGA from the source. These steps will require that the following package `git` is installed.


The process involves downloading the `anuga_core` repository from `github` and then running the `install_miniforge.sh` 
(or `install_miniforge_windows.bat` on windows) script from the `anuga_core/tools` directory. 
This will install `Miniforge` (if not already installed) and then create a `conda` environment with the required dependencies 
and finally `pip` install ANUGA in editable mode via the `-e` option of the `pip install` command.

Here are the details.

Download ANUGA from `github`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We need to download (clone) the ANUGA source code from `github`

.. code-block:: bash

    git clone https://github.com/anuga-community/anuga_core.git

This creates a directory `anuga_core`.

.. note::

    If you want to also contribute to the code base, you must have a GitHub 
    account and setup authentication from your developer workstation to GitHub 
    as per these instructions:  https://docs.github.com/en/authentication/managing-commit-signature-verification. 
    The command to clone ANUGA as a developer is then 

    .. code-block:: bash

        git clone git@github.com:anuga-community/anuga_core.git

Install ANUGA using Script
~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have a scripts in the `anuga_core/tools` directory that will install `Miniforge` 
and ANUGA and its dependencies.

Simply run the following command from the `anuga_core` directory:

.. code-block:: bash

    bash tools/install_miniforge.sh

or on windows run the script:

.. code-block:: bash

    call tools\\install_miniforge_windows.bat

This will create a `conda` python 3.12 environment `anuga_env_3.12` and install ANUGA 
and its dependencies.

.. note::

    If you want to install ANUGA for a different version of python, you can set the PY 
    environment variable when running the `install_miniforge.sh` as follows:
    
    
    .. code-block:: bash

      export PY=3.11; bash tools/install_miniforge.sh

    or for windows:

    .. code-block:: bash

      set PY=3.11 && call tools\\install_miniforge_windows.bat
    
    This will install ANUGA for python 3.11. 

.. note::

    The install scripts essentially does the following:

    1. Downloads and Installs `Miniforge` if not already installed.
    2. Creates a `conda` environment with the required dependencies for ANUGA (including required compilers on linux, windows and macos).
    3. Installs ANUGA in editable mode via `pip install --no-build-isolation -e .`

    For instance for python 3.12 the script  essentially does the following (without error checking):

    .. code-block:: bash

      wget -O "$HOME/Miniforge3.sh" "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
      bash "$HOME/Miniforge3.sh" -b -p "$HOME/miniforge3"
      cd anuga_core
      conda env create -n anuga_env_3.12 -f environments/environment_3.12.yml
      conda activate anuga_env_3.12
      conda install compilers
      pip install --no-build-isolation -e .


.. note::

    A compiler is needed to complete the `pip install`. 
    You can use the system compilers or use `conda` to install compilers as such:

    For linux:

    .. code-block:: bash

        conda install compilers

    or for win32:

    .. code-block:: bash

        conda install libpython gcc_win-64 gxx_win-64

    or for macOS:

    .. code-block:: bash

        conda install cxx-compiler llvm-openmp

    Once you have installed the compilers you can run the `pip install` command
    to install ANUGA.

    .. code-block:: bash

        pip install --no-build-isolation -e .

    The `--no-build-isolation` option is needed to ensure that the dependencies (in particular the compilers)
    installed in the `conda` environment are used during the build process.

Testing the installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Once the installation is complete you can activate the `anuga_env_3.12` environment
and run the unit tests to check that everything is working. 

Test the installation.

.. code-block:: bash

    cd sandpit
    conda activate anuga_env_3.12   
    pytest --pyargs anuga

ANUGA also comes with a validation test suite which verifies the correctness of 
real life hydraulic scenarios. You can run them as follows:

.. code-block:: bash

    cd validation_tests 
    python run_auto_validation_tests.py

Using the installation
~~~~~~~~~~~~~~~~~~~~~~

You can now use ANUGA by activating the `anuga_env_3.12` environment and then running your python scripts
that use ANUGA.

.. code-block:: bash

    conda activate anuga_env_3.12
    python my_anuga_script.py

If you have a machine with multiple cores you might want to run your anuga scripts using multiple threads. For instance 4 threads.
You can set the environment variable `OMP_NUM_THREADS=4`, as such:

.. code-block:: bash

    conda activate anuga_env_3.12
    export OMP_NUM_THREADS=4
    python my_anuga_script.py


Updating
~~~~~~~~

From time to time you might like to update your version of anuga to the latest version on 
github. You can do this by going to the `anuga_core` directory and `pulling` the latest
version and then reinstalling via the following commands:
 
.. code-block:: bash

  conda activate anuga_env_3.12
  cd anuga_core
  git pull
  pip install --no-build-isolation -editable .

And finally check the new installation by running the unit tests via:

.. code-block:: bash
    
    cd sandpit
    pytest -q --pyargs anuga

 


