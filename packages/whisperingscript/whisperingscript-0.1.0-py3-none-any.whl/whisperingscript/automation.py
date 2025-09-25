#!/usr/bin/env python3
"""
Whispering.bradenwong.com Browser Automation Script

This script automates the following workflow:
1. Opens whispering.bradenwong.com in a headless Chrome browser
2. Navigates to settings and configures recording/transcription
3. Starts recording
4. Stops recording, waits for transcription, and copies then pastes the result
"""
import os
import signal
import subprocess
import sys
import threading
import time
from pathlib import Path

import pyperclip
from plyer import notification
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class WhisperingAutomation:
    def __init__(
        self, headless=True, stop_method="file", recording_duration=30
    ):
        self.driver = None
        self.wait = None
        self.headless = headless
        self.stop_signal_received = False
        self.stop_method = stop_method  # Options: "file", "signal", "time"
        self.recording_duration = (
            recording_duration  # seconds for time-based stopping
        )

    def setup_browser(self):
        """Initialize Chrome browser with necessary options"""
        chrome_options = Options()

        if self.headless:
            chrome_options.add_argument("--headless")

        # Enable microphone access
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--disable-features=VizDisplayCompositor")
        chrome_options.add_argument(
            "--disable-notifications"
        )  # Blocks all notifications
        chrome_options.add_argument("--disable-popup-blocking")

        if self.headless:
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--remote-debugging-port=9222")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-plugins")
            chrome_options.add_argument(
                "--window-size=1920,1080"
            )  # Set explicit window size

        # Grant microphone permissions
        prefs = {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.notifications": 1,
        }
        chrome_options.add_experimental_option("prefs", prefs)

        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.wait = WebDriverWait(self.driver, 10)
            print("✓ Browser initialized successfully")
        except Exception as e:
            print(f"✗ Failed to initialize browser: {e}")
            raise

    @staticmethod
    def show_notification(message, timeout=5):
        """
        Show a notification
        :param message: the message to show
        :param timeout: the timeout in seconds
        """
        notification.notify(
            title="Whisperer",
            message=message,
            timeout=timeout,
        )

    def navigate_to_site(self):
        """Navigate to the whispering website"""
        try:
            print("Navigating to whispering.bradenwong.com...")
            self.driver.get("https://whispering.bradenwong.com/")
            print("✓ Successfully loaded the website")
        except Exception as e:
            print(f"✗ Failed to load website: {e}")
            raise

    def click_settings(self):
        """Click the settings button"""
        try:
            print("Looking for settings button...")
            # Try multiple selectors for the settings button
            selectors = [
                'a[href="/settings"]',
                'a[data-slot="tooltip-trigger"]',
                'svg[class*="lucide-settings"]',
                ".lucide-settings",
            ]

            settings_button = None
            for selector in selectors:
                try:
                    settings_button = self.wait.until(
                        ec.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    break
                except TimeoutException:
                    continue

            if settings_button is None:
                raise Exception("Could not find settings button")

            settings_button.click()
            print("✓ Clicked settings button")
            time.sleep(0.2)  # Wait for navigation
        except Exception as e:
            print(f"✗ Failed to click settings: {e}")
            raise

    def safe_click(self, element):
        """
        Click an element safely
        """
        try:
            element.click()
            return True
        except Exception:
            try:
                self.driver.execute_script("arguments[0].click();", element)
                return True
            except Exception:
                try:
                    ActionChains(self.driver).move_to_element(
                        element
                    ).click().perform()
                    return True
                except Exception:
                    return False

    def configure_recording(self):
        """Click on Recording section"""
        try:
            print("Looking for Recording section...")
            # Try multiple selectors for Recording
            selectors = [
                '//a[contains(@href, "recordings") or contains(@href, "recording")]',
                '//a[.//span[contains(text(), "Recording")]]',
                '//span[contains(text(), "Recording")]/parent::*',
                '//span[contains(text(), "Recording")]/ancestor::a',
                'a[href*="recording"]',
            ]

            recording_element = None
            for selector in selectors:
                try:
                    if selector.startswith("//"):
                        recording_element = self.wait.until(
                            ec.element_to_be_clickable((By.XPATH, selector))
                        )
                    else:
                        recording_element = self.wait.until(
                            ec.element_to_be_clickable(
                                (By.CSS_SELECTOR, selector)
                            )
                        )
                    break
                except TimeoutException:
                    continue

            if recording_element is None:
                raise Exception("Could not find Recording section")

            # Use safe click method
            if self.safe_click(recording_element):
                print("✓ Clicked Recording section")
                time.sleep(0.2)
            else:
                raise Exception(
                    "Failed to click Recording element with all methods"
                )

        except Exception as e:
            print(f"✗ Failed to click Recording section: {e}")
            raise

    def configure_transcription(self):
        """Configure transcription settings"""
        try:
            print("Looking for Transcription section...")
            # Try multiple selectors for Transcription
            selectors = [
                '//a[contains(@href, "transcription")]',
                '//a[.//span[contains(text(), "Transcription")]]',
                '//span[contains(text(), "Transcription")]/parent::*',
                '//span[contains(text(), "Transcription")]/ancestor::a',
                'a[href*="transcription"]',
            ]

            transcription_element = None
            for selector in selectors:
                try:
                    if selector.startswith("//"):
                        transcription_element = self.wait.until(
                            ec.element_to_be_clickable((By.XPATH, selector))
                        )
                    else:
                        transcription_element = self.wait.until(
                            ec.element_to_be_clickable(
                                (By.CSS_SELECTOR, selector)
                            )
                        )
                    break
                except TimeoutException:
                    continue

            if transcription_element is None:
                raise Exception("Could not find Transcription section")

            # Use safe click method
            if self.safe_click(transcription_element):
                print("✓ Clicked Transcription section")
                time.sleep(0.2)  # Give more time for page to load
            else:
                raise Exception(
                    "Failed to click Transcription element with all methods"
                )

            # Look for the current transcription service display
            print("Looking for current transcription service...")
            try:
                current_service = self.driver.find_element(
                    By.XPATH,
                    "//*[contains(text(), 'Current transcription service')]",
                )
                if current_service:
                    print(
                        f"Found current service text: {current_service.text}"
                    )
            except:
                pass

            # Find the actual dropdown button for transcription service
            print("Looking for transcription service dropdown button...")
            dropdown_selectors = [
                # Target the specific select trigger button
                'button[data-slot="select-trigger"]',
                "button[data-select-trigger]",
                'button[aria-haspopup="listbox"]',
                # Look for button containing current service
                "//button[contains(text(), 'Groq Whisper')]",
                "//button[contains(text(), 'Whisper')]",
            ]

            dropdown_button = None
            for selector in dropdown_selectors:
                try:
                    if selector.startswith("//"):
                        dropdown_button = WebDriverWait(self.driver, 5).until(
                            ec.element_to_be_clickable((By.XPATH, selector))
                        )
                    else:
                        dropdown_button = WebDriverWait(self.driver, 5).until(
                            ec.element_to_be_clickable(
                                (By.CSS_SELECTOR, selector)
                            )
                        )
                    print(f"Found dropdown button with selector: {selector}")
                    print(f"Button text: '{dropdown_button.text.strip()}'")
                    break
                except TimeoutException:
                    continue

            if dropdown_button and self.safe_click(dropdown_button):
                print("✓ Opened transcription service dropdown")
                time.sleep(0.5)  # Wait for dropdown options to appear

                # Now look for OpenAI Whisper option using the exact selectors from your HTML
                print("Searching for OpenAI Whisper option...")
                whisper_selectors = [
                    # Target the exact element structure you provided
                    'div[data-value="OpenAI"]',
                    'div[data-label="OpenAI"]',
                    'div[data-slot="select-item"][data-value="OpenAI"]',
                    '[role="option"][data-value="OpenAI"]',
                    # Fallback selectors
                    "//div[contains(text(), 'OpenAI Whisper')]",
                    "//div[@role='option' and contains(text(), 'OpenAI')]",
                    "[role='option']:contains('OpenAI Whisper')",
                ]

                # First, debug what's actually in the dropdown
                try:
                    print("Dropdown contents after clicking:")
                    time.sleep(0.5)  # Brief wait for dropdown to fully appear

                    # Look specifically for select items and options
                    dropdown_options = self.driver.find_elements(
                        By.CSS_SELECTOR,
                        '[data-slot="select-item"], [role="option"], div[data-value]',
                    )
                    if dropdown_options:
                        print(
                            f"Found {len(dropdown_options)} dropdown options:"
                        )
                        for i, option in enumerate(dropdown_options):
                            try:
                                text = option.text.strip()
                                data_value = (
                                    option.get_attribute("data-value") or "N/A"
                                )
                                visible = option.is_displayed()
                                print(
                                    f"  Option {i + 1}: '{text}' (data-value: {data_value}, visible: {visible})"
                                )
                            except:
                                pass
                    else:
                        # Fallback - look for any elements with OpenAI or Whisper
                        all_whisper_elements = self.driver.find_elements(
                            By.XPATH,
                            "//*[contains(text(), 'OpenAI') or contains(text(), 'Whisper')]",
                        )
                        print(
                            f"Found {len(all_whisper_elements)} elements containing 'OpenAI' or 'Whisper':"
                        )
                        for i, element in enumerate(all_whisper_elements[:5]):
                            try:
                                text = element.text.strip()
                                tag = element.tag_name
                                visible = element.is_displayed()
                                if text and len(text) < 100:
                                    print(
                                        f"  Element {i + 1}: '{text}' (tag: {tag}, visible: {visible})"
                                    )
                            except:
                                pass

                except Exception as debug_e:
                    print(f"Debug dropdown contents failed: {debug_e}")

                # Try to find and click OpenAI Whisper
                whisper_option = None
                for selector in whisper_selectors:
                    try:
                        if selector.startswith("//"):
                            whisper_option = WebDriverWait(
                                self.driver, 3
                            ).until(
                                ec.element_to_be_clickable(
                                    (By.XPATH, selector)
                                )
                            )
                        else:
                            whisper_option = WebDriverWait(
                                self.driver, 3
                            ).until(
                                ec.element_to_be_clickable(
                                    (By.CSS_SELECTOR, selector)
                                )
                            )
                        print(
                            f"Found OpenAI Whisper with selector: {selector}"
                        )
                        break
                    except TimeoutException:
                        continue

                if whisper_option:
                    if self.safe_click(whisper_option):
                        print("✓ Selected OpenAI Whisper")
                        time.sleep(0.5)
                    else:
                        print(
                            "⚠ Found OpenAI Whisper option but failed to click it"
                        )
                else:
                    print("⚠ Could not find OpenAI Whisper option in dropdown")
                    # Try to close dropdown by clicking it again
                    if dropdown_button:
                        self.safe_click(dropdown_button)
            else:
                print(
                    "⚠ Could not find or open transcription service dropdown"
                )

            # Enter API key
            print("Looking for API key input...")
            api_key_selectors = [
                'input[type="password"]',
                'input[placeholder*="OpenAI API Key"]',
                'input[placeholder*="API Key"]',
                'input[id*="openai"]',
                'input[id*="api-key"]',
                'input[name*="api"]',
                # Look near OpenAI related text
                "//*[contains(text(), 'OpenAI')]/following::input[1]",
                "//*[contains(text(), 'API Key')]/following::input[1]",
            ]

            api_key_input = None
            for selector in api_key_selectors:
                try:
                    if selector.startswith("//"):
                        api_key_input = WebDriverWait(self.driver, 3).until(
                            ec.presence_of_element_located(
                                (By.XPATH, selector)
                            )
                        )
                    else:
                        api_key_input = WebDriverWait(self.driver, 3).until(
                            ec.presence_of_element_located(
                                (By.CSS_SELECTOR, selector)
                            )
                        )
                    print(f"Found API key input with selector: {selector}")
                    break
                except TimeoutException:
                    continue

            # Enter API key
            api_key_input.clear()
            key = self.read_openai_api_key()

            if self.headless:
                # For headless mode, use JavaScript to clear and set value
                self.driver.execute_script(
                    "arguments[0].value = '';", api_key_input
                )
                self.driver.execute_script(
                    "arguments[0].value = arguments[1];", api_key_input, key
                )
                # Trigger input events for validation
                self.driver.execute_script(
                    """
                    var element = arguments[0];
                    element.dispatchEvent(new Event('input', { bubbles: true }));
                    element.dispatchEvent(new Event('change', { bubbles: true }));
                """,
                    api_key_input,
                )
            else:
                pyperclip.copy(key)
                print("Entering API key...")
                api_key_input.click()
                api_key_input.send_keys(Keys.CONTROL + "V")
                pyperclip.copy("BLANK")
                print("✓ Entered API key")

        except Exception as e:
            print(f"✗ Failed to configure transcription: {e}")
            # Don't raise exception, continue with the rest of the workflow
            print("⚠ Continuing with default transcription settings...")

    @staticmethod
    def read_openai_api_key():
        """Read OpenAI API key from ~/.openai file"""
        try:
            openai_file = Path.home() / ".openai"

            if not openai_file.exists():
                print(f"⚠ OpenAI API key file not found: {openai_file}")
                return "123"  # Fallback to default

            api_key = openai_file.read_text().strip()
            if not api_key:
                print(f"⚠ OpenAI API key file is empty: {openai_file}")
                return "123"  # Fallback to default

            print(f"✓ Successfully read API key from {openai_file}")
            # Only show first/last few characters for security
            masked_key = (
                f"{api_key[:6]}...{api_key[-4:]}"
                if len(api_key) > 10
                else "***"
            )
            print(f"  API key: {masked_key}")
            return api_key

        except Exception as e:
            print(f"⚠ Failed to read OpenAI API key from ~/.openai: {e}")
            print("  Using fallback key '123', which will fail")
            return "123"

    def return_to_home(self):
        """Click on the whispering logo to return to home"""
        try:
            print("Returning to home page...")
            # Try multiple selectors for the home link
            selectors = [
                '//span[contains(text(), "whispering")]/parent::*',
                '//span[contains(text(), "whispering")]/ancestor::a',
                '//a[contains(@href, "/") and contains(text(), "whispering")]',
                'a[href="/"]',
                '//h1//span[contains(text(), "whispering")]',
                '.logo, [class*="logo"]',
            ]

            home_link = None
            for selector in selectors:
                try:
                    if selector.startswith("//"):
                        home_link = self.wait.until(
                            ec.element_to_be_clickable((By.XPATH, selector))
                        )
                    else:
                        home_link = self.wait.until(
                            ec.element_to_be_clickable(
                                (By.CSS_SELECTOR, selector)
                            )
                        )
                    break
                except TimeoutException:
                    continue

            if home_link and self.safe_click(home_link):
                print("✓ Returned to home page")
                time.sleep(0.5)
            else:
                # Alternative: navigate directly to home page
                print("⚠ Could not find home link, navigating directly...")
                self.driver.get("https://whispering.bradenwong.com/")
                time.sleep(0.5)
                print("✓ Navigated to home page")

        except Exception as e:
            print(f"✗ Failed to return to home: {e}")
            raise

    def start_recording(self):
        """Click the microphone button to start recording"""
        try:
            print("Looking for microphone button...")
            # Try multiple selectors for the microphone button based on your HTML
            selectors = [
                # Target the specific button structure you provided
                'button[data-slot="tooltip-trigger"]',
                "button[data-tooltip-trigger]",
                # Look for button containing the microphone emoji span
                "//button[.//span[contains(text(), '🎙️')]]",
                "//button[contains(@class, 'size-32') or contains(@class, 'size-36')]",
                # Look for button with "Start recording" text in sr-only span
                "//button[.//span[contains(text(), 'Start recording')]]",
                # Fallback selectors
                "//span[contains(text(), '🎙️')]/parent::button",
                "//span[contains(text(), '🎙️')]/ancestor::button",
                "//*[contains(text(), '🎙️')]",
                "[aria-label*='microphone' i], [aria-label*='record' i]",
                "button[class*='microphone'], button[class*='record']",
            ]

            mic_button = None
            for selector in selectors:
                try:
                    if selector.startswith("//"):
                        mic_button = WebDriverWait(self.driver, 5).until(
                            ec.element_to_be_clickable((By.XPATH, selector))
                        )
                    else:
                        mic_button = WebDriverWait(self.driver, 5).until(
                            ec.element_to_be_clickable(
                                (By.CSS_SELECTOR, selector)
                            )
                        )
                    print(f"Found microphone button with selector: {selector}")
                    # Try to get some info about the button
                    try:
                        button_id = mic_button.get_attribute("id") or "N/A"
                        button_text = mic_button.text.strip() or "N/A"
                        print(f"Button ID: {button_id}, Text: '{button_text}'")
                    except:
                        pass
                    break
                except TimeoutException:
                    continue

            if mic_button:
                if self.safe_click(mic_button):
                    print("✓ Started recording - waiting for stop signal...")
                    self.show_notification("✓ RECORDING ENABLED")
                else:
                    print("⚠ Found microphone button but failed to click it")
                    # Try scrolling to the button and clicking again
                    try:
                        self.driver.execute_script(
                            "arguments[0].scrollIntoView(true);", mic_button
                        )
                        time.sleep(0.5)
                        if self.safe_click(mic_button):
                            print(
                                "✓ Started recording after scrolling - waiting for stop signal..."
                            )
                        else:
                            raise Exception(
                                "Failed to click microphone button even after scrolling"
                            )
                    except Exception as scroll_e:
                        raise Exception(
                            f"Could not click microphone button: {scroll_e}"
                        )
            else:
                # Debug: show what buttons are available on the page
                print("Could not find microphone button. Available buttons:")
                try:
                    all_buttons = self.driver.find_elements(
                        By.TAG_NAME, "button"
                    )
                    for i, button in enumerate(
                        all_buttons[:10]
                    ):  # Show first 10 buttons
                        try:
                            text = button.text.strip()[
                                :50
                            ]  # Limit text length
                            data_slot = button.get_attribute("data-slot") or ""
                            classes = button.get_attribute("class") or ""
                            visible = button.is_displayed()
                            print(
                                f"  Button {i + 1}: '{text}' (data-slot: {data_slot}, visible: {visible})"
                            )
                            if (
                                "🎙️" in text
                                or "microphone" in classes.lower()
                                or "record" in classes.lower()
                            ):
                                print(
                                    f"    *** This might be the microphone button! ***"
                                )
                        except:
                            pass
                except:
                    pass
                raise Exception("Could not find microphone button")

        except Exception as e:
            print(f"✗ Failed to start recording: {e}")
            raise

    def setup_stop_listener(self):
        """Set up stop signal detection based on chosen method"""
        if self.stop_method == "file":
            self.setup_file_watcher()
        elif self.stop_method == "signal":
            self.setup_signal_handler()
        elif self.stop_method == "time":
            self.setup_timer()

    def setup_file_watcher(self):
        """Watch for a stop file to be created"""

        def watch_for_stop_file():
            stop_file = "/tmp/whispering_stop"
            print(f"Monitoring for stop file: {stop_file}")
            print("To stop recording: touch /tmp/whispering_stop")

            while not self.stop_signal_received:
                if os.path.exists(stop_file):
                    self.stop_signal_received = True
                    print("✓ Stop file detected!")
                    # Clean up the file
                    try:
                        os.remove(stop_file)
                    except:
                        pass
                    break
                time.sleep(0.2)

        listener_thread = threading.Thread(
            target=watch_for_stop_file, daemon=True
        )
        listener_thread.start()

    def setup_signal_handler(self):
        """Set up SIGUSR1 signal handler for stopping"""

        def signal_handler(signum, _):
            if signum == signal.SIGUSR1:
                self.stop_signal_received = True
                print("✓ SIGUSR1 signal received!")

        signal.signal(signal.SIGUSR1, signal_handler)
        print(f"To stop recording: kill -USR1 {os.getpid()}")

    def setup_timer(self):
        """Set up automatic timer-based stopping"""

        def timer_stop():
            time.sleep(self.recording_duration)
            self.stop_signal_received = True
            print(f"✓ Timer expired after {self.recording_duration} seconds!")

        timer_thread = threading.Thread(target=timer_stop, daemon=True)
        timer_thread.start()
        print(
            f"Recording will automatically stop after {self.recording_duration} seconds"
        )

    def wait_for_stop_signal(self):
        """Wait for stop signal based on chosen method"""
        method_messages = {
            "file": "Create the file /tmp/whispering_stop to stop recording",
            "signal": f"Send SIGUSR1 to process {os.getpid()} to stop recording",
            "time": f"Recording will stop automatically in {self.recording_duration} seconds",
        }

        print(
            f"Recording started. {method_messages.get(self.stop_method, '')}"
        )

        # Wait for the signal
        while not self.stop_signal_received:
            time.sleep(0.1)

    def stop_recording(self):
        """Click the stop button to end recording"""
        try:
            print("Stopping recording...")
            # Try multiple selectors for the stop button based on your HTML
            selectors = [
                # Target the specific button structure you provided
                'button[data-slot="tooltip-trigger"]',
                "button[data-tooltip-trigger]",
                # Look for button containing the stop emoji span
                "//button[.//span[contains(text(), '⏹️')]]",
                "//button[contains(@class, 'size-32') or contains(@class, 'size-36')]",
                # Look for button with "Stop recording" text in sr-only span
                "//button[.//span[contains(text(), 'Stop recording')]]",
                # Fallback selectors
                "//span[contains(text(), '⏹️')]/parent::button",
                "//span[contains(text(), '⏹️')]/ancestor::button",
                "//*[contains(text(), '⏹️')]",
                "[aria-label*='stop' i]",
                "button[class*='stop']",
            ]

            stop_button = None
            for selector in selectors:
                try:
                    if selector.startswith("//"):
                        stop_button = WebDriverWait(self.driver, 5).until(
                            ec.element_to_be_clickable((By.XPATH, selector))
                        )
                    else:
                        stop_button = WebDriverWait(self.driver, 5).until(
                            ec.element_to_be_clickable(
                                (By.CSS_SELECTOR, selector)
                            )
                        )
                    print(f"Found stop button with selector: {selector}")
                    # Try to get some info about the button
                    try:
                        button_id = stop_button.get_attribute("id") or "N/A"
                        button_text = stop_button.text.strip() or "N/A"
                        print(f"Button ID: {button_id}, Text: '{button_text}'")
                    except:
                        pass
                    break
                except TimeoutException:
                    continue

            if stop_button:
                if self.safe_click(stop_button):
                    print("✓ Stopped recording")
                else:
                    print("⚠ Found stop button but failed to click it")
                    # Try scrolling to the button and clicking again
                    try:
                        self.driver.execute_script(
                            "arguments[0].scrollIntoView(true);", stop_button
                        )
                        time.sleep(1)
                        if self.safe_click(stop_button):
                            print("✓ Stopped recording after scrolling")
                        else:
                            raise Exception(
                                "Failed to click stop button even after scrolling"
                            )
                    except Exception as scroll_e:
                        raise Exception(
                            f"Could not click stop button: {scroll_e}"
                        )
            else:
                # Debug: show what buttons are available on the page
                print("Could not find stop button. Available buttons:")
                try:
                    all_buttons = self.driver.find_elements(
                        By.TAG_NAME, "button"
                    )
                    for i, button in enumerate(
                        all_buttons[:10]
                    ):  # Show first 10 buttons
                        try:
                            text = button.text.strip()[
                                :50
                            ]  # Limit text length
                            data_slot = button.get_attribute("data-slot") or ""
                            classes = button.get_attribute("class") or ""
                            visible = button.is_displayed()
                            print(
                                f"  Button {i + 1}: '{text}' (data-slot: {data_slot}, visible: {visible})"
                            )
                            if "⏹️" in text or "stop" in classes.lower():
                                print(
                                    f"    *** This might be the stop button! ***"
                                )
                        except:
                            pass
                except:
                    pass
                raise Exception("Could not find stop button")

        except Exception as e:
            print(f"✗ Failed to stop recording: {e}")
            raise

    def get_transcription(self):
        """Wait for transcription and copy it to clipboard"""
        try:
            print("Looking for transcription textarea...")
            # Look for textarea with transcribed text
            selectors = [
                'textarea[id*="transcribedText"]',
                'textarea[data-slot="dialog-trigger"]',
                "textarea[readonly]",
            ]

            transcription_textarea = None
            for selector in selectors:
                try:
                    transcription_textarea = WebDriverWait(
                        self.driver, 5
                    ).until(
                        ec.presence_of_element_located(
                            (By.CSS_SELECTOR, selector)
                        )
                    )
                    print(
                        f"Found transcription textarea with selector: {selector}"
                    )
                    break
                except TimeoutException:
                    continue

            if transcription_textarea is None:
                raise Exception("Could not find transcription textarea")

            # Wait for the textarea to contain transcribed text (non-empty and not placeholder)
            print("Waiting for transcription to appear...")
            max_wait_time = 60  # Maximum 60 seconds to wait for transcription
            wait_interval = 1  # Check every 1 second

            for attempt in range(max_wait_time):
                # Get the text content
                transcription_text = transcription_textarea.get_attribute(
                    "value"
                )
                if not transcription_text:
                    transcription_text = transcription_textarea.text

                # Check if we have actual transcription content
                if transcription_text and transcription_text.strip():
                    # Make sure it's not just placeholder or loading text
                    placeholder_phrases = [
                        "loading",
                        "processing",
                        "transcribing",
                        "please wait",
                        "...",
                    ]
                    is_placeholder = any(
                        phrase in transcription_text.lower()
                        for phrase in placeholder_phrases
                    )

                    if (
                        not is_placeholder
                        and len(transcription_text.strip()) > 3
                    ):
                        print(
                            f"✓ Transcription appeared after {attempt + 1} seconds"
                        )
                        break

                # Show progress every 5 seconds
                if (attempt + 1) % 5 == 0:
                    print(
                        f"  Still waiting for transcription... ({attempt + 1}/{max_wait_time}s)"
                    )

                time.sleep(wait_interval)
            else:
                # If we get here, we've waited the full time without getting transcription
                print(
                    f"⚠ Timeout waiting for transcription after {max_wait_time} seconds"
                )
                transcription_text = (
                    transcription_textarea.get_attribute("value")
                    or transcription_textarea.text
                    or ""
                )

            # Copy to clipboard
            if transcription_text and transcription_text.strip():
                pyperclip.copy(transcription_text)
                print(
                    f"✓ Transcription copied to clipboard: '{transcription_text}'"
                )
                return transcription_text
            else:
                print("⚠ No transcription text found")
                return ""

        except Exception as e:
            print(f"✗ Failed to get transcription: {e}")
            raise

    def cleanup(self):
        """Clean up browser resources"""
        if self.driver:
            self.driver.quit()
            print("✓ Browser closed")

    def run(self):
        """Execute the complete automation workflow"""
        try:
            print("Starting Whispering automation...")
            print("=" * 50)

            # Setup
            self.setup_browser()
            self.setup_stop_listener()

            # Navigation and configuration
            self.navigate_to_site()
            self.click_settings()
            self.configure_transcription()
            self.return_to_home()

            # Recording workflow
            self.start_recording()
            self.wait_for_stop_signal()
            self.stop_recording()

            # Get results
            transcription = self.get_transcription()

            print("=" * 50)
            print("✓ Automation completed successfully!")
            if transcription:
                print(f"Final transcription: {transcription}")
                subprocess.run(["xdotool", "key", "ctrl+v"])
                self.show_notification("✓ RECORDING STOPPED")

            return transcription

        except Exception as e:
            print(f"✗ Automation failed: {e}")
            raise
        finally:
            self.cleanup()


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Whispering Browser Automation"
    )
    parser.add_argument(
        "--stop-method",
        choices=["file", "signal", "time"],
        default="file",
        help="Method to stop recording (default: file)",
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=30,
        help="Recording duration in seconds for timer method (default: 30)",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        default=True,
        help="Run browser in headless mode",
    )

    args = parser.parse_args()

    print("Whispering Browser Automation")
    print("This script will automate the whispering.bradenwong.com workflow")
    print(f"Stop method: {args.stop_method}")
    if args.stop_method == "time":
        print(f"Recording duration: {args.duration} seconds")
    print()

    # Check if running in terminal
    if not sys.stdin.isatty() and args.stop_method not in [
        "file",
        "signal",
        "time",
    ]:
        print("Warning: Not running in an interactive terminal.")
        print(
            "Consider using --stop-method file, signal, or time for background operation."
        )

    try:
        # Create and run automation
        automation = WhisperingAutomation(
            headless=args.headless,
            stop_method=args.stop_method,
            recording_duration=args.duration,
        )
        result = automation.run()

        if result:
            print(f"\nFinal result: {result}")

    except KeyboardInterrupt:
        print("\n⚠ Automation interrupted by user")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
