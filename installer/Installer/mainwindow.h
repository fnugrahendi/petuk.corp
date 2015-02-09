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
    void None() {return;}
    void Popup(QString Text, function *FCB_Ok, function *FCB_Cancel);
    void Quit() {exit (0);}
public slots:
    void Quit_Confirm();
    void Browse();
private:
    Ui::MainWindow *ui;
    QSignalMapper *signalMapper = new QSignalMapper (this);
};

#endif // MAINWINDOW_H
