#!/bin/bash
# Install python requirements
pip3 install -r ./src/requirements.txt
# Install prettier to get svelte files prettier
npm --prefix src/ install