#!/usr/bin/env python3
"""A function that changes all topics of a school document based in the name"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name

    Parameters:
        mongo_collection: A pymongo collection object
        name (str): Name of the school
        topics (list[str]): List of topics to be added to the school
    """

    mongo_collection.update_many({"name": name},
                                 {"$set": {"topics": topics}}
                                 )
