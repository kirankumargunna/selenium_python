from pymongo import MongoClient

# connect to mongodb server
client=MongoClient("mongodb://localhost:27017/")

# connect to database
db=client["test_datbase"]

#connect to schema
collection = db["schema1"]

print("connected to mongo db ")

# Insert a single document
single_document = {"name": "Alice", "age": 25, "email": "alice@example.com"}
insert_result = collection.insert_one(single_document)
print(f"Inserted document with ID: {insert_result.inserted_id}")

# Insert multiple documents
multiple_documents = [
    {"name": "Bob", "age": 30, "email": "bob@example.com"},
    {"name": "Charlie", "age": 35, "email": "charlie@example.com"}
]
insert_many_result = collection.insert_many(multiple_documents)
print(f"Inserted documents with IDs: {insert_many_result.inserted_ids}")


# Find one document
one_document = collection.find_one({"name": "Alice"})
print(f"Found one document: {one_document}")

# Find multiple documents
multiple_documents = collection.find({"age": {"$gte": 30}})  # Query for age >= 30
print("Documents with age >= 30:")
for doc in multiple_documents:
    print(doc)

# Get all documents
all_documents = collection.find()
print("All documents:")
for doc in all_documents:
    print(doc)


# Update one document
update_result = collection.update_one(
    {"name": "Alice"},  # Query: Find Alice
    {"$set": {"age": 26}}  # Update: Set age to 26
)
print(f"Matched {update_result.matched_count} document(s), Modified {update_result.modified_count} document(s)")

# Update multiple documents
update_many_result = collection.update_many(
    {"age": {"$gte": 30}},  # Query: Find documents with age >= 30
    {"$set": {"status": "senior"}}  # Update: Add a new field 'status'
)
print(f"Matched {update_many_result.matched_count} document(s), Modified {update_many_result.modified_count} document(s)")
