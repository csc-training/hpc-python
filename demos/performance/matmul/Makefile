CC=gcc
CFLAGS=-O3
LDFLAGS=-lopenblas

mm: matmul.c
	$(CC) -o mm $(LDFLAGS) $(CFLAGS) matmul.c

clean:
	rm -f mm *.o
