"""

Output defines how simulation data are displayed on screen and saved to result files. It may include a list of filter nodes.
Output may be modified on the fly during render, using the output toolbox, or by right clicking on the result tab.
"""
from __future__ import annotations
import numpy
import ocean.abyss.nodes
__all__ = ['Bsdf', 'Channelimage', 'Glaremap', 'Glarereport', 'Linked', 'Rgbimage', 'Special', 'Table']
class Bsdf(ocean.abyss.nodes.Node, ocean.abyss.nodes.CNodeHandler):
    """
    **Bsdf**
    
    .. raw:: html
    
        <iframe id="Bsdf" src="https://docs.eclat-digital.com/ocean2024-docs/reference/nodes/output/bsdf.html" loading="lazy" alt="https://docs.eclat-digital.com/ocean2024-docs/reference/nodes/output/bsdf.html"></iframe>
    """
    def __init__(self, name: str) -> None:
        ...
    def getLight(self) -> numpy.ndarray[numpy.float32]:
        """
        Get the light parameter
        """
    def getMatname(self) -> str:
        """
        Get the matname parameter
        """
    def getRange(self) -> float:
        """
        Get the range parameter
        """
    def setLight(self, light: numpy.ndarray[numpy.float32]) -> bool:
        """
        Set the light parameter
        """
    def setMatname(self, matname: str) -> bool:
        """
        Set the matname parameter
        """
    def setRange(self, range: float) -> bool:
        """
        Set the range parameter
        """
class Channelimage(ocean.abyss.nodes.Node, ocean.abyss.nodes.CNodeHandler):
    """
    **Channelimage**
    
    .. raw:: html
    
        <iframe id="Channelimage" src="https://docs.eclat-digital.com/ocean2024-docs/reference/nodes/output/channelimage.html" loading="lazy" alt="https://docs.eclat-digital.com/ocean2024-docs/reference/nodes/output/channelimage.html"></iframe>
    """
    def __init__(self, name: str) -> None:
        ...
    def getChannel(self) -> str:
        """
        Get the channel parameter
        """
    def getColors(self) -> str:
        """
        Get the colors parameter
        """
    def getColorsChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def getGrid(self) -> bool:
        """
        Get the grid parameter
        """
    def getGridx(self) -> int:
        """
        Get the gridx parameter
        """
    def getGridy(self) -> int:
        """
        Get the gridy parameter
        """
    def getInfo(self) -> bool:
        """
        Get the info parameter
        """
    def getLegend(self) -> bool:
        """
        Get the legend parameter
        """
    def getLogarithmic(self) -> bool:
        """
        Get the logarithmic parameter
        """
    def getLogdecades(self) -> int:
        """
        Get the logdecades parameter
        """
    def getQuantity(self) -> str:
        """
        Get the quantity parameter
        """
    def getQuantityChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def getRangemax(self) -> float:
        """
        Get the rangemax parameter
        """
    def setChannel(self, channel: str) -> bool:
        """
        Set the channel parameter
        """
    def setColors(self, colors: str) -> bool:
        """
        Set the colors parameter
        """
    def setGrid(self, grid: bool) -> bool:
        """
        Set the grid parameter
        """
    def setGridx(self, gridx: int) -> bool:
        """
        Set the gridx parameter
        """
    def setGridy(self, gridy: int) -> bool:
        """
        Set the gridy parameter
        """
    def setInfo(self, info: bool) -> bool:
        """
        Set the info parameter
        """
    def setLegend(self, legend: bool) -> bool:
        """
        Set the legend parameter
        """
    def setLogarithmic(self, logarithmic: bool) -> bool:
        """
        Set the logarithmic parameter
        """
    def setLogdecades(self, logdecades: int) -> bool:
        """
        Set the logdecades parameter
        """
    def setQuantity(self, quantity: str) -> bool:
        """
        Set the quantity parameter
        """
    def setRangemax(self, rangemax: float) -> bool:
        """
        Set the rangemax parameter
        """
