# from app import db
#
# class Passport(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     wallet_address = db.Column(db.String(42), unique=True, nullable=False)
#     data = db.Column(db.JSON)
#
#     def __repr__(self):
#         return f'<Passport {self.wallet_address}>'