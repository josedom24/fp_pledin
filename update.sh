git commit -am "$1"
git push
ssh debian@endor.josedomingo.org "export PATH="$HOME/.gems/bin:$PATH";sh www/fp_pledin/fp.sh"
