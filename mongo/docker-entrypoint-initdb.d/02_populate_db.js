let todolists = [
    {
        "name": "name_1",
        "items": [
            {
                "id": ObjectId(),
                "text": "text_1_1",
                "due_date": ISODate("2021-07-16T19:20:30"),
                "finished": true
            },
            {
                "id": ObjectId(),
                "text": "text_1_2",
                "due_date": ISODate("2021-07-16T19:20:30"),
                "finished": true
            },
        ]
    },
    {
        "name": "name_2",
        "items": [
            {
                "id": ObjectId(),
                "text": "text_2_1",
                "due_date": ISODate("2021-07-16T19:20:30"),
                "finished": true
            },
            {
                "id": ObjectId(),
                "text": "text_2_2",
                "due_date": ISODate("2021-07-16T19:20:30"),
                "finished": true
            },
        ]
    },
]

db.createCollection("todolists");
db.todolists.insert(todolists);
