# botzo
Various tools and Jekyll source files to support botzilla.com

Simple dopey install:

cd ~/code/botzo && JEKYLL_ENV=production bundle exec jekyll build && cd ~/code/botzo/_site/; tar -czvf botzo.tar.gz *; scp botzo.tar.gz botzilla.com@botzilla.com:html/botzo.tar.gz; cd ~/src/botzo

and a similar tar extraction on botzilla.com
