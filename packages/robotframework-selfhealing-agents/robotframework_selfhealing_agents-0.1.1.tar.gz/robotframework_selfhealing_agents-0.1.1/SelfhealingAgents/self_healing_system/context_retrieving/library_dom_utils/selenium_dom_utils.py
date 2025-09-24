from typing import List, Dict

from robot.libraries.BuiltIn import BuiltIn
from bs4 import BeautifulSoup, ResultSet, Tag
from selenium.webdriver.remote.webelement import WebElement

from SelfhealingAgents.utils.logging import log
from SelfhealingAgents.self_healing_system.context_retrieving.dom_soap_utils import SoupDomUtils
from SelfhealingAgents.self_healing_system.context_retrieving.library_dom_utils.base_dom_utils import BaseDomUtils


class SeleniumDomUtils(BaseDomUtils):
    """Selenium library specific DOM utility implementation.

    This class provides DOM interaction methods specific to the Robot Framework
    SeleniumLibrary.

    Attributes:
        _library_instance: Instance of the SeleniumLibrary used for DOM interactions.
    """
    def __init__(self):
        """Initialize Selenium DOM utilities."""
        self._library_instance = BuiltIn().get_library_instance("SeleniumLibrary")

    def is_locator_valid(self, locator: str) -> bool:
        """Check if the locator is valid using Selenium library methods.

        Args:
            locator: The locator to check.

        Returns:
            True if the locator is valid, False otherwise.
        """
        if self._library_instance is None:
            return True
        try:
            # Use dynamic attribute access to handle different SeleniumLibrary versions
            getattr(self._library_instance, "get_webelement")(locator)
            return True
        except Exception:
            return False

    def is_locator_unique(self, locator: str) -> bool:
        """Check if the locator is unique using Selenium library methods.

        Args:
            locator: The locator to check.

        Returns:
            True if the locator is unique, False otherwise.
        """
        if self._library_instance is None:
            return True  # Skip validation if library is not available

        try:
            # Use dynamic attribute access to handle different SeleniumLibrary versions
            elements: List[WebElement] = getattr(self._library_instance, "get_webelements")(locator)
            return len(elements) == 1
        except Exception:
            return False

    def get_dom_tree(self) -> str:
        """Retrieve the DOM tree using Selenium library methods.

        Returns:
            str: The DOM tree as a string.
        """
        if self._library_instance is None:
            return "<html><body>SeleniumLibrary not available</body></html>"

        try:
            page_source: str = getattr(self._library_instance, "get_source")()

            soup: BeautifulSoup = BeautifulSoup(page_source, "html.parser")
            source: str = SoupDomUtils().get_simplified_dom_tree(
                str(soup.body) if soup.body else str(soup)
            )
            return source

        except Exception as e:
            return f"<html><body>Error retrieving DOM tree: {str(e)}</body></html>"

    def get_library_type(self) -> str:
        """Get the library type identifier.

        Returns:
            str: The library type identifier.
        """
        return "selenium"

    def is_element_clickable(self, locator: str) -> bool:
        """Check if the element is clickable using Selenium library methods.

        Args:
            locator: The locator to check.

        Returns:
            True if the element is clickable, False otherwise.
        """
        if self._library_instance is None:
            return False
        try:
            element: WebElement = getattr(self._library_instance, "get_webelement")(locator)

            # Get tag name using element property
            tag: str = element.tag_name.lower()

            # Check basic clickable tags
            if tag == "button" or tag == "a" or tag == "select":
                return True
            elif tag == "input":
                # Check input type for clickable input elements
                input_type: str = getattr(self._library_instance, "execute_javascript")(
                    "return arguments[0].type;", "ARGUMENTS", element
                )
                if input_type in [
                    "button",
                    "radio",
                    "checkbox",
                    "search",
                    "reset",
                    "submit",
                ]:
                    return True

            # Check for custom/framework-specific clickable elements
            other_clickable_tags: List[str] = [
                "mat-button",  # Angular Material
                "mat-radio-button",
                "mat-checkbox",
                "md-button",  # Older Angular Material
                "ion-button",  # Ionic
                "vaadin-button",  # Vaadin
                "paper-button",  # Polymer
                "x-button",  # Generic custom button
                "select",
                "textarea",
            ]

            if tag in other_clickable_tags:
                return True

            # Check cursor style as final indicator
            cursor_style: str = getattr(self._library_instance, "execute_javascript")(
                "return window.getComputedStyle(arguments[0]).getPropertyValue('cursor');",
                "ARGUMENTS",
                element,
            )
            if cursor_style == "pointer":
                return True

            return False
        except Exception:
            return False

    @log
    def get_locator_proposals(
        self, failed_locator: str, keyword_name: str
    ) -> List[str]:
        """Get proposals for the given locator.

        Args:
            locator: The locator to get proposals for.

        Returns:
            A list of proposed locators.
        """
        dom_tree: str = self.get_dom_tree()
        soup: BeautifulSoup = BeautifulSoup(dom_tree, "html.parser")

        match keyword_name:
            case (
                "Input Text"
                | "Input Password"
                | "Press Keys"
                | "Press Key"
                | "Textarea Should Contain"
                | "Textarea Value Should Be"
                | "Textfield Should Contain"
                | "Textfield Value Should Be"
                | "Clear Text"
            ):
                element_types: List[str] = ["textarea", "input"]
                elements: ResultSet = soup.find_all(element_types)
            case (
                "Click Button"
                | "Click Link"
                | "Click Element"
                | "Click Image"
                | "Click Element At Coordinates"
            ):
                element_types: List[str] = [
                    "a",
                    "button",
                    "checkbox",
                    "link",
                    "input",
                    "label",
                    "li",
                    SoupDomUtils.has_direct_text,
                ]
                elements: ResultSet = soup.find_all(element_types)
            case s if "list" in s.lower():
                element_types: List[str] = ["select"]
                elements: ResultSet = soup.find_all(element_types)
            case c if "checkbox" in c.lower():
                element_types: List[str] = ["input", "button", "checkbox"]
                elements: ResultSet = soup.find_all(element_types)
            case "Get Text" | "Element Text Should Be" | "Element Text Should Not Be":
                element_types: List[str] = ["label", "div", "span", SoupDomUtils.has_direct_text]
                elements: ResultSet = soup.find_all(element_types)

        filtered_elements: List[Tag] = [
            elem
            for elem in elements
            if (
                (SoupDomUtils.is_leaf_or_lowest(elem) or SoupDomUtils.has_direct_text(elem))
                and (not SoupDomUtils.has_parent_dialog_without_open(elem))
                and (not SoupDomUtils.has_child_dialog_without_open(elem))
                and (not SoupDomUtils.is_headline(elem))
                and (not SoupDomUtils.is_div_in_li(elem))
                and (not SoupDomUtils.is_p(elem))
            )
        ]

        locators: List = []
        # Generate and display unique selectors
        for elem in filtered_elements:
            try:
                locator: str | None = SeleniumDomUtils._get_locator(elem, soup)
            except Exception:
                locator = None
            if locator:
                locators.append(locator)
        return locators

    def get_locator_metadata(self, locator: str) -> List[Dict]:
        """Get metadata for the given locator.

        Args:
            locator: The locator to get metadata for.

        Returns:
            A list of dictionaries containing metadata about elements matching the locator.
        """
        if self._library_instance is None:
            return []

        try:
            element: WebElement = getattr(self._library_instance, "get_webelement")(locator)
            metadata_list: List = []

            if element:
                metadata: Dict = {}

                # Properties (retrieved via JavaScript execution for consistency)
                property_list = [
                    "tagName",
                    "childElementCount",
                    "innerText",
                    "type",
                    "value",
                    "name",
                ]
                for property in property_list:
                    try:
                        value = getattr(self._library_instance, "execute_javascript")(
                            f"return arguments[0].{property};", "ARGUMENTS", element
                        )
                        if value:
                            metadata[property] = str(value)
                    except Exception:
                        pass

                # Additional properties with parent/sibling context
                additional_properties = [
                    "parentElement.tagName",
                    "parentElement.innerText",
                    "previousSibling.tagName",
                    "previousSibling.innerText",
                    "nextSibling.tagName",
                    "nextSibling.innerText",
                ]
                for property in additional_properties:
                    try:
                        value = getattr(self._library_instance, "execute_javascript")(
                            f"return arguments[0].{property};", "ARGUMENTS", element
                        )
                        if value:
                            metadata[property] = str(value)
                    except Exception:
                        pass

                # Attributes (retrieved via get_attribute)
                allowed_attributes = [
                    "id",
                    "class",
                    "placeholder",
                    "role",
                    "href",
                    "title",
                ]
                for attribute in allowed_attributes:
                    try:
                        value = element.get_attribute(attribute)
                        if value:
                            metadata[attribute] = str(value)
                    except Exception:
                        pass

                # Element state information
                try:
                    metadata["is_displayed"] = element.is_displayed()
                except Exception:
                    metadata["is_displayed"] = False

                try:
                    metadata["is_enabled"] = element.is_enabled()
                except Exception:
                    metadata["is_enabled"] = False

                try:
                    metadata["is_selected"] = element.is_selected()
                except Exception:
                    metadata["is_selected"] = False

                # Clickable detection (following the pattern from your example)
                try:
                    tag_name = metadata.get("tagName", "").upper()
                    clickable_tags = ["BUTTON", "A", "INPUT", "SELECT"]

                    if tag_name in clickable_tags:
                        metadata["clickable"] = True
                    else:
                        # Check cursor style
                        cursor_clickable = False
                        try:
                            cursor_style = getattr(
                                self._library_instance, "execute_javascript"
                            )(
                                "return window.getComputedStyle(arguments[0]).getPropertyValue('cursor');",
                                "ARGUMENTS",
                                element,
                            )
                            cursor_clickable = cursor_style == "pointer"
                        except Exception:
                            pass

                        # Check for other clickable indicators
                        value_clickable = False
                        try:
                            value = getattr(
                                self._library_instance, "execute_javascript"
                            )("return arguments[0].value;", "ARGUMENTS", element)
                            value_clickable = value in ["on", "off"]
                        except Exception:
                            pass

                        checked_clickable = False
                        try:
                            checked = getattr(
                                self._library_instance, "execute_javascript"
                            )("return arguments[0].checked;", "ARGUMENTS", element)
                            checked_clickable = (
                                checked is not None and str(checked) != ""
                            )
                        except Exception:
                            pass

                        metadata["clickable"] = (
                            cursor_clickable or value_clickable or checked_clickable
                        )
                except Exception:
                    metadata["clickable"] = False

                metadata_list.append(metadata)

            return metadata_list

        except Exception:
            return []

    @staticmethod
    def _get_locator(elem: Tag, soup: BeautifulSoup) -> str | None:
        selector: str = SoupDomUtils.generate_unique_xpath_selector(elem, soup)
        if selector:
            return "xpath:" + selector
        return None
