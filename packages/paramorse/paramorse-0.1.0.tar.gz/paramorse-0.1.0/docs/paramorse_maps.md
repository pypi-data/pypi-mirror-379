# ParaMorse maps

The ParaMorse maps are the tables with the mappings between:
- symbols (i.e. characters in the payload alphabet)
- marks (i.e. the Morse code dots and dashes)
- paralanguage (i.e. the filler tokens including *um*, *uh*, *okay*, etc.)

Note these can be modified through the `ParaMorseConfig` class.


### Paralanguage tokens
| Para  | Morse | 
| :- | ---- |
| um | dot `.` |
| uh | dash `-` |
| okay | new letter ` ` |
| alright | new word ` / ` |

### Morse alphabet
| Sym | Morse | Paralanguage | 
| - | --------- | ----------------------- |
| A | `.-     ` | um ... uh |
| B | `-...   ` | uh ... um ... um ... um |
| C | `-.-.   ` | uh ... um ... uh ... um |
| D | `-..    ` | uh ... um ... um |
| E | `.      ` | um |
| F | `..-.   ` | um ... um ... uh ... um |
| G | `--.    ` | uh ... uh ... um |
| H | `....   ` | um ... um ... um ... um |
| I | `..     ` | um ... um |
| J | `.---   ` | um ... uh ... uh ... uh |
| K | `-.-    ` | uh ... um ... uh |
| L | `.-..   ` | um ... uh ... um ... um |
| M | `--     ` | uh ... uh |
| N | `-.     ` | uh ... um |
| O | `---    ` | uh ... uh ... uh |
| P | `.--.   ` | um ... uh ... uh ... um |
| Q | `--.-   ` | uh ... uh ... um ... uh |
| R | `.-.    ` | um ... uh ... um |
| S | `...    ` | um ... um ... um |
| T | `-      ` | uh |
| U | `..-    ` | um ... um ... uh |
| V | `...-   ` | um ... um ... um ... uh |
| W | `.--    ` | um ... uh ... uh |
| X | `-..-   ` | uh ... um ... um ... uh |
| Y | `-.--   ` | uh ... um ... uh ... uh |
| Z | `--..   ` | uh ... uh ... um ... um |
| 0 | `-----  ` | uh ... uh ... uh ... uh ... uh |
| 1 | `.----  ` | um ... uh ... uh ... uh ... uh |
| 2 | `..---  ` | um ... um ... uh ... uh ... uh |
| 3 | `...--  ` | um ... um ... um ... uh ... uh |
| 4 | `....-  ` | um ... um ... um ... um ... uh |
| 5 | `.....  ` | um ... um ... um ... um ... um |
| 6 | `-....  ` | uh ... um ... um ... um ... um |
| 7 | `--...  ` | uh ... uh ... um ... um ... um |
| 8 | `---..  ` | uh ... uh ... uh ... um ... um |
| 9 | `----.  ` | uh ... uh ... uh ... uh ... um |
| . | `.-.-.- ` | um ... uh ... um ... uh ... um ... uh |
|   | `--..-- ` | uh ... uh ... um ... um ... uh ... uh |
| ? | `..--.. ` | um ... um ... uh ... uh ... um ... um |
| ' | `.----. ` | um ... uh ... uh ... uh ... uh ... um |
| ! | `-.-.-- ` | uh ... um ... uh ... um ... uh ... uh |
| / | `-..-.  ` | uh ... um ... um ... uh ... um |
| ( | `-.--.  ` | uh ... um ... uh ... uh ... um |
| ) | `-.--.- ` | uh ... um ... uh ... uh ... um ... uh |
| & | `.-...  ` | um ... uh ... um ... um ... um |
| : | `---... ` | uh ... uh ... uh ... um ... um ... um |
| ; | `-.-.-. ` | uh ... um ... uh ... um ... uh ... um |
| = | `-...-  ` | uh ... um ... um ... um ... uh |
| + | `.-.-.  ` | um ... uh ... um ... uh ... um |
| - | `-....- ` | uh ... um ... um ... um ... um ... uh |
| _ | `..--.- ` | um ... um ... uh ... uh ... um ... uh |
| " | `.-..-. ` | um ... uh ... um ... um ... uh ... um |
| $ | `...-..-` | um ... um ... um ... uh ... um ... um ... uh |
| @ | `.--.-. ` | um ... uh ... uh ... um ... uh ... um |
