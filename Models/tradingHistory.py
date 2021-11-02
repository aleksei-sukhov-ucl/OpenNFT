from datetime import datetime

from Models import db
from sqlalchemy.exc import (IntegrityError, PendingRollbackError)
from datetime import timedelta


class TradingHistory(db.Model):
    __tablename__ = 'TradingHistory'
    smartContractAddress = db.Column(db.String(255), db.ForeignKey('SmartContract.smartContractAddress'),
                                     primary_key=True)
    token_id = db.Column(db.Integer, primary_key=True)
    timeStamp = db.Column(db.DateTime(6), primary_key=True)
    eventType = db.Column(db.String(255), primary_key=True)
    salePrice = db.Column(db.Float)
    saleCurrency = db.Column(db.String(255))
    usdSalePrice = db.Column(db.Float)

    def __init__(self, smartContractAddress, token_id, timeStamp, eventType,
                 salePrice=None, saleCurrency=None, usdSalePrice=None):
        self.smartContractAddress = smartContractAddress
        self.token_id = token_id
        self.timeStamp = timeStamp
        self.salePrice = salePrice
        self.saleCurrency = saleCurrency
        self.usdSalePrice = usdSalePrice
        self.eventType = eventType

    def __eq__(self, other):
        return type(self) is type(other) and self.smartContractAddress == other.smartContractAddress \
               and self.token_id == other.token_id and self.timeStamp == other.timeStamp

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.smartContractAddress, self.token_id, self.timeStamp))

    @staticmethod
    def insertIntoDB(tradingRecords):
        try:
            db.session.add_all(tradingRecords)
            db.session.flush()
            db.session.commit()
        except (IntegrityError, PendingRollbackError) as e:
            print()

    @staticmethod
    def checkIfInDBSmartContractAddressTradingHistory(address, event_type):
        q = db.session.query(TradingHistory).filter(TradingHistory.smartContractAddress == address,
                                                    TradingHistory.eventType == event_type)
        existStatus = db.session.query(q.exists()).scalar()

        return existStatus

    @staticmethod
    def checkIfInDBTradingHistory(smartContractAddress: str, token_id: int):
        tradingHistoryObjects = set(
            db.session.query(TradingHistory).filter(TradingHistory.smartContractAddress == smartContractAddress,
                                                    TradingHistory.token_id == token_id).all())
        return tradingHistoryObjects

    @staticmethod
    def checkIfInDBSmartContractAddress(address):
        q = db.session.query(TradingHistory).filter(TradingHistory.smartContractAddress == address)
        existStatus = db.session.query(q.exists()).scalar()

        return existStatus

    @staticmethod
    def getLatestEventDate(address: str, event_type: str):

        query = db.session.query(TradingHistory.timeStamp).filter(
            TradingHistory.smartContractAddress == address)

        match event_type:
            case 'created':
                latestTimeStamp = query.order_by(TradingHistory.timeStamp).first()
            case 'successful' | 'offer_entered':
                latestTimeStamp = query.order_by(TradingHistory.timeStamp.desc()).first()
            case 'transfer':
                latestTimeStamp = query.order_by(TradingHistory.timeStamp.desc()).first()
            case _:
                latestTimeStamp = [datetime.datetime.now()]

        print(latestTimeStamp[0])
        return latestTimeStamp[0] + timedelta(hours=1, seconds=2)
