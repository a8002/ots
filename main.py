from fastapi import FastAPI, HTTPException
from db import get_database_connection

app = FastAPI()

@app.get("/v1/categories")
async def get_categories():
    db = get_database_connection()
    cursor = db.cursor()

    categories = []

    cursor.execute("SELECT * FROM categories")
    
    for category in cursor.fetchall():
        categories.append({"slug": category[1], "name": category[2]})

    db.close()

    return {
        "message": "success",
        "categories": categories
    }

@app.get("/v1/channels")
async def get_channels(category = None):
    db = get_database_connection()
    cursor = db.cursor()

    channels = []

    if category:
        cursor.execute("SELECT * FROM channels WHERE category_slug=?", [category])
    else:
        cursor.execute("SELECT * FROM channels")

    for category in cursor.fetchall():
        channels.append({
            "slug": category[1],
            "name": category[2],
            "icon_url": category[3],
            "supported_quality": category[4].split(','),
            "stream_url": category[5],
            "category_slug": category[6],
            "category_name": category[7]
        })

    db.close()

    if len(channels) == 0:
        raise HTTPException(status_code=404, detail="selected category not found!")

    return {"message": "success", "channels": channels}