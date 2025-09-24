from abc import abstractmethod
from typing import Optional

from PyMca5.PyMcaPhysics.xrf.XRFBatchFitOutput import OutputBuffer as _OutputBuffer


class AbstractOutputBuffer(_OutputBuffer):

    @property
    @abstractmethod
    def xrf_results_uri(self) -> Optional[str]:
        pass

    @property
    @abstractmethod
    def already_existed(self) -> bool:
        pass
