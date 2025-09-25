class BaseException(Exception):
    """The base exception used in the system."""
    
    def __init__(self, msg=None):
        # Default message if none is provided
        if msg is None:
            msg = "An error occurred in the system"
        super().__init__(msg)


class TemplateNotFound(BaseException):
    """The exception raised when a template is not found."""
    
    def __init__(self, template_name=None):
        msg = f"Template '{template_name}' doesn't exist" if template_name else "Template doesn't exist"
        super().__init__(msg)


class InvalidSendTime(BaseException):
    """Raised when the specified send time is in the past."""
    
    def __init__(self, msg=None):
        if not msg:
            msg = "The specified send time is invalid"
        super().__init__(msg)


class InvalidFileFormat(BaseException):
    """Raised when the specified send time is in the past."""
    
    def __init__(self, msg=None):
        if not msg:
            msg = "Invalid file format"
        super().__init__(msg)


class InvalidEmailProcessor(BaseException):
    """raises when user use a wrong email processor"""
