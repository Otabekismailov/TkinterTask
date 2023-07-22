class Task:
    def __init__(self, orginal_language, created_at, tarns_language,):
        self.orginal_language = orginal_language
        self.created_at = created_at
        self.tarns_language = tarns_language

    def get_attrs_as_dict(self):
        return {
            "orginal_language": self.orginal_language,
            "created_at": self.created_at,
            "tarns_language": self.tarns_language
        }
