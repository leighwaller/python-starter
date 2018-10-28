# Update this to give whichever name you want. This may be set on the command line:
# > make build OUT_FILE=./outfile.zip
OUT_FILE?=./dist/python-starter.zip

### Below this point it should not need to be changed
# get absolute path of zipfile to deliver
ARTIFACT=$(abspath $(OUT_FILE))

# Install all the libs locally
install:
	pipenv install --python 3.6

install-dev: install
	pipenv install --dev

# Destroy the virtualenv
uninstall:
	pipenv --rm

# Run the import
run:
	pipenv run python ./handler.py

# Clean delivrable
clean:
	rm -f ${ARTIFACT}

test: install-dev
	pipenv run py.test

# Rebuild the artifact
package: clean install
	$(eval VENV = $(shell pipenv --venv))
	cd ${VENV}/lib/python3.6/site-packages && zip -r9 ${ARTIFACT} ./*
	zip -r9 ${ARTIFACT} *.py -x tests

