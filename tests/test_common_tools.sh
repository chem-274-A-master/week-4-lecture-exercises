#!/bin/bash

set -eu

THIS_DIR="$(dirname $0)"
TOP_DIR="$(dirname ${THIS_DIR})"

MAIN_DIR="${TOP_DIR}/$1"
MAIN_FILE="main.sh"
REF_FILE="${THIS_DIR}/$1.output"
TEST_FILE="${TOP_DIR}/$1.test"

cd "${MAIN_DIR}"
bash "${MAIN_FILE}" | sort > "../${TEST_FILE}"
cd ../

diff "${TEST_FILE}" "${REF_FILE}"
