py -m venv venv

.\venv\Scripts\python -m pip install --upgrade pip

.\venv\Scripts\pip install build
.\venv\Scripts\pip install twine
.\venv\Scripts\pip install wheel
.\venv\Scripts\pip install mido

.\venv\Scripts\pip install plmidi
.\venv\Scripts\pip install viztracer

.\venv\Scripts\pip install pybind11
xcopy .\venv\Lib\site-packages\pybind11\include\pybind11\* .\plmidiModule\pybind11\ /s