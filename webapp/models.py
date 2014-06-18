import datetime

from webapp.meta import db


# ================================
# Define models
# ================================
class User(db.Model):
    """User object
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(60), index=True, nullable=False)
    password_reset_requests = db.relationship(
        'PasswordResetRequest',
        backref=db.backref('user'))
    account_verification_requests = db.relationship(
        'AccountVerificationRequest',
        backref=db.backref('user'))

    def __repr__(self):
        return '<User %r>' % self.email

    # ===========================
    # Flask-Login methods
    # ===========================
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


class PasswordResetRequest(db.Model):
    """PasswordResetRequest object
    """
    key = db.Column(db.String(64), primary_key=True)
    fk_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_ts = db.Column(db.DateTime, default=datetime.datetime.utcnow, \
                              nullable=False)


class AccountVerificationRequest(db.Model):
    """AccountVerificationRequest object
    """
    key = db.Column(db.String(64), primary_key=True)
    fk_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_ts = db.Column(db.DateTime, default=datetime.datetime.utcnow, \
                              nullable=False)
