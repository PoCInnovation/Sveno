#!/bin/bash
python3 main.py ../tests/react ../tests/svelte/src && cd ../tests/svelte && npm run test && cd -