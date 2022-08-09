import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Simple Game")

# 배경 이미지 불러오기
background = pygame.image.load("/home/dlwprmaksaks/Code/GameDevelop/pygame_basic/background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트
            running = False

    # screen.fill((0,0, 255)) 색상표를 이용해 넣는 방식
    screen.blit(background, (0,0)) # 배경 그리기

    pygame.display.update() # 게임화면을 다시 그리기! (while을 계속 돌면서)

# pygame 종료
pygame.quit()
