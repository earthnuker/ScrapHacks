import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore, QtWidgets
from threading import Thread
from queue import Queue
from construct import *
from glob import glob
import os

ScrapFile = Struct(
    'path'/PrefixedArray(Int32ul, Byte),
    'size'/Int32ul,
    'offset'/Int32ul,
)

PackedFile = Struct(
    Const(b'BFPK'),
    Const(b'\0\0\0\0'),
    'files'/PrefixedArray(Int32ul, ScrapFile),
)


def get_path(file):
    return str(bytes(file.path), "utf-8",
               "backslashreplace")


def fsize(n):
    idx = 0
    l = ["", "K", "M", "G", "T", "P", "E"]
    while n > 1024:
        idx += 1
        n /= 1024
    return "{:.02f} {}B".format(n, l[idx])


class Tree(dict):
    def __init__(self, *args, **kwargs):
        self._size = 0
        self.data = None
        self.path = None
        super(type(self), self).__init__(*args, **kwargs)

    def __missing__(self, k):
        self[k] = type(self)()
        return self[k]

    @property
    def size(self):
        if self.data:
            ret = self.data.size
        else:
            ret = 0
        for v in self.values():
            ret += v.size
        return ret

    @size.setter
    def size(self, s):
        self._size = s


def load_data(path):
    ret = Tree()
    fn = os.path.split(path)[-1]
    ret[fn] = Tree()
    with open(path, "rb") as fh:
        data = PackedFile.parse_stream(fh)
        for entry in data.files:
            path = get_path(entry).split("/")
            root = ret[fn]
            for elem in path:
                root = root[elem]
            root.data = entry
    return ret


class Patcher(object):
    def __init__(self, ed):
        self.editor = ed

    def debug(self, *args):
        "Enable Scengraph Debugging Console"
        print("DBG")

    def test(self, *args):
        "TEST!"
        print(self.editor.selected())
        pass


class PackerThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, node, path):
        super().__init__()

        self.node = node
        self.path = path

    def func(self, *args, **kwargs):
        self.signal.emit(*args, **kwargs)

    def run(self):
        try:
            self.__run()
        except:
            (type, value, traceback) = sys.exc_info()
            print(type, value, traceback)
            sys.excepthook(type, value, traceback)

    def __run(self):
        node = self.node
        path = self.path
        PAK = node.pak
        file_list = []

        self.func(("wtl", "Preprocessing"))
        self.func(("range", 0,  0))
        for item in walk(node):
            if item.struct:
                file_list.append(item)
                self.func(("upd", get_loc(item)[1], 1))

        header = PackedFile.build(dict(files=[f.struct for f in file_list]))
        total_size = len(header)
        self.func(("wtl", "Updating offsets"))
        self.func(("range", 0,  len(file_list)))
        for idx, file in enumerate(file_list):
            file.struct.offset = total_size
            total_size += file.struct.size
            self.func(("upd", get_loc(file)[1], idx))

        header = PackedFile.build(dict(files=[f.struct for f in file_list]))
        cnt = 0
        if path:
            self.func(("wtl", "Writing output"))
            self.func(("range", 0, total_size))
            with open(path, "wb") as of:
                of.write(header)
                written = len(header)
                self.func(("upd", "Header", written))
                for file in file_list:
                    loc = get_loc(file)
                    data = get_data(file)[0]
                    written += len(data)
                    self.func(("upd", get_loc(file)[1], written))
                    of.write(data)
            print("XXXXXXXXXXXXXXXXXXXXX")
        self.func(("close",))
        return


