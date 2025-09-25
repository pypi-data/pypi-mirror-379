from typing import Optional, Any, Iterable
from tqdm import tqdm
import requests
import logging
from hrid import HRID

class mytqdm(tqdm):
    
    PROGRESS_URL = "https://mytqdm.ai/progress"
    
    def __init__(
        self,
        iterable: Optional[Iterable[Any]] = None,
        *,
        api_key: str = None,
        title: Optional[str] = None,
        **kwargs: Any
    ):
        self.api_key = api_key
        self.title = title
        self.mytqdm_id = HRID().generate()
        tqdm_url = PROGRESS_URL + "/" + self.mytqdm_id
        logger.info(f"Use the following url to get your tqdm progress: {tqdm_url}")
        with open('mytqdm_id.txt', 'w') as f:
            f.write(tqdm_url)
        super().__init__(iterable=iterable, **kwargs)
        
    def update(self, n: int = 1) -> bool:
        displayed = super().update(n)
        current = self.n
        total = self.total    
        if displayed:
            headers = {
                "Authorization": f"X-API-Key {api_key}",
                "Accept": "application/json",
            }
            payload = {
                "title": self.title,
                "progress": current,
                "total": total,
            }
            resp = requests.post(PROGRESS_URL, json=payload, headers=headers, timeout=10)
            if resp.ok:
                logging.debug("mytqdm state successfully updated.")
            else:
                logging.warn(f"Got non-ok response from mytqdm {resp.status_code}")
        return displayed
