import pygame
import math
from bullet import Bullet

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700


class Player(pygame.sprite.Sprite):
    def __init__(self, background_x, background_y, all_sprites):
        super().__init__()
        self.radius = 22  # 圆形的半径
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.draw.circle(self.image, (128, 128, 128), (self.radius, self.radius), self.radius)
        self.speed = 1
        self.health = 100
        self.background_offset_x = background_x
        self.background_offset_y = background_y
        self.all_sprites = all_sprites

        self.bullets_left_click = []  # 存儲 (bullet_x, bullet_y, dx, dy)
        self.bullets_click_site = []

        self.directionX = 0
        self.directionY = 0

    def update(self):

        keys = pygame.key.get_pressed()

        if -3000 <= self.background_offset_x <= 3000:
            if keys[pygame.K_a]:
                self.directionX += 1
                if self.directionX >= 5:
                    self.directionX = 5
                self.background_offset_x += 8
                if self.background_offset_x >= 3000:
                    self.background_offset_x = 3000
                elif self.background_offset_x <= -3000:
                    self.background_offset_x = -3000
            elif keys[pygame.K_d]:
                self.directionX -= 1
                if self.directionX <= -5:
                    self.directionX = -5
                self.background_offset_x -= 8
                if self.background_offset_x >= 3000:
                    self.background_offset_x = 3000
                elif self.background_offset_x <= -3000:
                    self.background_offset_x = -3000

            if self.directionX < -2:
                self.background_offset_x += -2
                if self.background_offset_x >= 3000:
                    self.background_offset_x = 3000
                elif self.background_offset_x <= -3000:
                    self.background_offset_x = -3000
            elif self.directionX > 2 :
                self.background_offset_x += 2
                if self.background_offset_x >= 3000:
                    self.background_offset_x = 3000
                elif self.background_offset_x <= -3000:
                    self.background_offset_x = -3000
        if -3000 <= self.background_offset_y <= 3000:
            if keys[pygame.K_w]:
                self.directionY += 1
                if self.directionY >= 5:
                    self.directionY = 5
                self.background_offset_y += 8
                if self.background_offset_y >= 3000:
                    self.background_offset_y = 3000
                elif self.background_offset_y <= -3000:
                    self.background_offset_y = -3000
            elif keys[pygame.K_s]:
                self.directionY -= 1
                if self.directionY <= -5:
                    self.directionY = -5
                self.background_offset_y -= 8
                if self.background_offset_y >= 3000:
                    self.background_offset_y = 3000
                elif self.background_offset_y <= -3000:
                    self.background_offset_y = -3000

            if self.directionY < -2:
                self.background_offset_y += -2
                if self.background_offset_y >= 3000:
                    self.background_offset_y = 3000
                elif self.background_offset_y <= -3000:
                    self.background_offset_y = -3000
            elif self.directionY > 2:
                self.background_offset_y += 2
                if self.background_offset_y >= 3000:
                    self.background_offset_y = 3000
                elif self.background_offset_y <= -3000:
                    self.background_offset_y = -3000

    def shoot(self, bullets, dx1, dy1, bullet_range, weaponkey):

        if weaponkey == 0:
            bullet_x1, bullet_y1 = self.rect.center  # 子彈的初始位置是玩家精靈的中心
            shoot_x = self.background_offset_x
            shoot_y = self.background_offset_y
            bullet = Bullet(shoot_x, shoot_y, bullet_x1, bullet_y1, dx1, dy1, bullet_range, weaponkey)
            # bullet = Bullet(shoot_x, shoot_y, dx1,dy1, bullet_range)
            self.all_sprites.add(bullet)
            bullets.add(bullet)
        elif weaponkey == 2:
            bullet_x1, bullet_y1 = self.rect.center  # 子彈的初始位置是玩家精靈的中心
            shoot_x = self.background_offset_x
            shoot_y = self.background_offset_y
            bullet = Bullet(shoot_x, shoot_y, bullet_x1, bullet_y1, dx1, dy1, bullet_range, weaponkey)
            # bullet = Bullet(shoot_x, shoot_y, dx1,dy1, bullet_range)
            self.all_sprites.add(bullet)
            bullets.add(bullet)
        elif weaponkey == 3:
            bullet_x1, bullet_y1 = self.rect.center  # 子彈的初始位置是玩家精靈的中心
            shoot_x = self.background_offset_x
            shoot_y = self.background_offset_y
            bullet = Bullet(shoot_x, shoot_y, bullet_x1, bullet_y1, dx1, dy1, bullet_range, weaponkey)
            # bullet = Bullet(shoot_x, shoot_y, dx1,dy1, bullet_range)
            self.all_sprites.add(bullet)
            bullets.add(bullet)
        elif weaponkey == 4:
            bullet_x1, bullet_y1 = self.rect.center  # 子彈的初始位置是玩家精靈的中心
            shoot_x = self.background_offset_x
            shoot_y = self.background_offset_y
            bullet = Bullet(shoot_x, shoot_y, bullet_x1, bullet_y1, dx1, dy1, bullet_range, weaponkey)
            # bullet = Bullet(shoot_x, shoot_y, dx1,dy1, bullet_range)
            self.all_sprites.add(bullet)
            bullets.add(bullet)