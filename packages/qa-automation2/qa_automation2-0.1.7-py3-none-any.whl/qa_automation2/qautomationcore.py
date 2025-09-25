import time, sys
from typing import Literal, List
from uiautomator2 import Direction
import uiautomator2 as u2
from .loginfor import setup_logger
from .adbcore import *

class qa_automation:
    def __init__(self, device:str=None, device_infor: dict=None):
        self.device = device
        self.logger = setup_logger(name=device_infor.get("model"))
    def wait_activity(self, activity_name:str, timeout:int=10)-> bool:

        if not self.device.wait_activity(activity_name, timeout=timeout):
            self.logger.error(f"Activity {activity_name} did not load within {timeout} seconds.")
            return False
        return True
    # def wait_for_element(self, name:str, type_:Literal["text", "talkback", "resource_id", "xpath"]="text", timeout:int=10)-> bool:
    #     if type_ == "text":
    #         element = self.device(text=name)
    #         element.wait_timeout = timeout
    #         if element.wait:
    #             return element
    #         return False


    def get_info_element(self, element,
                                type_get:Literal["bounds", "childCount", "className", "contentDescription", "packageName", "resourceName", "text",
                                    "visibleBounds", "checkable", "checked", "clickable", "enabled", "focusable", "focused", "longClickable", 
                                    "scrollable", "selected"] = "text")-> str | int | bool | None:
        """"
        {
            'bounds': {'bottom': 1348, 'left': 39, 'right': 285, 'top': 1005},
            'childCount': 0,
            'className': 'android.widget.TextView',
            'contentDescription': 'Camera',
            'packageName': 'com.sec.android.app.launcher',
            'resourceName': 'com.sec.android.app.launcher:id/apps_icon',
            'text': 'Camera',
            'visibleBounds': {'bottom': 1348, 'left': 39, 'right': 285, 'top': 1005},
            'checkable': False,
            'checked': False,
            'clickable': True,
            'enabled': True,
            'focusable': True,
            'focused': False,
            'longClickable': True,
            'scrollable': False,
            'selected': False
        }
        """
        if element:
            return element.info.get(type_get)
        return None
    def get_all_text_element(self, name:str, type_:Literal["text", "talkback", "resource_id", "xpath"]="text")-> List[str] | None:
        """
        Get all text from element
        """
        element = self.Find_element(name=name, type_=type_)
        if element:
            print(element.sibling().count)
            # parent = element.from_parent()
            # print(len(parent.child()))
            # if parent:
            #     # Lấy tất cả các con của parent (tức là sibling của element)
            #     all_children = parent.child()
            #     return [el.info.get("text") for el in all_children if el.info.get("text")]
        return None
    def Find_element(self, name:str, type_:Literal["text", "talkback", "resource_id", "xpath"]="text")->bool:
        if type_ =="text":
            element = self.device(text=name)
            if element.exists:
                return element
            return False
        elif type_ == "resource_id":
            element = self.device(resourceId=name)
            if element.exists:
                return element
            return False
        elif type_ == "talkback":
            element = self.device(description=name)
            if element.exists:
                return element
            return False
        elif type_ =="xpath":
            element = self.device.xpath(name)
            if element.exists:
                return element
            return False
        else:
            print(f'{type_} wrong not in "text", "talkback", "resource_id", "xpath" please input correct')
            return False
    def Touch(self, name:str, type_:Literal["text", "talkback", "resource_id", "xpath"]="text", long_:bool=False)->bool:
        element = self.Find_element(name=name, type_=type_)
        if element:
            if long_:
                element.long_click()
            element.click()
            return True
        return False

    def scroll(self, type_:Literal["up", "down", "left", "right", "top", "bottom"]="up",
            scale:float=0.9, box:list[int, int, int, int]=None,duration:float=None, steps:float=None):
        if type_ =="top":
            self.device(scrollable=True).scroll.toBeginning()
        elif type_ =="bottom":
            self.device(scrollable=True).scroll.toEnd()
        elif type_=="up":
            self.device.swipe_ext(direction=Direction.UP, scale=scale, box=box, duration=duration, steps=steps)
        elif type_=="down":
            self.device.swipe_ext(direction=Direction.DOWN, scale=scale, box=box, duration=duration, steps=steps)
        elif type_ == "left":
            self.device.swipe_ext(direction=Direction.LEFT, scale=scale, box=box, duration=duration, steps=steps)
        elif type_ == "right":
            self.device.swipe_ext(direction=Direction.RIGHT, scale=scale, box=box, duration=duration, steps=steps)
        else:
            return False        
    def scroll_to_find_element(self, name:str, type_:Literal["text", "talkback", "resource_id", "xpath"]="text",
                            type_scroll:Literal["up", "down", "left", "right", "top", "bottom"]="up",
                            max_scrolls=20, delay=0.5, scale:float=0.9, box:list[int, int, int, int]=None,
                            duration:float=None, steps:float=None)->bool:
        last_ui = ""
        for _ in range(max_scrolls):
            element = self.Find_element(name=name, type_=type_)
            if element:
                return element
            current_ui = self.device.dump_hierarchy(compressed=True)
            if current_ui == last_ui:
                break
            self.scroll(type_=type_scroll, scale=scale, box=box, duration=duration, steps=steps)
            time.sleep(delay)
            last_ui = current_ui
        return False


    def scroll_and_click_element(self, name:str, type_:Literal["text", "talkback", "resource_id", "xpath"]="text",
                                type_scroll:Literal["up", "down", "left", "right", "top", "bottom"]="up",
                                max_scrolls=20, delay=0.5, scale:float=0.9, box:list[int, int, int, int]=None,
                                duration:float=None, steps:float=None)->bool:
        element = self.scroll_to_find_element(name, type_, type_scroll, max_scrolls, delay, scale, box, duration, steps)
        if element:
            element.click()
            return True
        return False
    def scroll_up_down_find_element(self, name:str, type_:Literal["text", "talkback", "resource_id", "xpath"]="text",
                                    type_scroll:Literal["updown", "letfright"]="updown",                           
                                    max_scrolls=20, delay=0.5, scale:float=0.9, box:list[int, int, int, int]=None,
                                    duration:float=None, steps:float=None)->bool:
        if type_scroll == "updown":
            element = self.scroll_to_find_element(name, type_, "up", max_scrolls, delay, scale, box, duration, steps)
            if element:
                return element
            element = self.scroll_to_find_element(name, type_,"down", max_scrolls, delay, scale, box, duration, steps)
            if element:
                return element
            return False
        elif type_scroll == "letfright":
            element = self.scroll_to_find_element(name, type_, "left", max_scrolls, delay, scale, box, duration, steps)
            if element:
                return element
            element = self.scroll_to_find_element(name, type_,"right", max_scrolls, delay, scale, box, duration, steps)
            if element:
                return element
            return False
        else:
            print(f"{type_scroll} wrong please input correct updown or letfright")
            return False

    def scroll_up_down_find_element_click(self, name:str, type_:Literal["text", "talkback", "resource_id", "xpath"]="text",
                                    type_scroll:Literal["updown", "letfright"]="updown",                           
                                    max_scrolls=20, delay=0.5, scale:float=0.9, box:list[int, int, int, int]=None,
                                    duration:float=None, steps:float=None)->bool:
        element = self.scroll_up_down_find_element(name, type_, type_scroll, max_scrolls, delay, scale, box, duration, steps)
        if element:
            element.click()
            return True
        return False
    

