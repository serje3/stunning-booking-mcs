import os

env_get = os.environ.get

SECRET_KEY = env_get("SECRET_KEY", "blablbalbbalbslasddajashfaioshohiadfsfdjsafasdjhfadshjhksdfjbjhafsdjhsdf")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
DATABASE_URL = env_get("AUTH_DATABASE_URL", "postgresql://auth_user:auth_password@localhost:5432/auth_database")
KAFKA_BOOTSTRAP_SERVERS = env_get("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
