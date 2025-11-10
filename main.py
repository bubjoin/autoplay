# pip install pyautogui keyboard opencv-python pillow numpy==1.26.4 pygetwindow pyperclip
# numpy==1.26.4 로 버젼 지정하는 것은 WinPython이 3.14 버젼이라도 내부적으로 Python 3.11을 쓰기 때문에
# 빌드 문제를 해결하려고

# --- 화면 제어 및 자동화 ---
import pyautogui          # 마우스, 키보드, 화면 캡처 : 화면 캡쳐, 마우스 이동, 클릭, 스크린샷 등
import keyboard           # 키보드 입력 감지 (ESC 등) : 특정 키 입력 감지(keyboard.is_pressed('esc'))
import cv2                # 이미지 인식 (OpenCV) : 유사도 매칭(pyautogui.locateOnScreen()에서 confidence계산)
import numpy as np        # 이미지 배열 처리 속도 향상 : 이미지 데이터를 행렬로 처리할 때 속도 향상
from PIL import Image     # Pillow (이미지 저장, 변환 등) : 이미지 저장(pyautogui.screenshot())

# --- 창, 클립보드 등 보조 기능 ---
import pygetwindow as gw  # 창 제어 (활성화, 이름 확인 등) : 창 이름 확인, 창 포커스 이동
import pyperclip          # 클립보드 복사/붙여넣기 (한글 안정화용) : 클립보드 제어(한글 붙여넣기 등 안정성 개선)

# --- 시간 제어 ---
import time # 대기 시간 제어
import random # 랜덤 지연 등 자연스러운 동작 연출


print("프로그램이 3초 후 시작됩니다. ESC를 누르면 언제든 종료됩니다.")
time.sleep(3)

# 화면 크기 확인
screen_width, screen_height = pyautogui.size()
print(f"화면 크기: {screen_width} x {screen_height}")

# --- ESC 즉시 종료용 함수 ---
running = True
def stop_program():
    global running
    running = False

keyboard.add_hotkey('esc', stop_program)   # 🔹 해결방법 2 적용

# 마우스 자동 이동 루프
while running:
    # 랜덤 이동 (예: 화면의 10~90% 범위 내)
    x = random.randint(int(screen_width * 0.1), int(screen_width * 0.9))
    y = random.randint(int(screen_height * 0.1), int(screen_height * 0.9))

    pyautogui.moveTo(x, y, duration=0.5)  # 부드럽게 이동
    time.sleep(1)  # 잠시 대기

print("프로그램 종료!")
