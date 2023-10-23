#!/bin/bash

rm -rf output

pelican content -s pelicanconf.py -t themes/tulpawikia

pelican --listen