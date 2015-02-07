#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

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
public slots:
    void Browse();
private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