class PackerWindow(QProgressDialog):

    def __init__(self, node, path, *args, **kwargs):
        self.node = node
        self.path = path
        self.mtx = QMutex()
        super().__init__()
        self.initUI()
        self.setAutoClose(True)
        self.setWindowTitle("Packing {}".format(node.pak))
        self.setCancelButtonText("Stop")
        self.run()

    def initUI(self):
        self.show()
        self.ensurePolished()
        self.setFixedSize(300, self.height())

    def closeEvent(self, event):
        print("BYE")
        if self.th:
            self.th.wait()
        event.accept()

    def sig(self, val):
        lock = QMutexLocker(self.mtx)
        #print("SIG:", val)
        typ, *args = val
        if typ == "wtl":
            self.setWindowTitle(*args)
        elif typ == "close":
            self.th.wait()
            self.th = None
            self.close()
        elif typ == "range":
            self.setRange(*args)
        elif typ == "upd":
            self.setLabelText(args[0])
            self.setValue(args[1])
        else:
            raise ValueError("Unknown signal: {}".format(val))

    def run(self):
        self.queue = Queue()
        self.th = PackerThread(self.node, self.path)
        self.th.signal.connect(self.sig)
        self.th.start()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("SMT - Scrap Mod Tool")
        self.resize(800, 600)
        self.center()

        menu_close_all = QAction("Close &All", self)
        menu_close_all.setShortcut("Ctrl+Shift+C")
        menu_close_all.triggered.connect(self.menu_close_all)

        menu_create = QAction("&Create new .packed file", self)
        menu_create.setShortcut("Ctrl+N")
        menu_create.triggered.connect(self.menu_new)

        menu_load = QAction("&Open .packed file", self)
        menu_load.setShortcut("Ctrl+O")
        menu_load.triggered.connect(self.menu_load)

        menu_exit = QAction("&Exit", self)
        menu_exit.setShortcut("Ctrl+Q")
        menu_exit.triggered.connect(qApp.quit)

        menu = self.menuBar()
        fileMenu = menu.addMenu('&File')
        fileMenu.addAction(menu_load)
        fileMenu.addAction(menu_create)
        fileMenu.addSeparator()
        fileMenu.addAction(menu_close_all)
        fileMenu.addSeparator()
        fileMenu.addAction(menu_exit)

        self.editor = PackedEditor(self)
        self.setCentralWidget(self.editor)
        self.show()
        self.menu_load(sys.argv[1:])

    def menu_new(self):
        data = PackedFile.build({'files': []})
        loc = QFileDialog.getSaveFileName(
            self, 'Save file', os.getcwd(), "Scrapland Data Files (*.packed)")[0]
        with open(loc, "wb") as of:
            of.write(data)
        self.editor.clear()
        self.editor.load(loc)

    def menu_load(self, paths=None):
        if not paths:
            paths = QFileDialog.getOpenFileNames(
                self, 'Open file', os.getcwd(), "Scrapland Data Files (*.packed)")[0]
        for path in paths:
            path = os.path.abspath(path)
            self.editor.load(path)

    def menu_close_all(self):
        self.editor.clear()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def get_loc(item):
    node = item
    path = []
    while node:
        path.insert(0, node.text(0))
        node = node.parent()
    if path:
        file = path.pop(0)
    else:
        file = None
    path = "/".join(path)
    return (file, path)


def walk(node):
    yield node
    for child_idx in range(node.childCount()):
        yield from walk(node.child(child_idx))


def read_file(path, size=None, offset=None):
    data = None
    with open(path, "rb") as fh:
        if offset:
            fh.seek(offset)
        data = fh.read(size)
    return data


def get_data(node, size=None):
    bin_data = None
    more = None
    if node.struct:
        if size:
            if node.struct.size > size:
                more = True
            size = min(node.struct.size, size)
        else:
            size = node.struct.size
        if node.path:
            bin_data = read_file(node.path, size)
        else:
            bin_data = read_file(node.pak, size, node.struct.offset)
    return bin_data, more


def hexdump(data, addr=0):
    res = []
    bin_data = list(data)
    while bin_data:
        chunk = bin_data[:16]
        bin_data = bin_data[16:]
        res.append("0x{:04x} | {}".format(
            addr, " ".join("{:02x}".format(b) for b in chunk)))
        addr += len(chunk)
    return "\n".join(res)


def build_tree(node, url):
    pak = get_loc(node)[0]
    subtree = Tree()
    path = url.toLocalFile().replace("/", "\\")
    if os.path.isfile(path):
        full_path = os.path.abspath(path)
        path, file = os.path.split(full_path)
        loc = os.path.join(get_loc(node)[1], file)
        root_node = subtree[pak]
        for elem in loc.split("/"):
            root_node = root_node[elem]
        root_node.data = Container(path=bytes(loc, "utf-8"), size=os.path.getsize(
            full_path), offset=0)
        root_node.size = root_node.data.size
        root_node.path = full_path
    else:
        for root, _, files in os.walk(path):
            root = root.replace("/", os.sep)
            for file in files:
                full_path = os.path.join(root, file)
                loc = full_path.replace(path.replace(
                    "/", os.sep), "").strip(os.sep)
                loc = os.path.join(os.path.split(
                    path)[-1], loc).replace(os.sep, "/")
                root_node = subtree[pak]
                for elem in loc.split("/"):
                    root_node = root_node[elem]
                root_node.data = Container(path=bytes(loc, "utf-8"), size=os.path.getsize(
                    full_path), offset=0)
                root_node.size = root_node.data.size
                root_node.path = full_path
    return subtree[pak]


