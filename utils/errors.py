class FreskError(Exception):
    pass


class FreskAddressNotFound(FreskError):
    def __init__(self, input_str: str):
        self.message = f"Address not found (input: {input_str})."
        super().__init__(self.message)


class FreskAddressBadFormat(FreskError):
    def __init__(self, address: str, input_str: str, attribute: str):
        self.message = f'Address "{address}" has a bad {attribute} format, unhandled by TuF (input: {input_str}).'
        super().__init__(self.message)


class FreskCountryNotSupported(FreskError):
    def __init__(self, address: str, input_str: str):
        self.message = (
            f'Address "{address}" is not located in a supported country (input: {input_str}).'
        )
        super().__init__(self.message)