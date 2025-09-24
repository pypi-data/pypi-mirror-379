from PySide6 import QtCore, QtGui, QtWidgets

from pathlib import Path

from itaxotools.common.bindings import Binder
from itaxotools.taxi_gui import app
from itaxotools.taxi_gui.utility import human_readable_seconds
from itaxotools.taxi_gui.view.animations import VerticalRollAnimation
from itaxotools.taxi_gui.view.cards import Card
from itaxotools.taxi_gui.view.tasks import ScrollTaskView
from itaxotools.taxi_gui.view.widgets import RadioButtonGroup

from .model import BatchDatabaseModel, BatchQueryModel
from .types import BatchResults, DoubleBatchResults, Results, WarnResults
from .widgets import BatchQueryHelp, ElidedLineEdit, ElidedLongLabel, GrowingListView


class BlastTaskView(ScrollTaskView):
    def report_results(self, task_name: str, results: Results | BatchResults | DoubleBatchResults | WarnResults):
        if isinstance(results, Results):
            self.report_results_single(task_name, results)
        elif isinstance(results, BatchResults):
            self.report_results_batch(task_name, results)
        elif isinstance(results, DoubleBatchResults):
            self.report_results_batch_double(task_name, results)
        elif isinstance(results, WarnResults):
            self.report_results_warn(task_name, results)

    def report_results_single(self, task_name: str, results: Results):
        msgBox = QtWidgets.QMessageBox(self.window())
        msgBox.setWindowTitle(app.config.title)
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(f"{task_name} completed successfully!")
        msgBox.setInformativeText(f"Time taken: {human_readable_seconds(results.seconds_taken)}.")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Open)
        button = self.window().msgShow(msgBox)
        if button == QtWidgets.QMessageBox.Open:
            url = QtCore.QUrl.fromLocalFile(str(results.output_path.absolute()))
            QtGui.QDesktopServices.openUrl(url)

    def report_results_batch(self, task_name: str, results: BatchResults):
        if not results.failed:
            self.report_results_single(task_name, results)
        else:
            msgBox = QtWidgets.QMessageBox(self.window())
            msgBox.setWindowTitle(app.config.title)
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setText(f"{task_name} completed with errors!")
            msgBox.setInformativeText(
                f"Time taken: {human_readable_seconds(results.seconds_taken)}.\nFiles with errors: {len(results.failed)}"
            )
            msgBox.setDetailedText(
                "Error logs were written for the following files:\n"
                + "\n".join(f"- {path.name}" for path in results.failed)
                + "\n"
            )
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Open)
            msgBox.setStyleSheet("QMessageBox { min-width: 400px; }")
            button = self.window().msgShow(msgBox)
            if button == QtWidgets.QMessageBox.Open:
                url = QtCore.QUrl.fromLocalFile(str(results.output_path.absolute()))
                QtGui.QDesktopServices.openUrl(url)

    def report_results_batch_double(self, task_name: str, results: DoubleBatchResults):
        if not results.failed:
            self.report_results_single(task_name, results)
        else:

            def log_report_for_database(database: Path, queries: list[Path]) -> str:
                return f"- For database {database.name}:\n" + "\n".join(f"* {path.name}" for path in queries)

            error_count = sum(len(queries) for queries in results.failed.values())

            msgBox = QtWidgets.QMessageBox(self.window())
            msgBox.setWindowTitle(app.config.title)
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setText(f"{task_name} completed with errors!")
            msgBox.setInformativeText(
                f"Time taken: {human_readable_seconds(results.seconds_taken)}.\nFiles with errors: {error_count}"
            )
            msgBox.setDetailedText(
                "Error logs were written for the following files:\n\n"
                + "\n\n".join(
                    log_report_for_database(database, queries) for database, queries in results.failed.items()
                )
                + "\n"
            )
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Open)
            msgBox.setStyleSheet("QMessageBox { min-width: 400px; }")
            button = self.window().msgShow(msgBox)
            if button == QtWidgets.QMessageBox.Open:
                url = QtCore.QUrl.fromLocalFile(str(results.output_path.absolute()))
                QtGui.QDesktopServices.openUrl(url)

    def report_results_warn(self, task_name: str, results: WarnResults):
        if not results.warnings:
            self.report_results_single(task_name, results)
        else:
            msgBox = QtWidgets.QMessageBox(self.window())
            msgBox.setWindowTitle(app.config.title)
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setText(f"{task_name} completed with warnings!")
            msgBox.setInformativeText(
                f"Time taken: {human_readable_seconds(results.seconds_taken)}.\nSee below for details."
            )
            msgBox.setDetailedText("\n".join(f"- {warn}" for warn in results.warnings) + "\n")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Open)
            msgBox.setStyleSheet("QMessageBox { min-width: 400px; }")
            button = self.window().msgShow(msgBox)
            if button == QtWidgets.QMessageBox.Open:
                url = QtCore.QUrl.fromLocalFile(str(results.output_path.absolute()))
                QtGui.QDesktopServices.openUrl(url)

    def request_confirmation(self, path: Path | None, callback, abort):
        msgBox = QtWidgets.QMessageBox(self.window())
        msgBox.setWindowTitle(f"{app.config.title} - Warning")
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.Cancel)

        if path is None:
            text = "Some files already exist. Overwrite?"
        else:
            name = path.name
            if len(name) > 42:
                name = name[:31] + "..." + name[-11:]
            text = f"File '{name}' already exists. Overwrite?"
        msgBox.setText(text)

        result = self.window().msgShow(msgBox)
        if result == QtWidgets.QMessageBox.Ok:
            callback()
        else:
            abort()