class Glaremap(ocean.abyss.nodes.Node, ocean.abyss.nodes.CNodeHandler):
    """
    **Glaremap**
    
    .. raw:: html
    
        <iframe id="Glaremap" src="https://docs.eclat-digital.com/ocean2024-docs/reference/nodes/output/glaremap.html" loading="lazy" alt="https://docs.eclat-digital.com/ocean2024-docs/reference/nodes/output/glaremap.html"></iframe>
    """
    def __init__(self, name: str) -> None:
        ...
    def getChannel(self) -> str:
        """
        Get the channel parameter
        """
    def getColors(self) -> str:
        """
        Get the colors parameter
        """
    def getColorsChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def getColorspace(self) -> str:
        """
        Get the colorspace parameter
        """
    def getColorspaceChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def getDepth(self) -> str:
        """
        Get the depth parameter
        """
    def getDepthChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def getDrawgminfo(self) -> bool:
        """
        Get the drawgminfo parameter
        """
    def getDrawinfo(self) -> bool:
        """
        Get the drawinfo parameter
        """
    def getGlareindex(self) -> str:
        """
        Get the glareindex parameter
        """
    def getGlareindexChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def getGrid(self) -> bool:
        """
        Get the grid parameter
        """
    def getGridx(self) -> int:
        """
        Get the gridx parameter
        """
    def getGridy(self) -> int:
        """
        Get the gridy parameter
        """
    def getHcc(self) -> float:
        """
        Get the hcc parameter
        """
    def getLegend(self) -> bool:
        """
        Get the legend parameter
        """
    def getLogarithmic(self) -> bool:
        """
        Get the logarithmic parameter
        """
    def getLogdecades(self) -> int:
        """
        Get the logdecades parameter
        """
    def getMethod(self) -> str:
        """
        Get the method parameter
        """
    def getMethodChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def getMinarea(self) -> int:
        """
        Get the minarea parameter
        """
    def getOutputtype(self) -> str:
        """
        Get the outputtype parameter
        """
    def getOutputtypeChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def getOverlay(self) -> bool:
        """
        Get the overlay parameter
        """
    def getOverlayidx(self) -> bool:
        """
        Get the overlayidx parameter
        """
    def getPositionindex(self) -> str:
        """
        Get the positionindex parameter
        """
    def getPositionindexChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def getQuantity(self) -> str:
        """
        Get the quantity parameter
        """
    def getQuantityChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def getRangemax(self) -> float:
        """
        Get the rangemax parameter
        """
    def getValue(self) -> float:
        """
        Get the value parameter
        """
    def getXwhite(self) -> float:
        """
        Get the xwhite parameter
        """
    def getYwhite(self) -> float:
        """
        Get the ywhite parameter
        """
    def setChannel(self, channel: str) -> bool:
        """
        Set the channel parameter
        """
    def setColors(self, colors: str) -> bool:
        """
        Set the colors parameter
        """
    def setColorspace(self, colorspace: str) -> bool:
        """
        Set the colorspace parameter
        """
    def setDepth(self, depth: str) -> bool:
        """
        Set the depth parameter
        """
    def setDrawgminfo(self, drawgminfo: bool) -> bool:
        """
        Set the drawgminfo parameter
        """
    def setDrawinfo(self, drawinfo: bool) -> bool:
        """
        Set the drawinfo parameter
        """
    def setGlareindex(self, glareindex: str) -> bool:
        """
        Set the glareindex parameter
        """
    def setGrid(self, grid: bool) -> bool:
        """
        Set the grid parameter
        """
    def setGridx(self, gridx: int) -> bool:
        """
        Set the gridx parameter
        """
    def setGridy(self, gridy: int) -> bool:
        """
        Set the gridy parameter
        """
    def setHcc(self, hcc: float) -> bool:
        """
        Set the hcc parameter
        """
    def setLegend(self, legend: bool) -> bool:
        """
        Set the legend parameter
        """
    def setLogarithmic(self, logarithmic: bool) -> bool:
        """
        Set the logarithmic parameter
        """
    def setLogdecades(self, logdecades: int) -> bool:
        """
        Set the logdecades parameter
        """
    def setMethod(self, method: str) -> bool:
        """
        Set the method parameter
        """
    def setMinarea(self, minarea: int) -> bool:
        """
        Set the minarea parameter
        """
    def setOutputtype(self, outputtype: str) -> bool:
        """
        Set the outputtype parameter
        """
    def setOverlay(self, overlay: bool) -> bool:
        """
        Set the overlay parameter
        """
    def setOverlayidx(self, overlayidx: bool) -> bool:
        """
        Set the overlayidx parameter
        """
    def setPositionindex(self, positionindex: str) -> bool:
        """
        Set the positionindex parameter
        """
    def setQuantity(self, quantity: str) -> bool:
        """
        Set the quantity parameter
        """
    def setRangemax(self, rangemax: float) -> bool:
        """
        Set the rangemax parameter
        """
    def setValue(self, value: float) -> bool:
        """
        Set the value parameter
        """
    def setXwhite(self, xwhite: float) -> bool:
        """
        Set the xwhite parameter
        """
    def setYwhite(self, ywhite: float) -> bool:
        """
        Set the ywhite parameter
        """
