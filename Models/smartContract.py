import json
import sys
from sqlite3 import IntegrityError

from sqlalchemy.exc import PendingRollbackError

from Models import db
from sqlalchemy.dialects.mysql import TEXT, VARCHAR


class SmartContract(db.Model):
    __tablename__ = 'SmartContract'
    smartContractAddress = db.Column(VARCHAR(255), primary_key=True)
    assetName = db.Column(db.VARCHAR(255))
    assetDescription = db.Column(db.TEXT)
    numberOfItems = db.Column(db.INT)
    website = db.Column(db.VARCHAR(255))
    discord = db.Column(db.VARCHAR(255))
    mediumUsername = db.Column(db.VARCHAR(255))
    telegramUrl = db.Column(db.VARCHAR(255))
    twitterUsername = db.Column(db.VARCHAR(255))
    instagramUsername = db.Column(db.VARCHAR(255))
    safeListRequestStatus = db.Column(db.VARCHAR(255))
    asset = db.relationship('Asset', backref='SmartContract', lazy=True)

    def __init__(self, smartContractAddress: str, assetName: str, assetDescription: str, numberOfItems: int, website: str,
                 discord: str, mediumUsername: str, telegramUrl: str, twitterUsername: str, instagramUsername: str,
                 safeListRequestStatus: str):
        self.smartContractAddress = smartContractAddress
        self.assetName = assetName
        self.assetDescription = assetDescription
        self.numberOfItems = numberOfItems
        self.website = website
        self.discord = discord
        self.mediumUsername = mediumUsername
        self.telegramUrl = telegramUrl
        self.twitterUsername = twitterUsername
        self.instagramUsername = instagramUsername
        self.safeListRequestStatus = safeListRequestStatus

    @staticmethod
    def insertIntoDB(smartContract):
        try:
            db.session.add_all(smartContract)
            db.session.flush()
            db.session.commit()
            return 200

        except (IntegrityError, PendingRollbackError) as e:
            return 400


    @staticmethod
    def checkSmartContractLocalDB(smartContract):
        """
        :rtype: Bool
        """
        q = db.session.query(SmartContract.smartContractAddress).filter(SmartContract.smartContractAddress == smartContract)
        existStatus = db.session.query(q.exists()).scalar()

        return existStatus

    # @staticmethod
    # def updateSmartContract(smart_contract_address: str, token_id: int, price: float, onSale: bool, metaData):
    #     asset = db.session.query(Asset).filter(Asset.token_id == token_id,
    #                                            Asset.smartContractAddress == smart_contract_address).first()
    #     print(asset)
    #
    #     asset.price = price
    #     asset.onSale = onSale
    #     asset.metaData = metaData
    #     db.session.merge(asset)
    #     db.session.commit()