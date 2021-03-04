
#! /usr/bin/sh

cd ~/src/botzo && JEKYLL_ENV=production bundle exec jekyll build && cd ~/src/botzo/_site/
echo //// SO FAR SO GOOD ////

tar -czvf botzo.tar.gz *
chmod 666 botzo.tar.gz
scp botzo.tar.gz botzilla.com@botzilla.com:html/botzo.tar.gz
cd ~/src/botzo

echo Now: 'ssh botzilla.com@botzilla.com'
echo and: 'cd html; tar -x -f botzo.tar.gz'


