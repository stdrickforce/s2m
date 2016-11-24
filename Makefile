help:
	@echo 'Makefile for s2m                        '
	@echo '                                        '
	@echo 'Usage:                                  '
	@echo '   make install    install as a package '
	@echo '   make develop    install as a package '

develop:
	pip install -r requirements.txt
	python setup.py develop
	@echo
	@echo "Install finished"

install:
	pip install -r requirements.txt
	python setup.py install --record install.record
	@echo
	@echo "Install finished."
