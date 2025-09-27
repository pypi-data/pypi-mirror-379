class Events:
    # AUTHENTICATION
    request_auth = "request.auth"
    response_auth = "response.auth"

    # ATTENTION
    request_attend_user = "request.attend.user"
    request_attend_location = "request.attend.location"

    # SPEAK
    request_speak_text = "request.speak.text"
    request_speak_audio = "request.speak.audio"
    request_speak_audio_start = "request.speak.audio.start"
    request_speak_audio_data = "request.speak.audio.data"
    request_speak_audio_end = "request.speak.audio.end"
    request_speak_stop = "request.speak.stop"
    response_speak_start = "response.speak.start"
    response_speak_end = "response.speak.end"
    response_speak_audio_buffer = "response.speak.audio.buffer"

    # LISTEN
    request_listen_config = "request.listen.config"
    request_listen_start = "request.listen.start"
    request_listen_stop = "request.listen.stop"
    response_listen_end = "response.listen.end"
    response_listen_start = "response.listen.start"

    # HEAR
    response_hear_start = "response.hear.start"
    response_hear_end = "response.hear.end"
    response_hear_partial = "response.hear.partial"

    # GESTURES
    request_gesture_start = "request.gesture.start"
    response_gesture_end = "response.gesture.end"
    response_gesture_start = "response.gesture.start"

    # VOICE
    request_voice_status = "request.voice.status"
    request_voice_config = "request.voice.config"
    response_voice_status = "response.voice.status"

    # FACE
    request_face_params = "request.face.params"
    request_face_status = "request.face.status"
    request_face_config = "request.face.config"
    request_face_reset = "request.face.reset"
    request_face_headpose = "request.face.headpose"
    response_face_status = "response.face.status"

    # LED
    request_led_set = "request.led.set"

    # USERS
    request_users_start = "request.users.start"
    request_users_stop = "request.users.stop"
    request_users_once = "request.users.once"
    response_users_data = "response.users.data"

    # CAMERA
    request_camera_start = "request.camera.start"
    request_camera_stop = "request.camera.stop"
    request_camera_once = "request.camera.once"
    response_camera_data = "response.camera.data"

    # AUDIO
    request_audio_start = "request.audio.start"
    request_audio_stop = "request.audio.stop"
    response_audio_data = "response.audio.data"
