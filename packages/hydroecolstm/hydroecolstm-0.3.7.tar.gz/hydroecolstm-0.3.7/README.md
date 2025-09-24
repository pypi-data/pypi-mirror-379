### HydroEcoLSTM <a href="https://github.com/tamnva/hydroecolstm/tree/master/docs/images/logo.svg"><img src="docs/images/logo.svg" align="right" height="120" /></a>

[![Documentation Status](https://readthedocs.org/projects/hydroecolstm/badge/?version=latest)](https://hydroecolstm.readthedocs.io/en/latest/?badge=latest) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10673255.svg)](https://doi.org/10.5281/zenodo.10673255) [![PyPI Latest Release](https://img.shields.io/pypi/v/hydroecolstm)](https://pypi.org/project/hydroecolstm/) 


- HydroEcoLSTM is a Python package with a graphical user interface (GUI) for modeling hydro-ecological processes using Long short-term Memory (LSTM) neural network. 
- Please check the [package documentation](https://hydroecolstm.readthedocs.io/en/latest/) for more details, especially about how to use HydroEcoLSTM without the GUI.
- Here is the [YouTube](https://www.youtube.com/playlist?list=PL7IsKPfYZuFtBk2yJ_ny2MU-WyTnANR-c) channel for tutorial videos on how to use HydroEcoLSTM with GUI.
- If you have any questions or want to report any issues, you can either report it in [GitHub](https://github.com/tamnva/hydroecolstm/issues) or [HydroEcoLSTM Google group](https://groups.google.com/g/hydroecolstm).

**Nguyen, T.V.**, Tran, V.N., Tran, H., Binh, D.V., Duong, T.D., Dang, T.D., Ebeling, P. (2025). *HydroEcoLSTM*: A Python package with graphical user interface for hydro-ecological modeling with long short-term memory neural network. Ecological Informatics, 102994. [10.1016/j.ecoinf.2025.102994](https://doi.org/10.1016/j.ecoinf.2025.102994).

### Quick start

Installation with Anaconda using environment ([environment.yml](https://github.com/tamnva/hydroecolstm/tree/master/environments)) file following the steps listed below. You can also see [my tutorial videos 1 and 7](https://www.youtube.com/watch?v=NPyr4HV2Ix4&list=PL7IsKPfYZuFvlz9ZYxM0wzNIdm-W-tP0q) for more details on how to install Anaconda and create a virtual environment. 

```python
# 1. Create the environment from environment.yml file (see link above)
conda env create -f environment.yml
conda activate hydroecolstm_env

# 2. Install the lastest version from github
pip install git+https://github.com/tamnva/hydroecolstm.git

# Or Install from PyPI (stable version)
pip install hydroecolstm

# 3. Import the package and show the GUI (please see below)
import hydroecolstm
hydroecolstm.interface.show_gui()
```

### The GUI

- After launchthe ing the GUI, you should see the following window (the latest version could look different). Two examples were documented in [these files](https://ars.els-cdn.com/content/image/1-s2.0-S1574954125000032-mmc1.pdf) 

<p align="center">
  <img src="https://github.com/tamnva/hydroecolstm/blob/master/docs/images/intro_figure.gif" width=100% title="hover text">
</p>
