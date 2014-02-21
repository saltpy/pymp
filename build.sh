#!/usr/bin/env bash

ROOT='pymp'
VIRTUALENV_WRAPPER='/usr/local/bin/virtualenvwrapper.sh'

lint() {
    flake8 $ROOT || exit $?
    echo "Lint passed!"
}

unittest() {
    python -m unittest discover -s $ROOT -p '_*_test.py' || exit $?
    echo "Unittest passed!"
}

dev_install() {
    pip install -r dev-requirements.pip || exit $?
    python setup.py develop || exit $?
    echo "Development install passed!"
}

resolve_virtualenv() {
    if [ "$VIRTUAL_ENV" != "$WORKON_HOME/$ROOT" ]
    then
        . $VIRTUALENV_WRAPPER || exit $?
        workon $ROOT || mkvirtualenv $ROOT || exit $?
    fi
    echo "Virtualenv resolution passed!"
}

resolve_virtualenv
dev_install
lint
unittest
echo "Build passed!"
echo "Everything installed into $WORKON_HOME/$ROOT"