class GraphicTitleCard(Card):
    def __init__(self, title, description, pixmap, parent=None):
        super().__init__(parent)

        label_title = QtWidgets.QLabel(title)
        font = label_title.font()
        font.setPixelSize(18)
        font.setBold(True)
        font.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, 1)
        label_title.setFont(font)

        label_description = QtWidgets.QLabel(description)
        label_description.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        label_description.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        label_description.setWordWrap(True)

        label_pixmap = QtWidgets.QLabel()
        label_pixmap.setPixmap(pixmap)
        label_pixmap.setFixedSize(pixmap.size())

        text_layout = QtWidgets.QVBoxLayout()
        text_layout.setContentsMargins(0, 6, 0, 4)
        text_layout.addWidget(label_title)
        text_layout.addWidget(label_description, 1)
        text_layout.setSpacing(8)

        pixmap_layout = QtWidgets.QVBoxLayout()
        pixmap_layout.setContentsMargins(0, 8, 0, 4)
        pixmap_layout.addWidget(label_pixmap)
        pixmap_layout.addStretch(1)

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 4, 0, 4)
        layout.setSpacing(16)
        layout.addLayout(pixmap_layout)
        layout.addLayout(text_layout, 1)
        layout.addSpacing(16)

        self.addLayout(layout)

        self.controls.title = label_title
        self.controls.description = label_description
        self.controls.pixmap = label_pixmap

    def setTitle(self, text):
        self.controls.title.setText(text)

    def setBusy(self, busy: bool):
        self.setEnabled(not busy)


class PathSelector(Card):
    selectedPath = QtCore.Signal(Path)

    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.draw_main(text)
        self.set_placeholder_text("---")

    def draw_main(self, text):
        label = QtWidgets.QLabel(text + ":")
        label.setStyleSheet("""font-size: 16px;""")
        label.setMinimumWidth(150)

        field = ElidedLineEdit()
        field.textDeleted.connect(self._handle_text_deleted)
        field.setReadOnly(True)

        browse = QtWidgets.QPushButton("Browse")
        browse.clicked.connect(self._handle_browse)
        browse.setFixedWidth(120)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(field, 1)
        layout.addWidget(browse)
        layout.setSpacing(16)
        self.addLayout(layout)

        self.controls.label = label
        self.controls.field = field
        self.controls.browse = browse

    def _handle_browse(self, *args):
        raise NotImplementedError()

    def _handle_text_deleted(self):
        self.selectedPath.emit(Path())

    def set_placeholder_text(self, text: str):
        self.controls.field.setPlaceholderText(text)

    def set_busy(self, busy: bool):
        self.setEnabled(True)
        self.controls.field.setEnabled(not busy)
        self.controls.browse.setEnabled(not busy)
        self.controls.label.setEnabled(not busy)

    def set_path(self, path: Path):
        text = str(path) if path != Path() else ""
        self.controls.field.setText(text)


