local factory = require 'factories.seek_avoid_factory'

return factory.createLevelApi{
    mapName = 'nav_maze_static_01',
    episodeLengthSeconds = 60
}
