#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o /tmp/response.tmp "$1" && [ $(curl -s -o /tmp/response.tmp -w "%{http_code}" "$1") -eq 200 ] && cat /tmp/response.tmp
