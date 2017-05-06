%.exchange: %.json
	./scripts/to_exchange.py $< > $@

all: $(addsuffix .exchange, $(basename $(wildcard blueprints/belt/balancer/smallest/*.json)))
