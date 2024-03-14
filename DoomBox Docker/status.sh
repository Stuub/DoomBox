#!/bin/bash
echo "System status:"
date
free -h
echo "Checking disk usage for user-provided path: $1"
du -sh $1
