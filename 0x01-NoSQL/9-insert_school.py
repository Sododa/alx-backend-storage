#!/usr/bin/env python3
"""task 9
"""


def insert_school(mongo_collection, **kwargs):
    """Function that inserts a new document in a collection based on
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
