import logging
from urllib.parse import urljoin

import httpx
import icechunk
import xarray

DEFAULT_CATALOG_API_V1_ENDPOINT = "https://catalog-api-v1.askpq.com"
"""@private"""


def open_ds(
    dataset_id: str,
    access_key_id: str,
    secret_access_key: str,
    catalog_api_v1_endpoint: str = DEFAULT_CATALOG_API_V1_ENDPOINT,
) -> xarray.Dataset:
    """
    Open a dataset using the dataset ID and your access keys. Returns an xarray Dataset.

    Find the dataset ID on the online catalog, and your access keys from the
    account page on [askpq.com](https://askpq.com).

    Simple test dataset code:
    ```python
    import os
    import askpq

    ds = askpq.open_ds(
        "ds_small-test",
        os.environ["ASKPQ_ACCESS_KEY_ID"],
        os.environ["ASKPQ_SECRET_ACCESS_KEY"],
    )
    print(ds)
    ```
    """
    logging.info("Querying Askpq catalog api to set up connection to data")
    url = urljoin(catalog_api_v1_endpoint, "/v1/bucket-and-prefix")
    resp = httpx.get(url, params={"dataset-id": dataset_id})
    bandp = resp.json()
    bucket = bandp["bucket"]
    prefix = bandp["prefix"]

    logging.info("Creating xarray.Dataset")
    icechunk_storage = icechunk.tigris_storage(
        bucket=bucket,
        prefix=prefix,
        access_key_id=access_key_id,
        secret_access_key=secret_access_key,
        region="auto",
    )
    icechunk_repo = icechunk.Repository.open(icechunk_storage)
    icechunk_session = icechunk_repo.readonly_session(branch="main")
    ds = xarray.open_dataset(icechunk_session.store, engine="zarr", consolidated=False)

    return ds
