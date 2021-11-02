import itertools
from Models import db


class Asset(db.Model):
    __tablename__ = 'Asset'
    id = db.Column(db.Integer, primary_key=True)
    smartContractAddress = db.Column(db.String(255),
                                     db.ForeignKey('SmartContract.smartContractAddress'))
    name = db.Column(db.String(255))
    token_id = db.Column(db.Integer)
    price = db.Column(db.Float)
    onSale = db.Column(db.Boolean)
    rarityScore = db.Column(db.Integer)
    metaData = db.Column(db.JSON)

    @staticmethod
    def insertIntoDB(assets):
        db.session.add_all(assets)
        db.session.flush()
        db.session.commit()

    @staticmethod
    def checkIfInDBSmartContractAddress(address):
        q = db.session.query(Asset.id).filter(Asset.smartContractAddress == address)
        existStatus = db.session.query(q.exists()).scalar()

        return existStatus

    @staticmethod
    def checkIfInDBAsset(assetName: str, tokenId: str, smartContractAddress: str):
        q = db.session.query(Asset.id).filter(Asset.smartContractAddress == smartContractAddress,
                                              Asset.name == assetName,
                                              Asset.token_id == tokenId)
        existStatus = db.session.query(q.exists()).scalar()

        return existStatus

    @staticmethod
    def updateAsset(smart_contract_address: str, token_id: int, price: float, onSale: bool, metaData):
        asset = db.session.query(Asset).filter(Asset.token_id == token_id,
                                               Asset.smartContractAddress == smart_contract_address).first()
        print(asset)

        asset.price = price
        asset.onSale = onSale
        asset.metaData = metaData
        db.session.merge(asset)
        db.session.commit()

    @staticmethod
    def getAllTokenIds(address):
        token_ids = list(
            itertools.chain(*db.session.query(Asset.token_id).filter(Asset.smartContractAddress == address).all()))
        return token_ids
