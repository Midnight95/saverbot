from urllib import parse

DOMAIN_LIST = [
        'tiktok.txt',
        'instagram.txt',
        'pinterest.txt'
        ]
ALLOWED_SOCIAL_MEDIA = (
        'tiktok',
        'instagram',
        'pinterest'
        )


async def generate_urls() -> set:
    allowed_urls = set()
    for file in DOMAIN_LIST:
        with open(f'saverbot/parser/{file}') as f:
            for line in f:
                allowed_urls.add(line[0:-1])
    return allowed_urls


async def parse_url(url: str) -> None | str:
    u = parse.urlparse(url)
    allowed = await generate_urls()
    if u.scheme not in ('http', 'https', ''):
        return

    current = u.netloc
    if current not in allowed:
        return

    return current
