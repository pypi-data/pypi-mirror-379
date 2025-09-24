# Super language overview

Below is a sketch of the super language framework which makes reference to the ParaMorse variant components as examples.  
For a more thorough presentation, see the [Heuristics for New Language](https://intro2024.superlang.org) (2025) paper on PsyArxiv.


## Superlang model

In a slightly more precise definition than the one in the [repository README](../README.md#super-language), a superlang *variant* $(V)$ is generated from a *base* language $(B)$ and a set of well-defined *modifications* $(M)$ via a super language *transformation* $(Z)$. 

```math
   Z \; : \; B \times M \rightarrow V
```
<br/>

| Superlang  | Definition  | Example 
| :---- | :---- | :---- |
| Base $(B)$ | Strings of the base language over which the *transformation* is applied. | English (oral form) |
| Modifications $(M)$ | Set of well-defined changes to the *forms* and/or *interpretations* of the *base* | Paralinguistic forms serving as the Morse code primitives. |
| Variant $(V)$  | Strings of the super language which is output by the *transformation*. | ParaMorse  |
| Transformation $(Z)$  | Mapping from *base* strings to super language *variant* strings according to the *modifications*. | ParaMorse variant specification including mapping *dot* &rarr; *um*, *dash* &rarr; *uh*, etc. |

This model is useful but it is primarily descriptive.  
An elaboration in this framework should consider how to operate the transformation forward and back.

## Transformation engine

Suppose you have a well-defined super language transformation $Z$, how do you go from a particular $b \in B$ to a particular $v \in V$?  
How might you go back in the other direction—from the variant string $v$ to its source base string $b$?  
In general, how do you control such a transformation and how do you formalize the values of its inputs and outputs beyond the base and variant strings?

The super language framework directly addresses the operation of super language by introducing the *transformation engine*:

```math
   Z[M] \; : \; B \times U \rightarrow V \times W
```

In more detailed notation:

```math
   Z[M(\tau, R, \mu)] \; : \; B \times U \rightarrow V \times (W_{int} \times W_{key})
```
<br/>

| Superlang | Var | ParaMorse example  |  
| :---- | :---- | :---- |
| Transformation | $Z$ | Transformation engine specification from *base* strings and modification *commands* to *variant* strings and modification *artifact*. May be written as  $Z[M(\tau, R, \mu)]$, $Z[\cdot]$ or just $Z$. |
| Commands | $U$| Set of commands (i.e. runtime input to modification function $\mu$) directing choice of particular $b \in B$ and $w \in W$ output. |
| Artifact | $W$ | Output of the modification function $\mu$; comprised of two subcomponents ($W_{int}$, $W_{key}$).
| Artifact interpretation | $W_{int}$ | Functional role served by the transformation. | 
| Artifact inverse key | $W_{key}$ | Necessary data to execute the inverse transformation. |  
| Tokenization | $\tau$ | Parsing of the strings in $B$ and $V$ into the target patterns and replacements of rewrite rules $R$. | 
| Rewrite rules | $R$ | Set of rewrite rules $r(\alpha, \beta)$ forming a rewrite system where $\alpha$ are the patterns and $\beta$ are the replacements. | 
| Modification function | $\mu$ | Function determining the particular $b \in B$ and $w \in W$ output; called on each token match, determining whether matching rewrite rule $r$ is applied and iteratively updating modification artifact $w \in W$. | 

The table below includes the contours for an example transformation specification using ParaMorse.

| Superlang | Var | ParaMorse example  |
| :---- | :---- | :---- |
| Transformation | $Z$ | ParaMorse super language operationalized via the transformation engine.  |
| Commands | $U$| The choice of payload message $u \in U$, such as the word "ten" from the set of all words in English vocabulary. |
| Artifact | $W$ | See artifact interpretation $W_{int}$ and inverse key  $W_{key}$.
| Artifact interpretation | $W_{int}$  | The semantic data in the payload string (i.e. the meaning of "ten").
| Artifact inverse key | $W_{key}$ | The variant's schema, including the mappings between symbols, paralanguage, and Morse code marks (i.e. it contains what is necessary to run `decode` on a ParaMorse package). |
| Tokenization | $\tau$ | Parsing of oral English $B$ or ParaMorse $V$ into constituent strings and tokens (roughly words) for transformation via cover, payload and package operations. Important edge case choices here (e.g. concatenations). |
| Rewrite rules | $R$ | Mappings from symbols in $B$ to those in $V$ (and vice versa) following the variant's schema (e.g. choice of [ParaMorse maps](../docs/paramorse_maps.md)). |
| Modification function | $\mu$ | Applies the choice in command $u$ to output a particular variant transformation $v \in V$. By default, the paralanguage payload is peppered in randomly over the base string but this function can be updated for different distributions. |


## Build your own superlang

The super language framework was designed for fast, modular, and iterative language augmentation.  
We encourage others to use it and generate new variants (and for those who wish to share them, we may link out to examples).

Refer to the super language typology in the [super language paper](https://www.sitovin.com/papers/Toshev2025_superlang_v2.pdf) (especially Appendix B: Transformation Variation) for ideas across:
- Forms (i.e. the structures containing modifications)
- Interpretations (i.e. the functional roles of the modifications)
- Augmentations (i.e. new or improved features in the variant resulting from the changes in forms/interpretations)

For more inspiration, see the *StegaPhone* variant [interactive demonstration](https://intro2024.superlang.org).  
In StegaPhone, short for steganographic phonetics, a speaker encodes binary bits in the the mispronunciation of words.