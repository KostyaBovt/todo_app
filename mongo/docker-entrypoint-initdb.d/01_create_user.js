db.createUser(
    {
        user: "user",
        pwd: "pass",
        roles:[
            {
                role: "readWrite",
                db:   "todo_db"
            }
        ]
    }
);
