import pygame
import random

yellowR = (245, 235, 250)
class Rock(pygame.sprite.Sprite):
    def __init__(self, playerx, playery,shoot_x, shoot_y, x, y, all_sprites):
        super().__init__()
        self.radius = random.randint(20,50)  # 圆形的半径
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        # self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.draw.circle(self.image, yellowR , (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.speed = 0
        self.health = self.radius*2

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.background_offset_x = playerx
        self.background_offset_y = playery

        # self.background_offset_x = shoot_x
        # self.background_offset_y = shoot_y
        self.site_x = shoot_x
        self.site_y = shoot_y

        self.distance_travelled = 0


    def update(self):
        diff_x = self.background_offset_x - self.site_x
        diff_y = self.background_offset_y - self.site_y

        # self.site_x -= self.direction_x * self.speed# x 軸 OK
        # self.site_y -= self.direction_y * self.speed

        self.rect.x = (self.rect.x ) + diff_x
        self.rect.y = (self.rect.y ) + diff_y

        self.site_x = self.background_offset_x
        self.site_y = self.background_offset_y

        # self.rect.x += self.direction_x * self.speed
        # self.rect.y += self.direction_y * self.speed

    def check_collision(self, bullets):
        collisions = pygame.sprite.spritecollide(self, bullets, True)

        for bullet in collisions:
            self.health -= 10  # Decrease the rock's health when hit by a bullet
            self.radius -= 2
            # self.rect = self.image.get_rect()
            self.image = pygame.transform.scale(self.image, (2 * self.radius, 2 * self.radius))

            # self.update()
            if self.health <= 0:
                self.kill()  # Remove the rock when its health reaches zero



        # keys = pygame.key.get_pressed()
        #
        # if -3000 <= self.background_offset_x <= 3000:
        #     if keys[pygame.K_a]:
        #         self.directionX += 1
        #         if self.directionX >= 5:
        #             self.directionX = 5
        #         self.background_offset_x += 8
        #         if self.background_offset_x >= 3000:
        #             self.background_offset_x = 3000
        #         elif self.background_offset_x <= -3000:
        #             self.background_offset_x = -3000
        #     elif keys[pygame.K_d]:
        #         self.directionX -= 1
        #         if self.directionX <= -5:
        #             self.directionX = -5
        #         self.background_offset_x -= 8
        #         if self.background_offset_x >= 3000:
        #             self.background_offset_x = 3000
        #         elif self.background_offset_x <= -3000:
        #             self.background_offset_x = -3000
        #
        #     if self.directionX < -2:
        #         self.background_offset_x += -2
        #         if self.background_offset_x >= 3000:
        #             self.background_offset_x = 3000
        #         elif self.background_offset_x <= -3000:
        #             self.background_offset_x = -3000
        #     elif self.directionX > 2 :
        #         self.background_offset_x += 2
        #         if self.background_offset_x >= 3000:
        #             self.background_offset_x = 3000
        #         elif self.background_offset_x <= -3000:
        #             self.background_offset_x = -3000
        # if -3000 <= self.background_offset_y <= 3000:
        #     if keys[pygame.K_w]:
        #         self.directionY += 1
        #         if self.directionY >= 5:
        #             self.directionY = 5
        #         self.background_offset_y += 8
        #         if self.background_offset_y >= 3000:
        #             self.background_offset_y = 3000
        #         elif self.background_offset_y <= -3000:
        #             self.background_offset_y = -3000
        #     elif keys[pygame.K_s]:
        #         self.directionY -= 1
        #         if self.directionY <= -5:
        #             self.directionY = -5
        #         self.background_offset_y -= 8
        #         if self.background_offset_y >= 3000:
        #             self.background_offset_y = 3000
        #         elif self.background_offset_y <= -3000:
        #             self.background_offset_y = -3000
        #
        #     if self.directionY < -2:
        #         self.background_offset_y += -2
        #         if self.background_offset_y >= 3000:
        #             self.background_offset_y = 3000
        #         elif self.background_offset_y <= -3000:
        #             self.background_offset_y = -3000
        #     elif self.directionY > 2:
        #         self.background_offset_y += 2
        #         if self.background_offset_y >= 3000:
        #             self.background_offset_y = 3000
        #         elif self.background_offset_y <= -3000:
        #             self.background_offset_y = -3000