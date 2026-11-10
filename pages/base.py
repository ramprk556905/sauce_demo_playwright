import os
import time
from playwright.sync_api import expect
import requests
from datetime import datetime


class BasePage:

    def __init__(self, page):
        self.page = page
        self.FILTERED_DATA1 = []
        self.FILTERED_DATA2 = []
        self.FILTERED_DATA3 = []

    def get_element(self, element_locator):
        """
        Return a WebElement instance which represents the UI node indicated by the provided element_locator
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        """
        return self.page.locator(element_locator)

    def get_elements(self, element_locator):
        """
        Return a WebElement instance which represents the UI node indicated by the provided element_locator
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        """
        return self.get_element(element_locator).all()

    def get_page_title(self):
        """
        Return the page title
        """
        return self.page.title()

    def get_element_text(self, element_locator):
        """
        Return the text value of the WebElement instance indicated by 'element_locator'
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        """
        element = self.get_element(element_locator)
        return element.inner_text()

    def get_elements_inner_text(self, element_locator):
        """
        Return the text value of the WebElement instance indicated by 'element_locator'
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        """
        element = self.get_element(element_locator)
        return element.all_inner_texts()

    def get_filtered_elements(self, element_locator, LIST):
        """
        Getting all the inner texts of elements which are matching with the locator and storing in list
        """
        while True:
            NAMES = self.get_elements_inner_text(element_locator)
            for NAME in NAMES:
                LIST.append(NAME)
            if self.is_element_visible(self.NEXT_BUTTON_PATH):
                self.click_element(self.NEXT_BUTTON_PATH)
                self.wait_for_element_to_be_invisible(self.GLOBAL_SPINNER_PATH)
            else:
                break

    def get_element_contents(self, element_locator):
        """
        Return the text value of the WebElement instance indicated by 'element_locator'
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        """
        return self.get_element(element_locator).all_text_contents()

    def clear_element_text(self, element_locator):
        """
        Remove the text value of the WebElement instance indicated by 'element_locator'
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        """
        return self.get_element(element_locator).clear()

    def get_element_attribute(self, element_locator, attribute_name):
        """
         Return the value of the attribute name provided on the WebElement instance indicated by 'element_locator'
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        :param attribute_name: The name of the attribute from which to retrieve the value
        """
        return self.get_element(element_locator).get_attribute(attribute_name)

    def fill_input_text(self, element_locator, text):
        """
        fill the given text to the WebElement instance indicated by 'element_locator'
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        :param text: The text value to type into the WebElement
        """
        return self.get_element(element_locator).fill(text)

    def click_element(self, element_locator):
        """
        Click the WebElement instance indicated by 'element_locator'
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        """
        return self.get_element(element_locator).click(timeout=100000)

    def get_element_options(self, element_locator):
        """
        Return the list of options available on the WebElement instance indicated by 'element_locator'
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        """
        return self.get_element(element_locator).all_inner_texts()

    def is_element_visible(self, element_locator):
        """
        Return whether a WebElement is visible using its  element_locator
        :param  element_locator: The Locator containing the strategy and value to be used to find a WebElement
        """
        element = self.get_element(element_locator).is_visible()
        return bool(element)

    def is_element_checked(self, element_locator):
        """
        Return whether a checkbox is selected using its element_locator
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        """
        element = self.get_element(element_locator).is_checked()
        return bool(element)

    def is_element_enabled(self, element_locator):
        """
        Return whether a WebElement is enabled using its element_locator
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        """
        element = self.get_element(element_locator).is_enabled()
        return bool(element)

    def is_element_disabled(self, element_locator):
        """
        Return whether a WebElement is disabled using its element_locator
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        """
        element = self.get_element(element_locator).is_disabled()
        return bool(element)

    def select_option_by_text(self, element_locator, text):
        """
        Select the visible option specified by 'label name' on the WebElement instance indicated by 'element_locator'
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        :param text: The text value to type into the WebElement
        """
        self.wait_for_locator(element_locator)
        self.get_element(element_locator).select_option(text, timeout=100000)

    def select_option_by_label(self, element_locator, label_name):
        """
        Select the visible option specified by 'label name' on the WebElement instance indicated by 'element_locator'
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        :param label_name: The text value to type into the WebElement
        """
        self.wait_for_locator(element_locator)
        self.get_element(element_locator).select_option(label_name, timeout=100000)

    def get_element_count(self, element_locator):
        """
        It returns number of the elements that are matching with provided element locator
        """
        return self.get_element(element_locator).count()

    def wait_for_locator_visible(self, element_locator):
        """
        Page will wait until element_locator is visible
        """
        return self.page.wait_for_selector(element_locator, state='visible')

    def wait_for_locator_clickable(self, element_locator):
        """
        Page will wait until element_locator is visible
        """
        return self.page.wait_for_selector(element_locator, state='attached')

    def wait_for_element_to_be_invisible(self, element_locator):
        """
        Page will wait until element_locator is visible
        """
        element = self.get_element(element_locator)
        expect(element).not_to_be_visible(timeout=500000)

    def wait_for_locator(self, element_locator):
        """
        Page will wait until WebElement of given element_locator becomes clickable state
        """
        return self.page.wait_for_selector(element_locator, timeout=50000)

    def wait_for_url(self, url):
        """
        Page will wait until visibility of provided url
        """
        return self.wait_for_url(url)

    def file_upload(self, locator, file_name):
        """
        it will select the file as per input data and will upload file in the web page
        """
        self.page.set_input_files(locator, file_name)

    def wait_for_selector(self, element_locator):
        """
        Page will wait until the selector is visible in the web page
        """
        return self.page.wait_for_selector(element_locator)

    def double_click_on_element(self, element_locator):
        """
        Click the WebElement instance indicated by 'element_locator'
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        """
        return self.get_element(element_locator).dblclick()

    def get_text_from_input_box(self, element_locator):
        """
        Getting the text from input box if html won't have required input box value and html tag won't contain inner text
        """
        input_value = self.get_element(element_locator).input_value()
        return input_value

    def mouse_hover_over_element(self, element_locator):
        """
        This is used to simulate moving the mouse over a specific element on the webpage. This action can trigger various
        events, such as displaying tooltips, dropdown menus, or changing the visual state of the element.
        :param element_locator:
        :return:
        """
        self.get_element(element_locator).hover()

    def element_scroll_into_view_if_needed(self, element_locator):
        """
        This is used to simulate moving the mouse over a specific element on the webpage. This action can trigger various
        events, such as displaying tooltips, dropdown menus, or changing the visual state of the element.
        :param element_locator:
        :return:
        """
        return self.get_element(element_locator).scroll_into_view_if_needed()

    def validate_page_loading(self):
        """
        waiting for completing loading of the page
        :return:
        """
        self.wait_for_element_to_be_invisible(self.GLOBAL_SPINNER_PATH)
        time.sleep(2.5)

    def shift_to_child_page(self):
        """
        Shifts control from the parent page to the child page.
        Parameters: click_selector (str): The selector for the element that triggers the popup (child page).
        Returns: Page: The child page object that opened as a result of the action.
        """
        child_page = self.page.context.wait_for_event('page')
        child_page.bring_to_front()
        child_page.wait_for_timeout(1000)
        page1 = BasePage(child_page)
        return page1

    def navigate_to_job_details_page(self):
        """
        Validation of edit tab, edit job and edit build it ui elements in job details page
        :return:
        """
        self.wait_for_locator(self.JOB_NUMBER_LISTING_PATH)
        self.fill_input_text(self.JOB_NUMBER_INPUT_BOX_PATH, self.config.get("job_number"))
        self.wait_for_element_to_be_invisible(self.LOADING_PROGRESS_CIRCLE_PATH)
        self.wait_for_locator(self.FILTERED_JOB_NUMBER_PATH)
        time_counter = 0
        while not self.get_element_text(self.FILTERED_JOB_NUMBER_PATH) == self.config.get(
                "job_number") and time_counter < self.TIME_TO_WAIT:
            self.page.reload()
            self.fill_input_text(self.JOB_NUMBER_INPUT_BOX_PATH, self.config.get("job_number"))
            self.wait_for_element_to_be_invisible(self.LOADING_PROGRESS_CIRCLE_PATH)
            self.wait_for_locator(self.FILTERED_JOB_NUMBER_PATH)
            time_counter = time_counter + 1
            """
            Job listing page ui is taking some extra time for filtering of job numbers, so we are using time.sleep
            """
            time.sleep(2)

        self.click_element(self.FILTERED_JOB_NUMBER_PATH)
        page1 = self.shift_to_child_page()
        return page1

    def set_input_files(self, element_locator, file_paths: list):
        """
        Set input files for file upload.
        """
        self.get_element(element_locator).set_input_files(file_paths)

    def create_pdf_files(self, directory_name, pdf_filenames):
        """
        Creating the empty pdf files amd saving in the provided directory
        :param directory_name:
        :param pdf_filenames:
        :return:
        """
        resources_dir = os.path.join(os.getcwd(), directory_name)
        os.makedirs(directory_name, exist_ok=True)
        for filename in pdf_filenames:
            path = os.path.join(resources_dir, filename)
            c = canvas.Canvas(path)
            c.save()

    def create_pdf_file(self, directory_name, pdf_filename):
        """
        Create an empty PDF file and save it in the specified directory.
        :param directory_name: Name of the directory to save the PDF.
        :param pdf_filename: Name of the single PDF file to create.
        :return: None
        """
        resources_dir = os.path.join(os.getcwd(), directory_name)
        os.makedirs(resources_dir, exist_ok=True)  # Ensure the directory exists
        path = os.path.join(resources_dir, pdf_filename)
        c = canvas.Canvas(path)  # Create an empty PDF
        c.save()

    def loading_function_child_page(self):
        """
        Function for job details page reload
        """
        self.page.reload()
        self.wait_for_element_to_be_invisible(self.GLOBAL_SPINNER_PATH)

    def reload_job_details_page(self):
        """
        Job details page will be reloaded
        """
        page1 = self.navigate_to_job_details_page()
        page1.loading_function_child_page()

    def handle_multiple_child_pages(self):
        """
        This is used to handle multiple child pages to work and validate the child page elements
        """
        page3 = self.page.context.wait_for_event('page')
        page3.bring_to_front()
        page3.wait_for_timeout(1000)
        page2 = BasePage(page3)
        return page2

    def validate_checkbox_and_input_box(self, locator1, locator2, text):
        """
        Validating whether checkbox is selected or not and if checkbox is selected, corresponding input should be
        disabled else it should enter the text
        :param locator1:
        :param locator2:
        :param text:
        :return:
        """
        if self.is_element_checked(locator1):
            assert self.is_element_disabled(locator2)
            self.click_element(locator1)
        self.fill_input_text(locator2, text)

    def press_key_from_keyboard(self, element_locator, key):
        """
        pressing key from keyboard
        """
        self.page.press(element_locator, key)

    def reload_page(self):
        """
        Page will be reloaded
        """
        return self.page.reload()

    def request(self, api_url, headers):
        """
        this function to make a request and it returns response
        """
        response = self.page.request.get(api_url, headers=headers)
        return response

    def get_auth_token(self, url, username, password):
        """
        Generating the x-auth value to get api response
        """
        auth_url = f"{url}"
        payload = {
            "username": username,
            "password": password
        }
        response = requests.post(auth_url, json=payload)
        response.raise_for_status()
        return response.json().get("token")

    def validation_of_edit_button_in_job_details_page(self):
        """
        Validating the visibility of edit button in job details page
        """
        self.wait_for_load_state()
        if self.is_element_visible(self.EDIT_BUTTON_PATH):
            assert self.is_element_visible(self.EDIT_BUTTON_PATH)
            assert self.is_element_enabled(self.EDIT_BUTTON_PATH)
            self.click_element(self.EDIT_BUTTON_PATH)
            self.wait_for_element_to_be_invisible(self.EDIT_JOB_POPUP_SPINNER_PATH)
            self.wait_for_locator(self.EDIT_JOB_PATH)
            assert self.is_element_visible(self.EDIT_JOB_PATH)
            assert self.is_element_visible(self.EDIT_BUILDID_PATH)

    def evaluate(self, script: str):
        """
        Evaluates a JavaScript script within the context of the current page.
        """
        return self.page.evaluate(script)

    def get_page_url(self):
        """
        Retrieves the current URL of the page.
        """
        return self.page.url

    def wait_for_load_state(self):
        """
        wait until the page reaches a certain "load state" before proceeding with the next action
        """
        self.page.wait_for_load_state('networkidle', timeout=100000)

    def enter_values_in_enclosure(self):
        """
        This is used to enter the data in each Enclosure text field.
        """
        self.click_element(self.EDIT_BUTTON_ENCLOSURE)
        self.wait_for_locator(self.ENCLOSURE_TEXT_ELEMENT)
        timestamp = datetime.now().strftime("%Y%m%dT%H%M")
        base_enclosure_value = f"EOC_PLS_{timestamp}"
        enclosure_elements = self.get_elements(self.ENCLOSURE_TEXT_ELEMENT)
        for i, element in enumerate(enclosure_elements):
            enclosure_text_value = f"{base_enclosure_value}_{i + 1}"
            element.fill(enclosure_text_value)
        self.click_element(self.SAVE_BUTTON_ENCLOSURE)
        self.wait_for_locator(self.ENCLOSURE_HEADING)

    def get_elements_as_array(self, element_locator):
        """
        Return the text values of the WebElement instance indicated by 'element_locator' as a list.
        :param element_locator: The Locator containing the strategy and value to be used to find a WebElement
        :return: List of text values
        """
        element_text = self.get_element_text(element_locator)
        return element_text.splitlines()

    def query_selector(self, selector):
        """
        Selects and returns the first matching element on the page based on the given CSS selector.
        """
        return self.page.query_selector(selector)

    def get_selected_text_from_dropdown(self, element_locator):
        """
        Gets the selected text from a dropdown field.
        """
        dropdown = self.get_element(element_locator)
        selected_value = dropdown.input_value()
        option = dropdown.locator(f"option[value='{selected_value}']")
        return option.inner_text()

    def get_selected_value_from_dropdown(self, element_locator):
        """
        Gets the selected value from a dropdown field.
        """
        dropdown = self.get_element(element_locator)
        selected_option = dropdown.locator("option:checked")
        selected_value = selected_option.get_attribute("label")
        return selected_value

    def navigate_to_build_id_rules_page(self):
        """
        navigate to the build id rules page from job listing page
        """
        self.wait_for_locator(self.SETTINGS_DROPDOWN_PATH)
        self.click_element(self.SETTINGS_DROPDOWN_PATH)
        self.click_element(self.BUILDID_RULES_TAB_PATH)
        page1 = self.shift_to_child_page()
        return page1

    def navigate_and_select_client_in_buildid_rules_page(self, client_name):
        """
        Navigating to build id rules page and selecting the provided client name from dropdowns
        """
        page1 = self.navigate_to_build_id_rules_page()
        page1.click_element(self.CLIENT_NAME_DROPDOWN_PATH)
        clients = page1.get_elements(self.CLIENT_NAME_PATH)
        for client in clients:
            if client.inner_text() == client_name:
                client.click()
                break
        return page1

    def get_filtered_names_like(self, column_locator):
        """
        Getting filtered names from a given column and ensuring all elements match the 'like' condition.
        If the next button is visible, it will click and capture elements; else, the loop will break.
        """
        all_filtered_names = []
        while True:
            filtered_names = self.get_elements_inner_text(column_locator)
            all_filtered_names.extend(filtered_names)
            if not self.is_element_visible(self.NEXT_PAGE_BUTTON) or not self.is_element_enabled(self.NEXT_PAGE_BUTTON):
                break
            self.click_element(self.NEXT_PAGE_BUTTON)
        return all_filtered_names

    def navigate_to_build_id_details_page(self, client_name):
        """
        Navigating to the Build ID rules details page by selecting a client from the dropdown
        """
        page1 = self.navigate_and_select_client_in_buildid_rules_page(client_name)
        page1.click_element(self.APPROVAL_STATUS_DROPDOWN)
        page1.select_option_by_text(self.APPROVAL_STATUS_DROPDOWN, "Approved")
        page1.click_element(self.EYE_ICON)
        page2 = self.shift_to_child_page()
        return page2

    def get_value_from_column(self, count, element_locator, rows):
        """
        This method is used to get the values from the field column in the component section
        """
        current_section = []
        for i in range(count):
            field_locator = f"{element_locator}[{i + rows}]"
            field_text = self.get_element_text(field_locator)
            current_section.append(field_text)
        return current_section

    def get_history_filtered(self, column_locator):
        """
        Getting filtered names from a given column and ensuring all elements match the 'like' condition.
        If the next button is visible, it will click and capture elements; else, the loop will break.
        """
        all_filtered_names = []
        while True:
            filtered_names = self.get_elements_inner_text(column_locator)
            all_filtered_names.extend(filtered_names)
            if not self.is_element_visible(self.HISTORY_NEXT_BUTTON) or not self.is_element_enabled(self.HISTORY_NEXT_BUTTON):
                break
            self.click_element(self.HISTORY_NEXT_BUTTON)
        return all_filtered_names

    def navigate_and_select_modified_by_column_in_build_id_rules(self):
        """
        Navigating to build id rules page and selecting the provided modified by
        """
        page1 = self.navigate_to_build_id_rules_page()
        page1.fill_input_text(self.MODIFIED_BY_TEXT_BOX,self.config.get("updated_by"))
        page1.select_option_by_text(self.APPROVAL_STATUS_DROPDOWN, "Pending")
        page1.validate_page_loading()
        return page1