class PathFileSelector(PathSelector):
    def _handle_browse(self, *args):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            parent=self.window(),
            caption=f"{app.config.title} - Browse file",
        )
        if not filename:
            return
        self.selectedPath.emit(Path(filename))


class PathFileOutSelector(PathSelector):
    def _handle_browse(self, *args):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            parent=self.window(),
            caption=f"{app.config.title} - Save file",
        )
        if not filename:
            return
        self.selectedPath.emit(Path(filename))


class PathDirectorySelector(PathSelector):
    def _handle_browse(self, *args):
        filename = QtWidgets.QFileDialog.getExistingDirectory(
            parent=self.window(),
            caption=f"{app.config.title} - Browse folder",
        )
        if not filename:
            return
        self.selectedPath.emit(Path(filename))


class PathDatabaseSelector(PathSelector):
    def _handle_browse(self, *args):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            parent=self.window(), caption=f"{app.config.title} - Browse file", filter="BLAST databases (*.nin *.pin)"
        )
        if not filename:
            return
        if filename.endswith(".nin"):
            filename = filename.removesuffix(".nin")
        elif filename.endswith(".pin"):
            filename = filename.removesuffix(".pin")
        self.selectedPath.emit(Path(filename))


class OutputDirectorySelector(PathDirectorySelector):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.set_placeholder_text("All output files will be saved here")
        self.draw_config()

    def draw_config(self):
        label = QtWidgets.QLabel("Filename options:")
        label.setStyleSheet("""font-size: 14px;""")
        label.setMinimumWidth(150)

        append_configuration = QtWidgets.QCheckBox("Append configuration values")
        append_timestamp = QtWidgets.QCheckBox("Append timestamp")

        checkbox_layout = QtWidgets.QHBoxLayout()
        checkbox_layout.setSpacing(16)
        checkbox_layout.addWidget(append_configuration)
        checkbox_layout.addWidget(append_timestamp, 1)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(label)
        layout.addLayout(checkbox_layout)
        layout.addSpacing(136)
        layout.setSpacing(16)
        self.addLayout(layout)

        self.controls.append_configuration = append_configuration
        self.controls.append_timestamp = append_timestamp


