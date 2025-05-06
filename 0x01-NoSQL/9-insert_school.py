#!/usr/bin/env python3
"""A function that inserts a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on **kwargs

    Parameters:
        mongo_collection: A pymongo collection object
        kwargs (dict): Attributes of the new document

    Returns:
        The id of the newly inserted document"""

    school = mongo_collection.insert_one(kwargs)

    return school.inserted_id
