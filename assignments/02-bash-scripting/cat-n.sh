if [[ $# -eq 0 ]]; then  
    echo "Usage: cat-n.sh FILE" 
    exit 1 #1 specify error code
fi

INPUT_FILE=$1 #put an argument into name variable

if [[ ! -f "$1" ]]; then
     echo "foo is not a file"
     exit 1
fi

i=0
while read -r LINE; do
    i=$((i+1))     
    echo "$i" "$LINE"
done < "$1"
