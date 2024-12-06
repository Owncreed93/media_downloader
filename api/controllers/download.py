from schemas.download import DownloadResponse

def create_download(url: str, successful: bool) -> DownloadResponse:
    '''
    Creates a new download record
    '''
    new_download = DownloadResponse(id=1, url=url, successful=successful)
    # return DownloadResponse(id=1, url=url, successful=successful)
    return new_download