import pytest
from gql import Client
from collection.get_country import COUNTRY



class TestCountry(object):
    @pytest.mark.usefixtures("graphql_client")
    def test_country_information(
        self,
        graphql_client: Client
    ):
        response = graphql_client.execute(
            COUNTRY,
            {
                "code": "UA"
            }
        )
        assert "errors" not in response, "You must get country information"
        assert response["country"]['awsRegion'] in "eu-north-1"
        assert response["country"]['capital'] in "Kyiv"
        assert response["country"]['phone'] in "380"
        assert response["country"]['code'] in "UA"