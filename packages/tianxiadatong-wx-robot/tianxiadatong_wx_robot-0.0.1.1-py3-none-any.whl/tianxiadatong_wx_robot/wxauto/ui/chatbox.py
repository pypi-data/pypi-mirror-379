from .base import BaseUISubWnd
from tianxiadatong_wx_robot.wxauto.ui.component import (
    CMenuWnd,
)
from tianxiadatong_wx_robot.wxauto.param import (
    WxParam, 
    WxResponse,
)
from tianxiadatong_wx_robot.wxauto.languages import *
from tianxiadatong_wx_robot.wxauto.utils import (
    SetClipboardText,
    SetClipboardFiles,
    GetAllWindowExs,
)
from tianxiadatong_wx_robot.wxauto.msgs import parse_msg
from tianxiadatong_wx_robot.wxauto import uiautomation as uia
from tianxiadatong_wx_robot.wxauto.logger import wxlog
from tianxiadatong_wx_robot.wxauto.uiautomation import Control
from tianxiadatong_wx_robot.wxauto.utils.tools import roll_into_view
import time
import os

USED_MSG_IDS = {}

class ChatBox(BaseUISubWnd):
    def __init__(self, control: uia.Control, parent):
        self.control: Control = control
        self.root = parent
        self.parent = parent  # `wx` or `chat`
        self.init()

    def init(self):
        self.msgbox = self.control.ListControl(Name=self._lang("消息"))
        # if not self.msgbox.Exists(0):
        #     return
        self.editbox = self.control.EditControl()
        self.sendbtn = self.control.ButtonControl(Name=self._lang('发送'))
        self.tools = self.control.PaneControl().ToolBarControl()
        # self.id = self.msgbox.runtimeid
        if (cid := self.id) and cid not in USED_MSG_IDS:
            USED_MSG_IDS[self.id] = tuple((i.runtimeid for i in self.msgbox.GetChildren()))

    def _lang(self, text: str) -> str:
        return WECHAT_CHAT_BOX.get(text, {WxParam.LANGUAGE: text}).get(WxParam.LANGUAGE)
    
    def _update_used_msg_ids(self):
        USED_MSG_IDS[self.id] = tuple((i.runtimeid for i in self.msgbox.GetChildren()))
    

    def _open_chat_more_info(self):
        for chatinfo_control, depth in uia.WalkControl(self.control):
            if chatinfo_control.Name == self._lang('聊天信息'):
                chatinfo_control.Click()
                break
        else:
            return WxResponse.failure('未找到聊天信息按钮')
        return ChatRoomDetailWnd(self)
    

    def _activate_editbox(self):
        if not self.editbox.HasKeyboardFocus:
            self.editbox.MiddleClick()

    @property
    def who(self):
        if hasattr(self, '_who'):
            return self._who
        self._who = self.editbox.Name
        return self._who

    @property
    def id(self):
        if self.msgbox.Exists(0):
            return self.msgbox.runtimeid
        return None

    @property
    def used_msg_ids(self):
        # print(self.id)
        # print(USED_MSG_IDS)
        # print(USED_MSG_IDS[self.id])
        return USED_MSG_IDS.setdefault(self.id, set())
        # return USED_MSG_IDS[self.id]
    
    def get_info(self):
        self._show()
        chat_info = {}
        walk = uia.WalkControl(self.control)
        for chat_name_control, depth in walk:
            if isinstance(chat_name_control, uia.TextControl):
                break
        if (
            not isinstance(chat_name_control, uia.TextControl)
            or depth < 8
        ):
            return {}
        
        # chat_name_control = self.control.GetProgenyControl(11)
        chat_name_control_list = chat_name_control.GetParentControl().GetChildren()
        chat_name_control_count = len(chat_name_control_list)
        
        if chat_name_control_count == 1:
            if self.control.ButtonControl(Name='公众号主页', searchDepth=9).Exists(0):
                chat_info['chat_type'] = 'official'
            else:
                chat_info['chat_type'] = 'friend'
            chat_info['chat_name'] = chat_name_control.Name
        elif chat_name_control_count >= 2:
            try:
                chat_info['group_member_count'] =\
                    int(chat_name_control_list[-1].Name.replace('(', '').replace(')', ''))
                chat_info['chat_type'] = 'group'
                chat_info['chat_name'] =\
                    chat_name_control.Name.replace(chat_name_control_list[-1].Name, '')
            except:
                chat_info['chat_type'] = 'friend'
                chat_info['chat_name'] = chat_name_control.Name
            
            ori_chat_name_control =\
                chat_name_control.GetParentControl().\
                    GetParentControl().TextControl(searchDepth=1)
            if ori_chat_name_control.Exists(0):
                chat_info['chat_remark'] = chat_info['chat_name']
                chat_info['chat_name'] = ori_chat_name_control.Name
        return chat_info
    

    def input_at(self, at_list):
        self._show()
        if isinstance(at_list, str):
            at_list = [at_list]
        self._activate_editbox()
        for friend in at_list:
            self.editbox.SendKeys('@'+friend.replace(' ', ''))
            atmenu = AtMenu(self)
            atmenu.select(friend)

    def input_at_all(self, at_list):
        self._show()
        self._activate_editbox()
        self.editbox.SendKeys('@')
        atmenu = AtMenu(self)
        atmenu.click_at_all()

    def clear_edit(self):
        self._show()
        self.editbox.Click()
        self.editbox.SendKeys('{Ctrl}a', waitTime=0)
        self.editbox.SendKeys('{DELETE}')


    def send_text(self, content: str):
        self._show()
        t0 = time.time()
        while True:
            if time.time() - t0 > 10:
                return WxResponse.failure(f'Timeout --> {self.who} - {content}')
            SetClipboardText(content)
            self._activate_editbox()
            self.editbox.SendKeys('{Ctrl}v')
            if self.editbox.GetValuePattern().Value.replace('￼', '').strip():
                break
            self.editbox.SendKeys('{Ctrl}v')
            if self.editbox.GetValuePattern().Value.replace('￼', '').strip():
                break
            self.editbox.RightClick()
            menu = CMenuWnd(self)
            menu.select('粘贴')
            if self.editbox.GetValuePattern().Value.replace('￼', '').strip():
                break
        t0 = time.time()
        while self.editbox.GetValuePattern().Value:
            if time.time() - t0 > 10:
                return WxResponse.failure(f'Timeout --> {self.who} - {content}')
            self._activate_editbox()

            self.sendbtn.Click()
            if not self.editbox.GetValuePattern().Value:
                return WxResponse.success(f"success")
            elif not self.editbox.GetValuePattern().Value.replace('￼', '').strip():
                return self.send_text(content)

    def send_msg(self, content: str, clear: bool=True, at=None):
        if not content and not at:
            return WxResponse.failure(f"参数 `content` 和 `at` 不能同时为空")
        
        if clear:
            self.clear_edit()
        if at:
            self.input_at(at)
        
        return self.send_text(content)

    def send_msg_at_all(self, content: str,at=None):
        self.input_at_all(at)
        return self.send_text(content)


    def send_file(self, file_path):
        self._show()
        if isinstance(file_path, str):
            file_path = [file_path]
        file_path = [os.path.abspath(f) for f in file_path]
        SetClipboardFiles(file_path)
        self._activate_editbox()
        self.editbox.SendKeys('{Ctrl}v')
        self.sendbtn.Click()
    
    def load_more(self, interval=0.3):
        self._show()
        msg_len = len(self.msgbox.GetChildren())
        loadmore = self.msgbox.GetChildren()[0]
        loadmore_top = loadmore.BoundingRectangle.top
        while True:
            if len(self.msgbox.GetChildren()) > msg_len:
                isload = True
                break
            else:
                msg_len = len(self.msgbox.GetChildren())
                self.msgbox.WheelUp(wheelTimes=10)
                time.sleep(interval)
                if self.msgbox.GetChildren()[0].BoundingRectangle.top == loadmore_top\
                    and len(self.msgbox.GetChildren()) == msg_len:
                    isload = False
                    break
                else:
                    loadmore_top = self.msgbox.GetChildren()[0].BoundingRectangle.top
                    
        self.msgbox.WheelUp(wheelTimes=1, waitTime=0.1)
        if isload:
            return WxResponse.success()
        else:
            return WxResponse.failure("没有更多消息了")
    

    def get_msgs(self):
        if self.msgbox.Exists(0):
            return [
                parse_msg(msg_control, self) 
                for msg_control 
                in self.msgbox.GetChildren()
                if msg_control.ControlTypeName == 'ListItemControl'
            ]
        return []
    
    def get_new_msgs(self):
        if not self.msgbox.Exists(0):
            return []
        msg_controls = self.msgbox.GetChildren()
        now_msg_ids = tuple((i.runtimeid for i in msg_controls))
        if (
            not now_msg_ids
            or (not self.used_msg_ids and now_msg_ids)
            or now_msg_ids[-1] == self.used_msg_ids[-1]
            or not set(now_msg_ids)&set(self.used_msg_ids)
        ):
            wxlog.debug('没有新消息sjs')
            return []
        
        used_msg_ids_set = set(self.used_msg_ids)
        last_one_msgid = max(
            (x for x in now_msg_ids if x in used_msg_ids_set), 
            key=self.used_msg_ids.index, default=None
        )
        new1 = [x for x in now_msg_ids if x not in used_msg_ids_set]
        new2 = now_msg_ids[now_msg_ids.index(last_one_msgid) + 1 :]\
            if last_one_msgid is not None else []
        new = [i for i in new1 if i in new2] if new2 else new1
        USED_MSG_IDS[self.id] = tuple(self.used_msg_ids + tuple(new))[-100:]
        new_controls = [i for i in msg_controls if i.runtimeid in new]
        self.msgbox.MiddleClick()
        return [
                parse_msg(msg_control, self) 
                for msg_control 
                in new_controls
                if msg_control.ControlTypeName == 'ListItemControl'
            ]
    
    def _get_tail_after_nth_match(self, msgs, last_msg, n):
        matches = [
            i for i, msg in reversed(list(enumerate(msgs))) 
            if msg.content == last_msg
        ]
        if len(matches) >= n:
            wxlog.debug(f'匹配到基准消息：{last_msg}')
        else:
            split_last_msg = last_msg.split('：')
            nickname = split_last_msg[0]
            content = ''.join(split_last_msg[1:])
            matches = [
                i for i, msg in reversed(list(enumerate(msgs))) 
                if msg.content == content
                and msg.sender_remark == nickname
            ]
            if len(matches) >= n:
                wxlog.debug(f'匹配到基准消息：<{nickname}> {content}')
            else:
                wxlog.debug(f"未匹配到基准消息，以最后一条消息为基准：{msgs[-1].content if msgs and hasattr(msgs[-1], 'content') else ''}")
                matches = [
                    i for i, msg in reversed(list(enumerate(msgs))) 
                    if msg.attr in ('self', 'friend')
                ]
        try:
            index = matches[n - 1]
            return msgs[index:]
        except IndexError:
            wxlog.debug(f"未匹配到第{n}条消息，返回空列表")
            return []
    
    def get_next_new_msgs(self, count=None, last_msg=None):
        # 1. 消息列表不存在，则返回空列表
        if not self.msgbox.Exists(0):
            wxlog.debug('消息列表不存在，返回空列表')
            return []
        
        # 2. 判断是否有新消息按钮，有的话点一下
        load_new_button = self.control.ButtonControl(RegexName=self._lang('re_新消息按钮'))
        if load_new_button.Exists(0): 
            self._show()
            wxlog.debug('检测到新消息按钮，点击加载新消息')
            load_new_button.Click()
            time.sleep(0.5)
        msg_controls = self.msgbox.GetChildren()
        USED_MSG_IDS[self.id] = tuple((i.runtimeid for i in msg_controls))
        msgs = [
            parse_msg(msg_control, self)
            for msg_control
            in msg_controls
            if msg_control.ControlTypeName == 'ListItemControl'
        ]

        # 3. 如果有“以下是新消息”标志，则直接返回该标志下的所有消息即可
        index = next((
            i for i, msg in enumerate(msgs) 
            if self._lang('以下为新消息') == msg.content
        ), None)
        if index is not None:
            wxlog.debug('获取以下是新消息下的所有消息')
            return msgs[index:]
        
        # 4. 根据会话列表传入的消息数量和最后一条新消息内容来判断新消息
        if count and last_msg:
            # index = next((
            #     i for i, msg in enumerate(msgs[::-1]) 
            #     if last_msg == msg.content
            # ), None)

            # if index is not None:
            wxlog.debug(f'获取{count}条新消息，基准消息内容为：{last_msg}')
            return self._get_tail_after_nth_match(msgs, last_msg, count)
                
    def get_group_members(self):
        self._show()
        roominfoWnd = self._open_chat_more_info()
        return roominfoWnd.get_group_members()


