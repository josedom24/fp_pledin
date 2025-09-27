git commit -am "$1"
git push
ssh -t debian@endor.josedomingo.org "sh www/fp_pledin/fp.sh $2"
