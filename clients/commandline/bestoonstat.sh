#!/bin/bash

source configure.sh

curl --data "token=$TOKEN" $BASE_URL/q/generalstat/
