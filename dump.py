#    Asset.updateAsset(token_id=101,smart_contract_address='0x370108cf39555e561353b20ecf1eaae89beb72ce', price=None, onSale=False, metaData=[{'trait_type': 'Top Eye',
 #  'value': 'Floating Apple',
 #  'display_type': None,
 #  'max_value': None,
 #  'trait_count': 181,
 #  'order': None},
 # {'trait_type': 'Mustache',
 #  'value': 'Esteemed Borpi',
 #  'display_type': None,
 #  'max_value': None,
 #  'trait_count': 613,
 #  'order': None},
 # {'trait_type': 'Body',
 #  'value': 'Floating Formes',
 #  'display_type': None,
 #  'max_value': None,
 #  'trait_count': 241,
 #  'order': None},
 # {'trait_type': 'Bottom Eye',
 #  'value': 'Eyeball',
 #  'display_type': None,
 #  'max_value': None,
 #  'trait_count': 191,
 #  'order': None},
 # {'trait_type': 'Mouth',
 #  'value': 'Smiling',
 #  'display_type': None,
 #  'max_value': None,
 #  'trait_count': 393,
 #  'order': None},
 # {'trait_type': 'Background',
 #  'value': 'Still Life',
 #  'display_type': None,
 #  'max_value': None,
 #  'trait_count': 205,
 #  'order': None},
 # {'trait_type': 'Hands',
 #  'value': 'Defeat',
 #  'display_type': None,
 #  'max_value': None,
 #  'trait_count': 312,
 #  'order': None},
 # {'trait_type': 'Hat',
 #  'value': 'Red Hat',
 #  'display_type': None,
 #  'max_value': None,
 #  'trait_count': 316,
 #  'order': None}])

# if len(allEventsSet) != 0:
                #     first = allEventsSet.pop()
                #     allEventsSet.add(first)
                #     # existingEvents: set
                #     existingEvents = TradingHistory.checkIfInDBTradingHistory(asset_contract_address,
                #                                                               first.token_id)
                #
                #     for event in range(len(existingEvents)):
                #         e = existingEvents.pop()
                #         existingEvents.add(TradingHistory(smartContractAddress=asset_contract_address,
                #                                           token_id=e.token_id,
                #                                           timeStamp=e.timeStamp.isoformat(),
                #                                           salePrice=e.salePrice,
                #                                           saleCurrency=e.saleCurrency,
                #                                           usdSalePrice=e.usdSalePrice))
                #     print(allEventsSet)
                #     print(existingEvents)
                #
                #     eventsToAddDB = allEventsSet - existingEvents
                #     print(f"Test: {eventsToAddDB}")
                #
                #     for record in eventsToAddDB:
                #         record.usdSalePrice = record.salePrice*float(OpenSeaEvents.CoinBaseAPIUSDPrice(record.saleCurrency, record.timeStamp))
                #
                #
                #     allEventsList = []
                #     allEventsSet = set()