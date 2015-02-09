/** Makin, 8Feb 2015 **/
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFileDialog>
#include <QString>
#include <QRect>
#include <QSignalMapper>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QObject::connect(ui->tb_Browse, SIGNAL(clicked()),this, SLOT(Browse()));
    QObject::connect(ui->tb_Quit, SIGNAL(clicked()),this, SLOT(Quit_Confirm()));


}
void MainWindow::Quit_Confirm()
{
    Popup(QString("Anda yakin akan keluar?"),&Quit,&None);
}


void MainWindow::Browse()
{

    QFileDialog dialog(this);
    dialog.setFileMode(QFileDialog::Directory);
    QString namafolder;
    namafolder = dialog.getExistingDirectory(this, tr("Open Directory"),
                                                     "",
                                                     QFileDialog::ShowDirsOnly
                                                     | QFileDialog::DontResolveSymlinks);
    ui->le_InstallDir->setText(namafolder);
}

void MainWindow::Popup(QString Text, function *FCB_Ok, function *FCB_Cancel)
{
    ui->fr_Popup->setParent(ui->centralWidget);
    ui->fr_Popup->setGeometry(QRect(0,0,480,230));
    ui->fr_Popup->show();
}

MainWindow::~MainWindow()
{
    delete ui;
}
