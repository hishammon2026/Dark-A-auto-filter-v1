import motor.motor_asyncio
from config import Config

class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self._db = self._client[database_name]
        self._col = self._db.files

    async def save_file(self, file_name, file_id, file_size, caption):
        file_data = {
            'file_name': file_name,
            'file_id': file_id,
            'file_size': file_size,
            'caption': caption
        }
        await self._col.update_one({'file_id': file_id}, {'$set': file_data}, upsert=True)

    async def get_search_results(self, query):
        cursor = self._col.find({"file_name": {"$regex": query, "$options": "i"}})
        return await cursor.to_list(length=10)

db = Database(Config.DATABASE_URI, Config.DATABASE_NAME)
