## Mutating DNA sequence with NumPy

Create a NumPy character array representing a DNA sequence.
Use then advanced indexing and NumPy random module for making random
mutations to DNA sequence:

 * Choose N random mutation sites using `numpy.random.random_integers()`
   (a single site can selected multiple times)
 * Create N random letters presenting the mutations
 * Use advanced indexing for creating mutated sequence

The end results should be something like:

```
Original DNA: ATGCTACAGT
Mutated  DNA: AGGCTACAGA
```

You can start from the provided skeleton code [skeleton.py](skeleton.py).
