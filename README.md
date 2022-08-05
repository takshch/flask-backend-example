# Flask Backend Example


## SETUP
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt


# Run Development
export ENV=development
flask run

# Run production
sudo docker-compose build
sudo docker-compose up

# Stop production
sudo docker-compose down