"""Download ofqual register"""
import re
import requests

BASE_URL = 'https://register.ofqual.gov.uk/Home/'
QUERY_PARAM = 'Download?category=Qualifications'


def get_filename_from_cd(content_disp):
    """
    Get filename from content-disposition
    """
    if not content_disp:
        return None
    fname = re.findall('filename=(.+)', content_disp)
    if not fname:
        return None
    return fname[0]


def get_url_query(query):
    """
    Get url for query
    """
    return BASE_URL + query


def get_file_from_url():
    """
    Get the file and save from url
    """
    resp = requests.get(get_url_query(QUERY_PARAM))
    filename = get_filename_from_cd(resp.headers.get('content-disposition'))
    open(filename, 'wb').write(resp.content)


get_file_from_url()
