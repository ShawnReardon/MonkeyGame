def on_a_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy += -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava0,
    on_overlap_tile)

def on_overlap_tile2(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.forest_tiles10,
    on_overlap_tile2)

def doSomething():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . c d f d d f d e e f f . . . . 
                        . c d f d d f d e e d d f . . . 
                        c d e e d d d d e e b d c . . . 
                        c d d d d c d d e e b d c . f f 
                        c c c c c d d d e e f c . f e f 
                        . f d d d d d e e f f . . f e f 
                        . . f f f f f e e e e f . f e f 
                        . . . . f e e e e e e e f f e f 
                        . . . f e f f e f e e e e f f . 
                        . . . f e f f e f e e e e f . . 
                        . . . f d b f d b f f e f . . . 
                        . . . f d d c d d b b d f . . . 
                        . . . . f f f f f f f f f . . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . c d f d d f d e e f . . . . . 
                        . c d f d d f d e e f f . . . . 
                        c d e e d d d d e e d d f . . . 
                        c d d d d c d d e e b d c . . . 
                        c c c c c d d e e e b d c . f f 
                        . f d d d d e e e f f c . f e f 
                        . f f f f f f e e e e f . f e f 
                        . f f f f e e e e e e e f f e f 
                        f d d f d d f e f e e e e f f . 
                        f d b f d b f e f e e e e f . . 
                        f f f f f f f f f f f f e f . . 
                        . . . . . . . . . f c d d f . . 
                        . . . . . . . . . . f f f f . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f f . . . . 
                        . c d d d d d d e e d d f . . . 
                        . c d f d d f d e e b d c . . . 
                        c d d f d d f d e e b d c . f f 
                        c d e e d d d d e e f c . f e f 
                        c d d d d c d e e e f . . f e f 
                        . f c c c d e e e f f . . f e f 
                        . . f f f f f e e e e f . f e f 
                        . . . . f e e e e e e e f f f . 
                        . . f f e f e e f e e e e f . . 
                        . f e f f e e f f f e e e f . . 
                        f d d b d d c f f f f f f b f . 
                        f d d c d d d f . . f c d d f . 
                        . f f f f f f f . . . f f f . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f f f . . . . 
                        . . f d d d e e e e d d f . . . 
                        . c d d d d d e e e b d c . . . 
                        . c d d d d d d e e b d c . . . 
                        c d d f d d f d e e f c . f f . 
                        c d d f d d f d e e f . . f e f 
                        c d e e d d d d e e f . . f e f 
                        . f d d d c d e e f f . . f e f 
                        . . f f f d e e e e e f . f e f 
                        . . . . f e e e e e e e f f f . 
                        . . . . f f e e e e e b f f . . 
                        . . . f e f f e e c d d f f . . 
                        . . f d d b d d c f f f . . . . 
                        . . f d d c d d d f f . . . . . 
                        . . . f f f f f f f . . . . . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . c d f d d f d e e f f . . . . 
                        . c d f d d f d e e d d f . . . 
                        c d e e d d d d e e b d c . . . 
                        c d d d d c d d e e b d c . . . 
                        c c c c c d d e e e f c . . . . 
                        . f d d d d e e e f f . . . . . 
                        . . f f f f f e e e e f . . . . 
                        . . . . f f e e e e e e f . f f 
                        . . . f e e f e e f e e f . e f 
                        . . f e e f e e f e e e f . e f 
                        . f b d f d b f b b f e f f e f 
                        . f d d f d d f d d b e f f f f 
                        . . f f f f f f f f f f f f f .
            """)],
        100,
        False)

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def doSomething2():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . f f e e d f d d f d c . 
                        . . . f d d e e d f d d f d c . 
                        . . . c d b e e d d d d e e d c 
                        f f . c d b e e d d c d d d d c 
                        f e f . c f e e d d d c c c c c 
                        f e f . . f f e e d d d d d f . 
                        f e f . f e e e e f f f f f . . 
                        f e f f e e e e e e e f . . . . 
                        . f f e e e e f e f f e f . . . 
                        . . f e e e e f e f f e f . . . 
                        . . . f e f f b d f b d f . . . 
                        . . . f d b b d d c d d f . . . 
                        . . . f f f f f f f f f . . . .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . . f e e d f d d f d c . 
                        . . . . f f e e d f d d f d c . 
                        . . . f d d e e d d d d e e d c 
                        . . . c d b e e d d c d d d d c 
                        f f . c d b e e e d d c c c c c 
                        f e f . c f f e e e d d d d f . 
                        f e f . f e e e e f f f f f f . 
                        f e f f e e e e e e e f f f f . 
                        . f f e e e e f e f d d f d d f 
                        . . f e e e e f e f b d f b d f 
                        . . f e f f f f f f f f f f f f 
                        . . f d d c f . . . . . . . . . 
                        . . f f f f . . . . . . . . . .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . f f e e e d d d d f . . 
                        . . . f d d e e d d d d d d c . 
                        . . . c d b e e d f d d f d c . 
                        f f . c d b e e d f d d f d d c 
                        f e f . c f e e d d d d e e d c 
                        f e f . . f e e e d c d d d d c 
                        f e f . . f f e e e d c c c f . 
                        f e f . f e e e e f f f f f . . 
                        . f f f e e e e e e e f . . . . 
                        . . f e e e e f e e f e f f . . 
                        . . f e e e f f f e e f f e f . 
                        . f b f f f f f f c d d b d d f 
                        . f d d c f . . f d d d c d d f 
                        . . f f f . . . f f f f f f f .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . f f f e e e e e f . . . 
                        . . . f d d e e e e d d d f . . 
                        . . . c d b e e e d d d d d c . 
                        . . . c d b e e d d d d d d c . 
                        . f f . c f e e d f d d f d d c 
                        f e f . . f e e d f d d f d d c 
                        f e f . . f e e d d d d e e d c 
                        f e f . . f f e e d c d d d f . 
                        f e f . f e e e e e d f f f . . 
                        . f f f e e e e e e e f . . . . 
                        . . f f b e e e e e f f . . . . 
                        . . f f d d c e e f f e f . . . 
                        . . . . f f f c d d b d d f . . 
                        . . . . . f f d d d c d d f . . 
                        . . . . . . f f f f f f f . . .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . f f e e d f d d f d c . 
                        . . . f d d e e d f d d f d c . 
                        . . . c d b e e d d d d e e d c 
                        . . . c d b e e d d c d d d d c 
                        . . . . c f e e e d d c c c c c 
                        . . . . . f f e e e d d d d f . 
                        . . . . f e e e e f f f f f . . 
                        f f . f e e e e e e f f . . . . 
                        f e . f e e f e e f e e f . . . 
                        f e . f e e e f e e f e e f . . 
                        f e f f e f b b f b d f d b f . 
                        f f f f e b d d f d d f d d f . 
                        . f f f f f f f f f f f f f . .
            """)],
        100,
        False)
