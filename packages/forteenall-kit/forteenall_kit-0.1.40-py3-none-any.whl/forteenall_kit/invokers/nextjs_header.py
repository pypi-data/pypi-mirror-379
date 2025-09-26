class LinkDefinition:
    pass

class HeaderFeatureData:
    pass

class Feature:
    def __init__(self, name, manager, options, invokerType):
        pass
    def _validate_fields(self):
        pass
    def _generate_link_code(self, link, indent):
        pass
    def _generate_header_code(self):
        pass
    def execute(self):
        pass