class BatchQuerySelector(Card):
    batchModeChanged = QtCore.Signal(bool)
    selectedSinglePath = QtCore.Signal(Path)
    requestedAddPaths = QtCore.Signal(list)
    requestedAddFolder = QtCore.Signal(Path)
    requestDelete = QtCore.Signal(list)
    requestClear = QtCore.Signal()

    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.binder = Binder()
        self.draw_mode()
        self.draw_single("\u25B6  ", text)
        self.draw_batch("\u25B6  ", text)

    def draw_mode(self):
        label = QtWidgets.QLabel("Input mode:")
        label.setStyleSheet("""font-size: 16px;""")
        label.setMinimumWidth(150)

        single = QtWidgets.QRadioButton("Single file")
        batch = QtWidgets.QRadioButton("Batch mode")

        group = RadioButtonGroup()
        group.valueChanged.connect(self._handle_batch_mode_changed)
        group.add(single, False)
        group.add(batch, True)

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(label)
        layout.addWidget(single)
        layout.addWidget(batch, 1)
        layout.addSpacing(136)
        layout.setSpacing(16)
        self.addWidget(widget)

        self.controls.label = label
        self.controls.single = single
        self.controls.batch = batch
        self.controls.batch_mode = group
        self.controls.header = widget

    def draw_single(self, symbol, text):
        label = QtWidgets.QLabel(f"{symbol}{text}:")
        label.setStyleSheet("""font-size: 16px;""")
        label.setMinimumWidth(150)

        field = ElidedLineEdit()
        field.setPlaceholderText("Sequences to match against database contents (FASTA or FASTQ)")
        field.textDeleted.connect(self._handle_single_path_deleted)
        field.setReadOnly(True)

        browse = QtWidgets.QPushButton("Browse")
        browse.clicked.connect(self._handle_browse)
        browse.setFixedWidth(120)

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(label)
        layout.addWidget(field, 1)
        layout.addWidget(browse)
        layout.setSpacing(16)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.addWidget(widget)
        widget.roll = VerticalRollAnimation(widget)
        widget.roll._visible_target = True

        self.controls.single_query = widget
        self.controls.single_field = field

    def draw_batch(self, symbol, text):
        label_symbol = QtWidgets.QLabel(symbol)
        label_symbol.setStyleSheet("""font-size: 16px;""")

        label_text = QtWidgets.QLabel(text + ":")
        label_text.setStyleSheet("""font-size: 16px;""")

        label_spacer = QtWidgets.QLabel("")
        label_spacer.setMinimumWidth(150)

        label_total = QtWidgets.QLabel("Total: 0")

        view = GrowingListView()
        view.requestDelete.connect(self.requestDelete)

        help = BatchQueryHelp()

        add_file = QtWidgets.QPushButton("Add files")
        add_folder = QtWidgets.QPushButton("Add folder")
        clear = QtWidgets.QPushButton("Clear")
        clear.setFixedWidth(120)

        add_file.clicked.connect(self._handle_add_paths)
        add_folder.clicked.connect(self._handle_add_folder)
        clear.clicked.connect(self._handle_clear_paths)

        labels = QtWidgets.QGridLayout()
        labels.setHorizontalSpacing(0)
        labels.setVerticalSpacing(16)
        labels.setColumnStretch(1, 1)
        labels.setRowStretch(3, 1)
        labels.addWidget(label_symbol, 0, 0)
        labels.addWidget(label_text, 0, 1)
        labels.addWidget(label_total, 1, 1)
        labels.addWidget(label_spacer, 2, 0, 1, 2)

        buttons = QtWidgets.QVBoxLayout()
        buttons.setSpacing(8)
        buttons.addWidget(add_file)
        buttons.addWidget(add_folder)
        buttons.addWidget(clear)
        buttons.addStretch(1)

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)
        layout.addLayout(labels)
        layout.addWidget(view, 1)
        layout.addWidget(help, 1)
        layout.addLayout(buttons)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.addWidget(widget)
        widget.roll = VerticalRollAnimation(widget)

        self.controls.batch_query = widget
        self.controls.batch_view = view
        self.controls.batch_help = help
        self.controls.batch_total = label_total

    def _handle_batch_mode_changed(self, value):
        self.batchModeChanged.emit(value)

    def _handle_single_path_deleted(self):
        self.selectedSinglePath.emit(Path())

    def _handle_browse(self, *args):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            parent=self.window(),
            caption=f"{app.config.title} - Browse file",
        )
        if not filename:
            return
        self.selectedSinglePath.emit(Path(filename))

    def _handle_add_paths(self, *args):
        filenames, _ = QtWidgets.QFileDialog.getOpenFileNames(
            parent=self.window(),
            caption=f"{app.config.title} - Browse files",
        )
        paths = [Path(filename) for filename in filenames]
        self.requestedAddPaths.emit(paths)

    def _handle_add_folder(self, *args):
        filename = QtWidgets.QFileDialog.getExistingDirectory(
            parent=self.window(),
            caption=f"{app.config.title} - Browse folder",
        )
        if not filename:
            return
        self.requestedAddFolder.emit(Path(filename))

    def _handle_clear_paths(self):
        self.requestClear.emit()

    def set_batch_mode(self, value: bool):
        self.controls.batch_mode.setValue(value)
        self.controls.batch_query.roll.setAnimatedVisible(value)
        self.controls.single_query.roll.setAnimatedVisible(not value)

    def set_batch_total(self, total: int):
        self.controls.batch_total.setText(f"Total: {total}")

    def set_batch_help_visible(self, visible: bool):
        self.controls.batch_help.setVisible(visible)
        self.controls.batch_view.setVisible(not visible)

    def set_path(self, path: Path):
        text = str(path) if path != Path() else ""
        self.controls.single_field.setText(text)

    def set_placeholder_text(self, text: str):
        self.controls.single_field.setPlaceholderText(text)
        self.controls.batch_help.setPlaceholderText(text)

    def set_batch_placeholder_text(self, text: str):
        self.controls.batch_help.setPlaceholderText(text)

    def set_batch_only(self, value: bool):
        self.controls.header.setVisible(not value)
        self.controls.single_query.roll._visible_target = not value
        self.controls.batch_query.roll._visible_target = value

    def bind_batch_model(self, binder: Binder, object: BatchQueryModel):
        self.controls.batch_view.setModel(object.query_list)

        binder.bind(object.properties.batch_mode, self.set_batch_mode)
        binder.bind(self.batchModeChanged, object.properties.batch_mode)

        binder.bind(object.properties.query_path, self.set_path)
        binder.bind(self.selectedSinglePath, object.set_path)

        binder.bind(self.requestClear, object.clear_paths)
        binder.bind(self.requestDelete, object.delete_paths)
        binder.bind(self.requestedAddPaths, object.add_paths)
        binder.bind(self.requestedAddFolder, object.add_folder)

        binder.bind(object.properties.query_list_total, self.set_batch_total)
        binder.bind(object.properties.query_list_rows, self.set_batch_help_visible, proxy=lambda x: x == 0)

        binder.bind(object.query_list.rowsInserted, self.controls.batch_view.updateGeometry)
        binder.bind(object.query_list.rowsRemoved, self.controls.batch_view.updateGeometry)
        binder.bind(object.query_list.modelReset, self.controls.batch_view.updateGeometry)


