GCC = gcc
LIBS = -lcurl

ace_webscrape: ace_webscrape.o
		$(GCC) -g -o $@ $< $(LIBS)

ace_webscrape.o: ace_webscrape.cpp
		$(GCC) -g -c $<

clean:
		rm -f ace_webscrape.o ace_webscrape