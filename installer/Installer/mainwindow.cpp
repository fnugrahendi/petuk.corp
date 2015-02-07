#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QObject::connect(ui->tb_Browse, SIGNAL(clicked()),this, SLOT(Browse()));

}

void MainWindow::Browse()
{
    ui->le_InstallDir->setText("aaa");
}

MainWindow::~MainWindow()
{
    delete ui;
}
