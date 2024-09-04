import logging

import uuid

from wiz_server import db
from wiz_server.core.models import User

logger = logging.getLogger(__name__)


def create_user_controller(email, username, name, password):
    # request_form = request.form.to_dict()
    id = str(uuid.uuid4())
    new_user = User(
        id=id,
        email=email,
        username=username,
        name=name,
        password_hash=password
    )
    db.session.add(new_user)
    db.session.commit()

    response = User.query.get(id)
    return response
