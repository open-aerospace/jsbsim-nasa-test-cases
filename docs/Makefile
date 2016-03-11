all: _site

_site: index.markdown case-01.md
	jekyll build

case-01.md: ../case-01-dragless_sphere/results.ipynb
	jupyter nbconvert --execute --to=markdown --template="site-markdown.tpl" $^
	mv results.md case-01.md
	rm -rf *_files

clean:
	rm -rf *_files
	rm -f case-01.md
	rm -rf _site
