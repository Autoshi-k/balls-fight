import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Ball:
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.initial_radius = radius
        self.radius = radius
        self.color = color
        self.movement_speed = 1
        self.gravity = 1
        self.increase_radius = False

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        self._move()
        self._change_radius()

    def _change_radius(self):
        if self.increase_radius:
            self.radius += 1
        elif self.radius != self.initial_radius:
            self.radius -= 1

    def _move(self):
        if self._has_wall_padding(self.position_x, SCREEN_WIDTH - 20):
            delta_position_x = self.movement_speed
            diff_wall_and_position = SCREEN_WIDTH - self.position_x + (self.radius / 2)
            self.position_x += min(delta_position_x, diff_wall_and_position)

        if self._has_wall_padding(self.position_y, SCREEN_HEIGHT) or self.gravity < 0:
            gravity_sign = 1 if self.gravity >= 0 else -1
            delta_position_y = self.gravity + ((50 / self.radius) * gravity_sign)
            diff_wall_and_position = SCREEN_HEIGHT - self.position_y + (self.radius / 2)
            self.position_y += min(delta_position_y, diff_wall_and_position)

    def _has_wall_padding(self, position, limit):
        return position + (self.radius / 2) < limit

    def switch_gravity_source(self):
        self.gravity = -self.gravity

    def enlarge_ball(self, value):
        self.increase_radius = value


class MyGame(arcade.Window):
    def __init__(self, screen_width, screen_height, title):
        # init
        super().__init__(screen_width, screen_height, title)

        # settings
        arcade.set_background_color(arcade.color.BLACK)

        # objects
        self.ball = Ball(screen_width / 2, screen_height / 2, 10, arcade.color.BABY_BLUE)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def on_update(self, delta_time: float):
        self.ball.update()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            self.ball.switch_gravity_source()
        if symbol == arcade.key.ENTER:
            self.ball.enlarge_ball(True)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.ball.switch_gravity_source()
        if symbol == arcade.key.ENTER:
            self.ball.enlarge_ball(False)


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'my game')
    arcade.run()


main()
