# Cifra de Cesar

A ideia deste projeto é represetar uma biblioteca capaz de executar a cifra de cesar (ROT13)

## Exemplos

##### Encriptação

```python
from cesar import encripta

encripta('eduardo') #rqheneb
```

##### Decriptação

```python
from cesar import decripta

decripta('rqheneb') # eduardo
```

##### Rotações diferentes de 13

```python
from cesar import encripta, decripta

encripta('eduardo') #rqheneb
decripta('rqheneb') # eduardo
```
