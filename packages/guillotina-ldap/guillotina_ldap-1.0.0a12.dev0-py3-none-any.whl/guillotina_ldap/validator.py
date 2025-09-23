from guillotina.component import get_utility
from guillotina_ldap.interfaces import ILDAPUsers
from guillotina.auth import find_user
import bonsai


class LDAPPasswordValidator:
    for_validators = "basic"

    async def validate(self, token):
        users = get_utility(ILDAPUsers)
        try:
            login_id, name = await users.validate_user(token["id"], token["token"])
        except bonsai.AuthenticationError:
            return None

        if login_id is not None:
            if name is None:
                name = login_id
            user = users.create_g_user(login_id, name)
            return user
        else:
            return None
