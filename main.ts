sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    bomb.destroy()
    info.changeScoreBy(1)
})
//  When "Saper" take a "Bomb" it is destroy
info.onLifeZero(function on_life_zero() {
    game.over(false)
})
//  Game is end with lose when life is 0
info.onScore(65, function on_on_score() {
    game.over(true)
})
//  When score is 65 game is end with Win
scene.onHitWall(SpriteKind.Projectile, function on_hit_wall(sprite2: Sprite, location: tiles.Location) {
    bomb.destroy(effects.fire, 500)
    info.changeLifeBy(-1)
})
// When "Bomb" hit the wall, it is destroy with fire effect and life change to -1
let bomb : Sprite = null
let sapper = sprites.create(img`
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
    `, SpriteKind.Player)
tiles.setCurrentTilemap(tilemap`
    level1
`)
controller.moveSprite(sapper, 150, 0)
sapper.setPosition(77, 200)
info.setLife(4)
scene.centerCameraAt(75, 550)
// This part of code create the "Sapper" and help him to move with speed 150 and take his position on (77,200)
game.onUpdateInterval(500, function on_update_interval() {
    
    bomb = sprites.create(img`
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
        `, SpriteKind.Projectile)
    bomb.setVelocity(0, 50)
    bomb.setPosition(randint(10, 145), 10)
})
