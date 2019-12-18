CC=gcc
CFLAGS=-fPIC -O3
LDFLAGS=-shared

libevolve.so: evolve.h evolve.c
	$(CC) -o libevolve.so $(LDFLAGS) $(CFLAGS) evolve.c

clean:
	rm -f libevolve.so evolve.o
