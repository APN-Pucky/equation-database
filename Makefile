livehtml:
	hatch run full:$(MAKE) -C docs livehtml

html:
	hatch run full:$(MAKE) -C docs html

pdf:
	hatch run full:$(MAKE) -C docs latexpdf

doc: html

install:
	poetry install --with docs --with dev --with test
	python3 -m pip install --user .

build:
	python -m build

test:
	rm -f .coverage coverage.xml
	poetry run pytest

commit:
	-git add .
	-git commit

push: commit
	git push

pull: commit
	git pull

clean:
	rm -r docs/build docs/source/_autosummary
	rm -r .eggs .pytest_cache *.egg-info dist build


release: push html
	git tag $(shell git describe --tags --abbrev=0 | perl -lpe 'BEGIN { sub inc { my ($$num) = @_; ++$$num } } s/(\d+\.\d+\.)(\d+)/$$1 . (inc($$2))/eg')
	git push --tags
