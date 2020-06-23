from app import db

class DocumentDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    did = db.Column(db.String(64), index=True, unique=False)
    wid = db.Column(db.String(64), index=True, unique=False)
    eid = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Document {} Workspace {} Element {}>'.format(self.did, self.wid, self.eid)    
        