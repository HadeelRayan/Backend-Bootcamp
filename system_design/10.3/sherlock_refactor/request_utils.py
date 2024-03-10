import requests
from requests.exceptions import RequestException


def make_request(url, method='get', headers=None, timeout=30, proxies=None, verify=True, allow_redirects=True, data=None):
    """Send an HTTP request and return the response.

    Args:
        url (str): The URL to send the request to.
        method (str): HTTP method to use (e.g., 'get', 'post'). Defaults to 'get'.
        headers (dict): Optional headers to include in the request.
        timeout (int): How many seconds to wait for the server to send data before giving up.
        proxies (dict): Optional proxy configuration.
        verify (bool): Whether to verify SSL certificates. Defaults to True.
        allow_redirects (bool): Whether to follow redirects. Defaults to True.
        data (dict): Optional dictionary to send in the body of the request.

    Returns:
        requests.Response: The response object.

    Raises:
        RequestException: For issues with making the request.
    """
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            timeout=timeout,
            proxies=proxies,
            verify=verify,
            allow_redirects=allow_redirects,
            data=data
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4XX, 5XX)
        return response
    except RequestException as e:
        raise RequestException(f"Error making request to {url}: {e}")


def handle_response(response):
    """Process a requests.Response object and return relevant data.

    Args:
        response (requests.Response): The response object to process.

    Returns:
        dict: A dictionary with processed response data (e.g., status code, content).
    """
    return {
        'status_code': response.status_code,
        'content': response.content,
        'headers': response.headers,
        'url': response.url
    }

