import xbmc, xbmcgui, os, xbmcaddon, xbmcplugin

__settings__ = xbmcaddon.Addon()
home = __settings__.getAddonInfo('path')
addon_handle = int(sys.argv[1])
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
li = xbmcgui.ListItem ('Iran International Live')
li.setArt({ 'thumb': icon })
li.setInfo('video', {'plot':'Iran International TV Live Stream'})

liveVideoUrl = "https://svs.itworkscdn.net/iinternationallive/iintl.smil/playlist.m3u8"

xbmcplugin.addDirectoryItem(handle=addon_handle, url=liveVideoUrl, listitem=li)
xbmcplugin.endOfDirectory(addon_handle)
