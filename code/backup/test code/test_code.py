import pygame
import sys


def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [200, 200]
    bg = [255, 255, 255]

    screen = pygame.display.set_mode(size)

    button = pygame.Rect(90, 90, 50, 50)
    button2 = pygame.Rect(9, 9, 50, 50)  # creates a rect object
    # The rect method is similar to a list but with a few added perks
    # for example if you want the position of the button you can simpy type
    # button.x or button.y or if you want size you can type button.width or
    # height. you can also get the top, left, right and bottom of an object
    # with button.right, left, top, and bottom

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                
                if button2.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button2 was pressed at {0}'.format(mouse_pos))

        screen.fill(bg)

        pygame.draw.rect(screen, [255, 0, 0], button)
        pygame.draw.rect(screen, [255, 0, 0], button2)  # draw button

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit


if __name__ == '__main__':
    main()