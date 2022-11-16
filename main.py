def on_on_overlap(sprite, otherSprite):
    bomb.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)
# When "Saper" take a "Bomb" it is destroy

def on_life_zero():
    game.over(False)
info.on_life_zero(on_life_zero)
# Game is end with lose when life is 0

def on_on_score():
    game.over(True)
info.on_score(65, on_on_score)
# When score is 65 game is end with Win

def on_hit_wall(sprite2, location):
    bomb.destroy(effects.fire, 500)
    info.change_life_by(-1)
scene.on_hit_wall(SpriteKind.projectile, on_hit_wall)
#When "Bomb" hit the wall, it is destroy with fire effect and life change to -1

bomb: Sprite = None
sapper = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f c c f f f . . . . 
            . . . f f f 8 8 8 8 f f f . . . 
            . . f f f c c c c c c f f f . . 
            . . f f 8 8 8 8 8 8 8 8 8 f . . 
            . . f c c f f f f f f c c f . . 
            . . f f f f c c c c f f f f . . 
            . f f c f c c c c c c f c f f . 
            . f c c c 1 f d d f 1 c c c f . 
            . . f f f f f f c c c c c f . . 
            . f c c 8 8 c c f 8 8 8 f . . . 
            . f 8 8 8 8 8 8 f c c f c c . . 
            . f c 8 c c 8 c f c c f c c . . 
            . . f c c c c c f 8 8 f 8 8 . . 
            . . . f f f f f c f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
controller.move_sprite(sapper, 150, 0)
sapper.set_position(77, 200)
info.set_life(4)
scene.center_camera_at(75, 550)
#This part of code create the "Sapper" and help him to move with speed 150 and take his position on (77,200)

def on_update_interval():
    global bomb
    bomb = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . 1 1 . . . . . . 
                    . . . . . . . 1 . . 1 . . . . . 
                    . . . . . . c 1 c . . . . . . . 
                    . . . . . c f 1 f f . . . . . . 
                    . . . . c f f f f f f . . . . . 
                    . . . . c f f f f f f . . . . . 
                    . . . . f f f f f f f . . . . . 
                    . . . . . f f f f f . . . . . . 
                    . . . . . . f f f . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.projectile)
    bomb.set_velocity(0, 50)
    bomb.set_position(randint(10, 145), 10)
game.on_update_interval(500, on_update_interval)
#This part of code create a "Bomb" and make it fall with interval (500ms) 