class BatchDatabaseSelector(BatchQuerySelector):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controls.label.setText("Database mode:")
        self.controls.single_field.setPlaceholderText("Match all query sequences against this database")
        self.controls.batch_help.setPlaceholderText("Match all query sequences against these databases")
        self.controls.single_database = self.controls.single_query
        self.controls.batch_database = self.controls.batch_query

    def draw_batch(self, symbol, text):
        super().draw_batch(symbol, text + "s")

    def bind_batch_model(self, binder: Binder, object: BatchDatabaseModel):
        super().bind_batch_model(binder, object)

    def _handle_browse(self, *args):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            parent=self.window(),
            caption=f"{app.config.title} - Browse file",
            filter="BLAST databases (*.nin *.pin)",
        )
        if not filename:
            return
        self.selectedSinglePath.emit(Path(filename))

    def _handle_add_paths(self, *args):
        filenames, _ = QtWidgets.QFileDialog.getOpenFileNames(
            parent=self.window(),
            caption=f"{app.config.title} - Browse files",
            filter="BLAST databases (*.nin *.pin)",
        )
        paths = [Path(filename) for filename in filenames]
        self.requestedAddPaths.emit(paths)


class ClickableWidget(QtWidgets.QWidget):
    clicked = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._mouse_pressed = False

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._mouse_pressed = True

    def mouseReleaseEvent(self, event):
        if self._mouse_pressed and event.button() == QtCore.Qt.LeftButton:
            self._mouse_pressed = False
            if self.rect().contains(event.pos()):
                self.clicked.emit()

    def leaveEvent(self, event):
        self._mouse_pressed = False
        super().leaveEvent(event)


class OptionCard(Card):
    toggled = QtCore.Signal(bool)

    def __init__(self, text, description, parent=None):
        super().__init__(parent)
        self.draw_title(text, description)

    def draw_title(self, text, description):
        title = QtWidgets.QCheckBox(" " + text)
        title.setStyleSheet("""font-size: 16px;""")
        title.toggled.connect(self.toggled)
        title.setFixedWidth(150)

        label = QtWidgets.QLabel(description)

        widget = ClickableWidget()
        widget.clicked.connect(title.toggle)

        layout = QtWidgets.QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(title)
        layout.addWidget(label, 1)
        layout.setSpacing(16)
        self.addWidget(widget)

        self.controls.title = title

    def setChecked(self, checked: bool):
        self.controls.title.setChecked(checked)


class BatchProgressCard(Card):
    def __init__(self, parent=None):
        super().__init__(parent)

        label = ElidedLongLabel()

        bar = QtWidgets.QProgressBar()
        bar.setMaximum(0)
        bar.setMinimum(0)
        bar.setValue(0)

        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(8)
        layout.addWidget(label)
        layout.addWidget(bar)

        self.controls.label = label
        self.controls.bar = bar

        self.addLayout(layout)

    def showProgress(self, report):
        self.controls.label.setText(report.text)
        self.controls.bar.setMaximum(report.maximum)
        self.controls.bar.setMinimum(report.minimum)
        self.controls.bar.setValue(report.value)
