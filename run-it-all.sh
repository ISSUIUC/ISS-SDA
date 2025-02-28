set -e
echo "Getting data..."
outf=$(python ./Wind-Model/main.py -s)
cp "$outf" ./Wind-Model/my-app/src/main_data.json
echo "Cleaning side-effects..."
rm $outf
echo "Starting main..."
cd ./Wind-Model/my-app/ && npm run start