s/^ *thumbnail:.*\(pix202.\)/thumbnail: ..\/..\/assets\/\1/
/^layout:/d
/^image:/d
/^ *path:/d
/^categories:/{
    s/\]//
    s/,\(.*\)/\n  <!-- \1 -->/
    s/.*\[/category: /
}
/^tags:/{
    s/.*\[/tags:\n  - /
    s/\]//
    s/, */\n  - /g
}
