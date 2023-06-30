BUILD = Build
COMP = cc
CFLAGS = -Wall -Werror
SERVS = $(wildcard ./*.c)
OBJS = $(patsubst ./%.c,$(BUILD)/%.o,$(SERVS))
TARGETS = $(patsubst ./%.c,%,$(SERVS))

all: $(TARGETS)

$(BUILD)/%.o: ./%.c 
	mkdir -p $(BUILD)
	$(COMP) $(CFLAGS) -c $< -o $@

$(TARGETS): % : $(BUILD)/%.o
	$(COMP) $(CFLAGS) $< -o $@