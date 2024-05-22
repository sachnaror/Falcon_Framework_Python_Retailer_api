from falcon_autocrud.resource import CollectionResource, SingleResource
from models import *


# /retailers
class RetailerCollectionResource(CollectionResource):
    model = Retailer
# /retailers/{id}


class RetailerResource(SingleResource):
    model = Retailer
