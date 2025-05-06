#!/usr/bin/env python3
"""Provides some stats about Nginx logs store in MongoDB"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    collection = db.nginx

    document_count = collection.count_documents({})
    print(f"{document_count} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_logs = {}
    for method in methods:
        document_count = collection.count_documents({"method": method})
        method_logs.update({method: document_count})

    print("Methods:")

    for key, value in method_logs.items():
        print(f"\tmethod {key}: {value}")

    method_path_count = collection.count_documents({
                                                    "method": "GET",
                                                    "path": "/status"
                                                    })
    print(f"{method_path_count} status check")

    ips = collection.aggregate([
                                {"$group": {"_id": "$ip",
                                            "count": {"$sum": 1}
                                            }
                                 },
                                {"$sort": {"count": -1}},
                                {"$limit": 10}
                                ])

    print("IPs:")
    for ip in ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")
