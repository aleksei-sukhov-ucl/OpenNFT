# This is where all the endpoint will be
from app import app

import requests
from flask import request, jsonify, Response

from Models.smartContract import SmartContract
from OpenSeaAssets import OpenSeaAssets
from app.celeryTasks import getAssets


@app.route("/", methods=['GET', 'POST'])
def default():
    pass


@app.route("/AddSmartContractAddress", methods=['GET'])
def insertSmartContract():
    """
    Desc: Add a smart contract address to database
    :param: Smart Contract Address
    :return: Successfully added/ Unsuccessful
    """
    SmartContractAddress = request.args.get('SmartContractAddress')

    if SmartContract.checkSmartContractLocalDB(SmartContractAddress):
        return "Smart Contract Already Exists", 400
    else:
        SmartContractObject = OpenSeaAssets.getSingleAsset(smart_contract_address=SmartContractAddress)
        if SmartContractObject == 400:
            return "Smart Contract Address Doesn't Exist", 400

        res = SmartContract.insertIntoDB(smartContract=[SmartContractObject])

        if res == 200:
            return "Smart Contract Successfully Added", 200
        else:
            return "Smart Contract Not Added", 400


@app.route("/AddAssetsForSmartContractAddress", methods=['GET'])
def getAllAssets():
    SmartContractAddress = request.args.get('SmartContractAddress')

    # Check if smart contract exist on Open Sea
    SmartContractObject = OpenSeaAssets.getSingleAsset(smart_contract_address=SmartContractAddress)
    if SmartContractObject == 400:
        return "Smart Contract Address Doesn't Exist", 400

    # Check if smart contract is in local DB, if not, add it
    if not SmartContract.checkSmartContractLocalDB(SmartContractAddress):
        # Add smart contract object and download assets
        res = SmartContract.insertIntoDB(smartContract=[SmartContractObject])

        if res == 400:
            return "Smart Contract Not Added", 400

    getAssets.delay(SmartContractAddress)
    return f"Assets downloading for: {SmartContractAddress}", 200
    # q.enqueue(getAssets, args={'SmartContractAddress': SmartContractAddress})



# @app.route("/AddSmartContractAddressAndAssets", methods=['GET'])
# def insertSmartContract():
#     SmartContractAddress = request.args.get('SmartContractAddress')
#     print(SmartContract.checkSmartContract(SmartContractAddress))
#
#     if SmartContract.checkSmartContract(SmartContractAddress):
#         return "Smart Contract Already Exists", 400
#     else:
#         res = OpenSeaAssets.getSingleAsset(smart_contract_address=SmartContractAddress)
#         print(res)
#         if res == 200:
#             return "Smart Contract Successfully Added", 200
#         else:
#             return "Smart Contract Not Added", 400


# # Getting Number of request to be sent to get all of the data
# totalNumberOfRequestsToBeMade = OpenSeaAssets.pagination(SmartContractAddress)
# # # Getting all the assets downloaded
# OpenSeaAssets.getAllAssets(SmartContractAddress, totalNumberOfRequestsToBeMade)
#
# return SmartContractAddress