class DataTree(QTreeWidget):
    def dragEnterEvent(self, event):
        m = event.mimeData()
        if m.hasUrls():
            for url in m.urls():
                if url.isLocalFile():
                    event.accept()
                    return
        event.accept()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
        else:
            event.setDropAction(QtCore.Qt.MoveAction)
        event.accept()

    def dropEvent(self, event):
        editor = self.window().editor
        target = self.itemAt(event.pos())
        if target.struct:
            return
        print("Drop: ", get_loc(target))
        if event.source():
            selected = event.source().selectedItems()
            for item in selected:
                labels = [item.text(i) for i in range(item.columnCount())]
                node = QTreeWidgetItem(target, labels)
                node.struct = item.struct
                node.struct.offset = 0
                node.path = item.path
                node.pak = item.pak
        else:
            m = event.mimeData()
            if m.hasUrls():
                for url in m.urls():
                    tree = build_tree(target, url)
                    editor.make_subtree(target, tree, target.pak)
        editor.update_tree()
        event.accept()


class DataLoader(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, path, subtree=None):
        super().__init__()
        self.path = path

    def run(self):
        self.signal.emit((self.path, load_data(self.path)))


class DataExtractor(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, nodes, dest):
        super().__init__()
        self.dest = dest
        self.nodes = nodes

    def run(self):
        for node in self.nodes:
            for ch in walk(node):
                if ch.struct:
                    self.__extract(ch, self.dest)
        self.signal.emit("Done!")
        return

    def __extract(self, node, dest):
        path = get_path(node.struct)
        self.signal.emit("Extracting {}".format(path))
        folder, file = os.path.split(path)
        folder = os.path.join(dest, folder)
        folder = folder.replace("/", os.sep).replace("\\", os.sep)
        file = os.path.join(folder, file)
        os.makedirs(folder, exist_ok=True)
        with open(node.pak, "rb") as pak:
            with open(file, "wb") as of:
                pak.seek(node.struct.offset)
                of.write(pak.read(node.struct.size))


