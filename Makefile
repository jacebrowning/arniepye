PROJECT := ArniePye
PACKAGE := arniepye
SOURCES := Makefile setup.py

CACHE := .cache
VIRTUALENV := env
DEPENDS := $(VIRTUALENV)/.depends
EGG_INFO := $(subst -,_,$(PROJECT)).egg-info

ifeq ($(OS),Windows_NT)
VERSION := C:\\Python33\\python.exe
BIN := $(VIRTUALENV)/Scripts
EXE := .exe
OPEN := cmd /c start
else
VERSION := python3
BIN := $(VIRTUALENV)/bin
OPEN := open
endif
MAN := man
SHARE := share

PYTHON := $(BIN)/python$(EXE)
PIP := $(BIN)/pip$(EXE)
RST2HTML := $(BIN)/rst2html.py
PDOC := $(BIN)/pdoc
PEP8 := $(BIN)/pep8$(EXE)
PYLINT := $(BIN)/pylint$(EXE)
NOSE := $(BIN)/nosetests$(EXE)

# Installation ###############################################################

.PHONY: all
all: develop

.PHONY: develop
develop: .env $(EGG_INFO)
$(EGG_INFO): $(SOURCES)
	$(PYTHON) setup.py develop
	touch $(EGG_INFO)  # flag to indicate package is installed

.PHONY: .env
.env: $(PYTHON)
$(PYTHON):
	virtualenv --python $(VERSION) $(VIRTUALENV)

.PHONY: depends
depends: .env $(DEPENDS) $(SOURCES)
$(DEPENDS):
	$(PIP) install docutils pdoc pep8 nose coverage --download-cache=$(CACHE)
	$(MAKE) .pylint
	touch $(DEPENDS)  # flag to indicate dependencies are installed

# issue: pylint is not currently installing on Windows
# tracker: https://bitbucket.org/logilab/pylint/issue/51/building-pylint-windows-installer-for
# workaround: skip pylint on windows
.PHONY: .pylint
ifeq ($(shell uname),Windows)
.pylint: .env
	@echo WARNING: pylint cannot be installed on Windows
else ifeq ($(shell uname),CYGWIN_NT-6.1)
.pylint: .env
	@echo WARNING: pylint cannot be installed on Cygwin
else
.pylint: .env
	$(PIP) install pylint --download-cache=$(CACHE)
endif

# Documentation ##############################################################

.PHONY: doc
doc: depends
	$(PYTHON) $(RST2HTML) README.rst docs/README.html
	$(PYTHON) $(PDOC) --html --overwrite $(PACKAGE) --html-dir apidocs

.PHONY: doc-open
doc-open: doc
	$(OPEN) docs/README.html
	$(OPEN) apidocs/$(PACKAGE)/index.html

# Static Analysis ############################################################

.PHONY: pep8
pep8: depends
	$(PEP8) $(PACKAGE) --ignore=E501 

# issue: pylint is not currently installing on Windows
# tracker: https://bitbucket.org/logilab/pylint/issue/51/building-pylint-windows-installer-for
# workaround: skip pylint on windows
.PHONY: pylint
ifeq ($(shell uname),Windows)
pylint: depends
	@echo pylint cannot be run on Windows
else ifeq ($(shell uname),CYGWIN_NT-6.1)
pylint: depends
	@echo pylint cannot be run on Cygwin
else
pylint: depends
	$(PYLINT) $(PACKAGE) --reports no \
	                     --msg-template="{msg_id}: {msg}: {obj} line:{line}" \
	                     --max-line-length=99 \
	                     --disable=I0011,W0142,W0511,R0801
endif

.PHONY: check
check: depends
	$(MAKE) doc
	$(MAKE) pep8
	$(MAKE) pylint

# Testing ####################################################################

.PHONY: test
test: develop depends
	$(NOSE)

.PHONY: tests
tests: develop depends
	TEST_INTEGRATION=1 $(NOSE) --verbose --stop --cover-package $(PACKAGE)

# Cleanup ####################################################################

.PHONY: .clean-env
.clean-env:
	rm -rf $(VIRTUALENV)

.PHONY: .clean-dist
.clean-dist:
	rm -rf dist build *.egg-info 

.PHONY: clean
clean: .clean-env .clean-dist
	rm -rf */*.pyc */*/*.pyc */*/*/*.pyc */*/*/*/*.pyc
	rm -rf */__pycache__ */*/__pycache__ */*/*/__pycache__ */*/*/*/__pycache__
	rm -rf apidocs docs/README.html .coverage

.PHONY: clean-all
clean-all: clean
	rm -rf $(CACHE)

# Release ####################################################################

.PHONY: dist
dist: .clean-dist
	$(PYTHON) setup.py sdist

.PHONY: upload
upload: .clean-dist
	$(PYTHON) setup.py sdist upload -r arnie

# Demo #######################################################################

.PHONY: demo
demo: serve

	# This demo starts a local server and verifies that bootstrap.py
	# installs ArniePye into a new virtualenv.

	# Create a temporary virtualenv for the demo and bootstrap ArniePye
	- virtualenv --python $(VERSION) demo ; cd demo ;\
	wget http://127.0.0.1:8080/packages/bootstrap/bootstrap.py ;\
	Scripts/python.exe bootstrap.py

	# Use 'arnie' to install and uninstall another package
	- demo/Scripts/arnie install testpackage
	- demo/Scripts/arnie uninstall testpackage

	# Clean up the demo and prompt the user to stop the server
	- rm -rf demo
	@echo
	@echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	@echo !!! press Ctrl+C to stop the server !!!
	@echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.PHONY: demo2
demo2: serve

	# This demo starts a local server and verifies that bootstrap.bat
	# installs Python 2 and 3 then runs bootstrap.py.

	# Create a temporary virtualenv for the demo and bootstrap ArniePye
	- mkdir demo2 ; cd demo2 ;\
	wget http://127.0.0.1:8080/packages/bootstrap/bootstrap.bat ;\
	cmd /c bootstrap.bat

	# Clean up the demo and prompt the user to stop the server
	- rm -rf demo2
	@echo
	@echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	@echo !!! press Ctrl+C to stop the server !!!
	@echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.PHONY: serve
serve: develop

	# Start a local PyPI server in the background
	$(BIN)/arnie serve --temp --verbose &

	# Upload the current version of ArniePye to the server
	$(PYTHON) setup.py sdist upload -r local

	# Notify the user that the server is still running
	@echo
	@echo press Ctrl+C when done serving...
