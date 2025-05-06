#!/usr/bin/env python3
"""A function that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Parameters:
        mongo_collection: pymongo collection object

    Returns:
        A list of documents of mongo_collection
    """

    return mongo_collection.find()
