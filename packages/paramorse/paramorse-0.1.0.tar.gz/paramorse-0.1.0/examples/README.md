# README Examples 

This repository includes example Jupyter notebooks so you can learn and explore the `paramorse` package.  
To use them, you will need a Jupyter kernel available in your Python environment. See the [notebook setup instructions](./README.md#notebook-setup-instructions) below for guidance.

Refer to the [ParaMorse maps](../docs/paramorse_maps.md) for the mappings between text symbols, Morse code marks, and paralanguage.

## Examples organization

The examples table links out to a set of notebooks that showcase different functionality in the package.  
Refer to the source code, especially the modules in [src/paramorse/core/](../src/paramorse/core/), for a variety of undocumented functionality. 

### Examples table

| Example set | Status | Component | 
| :---- | :---- | :---- |
| [Basic](examples_basic.ipynb) | dev | `paramorse` | 
| [Cover](examples_cover.ipynb) | exp | `paramorse.core.cover` | 
| [Payload](examples_payload.ipynb) | exp | `paramorse.core.payload` | 
| [Package](examples_package.ipynb) | exp | `paramorse.core.package` | 
| [Transform](examples_transform.ipynb) | exp | `paramorse.core.transform` | 
| [Generator](examples_generator.ipynb) | exp | `paramorse.core.generator` | 
| [Linguistics](examples_linguistics.ipynb) | exp | `paramorse.core.linguistics` | 
| [Config](examples_config.ipynb) | exp | `paramorse.core.config` | 
| ... | ... | ... | 
<!-- | [Experimental](examples_experimental.ipynb) | exp | `paramorse` |  -->

#### Examples table key

| Table key | Value | Description |
| :---- | ---- | :---- |
| Status | exp | Exploratory functionality. Lots of features but can change any time. |
| Status | dev | Probably stable and to be supported moving forward. |
| Status | pub | Stable with some backward compatibility. After end of beta. |
| Component |   | Package, subpackage, or module that is the focus of the examples. |



### Examples of minimally exposed API 

Currently there are only a handful of functions or objects exposed directly in an import.

```python
import paramorse as pm 

# encoding/decoding ParaMorse messages
pm.encode(...)
pm.decode(...)

# logging
pm.configure_logs(...)
pm.__version__
```

These are demonstrated in the [Basic examples](examples_basic.ipynb) notebook.

### Examples of extensive API functionality underneath

You can make use of much more `paramorse` functionality by directly importing the subpackage modules.  
For instance from the module `paramorse.core.payload`, you can use `build_payload` to create a payload and transform it into its equivalent forms (text symbols, paralanguage tokens, or Morse code marks).

```python
import paramorse.core.payload as pm_payload 

# an example payload 
my_payload = "I am"
payload_dict = pm_payload.build_payload(my_payload)

# creates this complete payload_dict

"""
{ 
  'sym': 'I am',
  'sym_list': ['I', 'am'],
  'dd': '.. / .- --',
  'dd_list': ['..', '/', '.-', '--'],
  'dd_flat': ['.', '.', ' ', '/', ' ', '.', '-', ' ', '-', '-', ' '],
  'dd_nest': [['.', '.'], ['/'], ['.', '-'], ['-', '-']],
  'para': 'um um alright um uh okay uh uh',
  'para_list': ['um um', 'alright', 'um uh', 'okay', 'uh uh'],
  'para_flat': ['um', 'um', 'alright', 'um', 'uh', 'okay', 'uh', 'uh'],
  'para_flat_rs': [ 'um ', 'um ', 'alright ', 'um ', 'uh ', 'okay ', 'uh ', 'uh '],
  'para_nest': [ ['um', 'um'], ['alright'], ['um', 'uh'], ['okay'], ['uh', 'uh']],
  'pay_format': 'string',
  'pay_kind': 'sym'
}
"""
```
There is minimal demonstration of this more "advanced" use in the [Examples table](./README.md#examples-table) notebooks listed with the experimental (exp) status. 

## Notebook setup instructions

First, be sure to have installed the `paramorse` package.  
To run a [Jupyter](https://jupyter.org/install) notebook, there are a few options. 

To get the default, browser-based interface, install JupyterLab:
```bash
pip install jupyterlab
```
and start it with:
```bash
jupyter lab
```
You can now open the notebooks in JupyterLab.

Alternatively if you use a different notebook IDE (such as VS Code with the Jupyter extension), you can install only the kernel:
```bash
pip install ipykernel
```
You can now open the notebooks directly in the IDE.
