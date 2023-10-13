git commit -am "$1"
git push
ssh debian@endor.josedomingo.org "sh www/fp_pledin/fp.sh $2"
