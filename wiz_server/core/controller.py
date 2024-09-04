import logging

import uuid

from wiz_server import db
from wiz_server.core.models import User, Journal, Category, Paper

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

    response = User.query.get(id).to_dict()
    return response


def read_journal_controller():
    response = Journal.query.all()
    return response


def create_journal_controller(name, impact_factor):
    id = str(uuid.uuid4())
    new_journal = Journal(
        id=id,
        name=name,
        impact_factor=impact_factor,
    )
    db.session.add(new_journal)
    db.session.commit()

    response = Journal.query.get(id).to_dict()
    return response


def read_category_controller():
    response = Category.query.all()
    return response


def create_category_controller(name, description):
    id = str(uuid.uuid4())
    new_category = Category(
        id=id,
        name=name,
        description=description,
    )
    db.session.add(new_category)
    db.session.commit()

    response = Category.query.get(id).to_dict()
    return response


def read_paper_controller():
    response = Category.query.all()
    return response


def create_paper_controller(title, abstract, publication_year, journal, category, doi, authors, citation_count, tags):
    # I am aware that this is a big vulnerability to allow strings to be used in filter/where clauses.
    journal_record = Journal.query.filter_by(name=journal).first().to_dict()
    if journal_record:
        journal_id = journal_record['id']
    cat = Category.query.filter_by(name=category).first().to_dict()
    if cat:
        category_id = cat['id']
    id = str(uuid.uuid4())
    new_paper = Paper(
        id=id,
        title=title,
        abstract=abstract,
        publication_year=publication_year,
        journal_id=journal_id,
        category_id=category_id,
        doi=doi,
        authors=authors,
        citation_count=citation_count
    )
    db.session.add(new_paper)
    db.session.commit()

    response = Paper.query.get(id).to_dict()
    return response
