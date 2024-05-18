import pygame

def generate_animation(image_path, rows, cols, actions):
    sprite_sheet = pygame.image.load(image_path).convert_alpha()
    sprite_width = sprite_sheet.get_width() // cols
    sprite_height = sprite_sheet.get_height() // rows

    sprites = []

    for row in range(rows):
        for col in range(cols):
            x = col * sprite_width
            y = row * sprite_height

            sprite = sprite_sheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
            sprites.append(sprite)


    for i in range(len(sprites)):
        sprites[i] = pygame.transform.flip(sprites[i], True, False)

    animations = {}
    current_index = 0

    for action, num_sprites in actions.items():
        animation = []
        
        for _ in range(num_sprites):
            animation.append(sprites[current_index])
            current_index += 1

        animations[action] = animation
        current_index=0

    return animations