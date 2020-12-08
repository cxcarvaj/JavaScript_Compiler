import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication  # ventana
from PyQt5.QtWidgets import QLabel  # diseño de la ventana
from PyQt5.QtWidgets import QWidget  # componentes
from PyQt5.QtWidgets import QPlainTextEdit  # TextArea
from PyQt5.QtWidgets import QPushButton  # Botones

from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QColor, QPainter, QTextFormat


def analizador_exec(command):
    return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)


def read_output():
    cadena = ""
    with open('output.txt', 'r') as file:
        cadena = file.read()
    return cadena


class QLineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.codeEditor = editor

    def sizeHint(self):
        return QSize(self.editor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event):
        self.codeEditor.lineNumberAreaPaintEvent(event)


class QCodeEditor(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lineNumberArea = QLineNumberArea(self)
        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)
        self.updateLineNumberAreaWidth(0)

    def lineNumberAreaWidth(self):
        digits = 1
        max_value = max(1, self.blockCount())
        while max_value >= 10:
            max_value /= 10
            digits += 1
        space = 3 + self.fontMetrics().width('9') * digits
        return space

    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

    def highlightCurrentLine(self):
        extraSelections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            lineColor = QColor(Qt.green).lighter(180)
            selection.format.setBackground(lineColor)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)
        self.setExtraSelections(extraSelections)

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)

        painter.fillRect(event.rect(), Qt.lightGray)

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        # Just to make sure I use the right font
        height = self.fontMetrics().height()
        while block.isValid() and (top <= event.rect().bottom()):
            if block.isVisible() and (bottom >= event.rect().top()):
                number = str(blockNumber + 1)
                painter.setPen(Qt.black)
                painter.drawText(0, top, self.lineNumberArea.width(), height, Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber += 1


def window():
    # Crea una instancia de QApplication
    app = QApplication(sys.argv)

    # Crea una instancia de tu interfaz QApplication
    window = QWidget()
    window.setWindowTitle("Proyecto de Lenguajes de Programación <ScriptVaders>")
    window.setMinimumHeight(800)
    window.setMinimumWidth(800)
    # window.setGeometry(200,200,280,280)
    window.move(360, 15)  # de izq a der, arriba hacia abajo

    labelTitle = QLabel('<h2>Escriba su código en JavaScript</h2>')

    # Cuadro de texto donde se ingresa el codigo
    inputLabel = QLabel('<h6>Input code: </h6>')
    codeTextArea = QPlainTextEdit()
    codeEditor = QCodeEditor(codeTextArea)

    labelAnalisis = QLabel("Analisis: ")
    labelAnalisis.size()

    # Connection effect
    tokens = []

    def change_text():
        if len(tokens) > 0:
            tokens.pop()
        tokens.append(codeEditor.toPlainText())

        print(tokens)
        labelAnalisis.setText('Processing!')

    def f_lexico():
        if codeEditor.toPlainText() == "":
            resultTextArea.insertHtml('<p style="color: red">Nada que analizar</p><br>')
            return
        f = open("data.txt", "w")
        f.write(codeEditor.toPlainText())
        f.close()
        currentPath = os.curdir
        filePath = currentPath + '/lexico.py'
        cmd = "python " + filePath
        print('initiating lexer.py')
        os.system('python '+filePath)
        resultTextArea.setText(analizador_exec(cmd))
        print('lexer.py finished')


    def f_sintactico():
        if codeEditor.toPlainText() == "":
            resultTextArea.insertHtml('<p style="color: red">Nada que analizar</p><br>')
            return
        f = open("data.txt", "w")
        f.write(codeEditor.toPlainText())
        f.close()
        print('initiating sintactico.py')
        currentPath = os.curdir
        filePath = currentPath + '/sintactico.py'
        cmd = "python " + filePath
        os.system('python ' + filePath)
        resultTextArea.setText(analizador_exec(cmd))
        print('sintactico.py finished')

    def f_sintactico1():
        resultTextArea.append("hola")

    # Buttons

    buttonLexer = QPushButton("Léxico")
    buttonLexer.clicked.connect(f_lexico)
    buttonSintactico = QPushButton("Sintáctico")
    buttonSintactico.clicked.connect(f_sintactico)

    # Cuadro de texto donde se visualiza el resultado
    resultLabel = QLabel('<h6>Result: </h6>')
    resultTextArea = QTextEdit()
    resultTextArea.setReadOnly(True)

    font = resultTextArea.font()
    font.setFamily("Courier")
    font.setPointSize(10)

    # LAYOUTS:

    # Subtitle Section
    layoutLabelCodigo = QHBoxLayout()
    layoutLabelCodigo.addWidget(labelTitle)

    # Input Section
    layoutInput = QVBoxLayout()
    layoutInput.addWidget(inputLabel)
    layoutInput.addWidget(codeEditor)

    layoutAnalisis = QHBoxLayout()
    layoutAnalisis.addWidget(labelAnalisis)
    layoutAnalisis.addWidget(buttonLexer)
    layoutAnalisis.addWidget(buttonSintactico)

    # Result Section
    layoutResult = QVBoxLayout()
    layoutResult.addWidget(resultLabel)
    layoutResult.addWidget(resultTextArea)

    # Main Section
    mainLayout = QVBoxLayout()
    mainLayout.addLayout(layoutLabelCodigo)
    mainLayout.addLayout(layoutInput)
    mainLayout.addLayout(layoutAnalisis)
    mainLayout.addLayout(layoutResult)

    window.setLayout(mainLayout)

    # Muestra interfaz
    window.show()
    # Ejecutar App desde Consola
    sys.exit(app.exec_())


window()
