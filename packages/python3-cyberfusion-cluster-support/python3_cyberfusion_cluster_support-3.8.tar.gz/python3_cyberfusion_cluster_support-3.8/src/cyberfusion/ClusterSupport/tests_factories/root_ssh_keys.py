"""Factories for API object."""

from typing import Optional

import factory
import factory.fuzzy

from cyberfusion.ClusterSupport.root_ssh_keys import RootSSHKey
from cyberfusion.ClusterSupport.tests_factories import BaseBackendFactory


class _RootSSHKeyFactory(BaseBackendFactory):
    """Factory for specific object."""

    class Meta:
        """Settings."""

        model = RootSSHKey

        exclude = ("cluster",)

    name = factory.Faker("user_name")
    public_key: Optional[str] = None
    private_key: Optional[str] = None
    cluster = factory.SubFactory(
        "cyberfusion.ClusterSupport.tests_factories.clusters.ClusterWebFactory"
    )
    cluster_id = factory.SelfAttribute("cluster.id")


class RootSSHKeyPrivateFactory(_RootSSHKeyFactory):
    """Factory for specific object."""

    private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAxNh+dKVBEkb8zw/4SmxdyenAaKQ5DuY4ifJabHloci7Uya6+
GPOpgPStC4/FxMlLNuw6FfFuCX2IQG1R6TcpCZd6XpyTTqn22nGlhULF6H3hSWmH
Z7MjlcysdMC+c/Lfe7yIlTQFy6exvQqbSi/cxX+b9q/TdAyMuuL6mm2r25+4S6W+
UCg25bkcgyOsf2HuyTLZaDQd15OU0/N3P32ykIMzLM9iqkMwbOyOiy5ECKpl5Yvm
UTR592p+JyfL+uqw9tdMeSXJmE8rPSVexGfGIV98ZmfpSxycpLEJQ5LBaBhm7DAs
BbuL161iiHy0GlN261F15RHL4cK84HZDkJ1axwIDAQABAoIBABgajnmIFsy/JovQ
X831MRLdbbMikN4TMM8rfwkTYMfClknP/PUfOR1SWLI2u7faEjy6dm5jbt74oSuK
d2JAX+UNyG03bQ5P36tmCSelQoiyiVis9GitVeks890kEO4vyk/jiTID+cWzVh9Y
4iUWcUk51AZEB3eJZd4olxk73rR4xl0tVo52Uw6ZqXHBjtrdAlILeepMlkAL4ZpQ
2D8x0TMOACFbmyfqaIH8uxvJdZTu1dc+eXj3UspLh9b4ykLBFQ9eoz/yhQYxIuiO
5WVIz01IxOberoDwnB4mSHM5iuCUA2Md1qpFjzrJx9IMPbpQra5tFJKDZONAsb/a
e7Sy2RECgYEA6E8hcqgPTz24ahk2eOZ9CEdBcPHpBnJjJ0b3qJ3nph0ZNr8x1SVC
V9+jnT6PXu+rx+P+lhFAgIDmZnbZru60GwF+wYsoHVrAFDPg8AP2oCJ0GgQ9PUkR
CcpIq5YLGxFwM27/Aqfgvt8F/zb7AKMjnN/EyQ+4kWMVdVV+huwILv8CgYEA2OuF
/qfYi6BS3ubAngj/BVp9Ifg1EAm6DpvuO0hLjIC1xnkr+Kfys1fwo7ODUj98JvOZ
/Kgth8hMU5TZzCm98dlIgkxDgOWrII1fa/h7+c+Tv4s8VS/6YKZVZeRVuPblUr9I
Q65M1ArF3YCGlsT6lA1wcYMD0Y3XxUbB5zlZHDkCgYEAnq6erFD71CbWtzJtsPvP
4D28B8hWYh70d7nUJYtm1mL9/BVxlqSSwq9ydVBsYm7YKfwkxKEYLC7gMpFwdDt9
Lw1AZjgFuLdqiOI+/fPXHN8r6zGGGzyztLpGFV6yS1UIDTn+WvQNYpO45vHJVlAZ
XWjEZIqmijjiSXmSqdrEZEUCgYAjKgsOvSbde5/zgnS3Kb4tn/2pBBOWBf2jYKO9
+HpGzJarFfmK1a8CY78eynr/WktGBTdxPdIjsNSut/KWpi2khxS6CqLmwlR7cm+F
kUKHvJ627ltZc+2ivVQasGk1EtEaGOgeEKNjvFtXDP7Ecios1gDkZdi4n8XatR25
3hIUAQKBgGNeH/1/eIJJdwO+CYiG7ygA8bfMuW4ySG8DCeTrxIAUCAVSOjpalX7I
0iTXXb7QsJJS5D6BxFOyzL6Yl2EAUos+EJPffgTJsnPwaPjAvq85pxGXSQdyRlR1
7SYTOWs5heS2h4vSkdv8mSBmiZP73QxdyqWTne0k6hY8kzn4OuiP
-----END RSA PRIVATE KEY-----\n"""


class RootSSHKeyPublicFactory(_RootSSHKeyFactory):
    """Factory for specific object."""

    public_key = """ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCY5L+Iw+i+2sGvKucTCP5ou4IHpSsaDsu3ob4KkFeuRKA2I715gXL4wwkK8FZMSqyeNfOp7TKg+6mAEh1BBsAHUABRjQ//WYM5dwcOSHuPeqRWTnGxhgzGEER03pBWMRVtuiITWZvcCjKTjhvyLvTcadFHNERa3oB0pwd+2a1g0eZ/TAMh1iPYqkxT4v9Gvf7rbEm9vKrkcVFLlXOXoIB53ppTEZZkL17pm/C1ttTDHX6+1rLWmYl3f77DWJnznISfITsjzRcsjFZVazqwAmeeKHKkkMlP9VufDpjCu+GbcC4xGRh4xIKC+H6zpX/vbi+MU+5NEvt8Owm8NT5IO6/5\n"""
