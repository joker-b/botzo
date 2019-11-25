# botzo
Various tools and Jekyll source files to support botzilla.com

Simple dopey install:

`cd ~/code/botzo && JEKYLL_ENV=production bundle exec jekyll build && cd ~/code/botzo/_site/; tar -czvf botzo.tar.gz *; chmod 666 botzo.tar.gz; scp botzo.tar.gz botzilla.com@botzilla.com:html/botzo.tar.gz; cd ~/code/botzo`

and a similar tar extraction on botzilla.com:

login, then
`cd html; tar -x -f botzo.tar.gz`

## some notes to myself

Using `site.baseurl` gives "" so use `site.url` or even (for testing locally) just the direct full URL.

Local testing: `bundle exec jekyll serve` in the top directory, then navigate to http://localhost:4000/

Be very careful about file permissions on Mac, they often come through as 600 so be sure to 666 them before sending to the server.
