import asyncio
import websockets
import json
import uuid
import logging
from contextlib import contextmanager
from typing import Callable, Dict, List, Any, Awaitable, Optional
from .events import Events  

class AsyncFurhatClient:

    def __init__(self, host:str, auth_key: Optional[str] = None):
        self.logger = logging.getLogger("AsyncFurhatClient")
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter("[Furhat Realtime API] %(message)s")
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
        self.host = host
        self.ws_url = f"ws://{host}:9000/v1/events"
        self.auth_key = auth_key
        self.ws = None
        self.is_connected = False
        self.event_handlers: Dict[str, List[Callable]] = {}
        self._listen_task = None


    async def connect(self):
        """Connect to the Furhat Realtime API"""
        if self.is_connected:
            return
        
        self.ws = await websockets.connect(self.ws_url)
        self.is_connected = True
        # Start listening for events
        self._listen_task = asyncio.create_task(self._listen_for_events())
        
        # Authenticate 
        event = {
            "type": Events.request_auth,
        }
        if self.auth_key is not None:
            event["key"] = self.auth_key
        auth_result = await self.send_event_and_wait(event = event, return_type = Events.response_auth)
        if auth_result and auth_result.get("access") == True:
            self.logger.info(f"Connected on {self.host} with scope '{auth_result['scope']}'")
        else:
            raise RuntimeError("Authentication failed.")


    def set_logging_level(self, level: int):
        """Set the logging level for the client"""
        self.logger.setLevel(level)


    async def disconnect(self):
        """Disconnect from the Furhat Realtime API"""
        if not self.is_connected:
            return
        
        if self._listen_task:
            self._listen_task.cancel()
            try:
                await self._listen_task
            except asyncio.CancelledError:
                pass
        await self.ws.close()
        self.is_connected = False


    async def wait_for_event(self, event_type: str | list[str], timeout: float = 5.0, request_id: str = None):
        """Wait for a specific event type (or list of types) and return its data"""
        if isinstance(event_type, str):
            event_types = [event_type]
        elif isinstance(event_type, list):
            event_types = event_type

        future = asyncio.get_event_loop().create_future()

        async def one_time_handler(event_data: Dict[str, Any]):
            if not future.done() and (request_id is None or event_data.get("request_id") == request_id):
                future.set_result(event_data)

        for et in event_types:
            self.add_handler(et, one_time_handler)

        try:
            return await asyncio.wait_for(future, timeout)
        finally:
            # Remove the one-time handler after it's used
            for et in event_types:
                self.event_handlers[et].remove(one_time_handler)


    async def _listen_for_events(self):
        """Listen for events from the websocket and dispatch to handlers"""
        if not self.is_connected or not self.ws:
            raise RuntimeError("Not connected to websocket")
        
        try:
            async for message in self.ws:
                if isinstance(message, str):
                    try:
                        self.logger.debug(message)
                        event = json.loads(message)
                        event_type = event.get("type", "")
                        await self._dispatch_event(event_type, event)
                    except Exception as e:
                        self.logger.error(f"Failed to parse message as JSON: {e}")
                        continue
        except websockets.exceptions.ConnectionClosed:
            self.is_connected = False

    async def _dispatch_event(self, event_type: str, event_data: Dict):
        """Dispatch event to all registered handlers"""
        if event_type in self.event_handlers:
            for handler in self.event_handlers[event_type]:
                try:
                    await handler(event_data)
                except Exception as e:
                    self.logger.error(f"Error in event handler for {event_type}: {e}")


    def add_handler(self, event_type: str | list[str], handler: Callable[[Dict[str, Any]], Awaitable[Any]]):
        """Register an event handler"""
        if isinstance(event_type, str):
            event_types = [event_type]
        elif isinstance(event_type, list):
            event_types = event_type
        for et in event_types:
            if et not in self.event_handlers:
                self.event_handlers[et] = []
            self.event_handlers[et].append(handler)
        return self


    def remove_handler(self, event_type: str | list[str], handler):
        """Remove an event handler"""
        if isinstance(event_type, str):
            event_types = [event_type]
        elif isinstance(event_type, list):
            event_types = event_type
        for et in event_types:
            if et in self.event_handlers:
                self.event_handlers[et].remove(handler)
        return self


    @contextmanager
    def scoped_handlers(self):
        added = []
        def add_handler(event_type: str | list[str], handler):
            self.add_handler(event_type, handler)
            added.append((event_type, handler))
        try:
            yield add_handler
        finally:
            for event_type, handler in added:
                self.remove_handler(event_type, handler)


    async def send_event_and_wait(self, event: Dict, return_type: str | list[str], timeout: float = 5.0):
        request_id = str(uuid.uuid4())
        event["request_id"] = request_id
        future = asyncio.get_event_loop().create_future()

        async def one_time_handler(event_data: Dict[str, Any]):
            if not future.done() and (request_id == None or event_data.get("request_id") == request_id):
                future.set_result(event_data)

        with self.scoped_handlers() as add_handler:
            add_handler(return_type, one_time_handler)
            await self.send_event(event)
            return await asyncio.wait_for(future, timeout)


    async def send_event(self, event: Dict):
        """Send a raw event to the websocket"""
        if not self.is_connected or not self.ws:
            raise RuntimeError("Not connected to websocket")
        
        events = json.dumps(event)
        self.logger.debug(events)
        await self.ws.send(events)

    async def send_bytes(self, data: bytes):
        """Send a raw event to the websocket"""
        if not self.is_connected or not self.ws:
            raise RuntimeError("Not connected to websocket")
        await self.ws.send(data)


    # SPEAK

    async def request_speak_text(self, text: str, abort: bool = False, wait: bool = False):
        """Make the robot say something using text-to-speech"""
        event = {
            "type": Events.request_speak_text,
            "text": text,
            "abort": abort
        }
        if wait:
            return await self.send_event_and_wait(event, Events.response_speak_end, timeout=30.0)
        else:
            await self.send_event(event)

    async def request_speak_audio(self, url: str, text: str = "AUDIO", lipsync: bool = True, abort: bool = False, wait: bool = False):
        """Make the robot play/say some audio from a URL (WAV format only)"""
        event = {
            "type": Events.request_speak_audio,
            "url": url,
            "text": text,
            "lipsync": lipsync,
            "abort": abort
        }
        if wait:
            return await self.send_event_and_wait(event, Events.response_speak_end, timeout=30.0)
        else:
            await self.send_event(event)

    async def request_speak_audio_start(self, sample_rate: int = 24000, lipsync: bool = False):
        """Start sending audio data to the robot"""
        await self.send_event({
            "type": Events.request_speak_audio_start,
            "sample_rate": sample_rate,
            "lipsync": lipsync
        })

    async def request_speak_audio_data(self, audio: str):
        """Send audio data to the robot"""
        await self.send_event({
            "type": Events.request_speak_audio_data,
            "audio": audio
        })

    async def request_speak_audio_end(self):
        """End sending audio data to the robot"""
        await self.send_event({
            "type": Events.request_speak_audio_end
        })

    async def request_speak_stop(self):
        """Make the robot stop speaking and/or abort any planned speech"""
        await self.send_event({"type": Events.request_speak_stop})

    # LISTEN

    async def request_listen_config(self, languages: list = ["en-US"], phrases: list = None):
        """Configure speech recognition languages"""
        event = {
            "type": Events.request_listen_config,
            "languages": languages
        }
        if phrases:
            event["phrases"] = phrases
        await self.send_event(event)

    async def request_listen_start(self, partial: bool = False, concat: bool = True, stop_no_speech: bool = True, stop_robot_start: bool = True, stop_user_end: bool = True, resume_robot_end: bool = False, no_speech_timeout: float = 8.0, end_speech_timeout: float = 1.0):
        """Make the robot listen for speech"""
        await self.send_event({
            "type": Events.request_listen_start,
            "partial": partial,
            "concat": concat,
            "stop_no_speech": stop_no_speech,
            "stop_robot_start": stop_robot_start,
            "stop_user_end": stop_user_end,
            "resume_robot_end": resume_robot_end,
            "no_speech_timeout": no_speech_timeout,
            "end_speech_timeout": end_speech_timeout
        })

    async def request_listen_stop(self):
        """Force the robot to stop listening"""
        await self.send_event({"type": Events.request_listen_stop})

    # VOICE

    async def request_voice_config(self, 
                                   voice_id: Optional[str] = None,
                                   name: Optional[str] = None,
                                   gender: Optional[str] = None,
                                   language: Optional[str] = None,
                                   provider: Optional[str] = None,
                                   input_language: bool = True):
        """Set the current voice"""
        event = {"type": Events.request_voice_config, "input_language": input_language}
        if voice_id is not None:
            event["voice_id"] = voice_id
        if name is not None:
            event["name"] = name
        if gender is not None:
            event["gender"] = gender
        if language is not None:
            event["language"] = language
        if provider is not None:
            event["provider"] = provider
        return await self.send_event_and_wait(
            event=event,
            return_type=Events.response_voice_status)

    async def request_voice_status(self, voice_id: bool = True, voice_list: bool = True):
        """Get current and available voices"""
        return await self.send_event_and_wait(
            event={"type": Events.request_voice_status, "voice_id": voice_id, "voice_list": voice_list},
            return_type=Events.response_voice_status)

    # ATTENTION

    async def request_attend_user(self, user_id: str = "closest"):
        """Make the robot attend to a user"""
        await self.send_event({
            "type": Events.request_attend_user,
            "user_id": user_id
        })

    async def request_attend_location(self, x: float, y: float, z: float):
        """Make the robot attend to a specific location (meters, relative to robot)"""
        await self.send_event({
            "type": Events.request_attend_location,
            "x": x,
            "y": y,
            "z": z
        })

    # GESTURES

    async def request_gesture_start(self, name: str, intensity: float = 1.0, duration: float = 1.0, wait: bool = False):
        """Make the robot perform a gesture"""
        event = {
            "type": Events.request_gesture_start,
            "name": name,
            "intensity": intensity,
            "duration": duration,
            "monitor": wait
        }
        if wait:
            return await self.send_event_and_wait(event, Events.response_gesture_end, timeout=10.0)
        else:   
            await self.send_event(event)

    # FACE

    async def request_face_params(self, params: dict):
        """Set facial animation parameters directly"""
        await self.send_event({
            "type": Events.request_face_params,
            "params": params
        })

    async def request_face_headpose(self, yaw: float, pitch: float, roll: float, relative: bool):
        """Override automatic head pose and directly control the head pose of the robot"""
        await self.send_event({
            "type": Events.request_face_headpose,
            "yaw": yaw,
            "pitch": pitch,
            "roll": roll,
            "relative": relative
        })

    async def request_face_config(self, face_id: Optional[str] = None, visibility: Optional[bool] = None, microexpressions: Optional[bool] = None):
        """Set the current mask and character (face_id), and/or face visibility"""
        event = {"type": Events.request_face_config}
        if face_id is not None:
            event["face_id"] = face_id
        if visibility is not None:
            event["visibility"] = visibility
        if microexpressions is not None:
            event["microexpressions"] = microexpressions
        await self.send_event(event)

    async def request_face_status(self, face_id: bool = True, face_list: bool = True):
        """Get current and available masks and characters (face_id)"""
        return await self.send_event_and_wait(
            event={"type": Events.request_face_status, "face_id": face_id, "face_list": face_list},
            return_type=Events.response_face_status)

    async def request_face_reset(self):
        """Resets all facial parameters to default"""
        await self.send_event({"type": Events.request_face_reset})

    # LED

    async def request_led_set(self, color: str):
        """Set the color of the LED"""
        await self.send_event({
            "type": Events.request_led_set,
            "color": color
        })

    # USERS

    async def request_users_once(self):
        """Get the current user status"""
        return await self.send_event_and_wait(
            event={"type": Events.request_users_once},
            return_type=Events.response_users_data)
    
    async def request_users_start(self):
        """Start monitoring users"""
        await self.send_event({"type": Events.request_users_start})

    async def request_users_stop(self):
        """Stop monitoring users"""
        await self.send_event({"type": Events.request_users_stop})

    # AUDIO

    async def request_audio_start(self, sample_rate: int = 16000, microphone: bool = True, speaker: bool = False):
        """Start sending audio data to the robot"""
        await self.send_event({
            "type": Events.request_audio_start,
            "sample_rate": sample_rate,
            "microphone": microphone,
            "speaker": speaker
        })

    async def request_audio_stop(self):
        """Stop sending audio data to the robot"""
        await self.send_event({"type": Events.request_audio_stop})

    # CAMERA

    async def request_camera_start(self):
        """Start sending camera data to the robot"""
        await self.send_event({
            "type": Events.request_camera_start
        })

    async def request_camera_once(self):
        """Get a single frame of camera data"""
        return await self.send_event_and_wait(
            event={"type": Events.request_camera_once},
            return_type=Events.response_camera_data)

    async def request_camera_stop(self):
        """Stop sending camera data to the robot"""
        await self.send_event({
            "type": Events.request_camera_stop
        })