class ChatRoomDetailWnd(BaseUISubWnd):
    _ui_cls_name: str = 'SessionChatRoomDetailWnd'

    def __init__(self, parent):
        self.parent = parent
        self.root = parent.root
        self.control = self.root.control.Control(ClassName=self._ui_cls_name, searchDepth=1)

    def _lang(self, text: str) -> str:
        return CHATROOM_DETAIL_WINDOW.get(text, {WxParam.LANGUAGE: text}).get(WxParam.LANGUAGE)

    def _edit(self, key, value):
        wxlog.debug(f'修改{key}为`{value}`')
        btn = self.control.TextControl(Name=key).GetParentControl().ButtonControl(Name=key)
        if btn.Exists(0):
            roll_into_view(self.control, btn)
            btn.Click()
        else:
            wxlog.debug(f'当前非群聊，无法修改{key}')
            return WxResponse.failure(f'Not a group chat, cannot modify `{key}`')
        while True:
            edit_hwnd_list = [
                i[0] 
                for i in GetAllWindowExs(self.control.NativeWindowHandle) 
                if i[1] == 'EditWnd'
            ]
            if edit_hwnd_list:
                edit_hwnd = edit_hwnd_list[0]
                break
            btn.Click()
        edit_win32 = uia.Win32(edit_hwnd)
        edit_win32.shortcut_select_all()
        edit_win32.send_keys_shortcut('{DELETE}')
        edit_win32.input(value)
        edit_win32.send_keys_shortcut('{ENTER}')
        return WxResponse.success()

    def get_group_members(self, control=False):
        """获取群成员"""
        more = self.control.ButtonControl(Name=self._lang('查看更多'), searchDepth=8)
        if more.Exists(0.5):
            more.Click()
        members = [i for i in self.control.ListControl(Name=self._lang('聊天成员')).GetChildren()]
        while members[-1].Name in [self._lang('添加'), self._lang('移出')]:
            members = members[:-1]
        if control:
            return members
        member_names = [i.Name for i in members]
        self.close()
        return member_names

