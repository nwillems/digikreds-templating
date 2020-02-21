#!/bin/bash

docker run -it --rm \
    -v ${PWD}:/data \
    nwillems/digikreds-templater \
    --template ./template.docx Deltager+Gruppe-Data.csv output/
