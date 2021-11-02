# import datetime
# import itertools
# from datetime import timedelta
#
# # Flask Migrate
# from flask_script import Manager
# from flask_migrate import Migrate
#
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.exc import (IntegrityError, PendingRollbackError)
#
# # Flask Migrate
#
#
# # manager = Manager(app)
# # manager.add_command('db', Migrate)
# import app
#
#
#
# db = SQLAlchemy(app)
#
#
# # class SmartContract(db.Model):
# #     __tablename__ = 'SmartContract'
# #     smartContractAddress = db.Column(db.String(255), primary_key=True)
# #     name = db.Column(db.String(255))
# #     description = db.Column(db.TEXT)
# #     numberOfItems = db.Column(db.INT)
# #     website = db.Column(db.TEXT)
# #     discord = db.Column(db.TEXT)
# #     mediumUsername = db.Column(db.TEXT)
# #     telegramUrl = db.Column(db.TEXT)
# #     twitterUsername = db.Column(db.TEXT)
# #     instagramUsername = db.Column(db.TEXT)
# #     safeListRequestStatus = db.String(255)
# #     asset = db.relationship('Asset', backref='SmartContract', lazy=True)
# #
# #     def __init__(self, smartContractAddress, name, description, numberOfItems, website,
# #                  discord, mediumUsername, telegramUrl, twitterUsername, instagramUsername, safeListRequestStatus):
# #         self.smartContractAddress = smartContractAddress
# #         self.name = name
# #         self.name = description
# #         self.name = numberOfItems
# #         self.name = website
# #         self.name = discord
# #         self.name = mediumUsername
# #         self.name = telegramUrl
# #         self.name = twitterUsername
# #         self.name = instagramUsername
# #         self.name = safeListRequestStatus
# #
# #     @staticmethod
# #     def updateSmartContract(smart_contract_address: str, token_id: int, price: float, onSale: bool, metaData):
# #         asset = db.session.query(Asset).filter(Asset.token_id == token_id,
# #                                                Asset.smartContractAddress == smart_contract_address).first()
# #         print(asset)
# #
# #         asset.price = price
# #         asset.onSale = onSale
# #         asset.metaData = metaData
# #         db.session.merge(asset)
# #         db.session.commit()
#
#
# # class Asset(db.Model):
# #     __tablename__ = 'Asset'
# #     id = db.Column(db.Integer, primary_key=True)
# #     smartContractAddress = db.Column(db.String(255),
# #                                      db.ForeignKey('SmartContract.smartContractAddress'))
# #     name = db.Column(db.String(255))
# #     token_id = db.Column(db.Integer)
# #     price = db.Column(db.Float)
# #     onSale = db.Column(db.Boolean)
# #     rarityScore = db.Column(db.Integer)
# #     metaData = db.Column(db.JSON)
# #
# #     @staticmethod
# #     def insertIntoDB(assets):
# #         db.session.add_all(assets)
# #         db.session.flush()
# #         db.session.commit()
# #
# #     @staticmethod
# #     def checkIfInDBSmartContractAddress(address):
# #         q = db.session.query(Asset.id).filter(Asset.smartContractAddress == address)
# #         existStatus = db.session.query(q.exists()).scalar()
# #
# #         return existStatus
# #
# #     @staticmethod
# #     def checkIfInDBAsset(assetName: str, tokenId: str, smartContractAddress: str):
# #         q = db.session.query(Asset.id).filter(Asset.smartContractAddress == smartContractAddress,
# #                                               Asset.name == assetName,
# #                                               Asset.token_id == tokenId)
# #         existStatus = db.session.query(q.exists()).scalar()
# #
# #         return existStatus
# #
# #     @staticmethod
# #     def updateAsset(smart_contract_address: str, token_id: int, price: float, onSale: bool, metaData):
# #         asset = db.session.query(Asset).filter(Asset.token_id == token_id,
# #                                                Asset.smartContractAddress == smart_contract_address).first()
# #         print(asset)
# #
# #         asset.price = price
# #         asset.onSale = onSale
# #         asset.metaData = metaData
# #         db.session.merge(asset)
# #         db.session.commit()
# #
# #     @staticmethod
# #     def getAllTokenIds(address):
# #         token_ids = list(
# #             itertools.chain(*db.session.query(Asset.token_id).filter(Asset.smartContractAddress == address).all()))
# #         return token_ids
#
#
# # class TradingHistory(db.Model):
# #     __tablename__ = 'TradingHistory'
# #     smartContractAddress = db.Column(db.String(255), db.ForeignKey('SmartContract.smartContractAddress'),
# #                                      primary_key=True)
# #     token_id = db.Column(db.Integer, primary_key=True)
# #     timeStamp = db.Column(db.DateTime(6), primary_key=True)
# #     eventType = db.Column(db.String(255), primary_key=True)
# #     salePrice = db.Column(db.Float)
# #     saleCurrency = db.Column(db.String(255))
# #     usdSalePrice = db.Column(db.Float)
# #
# #     def __init__(self, smartContractAddress, token_id, timeStamp, eventType,
# #                  salePrice=None, saleCurrency=None, usdSalePrice=None):
# #         self.smartContractAddress = smartContractAddress
# #         self.token_id = token_id
# #         self.timeStamp = timeStamp
# #         self.salePrice = salePrice
# #         self.saleCurrency = saleCurrency
# #         self.usdSalePrice = usdSalePrice
# #         self.eventType = eventType
# #
# #     def __eq__(self, other):
# #         return type(self) is type(other) and self.smartContractAddress == other.smartContractAddress \
# #                and self.token_id == other.token_id and self.timeStamp == other.timeStamp
# #
# #     def __ne__(self, other):
# #         return not self.__eq__(other)
# #
# #     def __hash__(self):
# #         return hash((self.smartContractAddress, self.token_id, self.timeStamp))
# #
# #     @staticmethod
# #     def insertIntoDB(tradingRecords):
# #         try:
# #             db.session.add_all(tradingRecords)
# #             db.session.flush()
# #             db.session.commit()
# #         except (IntegrityError, PendingRollbackError) as e:
# #             print()
# #
# #     @staticmethod
# #     def checkIfInDBSmartContractAddressTradingHistory(address, event_type):
# #         q = db.session.query(TradingHistory).filter(TradingHistory.smartContractAddress == address,
# #                                                     TradingHistory.eventType == event_type)
# #         existStatus = db.session.query(q.exists()).scalar()
# #
# #         return existStatus
# #
# #     @staticmethod
# #     def checkIfInDBTradingHistory(smartContractAddress: str, token_id: int):
# #         tradingHistoryObjects = set(
# #             db.session.query(TradingHistory).filter(TradingHistory.smartContractAddress == smartContractAddress,
# #                                                     TradingHistory.token_id == token_id).all())
# #         return tradingHistoryObjects
# #
# #     @staticmethod
# #     def checkIfInDBSmartContractAddress(address):
# #         q = db.session.query(TradingHistory).filter(TradingHistory.smartContractAddress == address)
# #         existStatus = db.session.query(q.exists()).scalar()
# #
# #         return existStatus
# #
# #     @staticmethod
# #     def getLatestEventDate(address: str, event_type: str):
# #
# #         query = db.session.query(TradingHistory.timeStamp).filter(
# #             TradingHistory.smartContractAddress == address)
# #
# #         match event_type:
# #             case 'created':
# #                 latestTimeStamp = query.order_by(TradingHistory.timeStamp).first()
# #             case 'successful' | 'offer_entered':
# #                 latestTimeStamp = query.order_by(TradingHistory.timeStamp.desc()).first()
# #             case 'transfer':
# #                 latestTimeStamp = query.order_by(TradingHistory.timeStamp.desc()).first()
# #             case _:
# #                 latestTimeStamp = [datetime.datetime.now()]
# #
# #         print(latestTimeStamp[0])
# #         return latestTimeStamp[0] + timedelta(hours=1, seconds=2)