class GroupMemberElement:
    def __init__(self, control, parent) -> None:
        self.control = control
        self.parent = parent
        self.root = self.parent.root
        self.nickname = self.control.Name

    def __repr__(self) -> str:
        return f"<wxauto Group Member Element at {hex(id(self))}>"
    
        
class AtMenu(BaseUISubWnd):
    _ui_cls_name = 'ChatContactMenu'

    def __init__(self, parent):
        self.root = parent.root
        self.control = parent.parent.control.PaneControl(ClassName='ChatContactMenu')
        # self.control.Exists(1)

    def clear(self, friend):
        if self.exists():
            self.control.SendKeys('{ESC}')
        for _ in range(len(friend)+1):
            self.root.chatbox.editbox.SendKeys('{BACK}')

    def select(self, friend):
        friend_ = friend.replace(' ', '')
        if self.exists():
            ateles = self.control.ListControl().GetChildren()
            if len(ateles) == 1:
                ateles[0].Click()
            else:
                atele = self.control.ListItemControl(Name=friend)
                if atele.Exists(0):
                    roll_into_view(self.control, atele)
                    atele.Click()
                else:
                    self.clear(friend_)
        else:
            self.clear(friend_)

    def click_at_all(self):
        """
        在At菜单弹出时，查找Name为“所有人”的控件并返回该控件对象。
        返回值：控件对象 或 None
        """
        # # 用法
        all_windows = self.control.ListControl().GetChildren()
        def find_and_click_all(control):
            try:
                if getattr(control, 'Name', '') == '所有人':
                    control.Click()
                    print("已点击所有人")
                    return True
                for child in control.GetChildren():
                    if find_and_click_all(child):
                        return True
            except Exception:
                pass
            return False

        for win in all_windows:
            if find_and_click_all(win):
                return True  # 找到并点击后立即返回
        return False