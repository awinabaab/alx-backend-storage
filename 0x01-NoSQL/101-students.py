#!/usr/bin/env python3
"""A function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """Returns all students sorted by average score

    Parameters:
        mongo_collection: A pymongo collection object

    Returns:
        A list of all students sorted by their average score"""

    documents = mongo_collection.find()
    students = []

    for document in documents:
        topics = document.get('topics')
        scores = [topic.get('score') for topic in topics]
        average_score = sum(scores) / len(scores)

        document.update({"averageScore": average_score})
        students.append(document)

    top_students = sorted(students,
                          key=lambda student: student['averageScore'],
                          reverse=True
                          )

    return top_students
