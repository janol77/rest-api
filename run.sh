#!/bin/bash
find . -name "*.pyc" -exec rm -rf {} \;
clear
python -m app.server
