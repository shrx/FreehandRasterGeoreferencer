# -*- coding: utf-8 -*-
"""
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os.path

from PyQt4.QtCore import qDebug
from qgis.core import QgsProject


# constants for saving data inside QGS
SETTINGS_KEY = "FreehandRasterGeoreferencer"
SETTING_BROWSER_RASTER_DIR = "browseRasterDir"


def toRelativeToQGS(imagePath):
    if os.path.isabs(imagePath):
        # Make it relative to current project if image below QGS
        imageFolder, imageName = os.path.split(imagePath)
        qgsPath = QgsProject.instance().fileName()
        qgsFolder, _ = os.path.split(qgsPath)
        imageFolder = os.path.abspath(imageFolder)
        qgsFolder = os.path.abspath(qgsFolder)

        if imageFolder.startswith(qgsFolder):
            # relative
            imageFolderRelPath = os.path.relpath(imageFolder, qgsFolder)
            imagePath = os.path.join(imageFolderRelPath, imageName)
            qDebug(imagePath.encode('utf8'))

    return imagePath
