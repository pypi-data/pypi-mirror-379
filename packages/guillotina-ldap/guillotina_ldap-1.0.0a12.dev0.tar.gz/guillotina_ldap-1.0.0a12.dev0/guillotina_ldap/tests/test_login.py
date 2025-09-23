import pytest
import json
import jwt

from guillotina.testing import TESTING_SETTINGS


@pytest.mark.asyncio
async def test_ldap_login(ldap, container_requester):
    async with container_requester as requester:
        resp, status_code = await requester(
            "POST",
            "/db/guillotina/@login",
            authenticated=False,
            data=json.dumps({"username": "anna", "password": "newsecret"}),
        )
        assert status_code == 200

        resp, status_code = await requester(
            "POST",
            "/db/guillotina/@login",
            authenticated=False,
            data=json.dumps({"username": "Anna", "password": "newsecret"}),
        )
        assert status_code == 200
        payload = jwt.decode(
            resp["token"], TESTING_SETTINGS["jwt"]["secret"], algorithms=["HS256"]
        )
        assert payload["id"] == "anna"
