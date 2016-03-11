all: _site

_site: index.md
	jekyll build

index.md: ../case-01-dragless_sphere/results.ipynb
	jupyter nbconvert --execute --to=markdown --template="site-markdown.tpl" $^
	mv results.md index.md

clean:
	rm -rf *_files
	rm -f index.md
