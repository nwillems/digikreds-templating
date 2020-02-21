#!/bin/bash

docker build -t nwillems/digikreds-templating .

# TODO: Consider adding a git-has tagged edition

docker push nwillems/digikreds-templating
