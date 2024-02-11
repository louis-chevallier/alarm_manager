SHELL := /usr/bin/bash
export DATE:=$(shell date +%Y-%m-%d_%Hh%Mm%Ss)
export HOST=$(shell hostname)
SHELL=bash
export GITINFO=$(shell git log --pretty=format:"%h - %an, %ar : %s" -1)

start  :
	python server.py

#2>> trace.txt

run :
	date
	source ${HOME}/scripts/.bashrc; spy; python_env; make start
