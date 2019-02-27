#!/usr/bin/env bash
mkdir test
touch test/1 test/2 test/3 test/4
mkdir test/test1
touch test/test1/ha test/test1/he test/test1/hi
echo -n "abcdef" > test/test1/ha
echo -n "123456" > test/test1/hi
echo -n "abcdef" > test/1
echo -n "123456" > test/2
echo -n "123456" > test/3
