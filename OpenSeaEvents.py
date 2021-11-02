import requests
import Models.tradingHistory as TradingHistory
import Models.asset as Asset


class OpenSeaEvents:
    globalUrl = "https://api.opensea.io/api/v1/"
    events = "events"
    url = globalUrl + events

    @staticmethod
    def eventsGetRequest(asset_contract_address: str):
        """
        :param asset_contract_address: Contract address of the NFT
        :param token_id: Token ID of a specific asset
        :return: all events for a particular asset
        """

        params = {
            'asset_contract_address': asset_contract_address,
            'only_opensea': 'false'
        }

        event_types = ['successful', 'offer_entered','created', 'transfer'] #
        for event_type in event_types:
            print(f"event_type: {event_type}")
            params['event_type'] = event_type

            if not TradingHistory.checkIfInDBSmartContractAddressTradingHistory(address=asset_contract_address,
                                                                              event_type=event_type):
                print("Downloading all data")
                # No pricing history exists
                OpenSeaEvents.GetAllTradingHistory(asset_contract_address, params=params)
            else:
                # Some pricing history already exists
                print("Some pricing history already exists")
                occurred_after = str(TradingHistory.getLatestEventDate(address=asset_contract_address,
                                                                       event_type=event_type).timestamp())
                params['occurred_after'] = occurred_after
                OpenSeaEvents.GetAllTradingHistory(asset_contract_address, params=params)
                del params['occurred_after']

    @staticmethod
    def GetAllTradingHistory(asset_contract_address: str, params: dict):
        number_of_events = 300
        offset = 0
        limit = 300

        print(f"Params: {params}")
        while number_of_events >= 300:
            params['offset'] = offset
            params['limit'] = limit
            print(f"Offset:{offset}")
            allEventsList = []
            allEventsSet = set()

            headers = {"Accept": "application/json"}

            response = requests.request("GET", OpenSeaEvents.url, headers=headers, params=params)
            print(response.url)
            status_code = response.status_code
            print("Res Status Code: " + str(status_code))
            if status_code != 200:
                print(response.content)
                break
            responseBody = response.json()['asset_events']
            number_of_events = len(responseBody)
            if number_of_events == 300:
                offset += 301
            elif number_of_events == 0:
                # In the case no events exist for an asset
                break

            allEventsList.extend(responseBody)

            for event in allEventsList:
                saleCurrency, cryptoPrice, USDTSalePrice = OpenSeaEvents.EventTypeCheck(event=event)

                try:
                    print(f"ID: {int(event['asset']['token_id'])}")
                    print(event['created_date'])

                    tradingHistoryEntity = TradingHistory(smartContractAddress=asset_contract_address,
                                                          token_id=int(event['asset']['token_id']),
                                                          # timeStamp=transactionTimeStamp,
                                                          timeStamp=event['created_date'],
                                                          eventType=event['event_type'],
                                                          salePrice=cryptoPrice,
                                                          saleCurrency=saleCurrency,
                                                          usdSalePrice=USDTSalePrice)

                    allEventsSet.add(tradingHistoryEntity)
                except TypeError as e:
                    pass
            # TODO: remove indentation
            TradingHistory.insertIntoDB(list(allEventsSet))



    @staticmethod
    def EventTypeCheck(event):
        match event['event_type']:
            case 'created': return OpenSeaEvents.Created_ReturnFullTransactionData(event)
            case 'successful' | 'offer_entered': return OpenSeaEvents.ReturnFullTransactionData(event)
            # case 'offer_entered':return OpenSeaEvents.ReturnFullTransactionData(event)
            case 'transfer': return None, None, None
            case _: return None, None, None

    @staticmethod
    def Created_ReturnFullTransactionData(event):
        factor = event['payment_token']['decimals']
        saleCurrency = event['payment_token']['symbol']
        try:
            tempPrice = int(event['ending_price'])
        except TypeError:
            tempPrice = 0
        cryptoPrice = tempPrice * (10 ** (-factor))
        USDTSalePrice = cryptoPrice * float(
            OpenSeaEvents.CoinBaseAPIUSDPrice(saleCurrency, event['created_date']))
        return saleCurrency, cryptoPrice, USDTSalePrice

    @staticmethod
    def ReturnFullTransactionData(event):
        factor = event['payment_token']['decimals']
        saleCurrency = event['payment_token']['symbol']
        try:
            tempPrice = int(event['total_price'])
        except TypeError:
            tempPrice = 0
        cryptoPrice = tempPrice * (10 ** (-factor))
        USDTSalePrice = cryptoPrice * float(
            OpenSeaEvents.CoinBaseAPIUSDPrice(saleCurrency, event['created_date']))
        return saleCurrency, cryptoPrice, USDTSalePrice

    @staticmethod
    def CoinBaseAPIUSDPrice(symbol: str, dateTime: str):
        """
        :param symbol: Cryto ticker
        :param dateTime: date time of sale
        :return: USDT equivalent of crypto at that time
        """
        if symbol == 'WETH':
            symbol = 'ETH'
        try:
            dict_dt_earlier = {'date': dateTime}
            url = f'https://api.coinbase.com/v2/prices/{symbol}-USD/spot/'
            r = requests.get(url, params=dict_dt_earlier)
            return r.json()['data']['amount']

        except requests.exceptions.HTTPError as err:
            raise SystemError(err)