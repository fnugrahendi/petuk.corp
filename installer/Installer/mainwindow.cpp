/** Makin, 8Feb 2015 **/
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFileDialog>
#include <QString>
#include <QRect>
#include <QSignalMapper>
#include "Popup.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QObject::connect(ui->tb_Browse, SIGNAL(clicked()),this, SLOT(Browse()));
    QObject::connect(ui->tb_Quit, SIGNAL(clicked()),this, SLOT(Quit_Confirm()));
    ui->stackedWidget->setCurrentIndex(0);
}
void MainWindow::Quit_Confirm()
{
    try
    {
        QObject::disconnect(ui->tb_Popup_Ok, SIGNAL(clicked()),0, 0);
        QObject::disconnect(ui->tb_Popup_Cancel, SIGNAL(clicked()),0, 0);
    }
    catch (...){;}

    QObject::connect(ui->tb_Popup_Ok, SIGNAL(clicked()),this, SLOT(Quit()));
    QObject::connect(ui->tb_Popup_Cancel, SIGNAL(clicked()),this, SLOT(Popup_Close()));

    Popup(QString("Anda yakin akan keluar?"));
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

void MainWindow::Popup(QString Text)
{
    ui->fr_Popup->setParent(this);
    ui->fr_Popup->setGeometry(QRect(0,0,480,230));
    ui->fr_Popup->show();
    ui->lb_Popup_Text->setText(Text);
}
void MainWindow::Popup_Close()
{
    ui->fr_Popup->hide();
}

MainWindow::~MainWindow()
{
    delete ui;
}
