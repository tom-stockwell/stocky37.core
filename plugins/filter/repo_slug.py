from ansible.module_utils.six.moves.urllib.parse import urlsplit


def repo_slug(repo, slug='-'):
    return urlsplit(repo).path.lstrip('/').replace('/', slug)


class FilterModule(object):
    @staticmethod
    def filters():
        return {
            'repo_slug': repo_slug,
        }

