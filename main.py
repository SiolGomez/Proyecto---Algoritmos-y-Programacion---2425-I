from db import db
from Museo import Museo

def main():

    museo = Museo(db)
    museo.load_data()
    museo.start()

main()