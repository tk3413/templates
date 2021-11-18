#!/bin/bash

black src/ && black e2e/

pylint src/ && pylint e2e/
