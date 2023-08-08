import os
import pytest
from dotenv import load_dotenv
from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport


@pytest.fixture(scope="class")
def graphql_client() -> Client:
    # Загрузить переменные окружения из файла .env
    load_dotenv()
    # Create a GraphQL client using the defined transport
    return Client(
        transport=AIOHTTPTransport(url=os.getenv("URL_TRANSPORT")),
        fetch_schema_from_transport=True
        )