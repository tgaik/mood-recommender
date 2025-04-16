from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    genre = db.Column(db.String(100), nullable = False)
    desc = db.Column(db.String(500), nullable = True)
    img_url = db.Column(db.String(500), nullable = True)

    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "genre":self.genre,
            "desc":self.desc,
            "imgUrl":self.img_url

        }