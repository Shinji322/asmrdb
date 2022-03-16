rm ./db/test.db
python recreate_db.py
echo .schema | sqlite3 ./db/test.db > ./db/test.schema.sql
