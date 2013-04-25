CC=gcc
CFLAGS=-I.

ODIR=obj
DESTDIR=bin

_OBJ = iteration.o
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))

$(ODIR)/%.o: %.c
	@mkdir -p $(ODIR)
	$(CC) -c -o $@ $< $(CFLAGS)

iteration: $(OBJ)
	@mkdir -p $(DESTDIR)
	gcc -o $(DESTDIR)/$@ $^ $(CFLAGS)

.PHONY: clean

clean:
	rm -rf $(ODIR) $(DESTDIR)

