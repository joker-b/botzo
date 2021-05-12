cd ~/src/botzo/_posts/
for f in 202*
do
    d=`echo $f | sed -e 's/\(202.-..-..\)-.*/\1/'`
    n=`echo $f | sed -e 's/202.-..-..-//' -e 's/\.md//'`
    n2="../../gbotz/content/blog/$n"
    echo $n2 from $f
    mkdir $n2
    sed -e "2idate: $d" -f ../cp-all-md.sed $f > $n2/index.md
done
cd ~/src/botzo/
