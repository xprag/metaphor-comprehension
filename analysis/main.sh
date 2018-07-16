#!/bin/bash
# This script create a SQLite database containing the psychopy output results

usage="$(basename "$0") [-h] [-s (number) -w (n/y)] -- program to set and get the metaphor comprehension experiment

where:
    -h  show this help text
    -s  set the threshold to determinate the trusted students (default: 0)
    -w  write the db (default: n)"

seed=42
while getopts ':hw:s:' option; do
	case "$option" in
		h) 	echo "$usage"
		   	exit
		   	;;
		s) 	seed=$OPTARG
			re='^[0-9]+$'
			if ! [[ $seed =~ $re ]] ; then
				echo "error: Not a number" >&2; exit 1
			else
				echo 'getting the data from the db ....'
				cd py
				python get_db.py  "$seed"
			fi
		   	;;
		w) 	seed=$OPTARG
			if [[ $seed = 'y' ]]; then
				echo 'writing the db from experimental data'
				cd py
				rm arguments.db
				pipenv shell
				python create_db.py
				python set_db.py
			else
				echo 'The db will be not written'
			fi
		   	;;
		:) 	printf "missing argument for -%s\n" "$OPTARG" >&2
		   	echo "$usage" >&2
		   	exit 1
		   	;;
		\?) 	printf "illegal option: -%s\n" "$OPTARG" >&2
		   	echo "$usage" >&2
		   	exit 1
		   	;;
	esac
done
shift $((OPTIND - 1))
#rm py/*.pyc
# if [ "w" = "$1" ]; then
# 	rm arguments.db
# 	python create_db.py
# 	python set_db.py
# 	rm *.pyc
# else
# 	python get_db.py "$1"
# fi
