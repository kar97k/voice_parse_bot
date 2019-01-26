#!/bin/bash

#default values
dir="$1"
word="$2"

#----------------------------------------------------------
#Need refactoring with case: https://habr.com/post/127084/
#----------------------------------------------------------

#Input verification:

#given 2 arguments:
#the first one is the directory where to search
#the second is the word to search in audio file
if 	[ "$#" -ge "2" ];	then
	#short from command: test -d $dir
	if ! [ -d "$dir" ]; then
		echo "Given directory does not exist"
		exit 1
	fi
	#No symbols enabled exept russian or english letters
	echo "$word" | grep -Eq '^[А-Яа-я]+$'
	if [ "$?" != "0" ];	then
		echo 'Invalid word to search given. It must be one russian word without any other symbols'
		exit 1
	fi
#1 argument given:
#current directory accepts as default directory to find audio files
#1 given argument is the word to search in audio file
elif [ "$#" -eq "1" ]; then
	dir="$(pwd)"
	word="$1"
	echo "$word" | grep -Eq '^[А-Яа-я]+$'
	if [ "$?" != "0" ];
		then echo 'Invalid word to search given. It must be one russian word without any other symbols'
		exit 1
	fi
else echo 'No arguments given'
fi
echo "Directory:$dir; Word to search:$word"

#========================================================================================================
#before_chomp=$(./fql.pl $dir)
#echo "Before:$before_chomp"
#IFS="%"
#read -a valid_files_array <<< "$before_chomp" 
#echo $valid_files_array
#opendir
#========================================================================================================
