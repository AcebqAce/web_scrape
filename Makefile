GCC = gcc
LIBS = -lcurl

mycurlapp: mycurlapp.o
		$(GCC) -g -o $@ $< $(LIBS)

mycurlapp.o: mycurlapp.cpp
		$(GCC) -g -c $<

clean:
		rm -f mycurlapp.o mycurlapp