from app import celery

from OpenSeaAssets import OpenSeaAssets


@celery.task
def getAssets(SmartContractAddress):
    # Getting Number of request to be sent to get all of the data
    totalNumberOfRequestsToBeMade = OpenSeaAssets.pagination(SmartContractAddress)
    # # Getting all the assets downloaded
    OpenSeaAssets.getAllAssets(SmartContractAddress, totalNumberOfRequestsToBeMade)
    # return f"Assets downloading for: {SmartContractAddress}", 200
