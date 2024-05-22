import falcon
from falcon_autocrud.middleware import Middleware
from resources import RetailerCollectionResource, RetailerResource
from sqlalchemy import create_engine

# Update the database connection string for MySQL
db_engine = create_engine(
    'mysql+pymysql://root@127.0.0.1/falcon_db')

# Initialize Falcon app
app = falcon.API(middleware=[Middleware()])

# Add routes for RetailerCollectionResource and RetailerResource
app.add_route('/retailers', RetailerCollectionResource(db_engine))
app.add_route('/retailers/{id}', RetailerResource(db_engine))
