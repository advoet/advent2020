if [ $(find "data/day$1.advent") ]
then
	echo "Day $1 already downloaded."
else
	SESSION=$(<".cookies")
	curl -o data/day$1.advent https://adventofcode.com/2020/day/$1/input --cookie "session=$SESSION"
	echo "Day $1 saved to /data/day$1.advent"
fi