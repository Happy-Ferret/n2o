BUILDTYPE ?=Release
N2O_TARGET =build/$(BUILDTYPE)/n2o.node
NODE_GYP_OPTS =

ifeq ($(BUILDTYPE),Debug)
	NODE_GYP_OPTS+= --debug
endif

all: $(N2O_TARGET)

test: $(N2O_TARGET) node_modules
	tap test/*.js

lint:
	@find . -type f -name "*.[ch]*" -not -path "./boost/*" -not -path "./node_modules/*" -not -name "*.swp" \
	| vera++ -s --root tools/vera++

clean:
	rm -rf build
	rm -rf test/build
	rm -rf samples/hello_world/build
	rm -rf samples/sandbox/build
	find . -name npm-debug.log -exec rm -rf {} \;

distclean: clean
	rm -rf node_modules samples/{sandbox,hello_world}/node_modules

.PHONY: all test clean distclean xcode

#==============================================================================

build/Makefile:
	node-gyp configure $(NODE_GYP_OPTS)

$(N2O_TARGET): build/Makefile
	node-gyp build $(NODE_GYP_OPTS)

node_modules:
	npm link

