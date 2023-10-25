import pygame

yellow = (255, 255, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, shoot_x, shoot_y, x, y, direction_x, direction_y, bullet_range, weaponkey):
        super().__init__()
        self.type = weaponkey
        if self.type == 0:
            self.image = pygame.Surface((10, 10))  # 可以替換為子彈的圖像
            self.image.fill(yellow)  # 藍色(0, 0, 255)
            self.speed = 15
        elif self.type == 2:
            self.image = pygame.Surface((10, 10))  # 可以替換為子彈的圖像
            self.image.fill(green)
            self.speed = 30
        elif self.type == 3:
            self.image = pygame.Surface((10, 10))  # 可以替換為子彈的圖像
            self.image.fill(blue)
            self.speed = 25
        elif self.type == 4:
            self.image = pygame.Surface((10, 10))  # 可以替換為子彈的圖像
            self.image.fill(red)
            self.speed = 5
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.type = weaponkey

        self.background_offset_x = shoot_x
        self.background_offset_y = shoot_y
        self.site_x = shoot_x
        self.site_y = shoot_y

        self.direction_x = direction_x
        self.direction_y = direction_y
        self.bullet_range = bullet_range

        self.distance_travelled = 0

    def update(self):

        diff_x = self.background_offset_x - self.site_x
        diff_y = self.background_offset_y - self.site_y

        # self.site_x -= self.direction_x * self.speed# x 軸 OK
        # self.site_y -= self.direction_y * self.speed

        self.rect.x = (self.rect.x + self.direction_x * self.speed) + diff_x
        self.rect.y = (self.rect.y + self.direction_y * self.speed) + diff_y

        self.site_x = self.background_offset_x
        self.site_y = self.background_offset_y

        # self.rect.x += self.direction_x * self.speed
        # self.rect.y += self.direction_y * self.speed

        # 計算子彈已經飛行的距離
        self.distance_travelled += self.speed

        # 如果子彈飛行距離超過指定的範圍，則刪除子彈
        if self.distance_travelled >= self.bullet_range:
            self.kill()