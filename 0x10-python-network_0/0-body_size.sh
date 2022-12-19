#!/bin/bash
# takes in a URL, sends a request to that URL, displays the size of the body
curl -s -w "%{download_size}" "$1"
