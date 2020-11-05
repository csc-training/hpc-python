import numpy as np

# Generate N element long random character array from given alphabet
def generate_string(N, alphabet='ACGT'):
    """
    Generate a random string.

    Args:
        N: (int): write your description
        alphabet: (float): write your description
    """
    base = np.array(alphabet, dtype='c')
    # Draw N random samples from alphabet
    dna = np.random.choice(base, N)
    return dna

# Perform N random mutations to DNA string
def mutate(dna, N):
    """
    Return a randomly sampled polynomial.

    Args:
        dna: (array): write your description
        N: (float): write your description
    """
    mutated = dna.copy()
    mutation_sites = np.random.random_integers(0, dna.size - 1, size=N)
    base = np.array('ACGT', dtype='c')
    new_bases = np.random.choice(base, N)
    mutated[mutation_sites] = new_bases
    return mutated

dna = generate_string(20)
dna_mutated = mutate(dna, 5)
print("Original DNA:", dna.tobytes().decode())
print("Mutated  DNA:", dna_mutated.tobytes().decode())
print("Similarity ", np.sum(dna == dna_mutated) / float(dna.size))
