#!/usr/bin/env bash

for file in schemas/NFSe/*
do
  module_name=$(echo $file | tr "/" "\n" | tail -n1)
  xsdata generate schemas/NFSe/"$module_name" --package nfselib."${module_name,,}"
done