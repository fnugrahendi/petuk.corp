#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QString>
#include <QSignalMapper>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    QMetaObject::Connection c_tb_Browse;
    void Popup(QString);

public slots:
    void Quit_Confirm();
    void Browse();
    static void Quit() {exit (0);}
    static void None() {return;}
    void Popup_Close();
private:
    Ui::MainWindow *ui;
    QSignalMapper *signalMapper = new QSignalMapper (this);
};

#endif // MAINWINDOW_H
