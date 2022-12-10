def main():
    screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
    image_test = pygame.Surface((64, 64))
    image_rect = pygame.draw.rect(image_test, "blue", image_test.get_rect())
    image_rect.top = screen.get_rect().top
    
    quit_image = pygame.Surface((64, 64))
    quit_rect = pygame.draw.rect(quit_image, "red", quit_image.get_rect())
    quit_rect.bottom = screen.get_rect().bottom
    
    
    running = True
    while running:
        for event in pygame.event.get(eventtype=(pygame.FINGERUP, pygame.QUIT)):
            if event.type == pygame.QUIT or (event.type == pygame.FINGERUP and quit_rect.collidepoint((event.x, event.y))):
                running = False
                

        screen.fill("black")
        screen.blit(image_test, image_rect)
        screen.blit(quit_image, quit_rect)
        print('displayed')
        pygame.display.flip()

if __name__ == '__main__':
    import pygame
    main()

