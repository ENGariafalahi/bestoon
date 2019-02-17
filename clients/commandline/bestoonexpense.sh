#!/bin/bash

source configure.sh

curl --data "token=$TOKEN&amount=$1&text=$2" $BASE_URL/submit/expense/
