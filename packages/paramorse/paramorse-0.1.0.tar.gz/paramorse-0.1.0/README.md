# ParaMorse
The `paramorse` python package is an open source software implementation of ParaMorse, a human super language.  

## How it works
*ParaMorse* is short for paralinguistic Morse code.  

In ParaMorse, the *dots* and *dashes* of Morse are encoded by the two paralinguistic filler sounds *uh* and *um*, respectively.  
A third interjection, *okay*, delimits letters in the Morse code sequence.  
Using just these simple rules, a ParaMorse speaker can embed a message in the disfluencies of their speech.  

| Para  | Morse | 
| :---- | :---- |
| um | dot `.` |
| uh | dash `-` |
| okay | new symbol ` ` |

For instance, the word "me" can be written in several ways using either the Latin alphabet, Morse marks, or paralanguage sounds.

| Text  | Morse  | Paralanguage | 
| :---- | :---- | :---- |
| me | `-- .` | uh ... uh ... okay ... um |

See the [ParaMorse maps](docs/paramorse_maps.md) document with the mappings between symbols, Morse marks (dots, dashes, etc.) and paralanguage.

There are three primary components to a ParaMorse utterance:   
- The *cover* is the speech in which the coded paralanguage will be inserted.  
- The *payload* is the sequence of Morse code symbols in paralanguage form. 
- The *package* is the resulting transformation of the cover with an embedded payload.  

Example sentence using payload word "me": 

| ParaMorse  | Example text |
| :---- | :---- |
| Cover | We need to decide who will go in first, but you should already know that. |
| Payload | me (uh ... uh ... okay ... um) |
| Package | Uh we need to decide uh who will go in first, okay, but um you should already know that. |

See the paralanguage values for letter M and letter E in the [Morse alphabet](docs/paramorse_maps.md#morse-alphabet).



## Video demonstration
Example ParaMorse speech in which the message is conveyed across both the cover and payload.  
Click the image to play the video on YouTube.

[![Paralinguistic Morse code](docs/video/video_thumb_last.jpg)](https://youtu.be/4exJFd0xuMg)

## Software package
This is the official repository for `paramorse`, which is a python package hosted on PyPI.  
The package is an OSS implementation of the ParaMorse super language transformations.  
It is currently in beta.


### Install
Installation is done via command line on a system with Python (>=3.10).

```shell
pip install paramorse
```
Note this will install the one package dependency, [spaCy](https://spacy.io/).

### Example snippet
This code snippet demonstrates simple use of the `encode` and `decode` functions to create and decode a ParaMorse message.

```python
# import beta of public api
import paramorse as pm

# transform input text
cover = (
  "Should you go in there? Yes certainly, unless you are listening "
  "very carefully to what it is I am saying."
)
payload = "no"
package = pm.encode(cover, payload)

# decode to get back payload
decoded_payload = pm.decode(package)

# display as table (example output package will vary)
rows = [['cover', cover], ['payload', payload], 
        ['package', package], ['payload (dec)', decoded_payload]]

# print as markdown table
from paramorse.utils.render import md_table_str
print(md_table_str(rows, table_max_width=85)) 

"""
| Item          | Value                                                             |
| ------------- | ----------------------------------------------------------------- |
| cover         | Should you go in there? Yes certainly, unless you are listening   |
|               | very carefully to what it is I am saying.                         |
| payload       | no                                                                |
| package       | Should uh you go in there? Yes certainly, um unless you are       |
|               | listening okay very uh carefully uh to what it is I uh am saying. |
| payload (dec) | NO                                                                |
"""
```

### Documentation

For a quick start, see the [basic examples](examples/examples_basic.ipynb) python notebook.

For more examples, see the [examples README](examples/README.md).

Currently, the API is not formally documented and while its public surface is minimal, there is a lot of functionality underneath.  
It is partially showcased in notebooks listed in the [examples table](examples/README.md#examples-table) and you are encouraged to skim the source code, especially the modules in [src/paramorse/core/](src/paramorse/core/).


## Seeking ParaMorse speakers
Can you understand ParaMorse speech, or produce it, without device assistance? Are you learning ParaMorse and would like to share some progress?  
If so, you are encouraged to reach out to contact@sitovin.com. 

The motivation behind the release of this OSS package is to seek out and develop proficient ParaMorse speakers. We find the ParaMorse variant to be well suited for a key proof-of-concept (PoC) of the broader framework: human acquisition of super language.
To learn more, go to the [Super Language blog](https://blog.superlang.org).

## Super language

ParaMorse is an example *super language* or *superlang*.  

Also known as a *variant*, the term *super language* signifies a base language (e.g. oral English) that has been augmented (e.g. with paralinguistic Morse code) to create a variant (e.g. ParaMorse). 
Leveraging its latin root *super* meaning "beyond", the resulting variant contributes new structural or functional properties that go beyond what is available in the base.  
More broadly, the super language *framework* is a modular system for the iterative modification of a base language through new forms (e.g. phonetic or morphological containers) and interpretations (e.g. semantic or pragmatic functions).  

For a limited framework summary, see the 
[super language overview](docs/superlang_overview.md) document. For a fuller treatment, see the introductory super language paper on PsyArxiv, [Heuristics for New Language](https://intro2024.superlang.org) (2025).  
For a cursory introduction here, we provide an abridged definition:  
A superlang *variant* $(V)$ is generated from a *base* language $(B)$ and a set of well-defined *modifications* $(M)$.

```math
   Z \; : \; B \times M \rightarrow V
```

<br/>

| Superlang  | Definition  | Example
| :---- | :---- | :---- |
| Base $(B)$ | Base language over which the transformation is applied. | English (oral form) |
| Mods $(M)$ | Set of well-defined changes to the *base*. | Paralanguage &rarr; Morse|
| Variant $(V)$ | Super language generated from the transformation of a *base* via a set of *modifications*. | ParaMorse |

We encourage others to advance the framework and [build your own superlang](docs/superlang_overview.md#build-your-own-superlang).


## Administrative info

### License
The OSS package `paramorse` is distributed under the MIT license.

### Cite

To cite the OSS package or the documentation, use the metadata in [CITATION.cff](CITATION.cff).  
For other formats, such as BibTex, see the [citation README](/docs/citation/README.md).

### Connect
For now, please direct all inquiries to contact@sitovin.com.  
Follow updates here or on the [Super Language blog](https://blog.superlang.org).



