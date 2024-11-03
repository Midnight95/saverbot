from urllib import parse


def generate_urls() -> set:
    urls = set()
    with open('saverbot/parser/tiktok.txt') as f:
        for line in f:
            urls.add(line)

    return urls


def parse_url(url: str) -> None | str:
    allowed = generate_urls()
    u = parse.urlparse(url)
    if u.netloc == '' or u.scheme not in ('http', 'https', ''):
        return
    if u.netloc not in allowed:
        return

    return u.netloc
