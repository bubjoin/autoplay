import keyboard  # pip install keyboard
import pyautogui # pip install pyautogui
import random
import time

print("프로그램이 3초 후 시작됩니다. ESC를 누르면 언제든 종료됩니다.")
time.sleep(3)

# 화면 크기 확인
screen_width, screen_height = pyautogui.size()
print(f"화면 크기: {screen_width} x {screen_height}")

# 마우스 자동 이동 루프
while True:
    if keyboard.is_pressed('esc'):
        print("프로그램 종료!")
        break

    # 랜덤 이동 (예: 화면의 10~90% 범위 내)
    x = random.randint(int(screen_width * 0.1), int(screen_width * 0.9))
    y = random.randint(int(screen_height * 0.1), int(screen_height * 0.9))

    pyautogui.moveTo(x, y, duration=0.5)  # 부드럽게 이동
    time.sleep(1)  # 잠시 대기
