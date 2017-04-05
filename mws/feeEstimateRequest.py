
class FeeEstimateRequest(object):
    def __init__(self,
                 marketplaceId,
                 listingPrice,
                 shippingPrice,
                 points=0,
                 asin=None,
                 sku=None,
                 isAmazonFulfilled=False,
                 listingPriceCurrencyCode='USD',
                 shippingPriceCurrencyCode = 'USD'):
        if not asin and not sku:
            raise ValueError("sku or asin must be defined")

        self.marketplaceId = marketplaceId
        self.listingPrice = listingPrice
        self.listingPriceCurrencyCode = listingPriceCurrencyCode
        self.shippingPrice = shippingPrice
        self.shippingPriceCurrencyCode = shippingPriceCurrencyCode
        self.idType = asin and 'ASIN' or 'SKU'
        self.idValue = asin or sku
        self.isAmazonFulfilled = isAmazonFulfilled
        self.points = points
