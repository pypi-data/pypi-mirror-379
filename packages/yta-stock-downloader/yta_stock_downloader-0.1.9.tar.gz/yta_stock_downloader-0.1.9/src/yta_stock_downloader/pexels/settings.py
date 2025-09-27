from yta_programming_env import Environment
from dataclasses import dataclass


ENVIRONMENT_VARIABLE_NAME = 'PEXELS_API_KEY'
"""
The name of the environment variable
that includes the Pexels API key.
"""

@dataclass
class PexelsSettings:
    """
    The settings of our Pexels API.
    """

    API_KEY = Environment.get_current_project_env(ENVIRONMENT_VARIABLE_NAME)
    """
    The api key, read from the environment
    variable.
    """
    RESULTS_PER_PAGE = 25
    """
    The result we will expect in the responses.
    """
    HEADERS = {
        'content-type': 'application/json',
        'Accept-Charset': 'UTF-8',
        'Authorization': API_KEY
    }
    """
    The headers we need to send in the request,
    including the Api key.
    """

@dataclass
class PexelsEndpoints:
    """
    The endpoints for the Pexels API.
    """

    SEARCH_IMAGE_API_ENDPOINT_URL = 'https://api.pexels.com/v1/search'
    """
    Endpoint of the Pexels platform to look
    for images.
    """
    SEARCH_VIDEOS_URL = 'https://api.pexels.com/videos/search'
    """
    Endpoint of the Pexels platform to look
    for videos.
    """
    GET_VIDEO_BY_ID_URL = 'https://api.pexels.com/videos/videos/'
    """
    Endpoint of the Pexels platform to obtain
    an specific video by its url.
    """
