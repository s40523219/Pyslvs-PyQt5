#Pyslvs Makefile

all: build run

generate_build: ./core/kernel/pyslvs_generate/*.pyx
	@echo ---Pyslvs generate Build---
ifeq ($(OS),Windows_NT)
	$(MAKE) -C .\core\kernel\pyslvs_generate
else
	$(MAKE) -C ./core/kernel/pyslvs_generate
endif

build: launch_pyslvs.py generate_build
	@echo ---Pyslvs Build---
	@echo ---$(OS) Version---
ifeq ($(OS),Windows_NT)
	$(eval PYTHON = py$(shell python -c "import sys;t='{v[0]}{v[1]}'.format(v=list(sys.version_info[:2]));sys.stdout.write(t)")w)
	$(eval CPPYTHON = cp$(shell python -c "import sys;t='{v[0]}{v[1]}'.format(v=list(sys.version_info[:2]));sys.stdout.write(t)"))
	$(eval PYQTPATH = $(shell python -c "import PyQt5, os, sys;sys.stdout.write(os.path.dirname(PyQt5.__file__))"))
	@echo --Python Version $(PYTHON)--
	rename .\core\kernel\kernel_getter.py _kernel_getter.py
	rename .\core\kernel\$(PYTHON).py kernel_getter.py
	pyinstaller -F $< -i ./icons/main_big.ico \
--path="$(PYQTPATH)\Qt\bin" \
--add-binary="core/kernel/$(PYTHON)/libslvs.so;." \
--add-binary="core/kernel/pyslvs_generate/de.$(CPPYTHON)-win_amd64.pyd;." \
--add-binary="core/kernel/pyslvs_generate/firefly.$(CPPYTHON)-win_amd64.pyd;." \
--add-binary="core/kernel/pyslvs_generate/planarlinkage.$(CPPYTHON)-win_amd64.pyd;." \
--add-binary="core/kernel/pyslvs_generate/rga.$(CPPYTHON)-win_amd64.pyd;." \
--add-binary="core/kernel/pyslvs_generate/tinycadlib.$(CPPYTHON)-win_amd64.pyd;."
	rename .\dist\launch_pyslvs.exe pyslvs.exe
	rename .\core\kernel\kernel_getter.py $(PYTHON).py
	rename .\core\kernel\_kernel_getter.py kernel_getter.py
else
	$(eval PYTHON = py$(shell python3 -c "import sys;t='{v[0]}{v[1]}'.format(v=list(sys.version_info[:2]));sys.stdout.write(t)"))
	$(eval PYQTPATH = $(shell python3 -c "import PyQt5, os, sys;sys.stdout.write(os.path.dirname(PyQt5.__file__))"))
	@echo --Python Version $(PYTHON)--
	mv core/kernel/kernel_getter.py core/kernel/_kernel_getter.py
	mv core/kernel/$(PYTHON).py core/kernel/kernel_getter.py
	pyinstaller -F $< --exclude-module="PyQt4"
	mv dist/launch_pyslvs dist/pyslvs
	mv core/kernel/kernel_getter.py core/kernel/$(PYTHON).py
	mv core/kernel/_kernel_getter.py core/kernel/kernel_getter.py
endif
	@echo ---Done---

run: build dist/
ifeq ($(OS),Windows_NT)
	@dist/pyslvs.exe -h
else
	@dist/pyslvs -h
endif

DEBIANCONTROL = dist/temp/DEBIAN/control

deb: build dist/pyslvs
ifeq ($(OS),Windows_NT)
	@echo ---Ubuntu only---
else
	mkdir dist/temp dist/temp/DEBIAN dist/temp/usr/ dist/temp/usr/bin dist/temp/usr/share/
	touch $(DEBIANCONTROL)
	echo 'Package: pyslvs' >> $(DEBIANCONTROL)
	$(eval PYSLVS = "Version: $(shell python3 -c "import sys;from core.info.info import VERSION;sys.stdout.write(VERSION[0])")")
	echo $(PYSLVS) >> $(DEBIANCONTROL)
	echo 'Architecture: all' >> $(DEBIANCONTROL)
	echo 'Description: Dimensional Synthesis of Planar Four-bar Linkages in PyQt5 GUI.' >> $(DEBIANCONTROL)
	echo 'Maintainer: Yuan Chang <daan0014119@gmail.com>' >> $(DEBIANCONTROL)
	mv dist/pyslvs dist/temp/usr/share/
	ln -s /usr/share/pyslvs dist/temp/usr/bin/pyslvs
	mv dist/temp dist/pyslvs
	dpkg -b dist/pyslvs
endif

clean:
ifeq ($(OS),Windows_NT)
	make -C .\core\kernel\pyslvs_generate clean
	rd build /s /q
	rd dist /s /q
	del launch_pyslvs.spec
else
	make -C ./core/kernel/pyslvs_generate clean
	rm -f -r build
	rm -f -r dist
	rm -f launch_pyslvs.spec
endif
