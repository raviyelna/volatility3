from volatility.framework.configuration import requirements
from volatility.framework.symbols import intermed
from volatility.framework.symbols.windows import extensions
from volatility.framework.symbols.windows.extensions import registry


class WindowsKernelIntermedSymbols(intermed.IntermediateSymbolTable):
    provides = {"type": "interface"}

    def __init__(self, context, config_path, name, isf_url):
        super().__init__(context = context, config_path = config_path, name = name, isf_url = isf_url)

        # Set-up windows specific types
        self.set_type_class('_ETHREAD', extensions._ETHREAD)
        self.set_type_class('_LIST_ENTRY', extensions._LIST_ENTRY)
        self.set_type_class('_EPROCESS', extensions._EPROCESS)
        self.set_type_class('_UNICODE_STRING', extensions._UNICODE_STRING)
        self.set_type_class('_EX_FAST_REF', extensions._EX_FAST_REF)
        self.set_type_class('_OBJECT_HEADER', extensions._OBJECT_HEADER)
        self.set_type_class('_FILE_OBJECT', extensions._FILE_OBJECT)
        self.set_type_class('_DEVICE_OBJECT', extensions._DEVICE_OBJECT)
        self.set_type_class('_CM_KEY_BODY', extensions._CM_KEY_BODY)
        self.set_type_class('_CMHIVE', registry._CMHIVE)
        self.set_type_class('_CM_KEY_NODE', registry._CM_KEY_NODE)
        self.set_type_class('_CM_KEY_VALUE', registry._CM_KEY_VALUE)
        self.set_type_class('_HMAP_ENTRY', registry._HMAP_ENTRY)

    @classmethod
    def get_requirements(cls):
        return [requirements.StringRequirement("isf_url",
                                               description = "JSON file containing the symbols encoded in the Intermediate Symbol Format")]
