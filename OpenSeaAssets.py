import json
import math
import sys

import requests

from Models.asset import Asset
from flask import jsonify


from Models.smartContract import SmartContract


class OpenSeaAssets:
    globalUrl = "https://api.opensea.io/api/v1/"

    @staticmethod
    def assetsGetRequest(payload={}):
        """
        :param payload: specify JSON parameters for querying Open Sea API
        :return: returns JSON of the data from Open Sea API
        """

        assets = "assets"
        url = OpenSeaAssets.globalUrl + assets

        response = requests.request("GET", url, params=payload)
        status_code = response.status_code
        print("Res Status Code: " + str(status_code))
        if status_code == 200:
            return response
        else:
            print(response.content)

    @staticmethod
    def pagination(smart_contract_address):
        """
        :param smart_contract_address: Input ETH address stored in MYSQL DB
        :return: int, number of request to get all of the data from Open Sea API
        """
        payloadPagination = {
            'asset_contract_address': smart_contract_address,
            'limit': 1,
            'order_by': 'pk',
            'offset': 0,
            'order_direction': 'desc'
        }

        res = OpenSeaAssets.assetsGetRequest(payloadPagination)
        totalAssetCount = float(res.json()['assets'][0]['token_id'])
        numberOfRequests = math.ceil(totalAssetCount / 50) + 1
        return numberOfRequests

    @staticmethod
    def getSingleAsset(smart_contract_address):

        asset = "asset"
        url = OpenSeaAssets.globalUrl + asset +f"/{smart_contract_address}/1/"
        response = requests.request("GET", url).json()

        if "success" in response:
            return 400
        else:
            if response['asset_contract']:

                smartContract = SmartContract(
                    smartContractAddress=response['asset_contract']['address'],
                    assetName=response['asset_contract']['name'],
                    assetDescription=response['asset_contract']['description'],
                    numberOfItems=int(response['collection']['stats']['total_supply']),
                    website=response['collection']['primary_asset_contracts'][0]['external_link'],
                    discord=response['collection']['discord_url'],
                    mediumUsername=response['collection']['medium_username'],
                    telegramUrl=response['collection']['telegram_url'],
                    twitterUsername="https://twitter.com/" + str(response['collection']['twitter_username']),
                    instagramUsername=response['collection']['instagram_username'],
                    safeListRequestStatus=response['collection']['safelist_request_status'])

                return smartContract

    @staticmethod
    def getAllAssets(smart_contract_address, totalNumberOfRequestsToBeMade):
        # Getting data from OpenSea API
        finalAssetsList = []
        for apiRequestNumber in range(0, totalNumberOfRequestsToBeMade):
            # Specify the payload
            payload = {
                'asset_contract_address': smart_contract_address,
                'limit': 50,
                'order_by': 'pk',
                'offset': apiRequestNumber * 50,
                'order_direction': 'asc'
            }
            res = OpenSeaAssets.assetsGetRequest(payload)
            assetsList = res.json()['assets']
            for asset in assetsList:

                assetOnSaleStatus = False
                assetPrice = None
                onSaleCheck = OpenSeaAssets.checkSaleStatus(asset)
                if onSaleCheck is not False:
                    assetOnSaleStatus = True
                    assetPrice = onSaleCheck

                # Check whether the asset exists and if does, update it, otherwise add it to the DB

                if Asset.checkIfInDBAsset(asset['name'], int(asset['token_id']), smart_contract_address):
                    # Updating existing asset
                    Asset.updateAsset(smart_contract_address=smart_contract_address,
                                      token_id=int(asset['token_id']),
                                      price=assetPrice, onSale=assetOnSaleStatus,
                                      metaData=asset['traits'])
                else:
                    finalAsset = Asset(smartContractAddress=smart_contract_address,
                                       name=asset['name'],
                                       token_id=int(asset['token_id']),
                                       onSale=assetOnSaleStatus,
                                       price=assetPrice,
                                       metaData=asset['traits'])
                    finalAssetsList.append(finalAsset)

            Asset.insertIntoDB(finalAssetsList)

    @staticmethod
    def checkSaleStatus(asset):
        """
        :param asset: pass a single JSON of an Asset
        :return: Returns Asset Class of an NFT with price if on sale
        """
        if asset['sell_orders'] is not None:
            current_price = int(float(asset['sell_orders'][0]['current_price']))
            decimals = asset['sell_orders'][0]['payment_token_contract']['decimals']
            return current_price / pow(10, decimals)
        else:
            return False
