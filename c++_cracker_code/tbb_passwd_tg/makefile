CC = g++
CC_FLAGS = -ansi -std=c++11 -Wall -Wno-write-strings -Wno-sign-compare -Wno-parentheses -Wno-format-security -Wno-unused-variable -I../tbb/include $(DEBUG_FLAG)
LDFLAGS = -L../tbb/lib/intel64/gcc4.7 -ltbb $(DEBUG_FLAG)

HEADERS = $(wildcard *.h)
SRC = $(wildcard *.cpp)
OBJECTS = $(SRC:.cpp=.o)

EXEC = tbb_passwd_tg

$(EXEC): $(OBJECTS)
	$(CC) $(OBJECTS) $(LDFLAGS) -o $(EXEC)

%.o: %.cpp $(HEADERS)
	$(CC) -c $(CC_FLAGS) $< -o $@

.PHONY: debug release clean

debug: DEBUG_FLAG = -g
debug: clean $(EXEC)

release: clean $(EXEC)

clean:
	rm -f $(EXEC) $(OBJECTS)