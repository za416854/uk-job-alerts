
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import MongoClient
import os
from dotenv import load_dotenv
# uri = "mongodb+srv://z416854:Chris710!@clusterkris.pzdoz64.mongodb.net/?retryWrites=true&w=majority&appName=ClusterKris"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
    
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print("This is error")

#     print(e)
    
    

# 將這段連線字串換成你自己的（可放到 .env）。讓程式從根目錄的 .env 載入
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
MONGO_URI = os.getenv("MONGO_URI")

def save_jobs(jobs):
    client = MongoClient(MONGO_URI)
    db = client["job_alerts"]
    collection = db["uk_jobs"]

    inserted = 0
    for job in jobs:
        if not collection.find_one({"url": job["url"]}):  # 避免重複
            collection.insert_one(job)
            inserted += 1

    print(f"成功新增 {inserted} 筆新職缺。")
    client.close()
