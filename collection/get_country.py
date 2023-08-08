"""get_kyc.py"""
from gql import gql

COUNTRY = gql(
    """
    query ($code: ID!){
      country(code:$code){
        awsRegion
        capital
        code
        phone
      }
    }
    """
)
