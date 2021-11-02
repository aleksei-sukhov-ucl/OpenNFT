from app import app

if __name__ == '__main__':
    app.run()


# # Secret login info
# from settings import *
#
# # FLASK imports
# from flask import Flask
# from OpenSeaAssets import OpenSeaAssets
# # from Models.Models import SmartContract, db, Asset, TradingHistory, manager
# from flask_migrate import Migrate
# from OpenSeaEvents import OpenSeaEvents
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# """
# Configure application from Config class in project-level
# config.py module.
#
# """
#
# from Models import db
#
# migrate = Migrate(app, db)
# # Initialize plugins
# # db.init_app(app)
# # migrate.init_app(app, db)
#
#
# if __name__ == '__main__':
#     db.init_app(app)
#     app.run()
#
#     # manager.run()
#     # allSmartContractAddresses = [i[0] for i in db.session.query(SmartContract.smartContractAddress).all()]
#     #
#     # allSmartContractAddresses = ['0x79da5fa272e8fb280cee4d0649aa6a9e4e62ceb0']
#     # for smartContractAddresses in allSmartContractAddresses:
#     #     print(f"Smart contract address: {smartContractAddresses}")
#     #
#     #     # Check if Smart Contract has all assets saved in DB
#     #
#     # # Getting Number of request to be sent to get all of the data
#     #     totalNumberOfRequestsToBeMade = OpenSeaAssets.pagination(smartContractAddresses)
#     # # Getting all the assets downloaded
#     #     OpenSeaAssets.getAllAssets(smartContractAddresses, totalNumberOfRequestsToBeMade)
#     #
#     # # Check if Smart Contract has full trading history downloaded
#     #     OpenSeaEvents.eventsGetRequest(smartContractAddresses)
#     # #     print(TradingHistory.getLatestEventDate(smartContractAddresses))
