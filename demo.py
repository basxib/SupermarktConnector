from supermarktconnector.jumbo import JumboConnector
connector = JumboConnector()
res = connector.search_products(query='Smint', size=1, page=0)
print (res)