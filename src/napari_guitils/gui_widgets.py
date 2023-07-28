

import os
from pathlib import Path
from qtpy.QtWidgets import QListWidget
from qtpy.QtCore import Qt
from natsort import natsorted


class FolderList(QListWidget):
    """
    A QListWidget that displays the files in a folder.
    
    Parameters
    ----------
    viewer : napari.Viewer
        The napari viewer.
    file_extensions : list of str
        The file extensions to display.
    parent : QWidget
        The parent widget.
    
    """

    def __init__(self, viewer, file_extensions=None, parent=None):
        super().__init__(parent)

        self.viewer = viewer
        self.setAcceptDrops(True)
        self.setDragEnabled(True)

        self.folder_path = None
        self.file_extensions = file_extensions


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):

        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            
            for url in event.mimeData().urls():
                file = str(url.toLocalFile())
                if not Path(file).is_dir():
                    self.update_from_path(Path(file).parent)
                    file_list = [self.item(x).text() for x in range(self.count())]
                    self.setCurrentRow(file_list.index(Path(file).name))
                else:
                    self.update_from_path(Path(file))

    def update_from_path(self, path):

        self.clear()
        self.folder_path = path
        files = os.listdir(self.folder_path)
        files = natsorted(files)

        if self.file_extensions is None:
            file_extensions = [Path(f).suffix for f in files]
        else:
            file_extensions = self.file_extensions
        for f in files:
            if (
                (f[0] != '.') 
                and (self.folder_path.joinpath(f).is_file())
                and (Path(f).suffix in file_extensions)
            ):
                self.addItem(f)
    
    def addFileEvent(self):
        pass

    def select_first_file(self):
        
        self.setCurrentRow(0)

    def get_selected_filepath(self):

        file_path = None
        if len(self.selectedItems()) > 0:
            file_name = self.selectedItems()[0].text()
            file_path = self.folder_path.joinpath(file_name)
        
        return file_path

