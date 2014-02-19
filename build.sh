#!/usr/bin/env bash

ROOT='pymp'

lint() {
    flake8 $ROOT
    if [ $? -ne 0 ]
    then
        exit $?
    fi
    echo "Lint passed!"
}

unittest() {
    python -m unittest discover -s $ROOT -p '_*_test.py'
    if [ $? -ne 0 ]
    then
        exit $?
    fi
    echo "Unittest passed!"
}

dev_install() {
    pip install -r dev-requirements.pip
    if [ $? -ne 0 ]
    then
        exit $?
    fi
    python setup.py develop
    if [ $? -ne 0 ]
    then
        exit $?
    fi
    echo "Development install passed!"
}

dev_install
lint
unittest
echo "Build passed!"
