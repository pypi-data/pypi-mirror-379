from . import BaseAttribute
from ..base_types import StrLike


class DfnAttrs:
    """
    This module contains functions for attributes in the 'dfn' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def title(value: StrLike) -> BaseAttribute:
        """
        "dfn" attribute: title  
        Full term or expansion of abbreviation  

        :param value: Text  
        :return: An title attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("title", value)
