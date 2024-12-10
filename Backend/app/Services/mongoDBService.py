from bson.json_util import dumps
from bson.objectid import ObjectId


class MongoDBService:
    def __init__(self, db):
        """
        Initialize the MongoDB service with the provided database instance.
        :param db: The database instance (e.g., from current_app.db).
        """
        self.db = db

    def get_all(self, collection_name):
        """
        Retrieve all documents from the specified collection.
        :param collection_name: The name of the collection.
        :return: A list of JSON-like dictionaries.
        """
        cursor = self.db[collection_name].find()
        return list(cursor)  # Convert cursor to a list of dictionaries

    def get_one(self, collection_name, document_id):
        """
        Retrieve a single document by its ObjectId.
        :param collection_name: The name of the collection.
        :param document_id: The ObjectId of the document to retrieve.
        :return: A JSON-like dictionary, or None if not found.
        """
        return self.db[collection_name].find_one({"_id": ObjectId(document_id)})

    def insert_one(self, collection_name, data):
        """
        Insert a single document into the specified collection.
        :param collection_name: The name of the collection.
        :param data: A dictionary representing the document to insert.
        :return: The inserted document's ID as a string.
        """
        result = self.db[collection_name].insert_one(data)
        return str(result.inserted_id)

    def update_one(self, collection_name, document_id, update_data):
        """
        Update a single document by its ObjectId.
        :param collection_name: The name of the collection.
        :param document_id: The ObjectId of the document to update.
        :param update_data: A dictionary with the fields to update.
        :return: A boolean indicating if the update was successful.
        """
        result = self.db[collection_name].update_one(
            {"_id": ObjectId(document_id)}, {"$set": update_data}
        )
        return result.modified_count > 0

    def delete_one(self, collection_name, document_id):
        """
        Delete a single document by its ObjectId.
        :param collection_name: The name of the collection.
        :param document_id: The ObjectId of the document to delete.
        :return: A boolean indicating if the deletion was successful.
        """
        result = self.db[collection_name].delete_one({"_id": ObjectId(document_id)})
        return result.deleted_count > 0
