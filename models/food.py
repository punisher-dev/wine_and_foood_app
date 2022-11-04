from init import db, ma
# This is one of the places where the init items are imported

from marshmallow import fields

# the class Food uses Sqlalchemy to create a table structure with column names and data types.
class Food(db.Model):
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # wine_id = db.Column(db.Integer, db.ForeignKey('wines.id'), nullable=False)

    user = db.relationship("User")
    # wine = db.relationship("Wine")



# Marshmallow ma converts these data types into db readable format via the Schema and with the use of marshmallow fields each column item can be retrieved by the controller on a Model View Control (MVC) structure.
class FoodSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    # wine = fields.Nested('WineSchema')
    
    class Meta:
        fields = ('id', 'name', 'description', 'type', 'date', 'user')
        ordered=True