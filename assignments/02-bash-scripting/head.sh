if [[ $# -eq 0 ]]; then
	echo "usage: head.sh FILE"
	exit 1
fi

INPUT_FILE=$1
NUM_ITERATIONS=${2:-3} #default value of NUM_ITERATIONS = 3

if [[ ! -f "$1" ]]; then
	echo "foo is not a file"
	exit 1
fi

i=0
while read -r LINE; do
	i=$((i+1))
	echo "$LINE"
	if [[ $i -eq $NUM_ITERATIONS ]]; then
		break
	fi
done < "$1"
