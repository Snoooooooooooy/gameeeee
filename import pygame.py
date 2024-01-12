import pygame
import sys
import os

# 初始化 Pygame
pygame.init()

# 設定遊戲視窗大小
window_size = (800, 600)

# 建立視窗
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("過關自動關機遊戲")

# 設定顏色
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# 設定玩家的初始位置和速度
player_size = 50
player_x = window_size[0] // 2 - player_size // 2
player_y = window_size[1] - player_size - 10
player_speed = 5

# 設定遊戲迴圈
clock = pygame.time.Clock()
score = 0
game_over = False

def shutdown_computer():
    try:
        print("遊戲通關！即將關機。")
        os.system("shutdown /s /t 1")  # Windows 的關機指令
    except Exception as e:
        print(f"發生錯誤：{e}")

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_size[0] - player_size:
        player_x += player_speed

    window.fill(white)
    pygame.draw.rect(window, green, [player_x, player_y, player_size, player_size])

    # 通關條件（此處假設分數達到某個值即視為通關）
    if score >= 10:
        game_over = True
        shutdown_computer()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