class PackedEditor(QWidget):
    def __init__(self, parent=None):
        super(PackedEditor, self).__init__(parent)
        self.initUI()
        self.data = {}
        self.threads = []
        self.log_mutex = QMutex()

    def initUI(self):
        self.initLayout()
        self.show()

    def initLayout(self):
        grid = QGridLayout()
        hgrid = QSplitter(Qt.Horizontal)
        vgrid = QSplitter(Qt.Vertical)
        patcher_grid = QGridLayout()

        self.info_tab_hex = QTextEdit()
        self.info_tab_text = QTextEdit()
        self.info_tab_info = QTextEdit()
        self.info_tabs = QTabWidget()

        self.info_tab_hex.setReadOnly(True)
        self.info_tab_text.setReadOnly(True)
        self.info_tab_info.setReadOnly(True)

        self.info_tabs.addTab(self.info_tab_info, "Info")
        self.info_tabs.addTab(self.info_tab_text, "Text")
        self.info_tabs.addTab(self.info_tab_hex, "Hexdump")

        self.util_tabs = QTabWidget()

        self.util_tab_log = QTextEdit()
        self.util_tab_log.setReadOnly(True)

        self.util_tab_patch = QWidget()

        self.util_tab_patch.setLayout(patcher_grid)
        self.util_tabs.addTab(self.util_tab_log, "Log")
        self.util_tabs.addTab(self.util_tab_patch, "Patcher")
        self.patcher = Patcher(self)
        i = 0
        patcher_grid_w = 0
        for func in dir(self.patcher):
            if func.startswith("__") or not hasattr(getattr(self.patcher, func), "__call__"):
                continue
            patcher_grid_w += 1
        patcher_grid_w = int(patcher_grid_w**0.5)
        for func in dir(self.patcher):
            if func.startswith("__") or not hasattr(getattr(self.patcher, func), "__call__"):
                continue
            func = getattr(self.patcher, func)
            x, y = divmod(i, patcher_grid_w)
            button = QPushButton(func.__name__.replace("_", " ").title())
            button.setToolTip(func.__doc__)
            button.clicked.connect(func)
            patcher_grid.addWidget(button, x, y)
            i += 1

        self.tree = DataTree()
        self.tree.setHeaderLabels(["Path", "Size", "Offset"])
        self.tree.setSelectionMode(self.tree.ExtendedSelection)
        self.tree.currentItemChanged.connect(self.tree_changed)
        self.tree.setDragDropMode(self.tree.DragDrop | self.tree.InternalMove)
        self.tree.setDragEnabled(True)
        self.tree.setAcceptDrops(True)
        self.tree.setDropIndicatorShown(True)

        hgrid.addWidget(self.tree)
        hgrid.addWidget(self.info_tabs)
        vgrid.addWidget(hgrid)
        vgrid.addWidget(self.util_tabs)
        grid.addWidget(vgrid)
        self.setLayout(grid)

    def info(self, msg):
        lock = QMutexLocker(self.log_mutex)
        self.util_tab_log.insertPlainText(msg + "\n")
        self.util_tab_log.moveCursor(QTextCursor.End)

    def load(self, path):
        if path in self.data:
            return
        self.data[path] = DataLoader(path)
        self.data[path].signal.connect(self.done_loading)
        self.data[path].start()
        self.info("Loading {}".format(path))

    def done_loading(self, result):
        path, data = result
        self.data[path] = data
        self.make_subtree(self.tree, data, path)

    def clear(self):
        self.data.clear()
        self.tree.clear()
        self.info_tab_hex.setText("")
        self.info_tab_text.setText("")
        self.info_tab_info.setText("")
        self.util_tab_log.setText("")

    def make_tree(self):
        for pak in self.data:
            if isinstance(self.data[pak], DataLoader):
                continue
            self.make_subtree(self.tree, self.data[pak], pak)

    def update_tree(self, node=None):
        total_size = 0
        if node is None:
            node = self.tree.invisibleRootItem()
        else:
            if node.struct:
                total_size += node.struct.size
        for child_idx in range(node.childCount()):
            total_size += self.update_tree(node.child(child_idx))
        node.setText(1, fsize(total_size))
        return total_size

    @classmethod
    def make_subtree(cls, tree, data, pak):
        total_size = 0
        for name, children in sorted(data.items()):
            total_size += children.size
            if children.data:
                labels = [name, fsize(children.size),
                          hex(children.data.offset)]
            else:
                labels = [name, fsize(children.size), ""]
            node = QTreeWidgetItem(tree, labels)
            node.struct = children.data
            node.path = children.path
            node.pak = pak
            cls.make_subtree(node, children, pak)

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        actions = {}
        actions[cmenu.addAction("Extract")] = self.extract_handler
        actions[cmenu.addAction("Delete")] = self.del_handler
        if all(node.parent() == None for node in self.selected()):
            actions[cmenu.addAction("Save")] = self.save_handler
        try:
            act_fn = actions.get(
                cmenu.exec_(self.mapToGlobal(event.pos())))
        except TypeError:
            return
        if not act_fn:
            return
        th = act_fn(self.selected())
        if th:
            th.signal.connect(self.info)
            th.start()
            self.threads.append(th)

    def extract_handler(self, nodes):
        dest = QFileDialog.getExistingDirectory(
            self, 'Open file', os.getcwd())
        if not nodes:
            return
        if not dest:
            return
        return DataExtractor(nodes, dest)

    def make_packed(self, node, path=None):
        a = PackerWindow(node, path)
        a.exec_()

    def save_handler(self, nodes):
        for node in nodes:
            path = QFileDialog.getSaveFileName(
                self, 'Save file', node.pak, "Scrapland Data Files (*.packed)")[0]
            self.make_packed(node, path)

    def del_handler(self, nodes):
        if not nodes:
            return
        root = self.tree.invisibleRootItem()
        for node in nodes:
            (node.parent() or root).removeChild(node)
        self.update_tree()

    def get_info(self, node):
        info = []
        if node.struct:
            info.append(("Size", node.struct.size))
            info.append(("Offset", hex(node.struct.offset)))
            info.append(("Path", get_path(node.struct)))
        ret = ""
        for k, v in info:
            ret += "{}:\t{}\n".format(k, v)
        return ret.strip()

    def tree_changed(self, new, old):
        if not new:
            return
        self.info_tab_text.setText("")
        self.info_tab_hex.setText("")
        self.info_tab_info.setText(self.get_info(new))
        data, more = get_data(new, 1024)
        if data:
            more_text = "\n<...>" if more else ""
            self.info_tab_hex.setText(hexdump(data)+more_text)
            try:
                data = str(data, "cp1252")
            except UnicodeDecodeError:
                data = repr(data)
            self.info_tab_text.setText(data+more_text)
            self.info_tab_info.setText(self.get_info(new))

    def selected(self):
        return self.tree.selectedItems()


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
