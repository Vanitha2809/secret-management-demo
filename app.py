import os

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")

print("Database User:", db_user)

# NEVER print password in real projects (important for security)
print("Database Password: ******")