mySprite: Sprite = None
banana: Sprite = None
def setupSprites(spriteToSpawn: Sprite, placeHolderTile: any):
    global banana
    for value in tiles.get_tiles_by_type(placeHolderTile):
        banana = sprites.create(assets.image("""
            ban
        """), SpriteKind.food)
        animation.run_image_animation(banana,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . 5 5 . . . 
                                                    . . . . . . . . . . 5 5 5 . . . 
                                                    . . . . . . . . . . 5 5 5 . . . 
                                                    . . . . . . . . . 5 5 5 5 . . . 
                                                    . . . . . . . . 5 5 5 5 5 . . . 
                                                    . . . . . . . . 5 5 5 5 5 . . . 
                                                    . . . . . . . 5 5 5 5 5 . . . . 
                                                    . . . . . . 5 5 5 5 5 5 . . . . 
                                                    . . . . 5 5 5 5 5 5 . . . . . . 
                                                    . . . 5 5 5 5 5 5 . . . . . . . 
                                                    . . 5 5 5 5 5 . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . 5 5 . . 
                                                    . . . . . . . . . . . 5 5 5 . . 
                                                    . . . . . . . . . 5 5 5 5 5 . . 
                                                    . . . . . . . . . 5 5 5 5 . . . 
                                                    . . . . . . . . 5 5 5 5 5 . . . 
                                                    . . . . . . . 5 5 5 5 5 . . . . 
                                                    . . . . . 5 5 5 5 5 5 5 . . . . 
                                                    . . . . 5 5 5 5 5 5 . . . . . . 
                                                    . . 5 5 5 5 5 . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . .
                """)],
            200,
            True)
        tiles.place_on_tile(banana, value)
        tiles.set_tile_at(value, assets.tile("""
            transparency16
        """))
scene.set_background_color(6)
tiles.set_tilemap(tilemap("""
    level1
"""))
mySprite = sprites.create(img("""
        . . . . f f f f f . . . . . . . 
            . . . f e e e e e f . . . . . . 
            . . f d d d d e e e f . . . . . 
            . c d f d d f d e e f f . . . . 
            . c d f d d f d e e d d f . . . 
            c d e e d d d d e e b d c . . . 
            c d d d d c d d e e b d c . f f 
            c c c c c d d d e e f c . f e f 
            . f d d d d d e e f f . . f e f 
            . . f f f f f e e e e f . f e f 
            . . . . f e e e e e e e f f e f 
            . . . f e f f e f e e e e f f . 
            . . . f e f f e f e e e e f . . 
            . . . f d b f d b f f e f . . . 
            . . . f d d c d d b b d f . . . 
            . . . . f f f f f f f f f . . .
    """),
    SpriteKind.player)
mySprite.ay = 100
scene.camera_follow_sprite(mySprite)
controller.move_sprite(mySprite, 100, 0)
for value2 in tiles.get_tiles_by_type(assets.tile("""
    myTile
""")):
    banana = sprites.create(assets.image("""
        ban
    """), SpriteKind.food)
    animation.run_image_animation(banana,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . 5 5 . . . 
                        . . . . . . . . . . 5 5 5 . . . 
                        . . . . . . . . . . 5 5 5 . . . 
                        . . . . . . . . . 5 5 5 5 . . . 
                        . . . . . . . . 5 5 5 5 5 . . . 
                        . . . . . . . . 5 5 5 5 5 . . . 
                        . . . . . . . 5 5 5 5 5 . . . . 
                        . . . . . . 5 5 5 5 5 5 . . . . 
                        . . . . 5 5 5 5 5 5 . . . . . . 
                        . . . 5 5 5 5 5 5 . . . . . . . 
                        . . 5 5 5 5 5 . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . 5 5 . . 
                        . . . . . . . . . . . 5 5 5 . . 
                        . . . . . . . . . 5 5 5 5 5 . . 
                        . . . . . . . . . 5 5 5 5 . . . 
                        . . . . . . . . 5 5 5 5 5 . . . 
                        . . . . . . . 5 5 5 5 5 . . . . 
                        . . . . . 5 5 5 5 5 5 5 . . . . 
                        . . . . 5 5 5 5 5 5 . . . . . . 
                        . . 5 5 5 5 5 . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        200,
        True)
    tiles.place_on_tile(banana, value2)
    tiles.set_tile_at(value2, assets.tile("""
        transparency16
    """))

def on_forever():
    mySprite.ay = 400
    if controller.left.is_pressed():
        doSomething()
        pause(350)
    if controller.right.is_pressed():
        doSomething2()
        pause(350)
forever(on_forever)
