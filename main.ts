controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (prideBoy.isHittingTile(CollisionDirection.Bottom)) {
        prideBoy.vy += -150
        console.log(prideBoy.vy)
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava0, function (sprite, location) {
    reset()
})
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.forestTiles10, function (sprite, location) {
    for (let value of sprites.allOfKind(SpriteKind.Food)) {
        value.destroy()
    }
    LoadLevel2()
})
function doSomething () {
    animation.runImageAnimation(
    prideBoy,
    [img`
        ................
        ..........99999.
        ...eeeeeee33333.
        ..eeeeeeee11111.
        ..eddddeee33333.
        ...dd9ddee99999.
        ...ddddddd22222.
        ..dddddddd44444.
        ..eeeeeedd55555.
        ..eeeeeed.77777.
        ....eeedd.88888.
        ......ddd.aaaaa.
        ......ddd.ff....
        ......ddd.ff....
        ..dd6ddddd6dd...
        ..dd6666666dd...
        ..dd6666666dd...
        ..dd6666666dd...
        ..dd6666666dd...
        ..dd6666666dd...
        ..dd6666666dd...
        ..dd6666666dd...
        .ddd1115111ddd..
        .d.d3333333d.d..
        ....3333333.....
        ....333.333.....
        ....333.333.....
        ....333.333.....
        ....333.333.....
        ....333.333.....
        .111333.333111..
        .111111.111111..
        `,img`
        ................
        ..........99999.
        ...eeeeeee33333.
        ..eeeeeeee11111.
        ..eddddeee33333.
        ...dd9ddee99999.
        ...ddddddd22222.
        ..dddddddd44444.
        ..eeeeeedd55555.
        ..eeeeeed.77777.
        ....eeedd.88888.
        ......ddd.aaaaa.
        ......ddd.ff....
        ......ddd.ff....
        ..dd6ddddd6dd...
        ..dd6666666dd...
        ..dd6666666dd...
        ..dd6666666dd...
        ..dd6666666dd...
        ..dd6666666dd...
        ..dd6666666dd...
        ..dd6666666dd...
        .ddd1115111ddd..
        .d.d3333333d.d..
        ....3333333.....
        ....333.333.....
        ...3333.333.....
        ...3333.333.....
        ...333..333.....
        ...333..333.....
        111111..333111..
        111111..111111..
        `],
    200,
    false
    )
}
function LoadLevel2 () {
    scene.setBackgroundColor(6)
    tiles.setTilemap(tilemap`level2`)
    for (let value2 of tiles.getTilesByType(assets.tile`myTile1`)) {
        tiles.placeOnTile(prideBoy, value2)
        scene.cameraFollowSprite(prideBoy)
        tiles.setTileAt(value2, assets.tile`transparency16`)
    }
    for (let value2 of tiles.getTilesByType(assets.tile`myTile`)) {
        banana = sprites.create(assets.image`ban`, SpriteKind.Food)
        animation.runImageAnimation(
        banana,
        [img`
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
            `,img`
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
            `],
        200,
        true
        )
        tiles.placeOnTile(banana, value2)
        tiles.setTileAt(value2, assets.tile`transparency16`)
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    otherSprite.destroy()
})
function doSomething2 () {
    animation.runImageAnimation(
    prideBoy,
    [img`
        ................
        .99999..........
        .33333eeeeeee...
        .11111eeeeeeee..
        .33333eeedddde..
        .99999eedd9dd...
        .22222ddddddd...
        .44444dddddddd..
        .55555ddeeeeee..
        .77777.deeeeee..
        .88888.ddeee....
        .aaaaa.ddd......
        ....ff.ddd......
        ....ff.ddd......
        ...dd6ddddd6dd..
        ...dd6666666dd..
        ...dd6666666dd..
        ...dd6666666dd..
        ...dd6666666dd..
        ...dd6666666dd..
        ...dd6666666dd..
        ...dd6666666dd..
        ..ddd1115111ddd.
        ..d.d3333333d.d.
        .....3333333....
        .....333.333....
        .....333.333....
        .....333.333....
        .....333.333....
        .....333.333....
        ..111333.333111.
        ..111111.111111.
        `,img`
        ................
        .99999..........
        .33333eeeeeee...
        .11111eeeeeeee..
        .33333eeedddde..
        .99999eedd9dd...
        .22222ddddddd...
        .44444dddddddd..
        .55555ddeeeeee..
        .77777.deeeeee..
        .88888.ddeee....
        .aaaaa.ddd......
        ....ff.ddd......
        ....ff.ddd......
        ...dd6ddddd6dd..
        ...dd6666666dd..
        ...dd6666666dd..
        ...dd6666666dd..
        ...dd6666666dd..
        ...dd6666666dd..
        ...dd6666666dd..
        ...dd6666666dd..
        ..ddd1115111ddd.
        ..d.d3333333d.d.
        .....3333333....
        .....333.333....
        .....333.3333...
        .....333.3333...
        .....333..333...
        .....333..333...
        ..111333..111111
        ..111111..111111
        `],
    200,
    false
    )
}
function reset () {
    for (let value of sprites.allOfKind(SpriteKind.Food)) {
        value.destroy()
    }
    scene.setBackgroundColor(6)
    tiles.setTilemap(tilemap`level1`)
    for (let value2 of tiles.getTilesByType(assets.tile`myTile1`)) {
        let mySprite: Sprite = null
        tiles.placeOnTile(mySprite, value2)
        scene.cameraFollowSprite(mySprite)
        tiles.setTileAt(value2, assets.tile`transparency16`)
    }
    for (let value2 of tiles.getTilesByType(assets.tile`myTile`)) {
        banana = sprites.create(assets.image`ban`, SpriteKind.Food)
        animation.runImageAnimation(
        banana,
        [img`
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
            `,img`
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
            `],
        200,
        true
        )
        tiles.placeOnTile(banana, value2)
        tiles.setTileAt(value2, assets.tile`transparency16`)
    }
}
let banana: Sprite = null
let prideBoy: Sprite = null
scene.setBackgroundColor(6)
tiles.setTilemap(tilemap`level1`)
prideBoy = sprites.create(assets.image`prideBoy`, SpriteKind.Player)
prideBoy.ay = 100
scene.cameraFollowSprite(prideBoy)
controller.moveSprite(prideBoy, 100, 0)
for (let value2 of tiles.getTilesByType(assets.tile`myTile`)) {
    banana = sprites.create(assets.image`ban`, SpriteKind.Food)
    animation.runImageAnimation(
    banana,
    [img`
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
        `,img`
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
        `],
    200,
    true
    )
    tiles.placeOnTile(banana, value2)
    tiles.setTileAt(value2, assets.tile`transparency16`)
}
forever(function () {
    prideBoy.ay = 400
    if (controller.left.isPressed()) {
        doSomething()
        pause(350)
    }
    if (controller.right.isPressed()) {
        doSomething2()
        pause(350)
    }
})
