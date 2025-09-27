from yta_programming_env import Environment
from dataclasses import dataclass


ENVIRONMENT_VARIABLE_NAME = 'PIXABAY_API_KEY'
"""
The name of the environment variable
that includes the Pixabay API key.
"""

@dataclass
class PixabaySettings:
    """
    The settings of our Pixabay API.
    """

    API_KEY = Environment.get_current_project_env(ENVIRONMENT_VARIABLE_NAME)
    """
    The api key, read from the environment
    variable.
    """

@dataclass
class PixabayEndpoints:
    """
    The endpoints for the Pixabay API.
    """

    API_ENDPOINT_URL = 'https://pixabay.com/api/?'
    """
    This endpoint must be called with specific 
    parameters to obtain a response. Those parameters
    must be 'key' (the API KEY), 'q' (the query to
    search) and 'image_type' (with 'photo' or 'video'
    according to what type we are looking for).

    Those parameters must be concatenated as encoded
    url parameters '.../?key=xxx&q=yyy...'.
    """
    VIDEOS_API_ENDPOINT_URL = 'https://pixabay.com/api/videos/?'
    """
    This endpoint must be called with specific 
    parameters to obtain a response. Those parameters
    must be 'key' (the API KEY), 'q' (the query to
    search) and 'pretty' (as 'true' or 'false' if we
    want the response made pretty).

    Those parameters must be concatenated as encoded
    url parameters '.../?key=xxx&q=yyy...'.
    """
