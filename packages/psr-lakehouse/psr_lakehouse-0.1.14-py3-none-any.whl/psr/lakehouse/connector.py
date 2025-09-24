import json
import os

import boto3
import sqlalchemy


class Connector:
    _instance = None

    _region_name = "us-east-1"
    _is_initialized: bool = False
    _user: str
    _password: str
    _endpoint: str
    _port: str
    _dbname: str

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def initialize(
        self,
        aws_access_key_id: str = os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key: str = os.getenv("AWS_SECRET_ACCESS_KEY"),
        postgres_password: str = os.getenv("POSTGRES_PASSWORD")
    ):
        
        if os.getenv("ENVIRONMENT") == "local":
            self._user = os.getenv("POSTGRES_USER")
            self._password = os.getenv("POSTGRES_PASSWORD")
            self._endpoint = os.getenv("POSTGRES_SERVER")
            self._port = os.getenv("POSTGRES_PORT")
            self._dbname = os.getenv("POSTGRES_DB")
            self._is_initialized = True
        else:
            aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
            aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
            postgres_password = os.getenv("POSTGRES_PASSWORD")
            boto_kwargs = {
                "region_name": self._region_name,
                "aws_access_key_id": aws_access_key_id,
                "aws_secret_access_key": aws_secret_access_key,
            }

            self._rds = boto3.client("rds", **boto_kwargs)
            self._secrets_manager = boto3.client("secretsmanager", **boto_kwargs)

            secret_response = self._secrets_manager.get_secret_value(SecretId="psr-lakehouse-secrets")
            secret = json.loads(secret_response["SecretString"])
            self._user = secret["POSTGRES_USER"]
            self._password = secret.get("POSTGRES_PASSWORD", postgres_password)
            self._endpoint = secret["POSTGRES_SERVER"]
            self._port = secret["POSTGRES_PORT"]
            self._dbname = secret["POSTGRES_DB"]

            self._is_initialized = True

    def engine(self) -> sqlalchemy.Engine:
        if self._is_initialized is False:
            self.initialize()

        # token = self._rds.generate_db_auth_token(
        #     DBHostname=self._endpoint,
        #     Port=self._port,
        #     DBUsername=self._user,
        #     Region=self._region_name,
        # )
        
        if os.getenv("ENVIRONMENT") == "local":
            connection_string = f"postgresql+psycopg://{self._user}:{self._password}@{self._endpoint}:{self._port}/{self._dbname}"
            return sqlalchemy.create_engine(connection_string)
        
        connection_string = f"postgresql+psycopg://{self._user}:{self._password}@{self._endpoint}:{self._port}/{self._dbname}?sslmode=require&sslrootcert=SSLCERTIFICATE"

        return sqlalchemy.create_engine(connection_string)


connector = Connector()
