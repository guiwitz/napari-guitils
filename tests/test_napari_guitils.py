from napari_guitils.gui_widgets import FolderList
from napari_guitils.gui_structures import TabSet
from qtpy.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QScrollArea
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


def test_tabset_basic(qtbot):
    tabs = TabSet(['Tab1', 'Tab2'])
    qtbot.addWidget(tabs)

    assert tabs.count() == 2
    assert tabs.tabText(0) == 'Tab1'
    assert tabs.tabText(1) == 'Tab2'


def test_tabset_custom_layout(qtbot):
    tabs = TabSet(['A', 'B'], tab_layouts=[QVBoxLayout(), QHBoxLayout()])
    qtbot.addWidget(tabs)

    assert isinstance(tabs.widget(0).layout(), QVBoxLayout)
    assert isinstance(tabs.widget(1).layout(), QHBoxLayout)


def test_tabset_add_named_tab(qtbot):
    tabs = TabSet(['Tab1', 'Tab2'])
    qtbot.addWidget(tabs)

    label = QLabel('hello')
    tabs.add_named_tab('Tab1', label)

    assert tabs.widget(0).layout().count() == 1
    assert tabs.widget(0).layout().itemAt(0).widget() is label


def test_tabset_scrollable_all(qtbot):
    tabs = TabSet(['Tab1', 'Tab2'], scrollable=True)
    qtbot.addWidget(tabs)

    # super().widget() should be a QScrollArea; tabs.widget() unwraps it
    for i in range(2):
        raw = QTabWidget.widget(tabs, i)
        assert isinstance(raw, QScrollArea)
        assert tabs.widget(i) is raw.widget()


def test_tabset_scrollable_per_tab(qtbot):
    tabs = TabSet(['Scroll', 'Plain'], scrollable=[True, False])
    qtbot.addWidget(tabs)

    assert isinstance(QTabWidget.widget(tabs, 0), QScrollArea)
    assert not isinstance(QTabWidget.widget(tabs, 1), QScrollArea)


def test_tabset_scrollable_add_widget(qtbot):
    tabs = TabSet(['Tab1'], scrollable=True)
    qtbot.addWidget(tabs)

    label = QLabel('inside scroll')
    tabs.add_named_tab('Tab1', label)

    assert tabs.widget(0).layout().itemAt(0).widget() is label

