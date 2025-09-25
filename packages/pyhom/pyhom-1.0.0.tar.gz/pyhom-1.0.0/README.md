# Pyhom

> ⚠️ **Warning:** Repository under construction!

In this repository, we present "PyHom: a Python library for homogenization".

This library is conceived for calculating the **effective conductivity properties** of **composite materials** with complex microstructures in a **2D framework**. The backbone of the code relies on the theory described in [[Cruz-González et al., 2024](https://doi.org/10.1016/j.ijsolstr.2024.112747)], and uses not only existing image processing modules, but also functionality and packages built by the authors. The main interest is using **PyHom** as a toolbox to study the core issues in the application of **IDD** and the **IDD-based PCW**.

For more information, please refer to the paper

1. Cruz-González, O., Cornaggia, R., Dartois, S., and Brenner, R. (2024). Accounting for spatial distribution in mean-field homogenization of particulate composites. International Journal of Solids and Structures, 294:112747. DOI [10.1016/j.ijsolstr.2024.112747](https://doi.org/10.1016/j.ijsolstr.2024.112747)

**Keywords:**\
Microstructures,
Particulate reinforced composites, Homogenization, RSA, Voronoï Diagram, Spatial distribution, Mean Field estimates, FFT-based solver.

## Updates

Main functionalities:

- `pyhom_core`: Calculate the normalized effective conductivity properties of composite materials in 2D by varying the conductivity contrast parameter `gamma`. (Dec 17, 2024)

All the functionalities described in the paper will be incorporated soon.

## Installation

1. Python 3.10 and Git installed on your system.

2. Clone the repository in a local directory.

```bash
git clone https://github.com/olcruzgonzalez/pyhom.git
cd pyhom
```

3. Create and activate a virtual environment

- On Linux/macOS:

```bash
python3.10 -m venv myenv
source myenv/bin/activate
```

- On Windows:

```bash
py -3.10 -m venv myenv
myenv/Scripts/Activate.ps1
```

4. Install dependencies

```bash
(myenv) pip install -r requirements.txt
```

5. Use the library.

## Basic Usage

In this section, we show how to use the library through some practical examples.

For demonstrating the most basic functionality of the `python_core` modulus, please, create a script `basic_usage.py` and use the following template:

```python
# basic_usage.py
from pyhom.pyhom_core import Core

if __name__ == '__main__':
    coreJob = Core()
    coreJob.input_data(output_dir = 'results', input_file_path = 'input.yaml')
    coreJob.run()
```

>💡 Notice that the only requirement to launch the code is to pass a YAML file as input. It defines various parameters related to the configuration of inclusions, cell properties, and other related settings.

Create a YAML file `input.yaml` and use the following template:

```YAML
#-----------------------------------------------
# Input Parameters - PyHom Core
#---------------------------------------------

N_incl: 10 # Number of inclusions.
# default varying parameter
gamma: [2,5,10,20,50,100]
# fixed parameters
c_incl: [0.05] 
e_incl: [1]
theta_incl: '[0*np.pi/180]'
e_cell_RSA: [0.5]
theta_cell_RSA: '[0*np.pi/180]'
size_factor: [0.375]
security_factor: 1.02

# Further information
meta_x_incl: 
  value: false
  path: null
meta_image: 
  value: false
  path: null
hasReproducibility:
  value: False
  seed: null
```

Launch the code

```bash
python basic_usage.py
```

## Built-in examples

We have incorporated built-in examples for different `input_core.yaml` files (see `src/pyhom/built-in`).

To do this, simply add the following line to `basic_usage.py` script. Notice that `labelNumber` is an integer between 1 and 8.

```python
# basic_usage.py
from pyhom.pyhom_core import Core

if __name__ == '__main__':
    coreJob = Core()
    coreJob.get_built_in_dataset(labelNumber = "1") # NEW LINE !
    coreJob.input_data(output_dir = 'results', input_file_path = 'built-in_input/labelNumber_1/input_core.yaml') # UPDATE input_file_path!
    coreJob.run()
```

## License

The template is available as open source under the terms of the [MIT License](https://github.com/olcruzgonzalez/pyhom/blob/main/LICENSE).