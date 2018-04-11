import numpy as np

# Generate N element long random character array from given alphabet
def generate_string(N, alphabet='ACGT'):
    base = np.array(alphabet, dtype='c')
    # Draw N random samples from alphabet
    dna = np.random.choice(base, N)
    return dna

dna = generate_string(20)
print("Original DNA", dna.tobytes().decode())

# TODO
# Use numpy.random.random_integers for selecting N mutation sites
# Utilise then numpy.random.choice for generating the mutations
# and use advanced indexing for creating mutated DNA
