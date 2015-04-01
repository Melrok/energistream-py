#!/bin/bash
set -e

# Update system
sudo apt-get update
#Install other dependencies (not sure yet as to why these won't resolve)
sudo apt-get install -y libsm6 libxrender1 libfontconfig1

# Define Miniconda install directory
echo "Working direcotry: $PWD"
if [ $# -eq 0 ]
    then
    echo "No path argument specified, setting install directory as working directory: $PWD."
    #sudo pip install -e .
    #sudo python setup.py install
    proj_dir=$PWD

else
    echo "Path argument specified, installing to: $1"
    #sudo pip install -e $1
    proj_dir=$1
fi

# Setup miniconda
miniconda="Miniconda-3.8.3-Linux-x86_64.sh"
#NOTE: can find most recent version at Miniconda-latest-Linux-x86_64.sh"
cd $proj_dir
PATH_CONDA_SCRIPT="$proj_dir/$miniconda"
echo "Defined miniconda script path: $PATH_CONDA_SCRIPT"

#TODO md5sum on miniconda to prevent incomplete download
if [[ -f "$PATH_CONDA_SCRIPT" ]]; then
  echo "Found existing Miniconda script at: $PATH_CONDA_SCRIPT"
else
  echo "Downloading Miniconda script to: $PATH_CONDA_SCRIPT ..."
  wget http://repo.continuum.io/miniconda/$miniconda
  echo "Downloaded $miniconda!"
  ls -al $PATH_CONDA_SCRIPT
  chmod 755 $PATH_CONDA_SCRIPT
fi

expectedHash="57321cab5bf40433219226412ac35a93"
#expectedHash="efb03496433f1dfab008ef114093b4b2"
md5Output=$(md5sum $miniconda | awk '{print $1}')
if [ "$expectedHash" != "$md5Output" ]; then
    echo "Unexpected md5sum $md5Output for $miniconda"
    exit 1
fi

# Bootstrap installation of miniconda
PATH_CONDA="$proj_dir/miniconda"
if [[ ! -d $PATH_CONDA ]]; then
    # Install Miniconda
    echo "Installing $miniconda to $PATH_CONDA..."
    bash $PATH_CONDA_SCRIPT -b -p $PATH_CONDA -f
    chmod 755 $PATH_CONDA
else
    echo "Existing directory at path: $PATH_CONDA, skipping install!"
fi

# Update PATH and conda...
echo "Setting environment variables..."
PATH_CONDA_BIN="$PATH_CONDA/bin"
export PATH="$PATH_CONDA_BIN:$PATH"
echo "Updated PATH: $PATH"
echo "And also HOME: $HOME"
hash -r
which conda
conda config --set always_yes yes --set changeps1 no
source ~/.bashrc

echo "Updating conda..."
conda update -q conda
# Useful for debugging any issues with conda
conda info -a

# Install dependencies for energiscore via conda
echo "Installing dependencies for EnergiStream-Py..."
deps='pandas requests pip'
conda create -q -n test-env $deps || true
echo "Activating test environment..."
source activate test-env
pip install testfixtures

# Install unittest dependencies
conda install nose coverage mock

# Install documentation build dependencies
sudo apt-get install -y pandoc make
conda install ipython sphinx numpydoc
pip install sphinx_rtd_theme testfixtures mistune

# Install reporting framework dependencies
#sudo apt-get install -y imagemagick git
#conda install ipython-notebook
#git clone -b merge_utility https://github.com/nehalecky/runipy.git || true
#pip install -e runipy/ || true
