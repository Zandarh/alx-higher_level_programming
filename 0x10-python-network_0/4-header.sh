#!/bin/bash
# takes in a URL as an argument, sends a GET request
curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
