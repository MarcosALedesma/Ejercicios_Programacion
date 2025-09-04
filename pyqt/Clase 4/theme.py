# theme.py

dark_theme = """
    QMainWindow {
        background-color: #252526;
    }
    QMenuBar {
        background-color: #333333;
        color: white;
    }
    QMenuBar::item:selected {
        background-color: #007acc;
    }
    QStatusBar {
        background-color: #1e1e1e;
        color: #cccccc;
    }
    QTextEdit {
        background-color: #1e1e1e;
        color: #d4d4d4;
        font-family: "Fira Code", monospace;
        font-size: 14px;
    }
"""

light_theme = """
    QMainWindow {
        background-color: #f5f5f5;
    }
    QMenuBar {
        background-color: #e0e0e0;
        color: black;
    }
    QMenuBar::item:selected {
        background-color: #007acc;
        color: white;
    }
    QStatusBar {
        background-color: #fafafa;
        color: black;
    }
    QTextEdit {
        background-color: white;
        color: black;
        font-family: "Arial";
        font-size: 12px;
    }
"""


chaca_theme = """
QMainWindow {
    background-color: #000000;  
}
QMenuBar {
    background-color: #FF0000;  
    color: #FFFFFF;             
}
QMenuBar::item:selected {
    background-color: #FFFFFF;   
    color: #FF0000;              
}
QStatusBar {
    background-color: #000000;  
    color: #FFFFFF;              
}
QTextEdit {
    background-color: #FFFFFF;   
    color: #000000;      
    font-family: "Courier New", monospace;
    font-size: 13px;
    border: 2px solid #FF0000; 
    selection-background-color: #FF0000;
    selection-color: #FFFFFF;
}
QScrollBar:vertical {
    background: #000000;
    width: 14px;
}
QScrollBar::handle:vertical {
    background: #FF0000;
    min-height: 20px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background: #FF0000;
    height: 14px;
}
"""
