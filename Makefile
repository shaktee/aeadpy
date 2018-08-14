# Makefile for AES-GCM testbench
# Copyright (C) 2018 Rajesh Vaidheeswarrana

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
SCRIPT := aesgcm2.py
TEST := ipsec_testcases
PYTHONPATH = $(shell echo build/lib*)

all: run

build:
	python setup.py build
clean:
	rm -rf build *~ core* *pyc

run: build
	PYTHONPATH=$(PYTHONPATH) python $(SCRIPT) -t $(TEST) $(ARGS)

debug:
	PYTHONPATH=$(PYTHONPATH) gdb python core

shell:
	PYTHONPATH=$(PYTHONPATH) python

help:
	@echo Make targets are:
	@echo build - build the libraries
	@echo run - run the testcase specified by TEST variable \(default: $(TEST)\)
	@echo clean - clean the area
	@echo debug - debug a core file
	@echo shell - drop into a python shell
