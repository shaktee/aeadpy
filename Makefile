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
SCRIPT := aesgcm.py
EMPTY :=
SPACE := $(EMPTY) $(EMPTY)
TEST := ipsec_testcases mcgrew_testcases
PYTHON := python
all: run

bld:
	$(PYTHON) setup.py build
clean:
	rm -rf build *~ core* *pyc

run: bld
	$(PYTHON) $(SCRIPT) $(ARGS) $(TEST)

debug:
	@echo execute PYTHONPATH=build/lib* gdb $(PYTHON) core

shell:
	@echo execute PYTHONPATH=build/lib* $(PYTHON)

help:
	@echo Make targets are:
	@echo build - build the libraries
	@echo run - run the testcases specified by TEST variable \(default: $(TEST)\)
	@echo clean - clean the area
	@echo debug - debug a core file
	@echo shell - drop into a $(PYTHON) shell
