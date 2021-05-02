#!/bin/bash
if [ "$0" != 'bash' ];then
echo "Please source this script to set PYTHONPATH."
else
a=$(pwd 2>&1)
echo "Add $a to PYTHONPATH."
PYTHONPATH="$PYTHONPATH:$a"
export PYTHONPATH
fi
cd c-bytearray
python2 setup.py build
cp build/lib.*/c_wildcard.so ../utils/.
rm -rf build
cd ..

