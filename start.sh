echo "Cloning Repo...."
git clone -b test https://github.com/Greymattersbot/link-search-bot---mdisk-search-bot /Mdisk-Search-Bot
cd /Mdisk-Search-Bot
pip3 install -r requirements.txt
echo "Starting Bot....GreyMatter_Bots"
python3 main.py
