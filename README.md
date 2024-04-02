# Camera Yoosee control: https://github.com/wredan/yoosee_camera_control_api
# CameraIP: Tải app VLC media để test link stream.
Guide how to conncet : How to play Yoosee camera RTSP stream?
1. Go to your smartphone to enable "RTSP", and create a new password.
2. RTSP://admin:Test1234@192.168.1.38:554/onvif1       # Change passwword trong App điện thoại khi connect RTSP  , User vẫn giữ nguyên admin
                                                       # Open fing app scan IP of camera change: 192.168.1.38:554 to 192.168.1.22 (ví dụ 22 là địa chỉ connect camera)
4. You can find camera's IP address via Yoosee app
5. admin is the username, Test1234 is the created/modified password


https://www.youtube.com/watch?v=bHn_n3CLQOI&ab_channel=ArnaldoVianaJr

https://www.youtube.com/watch?v=ziNFn54Iy7I&ab_channel=CodePublic

Cài đặt:
  1. brew update
  2. brew upgrade
  3. brew install ffmpeg
  4. ffmpeg
https://phoenixnap.com/kb/ffmpeg-mac
https://stackoverflow.com/questions/43743592/getting-rtsp-stream-with-opencv-and-python
