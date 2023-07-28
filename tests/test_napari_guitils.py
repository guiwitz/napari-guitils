from napari_guitils.gui_widgets import FolderList
from pathlib import Path

def test_folderlist_one_extension(make_napari_viewer):
    
    viewer = make_napari_viewer()
    file_name = 'tests/atest.txt'
    with open(file_name, 'w') as f:
        f.write('test')

    widget = FolderList(viewer=viewer, file_extensions=['.py'])
    widget.update_from_path(Path('tests'))

    assert widget.count()==1, f"expected 1 .py file found {widget.count()} files"
    assert widget.item(0).text() == 'test_napari_guitils.py', f"expected test_napari_guitils.py file but got {widget.item(0).text()}"   

    widget = FolderList(viewer=viewer, file_extensions=['.txt', '.py'])
    widget.update_from_path(Path('tests'))

    assert widget.count()==2, f"expected 2 files found {widget.count()} files"
    assert widget.item(0).text() == 'atest.txt', f"expected atest.txt file but got {widget.item(0).text()}"   

