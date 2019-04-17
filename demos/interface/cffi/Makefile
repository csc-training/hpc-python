CC=gcc
CFLAGS=-fPIC -O3
LDFLAGS=-shared

libmyclib.so: myclib.c
	$(CC) -o $@ $(LDFLAGS) $(CFLAGS) $<
