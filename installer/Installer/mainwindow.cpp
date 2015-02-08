#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFileDialog>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QObject::connect(ui->tb_Browse, SIGNAL(clicked()),this, SLOT(Browse()));



}

void MainWindow::Browse()
{

    QFileDialog dialog(this);
    dialog.setFileMode(QFileDialog::Directory);

    ui->le_InstallDir->setText(dialog.getOpenFileName());
}

MainWindow::~MainWindow()
{
    delete ui;
}
