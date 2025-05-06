#!/usr/bin/env python3
"""A function that returns a list of schools having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools having a specific topic

    Parameters:
        mongo_collection: A pymongo collection object
        topic (str): Name of the topic to search for

    Returns:
        A list of schools having topic in the topics attribute"""

    return mongo_collection.find({"topics": topic})
