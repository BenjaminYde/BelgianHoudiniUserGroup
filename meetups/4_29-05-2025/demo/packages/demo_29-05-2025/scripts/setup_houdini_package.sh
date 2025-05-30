#!/usr/bin/env bash

# global variables
PACKAGE_FOLDER=$(dirname $0)/..

function install_python310()
{
    # check existence of python
    if ! command -v python3.10 >&2; then
        # install it
        sudo add-apt-repository --yes ppa:deadsnakes/ppa
        sudo apt update
        sudo apt -qq install -y python3.10 python3.10-venv python3.10-distutils
        python3.10 --version
    else
        echo Python already exists!
    fi
}

function install_virtual_environment()
{
    PYTHON_FOLDER=$PACKAGE_FOLDER/python
    VENV_FOLDER=$PYTHON_FOLDER/.venv

    # check existence of venv folder
    if [ ! -f $VENV_FOLDER ]; then
        # create venv
        cd $PYTHON_FOLDER
        python3.10 -m venv $VENV_FOLDER
        source $VENV_FOLDER/bin/activate
        # install python packages
        pip install -r ./requirements.txt 
    fi
}

function boostrap_houdini_packages()
{   
    # create symbolic link from package folder to houdini packages folder
    PACKAGE_NAME=demo_29-05-2025
    HOUDINI_VERSION=20.5
    FROM=$(realpath $PACKAGE_FOLDER)
    TO=$HOME/houdini$HOUDINI_VERSION/packages/$PACKAGE_NAME

    ## remove existing    
    rm -rf $TO
    rm -rf $TO.json
    
    ## create new symbolic links
    ln -s $FROM $TO
    ln -s $FROM.json $TO.json
}

echo "🚀 Installing Python 3.10..."
install_python310
echo -e "🚀 Done!\n"

echo "🚀 Installing Virtual Environment..."
install_virtual_environment
echo -e "🚀 Done!\n"

echo "🚀 Boostrap Houdini Tools..."
boostrap_houdini_packages
echo -e "🚀 Done!\n"