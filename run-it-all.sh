set -e

get_data=$1

echo "Extra args: $get_data"

echo "<Running wind model python script>"

if [ $get_data == "new" ]; then
    echo "Retrieving new API data..."
    outf=$(python ./Wind-Model/main.py -s -n)
else
    echo "Using existing data..."
    outf=$(python ./Wind-Model/main.py -s)
fi

cp "$outf" ./Wind-Model/my-app/src/main_data.json
echo "Cleaning side-effects..."
rm $outf
echo "Starting main..."
cd ./Wind-Model/my-app/ && npm i && npm run start