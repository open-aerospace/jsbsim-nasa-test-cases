all: readme

readme: run results.md
	mv results.md README.markdown

run:
	JSBSim run.xml

%.md: %.ipynb
	jupyter nbconvert --execute --to=markdown --template="nb-markdown.tpl" $^
