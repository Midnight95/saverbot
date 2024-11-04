from urllib import parse

DOMAIN_LIST = [
        'tiktok.txt',
        'instagram.txt',
        'pintrest.txt'
        ]
ALLOWED_SOCIAL_MEDIA = (
        'tiktok',
        'instagram',
        'pintrest'
        )


def generate_urls() -> set:
    allowed_urls = set()
    for file in DOMAIN_LIST:
        with open(f'saverbot/parser/{file}') as f:
            for line in f:
                allowed_urls.add(line[0:-1])
    return allowed_urls


def parse_url(url: str) -> None | str:
    allowed = generate_urls()
    u = parse.urlparse(url)
    if u.scheme not in ('http', 'https', ''):
        return

    domain = u.netloc
    if domain not in allowed:
        return

    for site in ALLOWED_SOCIAL_MEDIA:
        if site in domain:
            return site
