from lxml import etree
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import GX_ElementMaker as GX

def rotate(name="rotate",repeat=1,duration="1.5",fov="60",long="-117.1010708578619",
           lat="32.63353533671049",alt="0",tilt="65",rnge="1500"):
    
    playlist = GX.Playlist()
    for i in range(0,(360*repeat),10):
        flyto = GX.FlyTo(
                    GX.duration(duration),
                    GX.flyToMode("smooth"),
                    KML.LookAt(
                        GX.horizFov(fov),
                        KML.longitude(long),
                        KML.latitude(lat),
                        KML.altitude(alt),
                        KML.heading(str(i%360)),
                        KML.tilt(tilt),
                        KML.range(rnge),
                        GX.altitudeMode("relativeToSeaFloor")
                        )
                    )
        playlist.append(flyto)

    doc = GX.Tour(
                KML.name(name),
                playlist)

    return etree.tostring(doc,pretty_print=True)
