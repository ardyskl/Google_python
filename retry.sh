#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 500 ]; do
  sleep $n
  ((n=n+1))
  echo "Retry #$n"
done;