class Glarereport(ocean.abyss.nodes.Node, ocean.abyss.nodes.CNodeHandler):
    """
    **Glarereport**
    
    .. raw:: html
    
        <iframe id="Glarereport" src="https://docs.eclat-digital.com/ocean2024-docs/reference/nodes/output/glarereport.html" loading="lazy" alt="https://docs.eclat-digital.com/ocean2024-docs/reference/nodes/output/glarereport.html"></iframe>
    """
    def __init__(self, name: str) -> None:
        ...
class Linked(ocean.abyss.nodes.Node, ocean.abyss.nodes.CNodeHandler):
    """
    Linked
    """
    def __init__(self, name: str) -> None:
        ...
    def getTarget(self) -> str:
        """
        Get the target parameter
        """
    def setTarget(self, target: str) -> bool:
        """
        Set the target parameter
        """
class Rgbimage(ocean.abyss.nodes.Node, ocean.abyss.nodes.CNodeHandler):
    """
    **Rgbimage**
    
    .. raw:: html
    
        <iframe id="Rgbimage" src="https://docs.eclat-digital.com/ocean2024-docs/reference/nodes/output/rgbimage.html" loading="lazy" alt="https://docs.eclat-digital.com/ocean2024-docs/reference/nodes/output/rgbimage.html"></iframe>
    """
    def __init__(self, name: str) -> None:
        ...
    def getColorspace(self) -> str:
        """
        Get the colorspace parameter
        """
    def getColorspaceChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def getDepth(self) -> str:
        """
        Get the depth parameter
        """
    def getDepthChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def getDrawinfo(self) -> bool:
        """
        Get the drawinfo parameter
        """
    def getHcc(self) -> float:
        """
        Get the hcc parameter
        """
    def getXwhite(self) -> float:
        """
        Get the xwhite parameter
        """
    def getYwhite(self) -> float:
        """
        Get the ywhite parameter
        """
    def setColorspace(self, colorspace: str) -> bool:
        """
        Set the colorspace parameter
        """
    def setDepth(self, depth: str) -> bool:
        """
        Set the depth parameter
        """
    def setDrawinfo(self, drawinfo: bool) -> bool:
        """
        Set the drawinfo parameter
        """
    def setHcc(self, hcc: float) -> bool:
        """
        Set the hcc parameter
        """
    def setXwhite(self, xwhite: float) -> bool:
        """
        Set the xwhite parameter
        """
    def setYwhite(self, ywhite: float) -> bool:
        """
        Set the ywhite parameter
        """
class Special(ocean.abyss.nodes.Node, ocean.abyss.nodes.CNodeHandler):
    """
    **Special**
    
    .. raw:: html
    
        <iframe id="Special" src="https://docs.eclat-digital.com/ocean2024-docs/reference/nodes/output/specialdisplay.html" loading="lazy" alt="https://docs.eclat-digital.com/ocean2024-docs/reference/nodes/output/specialdisplay.html"></iframe>
    """
    def __init__(self, name: str) -> None:
        ...
    def getMode(self) -> str:
        """
        Get the mode parameter
        """
    def getModeChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def setMode(self, mode: str) -> bool:
        """
        Set the mode parameter
        """
class Table(ocean.abyss.nodes.Node, ocean.abyss.nodes.CNodeHandler):
    """
    **Table**
    
    .. raw:: html
    
        <iframe id="Table" src="https://docs.eclat-digital.com/ocean2024-docs/reference/nodes/output/table.html" loading="lazy" alt="https://docs.eclat-digital.com/ocean2024-docs/reference/nodes/output/table.html"></iframe>
    """
    def __init__(self, name: str) -> None:
        ...
    def getChannel(self) -> str:
        """
        Get the channel parameter
        """
    def getLayout(self) -> str:
        """
        Get the layout parameter
        """
    def getLayoutChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def getQuantity(self) -> str:
        """
        Get the quantity parameter
        """
    def getQuantityChoices(self) -> list:
        """
        Retrieve the possible choices
        """
    def getX(self) -> int:
        """
        Get the x parameter
        """
    def getY(self) -> int:
        """
        Get the y parameter
        """
    def setChannel(self, channel: str) -> bool:
        """
        Set the channel parameter
        """
    def setLayout(self, layout: str) -> bool:
        """
        Set the layout parameter
        """
    def setQuantity(self, quantity: str) -> bool:
        """
        Set the quantity parameter
        """
    def setX(self, x: int) -> bool:
        """
        Set the x parameter
        """
    def setY(self, y: int) -> bool:
        """
        Set the y parameter
        """
